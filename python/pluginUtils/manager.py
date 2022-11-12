from __future__ import (absolute_import, division,
                        print_function)

from builtins import (ascii, chr, dict, filter, hex, input,
                      int, map, next, oct, open, pow, range, round,
                      str, super, zip)

import atexit, os, platform, shutil, subprocess, sys, threading, time

from .log import printLog
from .path import getAppManagerHost

join = os.path.join

if sys.version_info[0] < 3:
    from httplib import HTTPConnection
else:
    from http.client import HTTPConnection

class AppManagerConn():
    root = None
    modPackage = None
    isThreaded = False

    servers = [] # for threaded only
    subThreads = []

    @classmethod
    def isAvailable(cls, root):
        if os.path.isfile(join(root, 'manager', 'server.py')):
            return True
        else:
            return False

    @classmethod
    def getPreviewDir(cls, cleanup=False):
        conn = HTTPConnection(getAppManagerHost(False))

        try:
            conn.request('GET', '/get_preview_dir')
        except ConnectionRefusedError:
            printLog('WARNING', 'App Manager connection error, wait a bit')
            time.sleep(0.3)
            conn = HTTPConnection(getAppManagerHost(False))
            conn.request('GET', '/get_preview_dir')

        response = conn.getresponse()

        if response.status != 200:
            printLog('ERROR', 'App Manager connection error: ' + response.reason)
            return None

        path = response.read().decode('utf-8')

        if cleanup:
            shutil.rmtree(path, ignore_errors=True)

            # COMPAT: Python 2.7 (instead of exist_ok)
            if not os.path.exists(path):
                os.makedirs(path)

        printLog('INFO', 'Performing export to preview dir: {}'.format(path))

        return path

    @classmethod
    def runServerProc(cls):
        sys.path.insert(0, join(cls.root, 'manager'))

        if cls.isThreaded:
            import server
            srv = server.AppManagerServer()
            cls.servers.append(srv)
            srv.start(cls.modPackage)
        else:
            system = platform.system()

            if system == 'Windows':
                pythonPath = join(cls.root, 'python', 'windows', 'pythonw.exe')
            elif system == 'Darwin':
                pythonPath = 'python3'
            else:
                pythonPath = 'python3'

            args = [pythonPath, join(cls.root, 'manager', 'server.py'), cls.modPackage]
            subprocess.Popen(args)

    @classmethod
    def start(cls, root, modPackage, isThreaded):
        cls.root = root
        cls.modPackage = modPackage
        cls.isThreaded = isThreaded

        if isThreaded:
            thread = threading.Thread(target=cls.runServerProc)
            thread.daemon = True
            thread.start()
            cls.subThreads.append(thread)
        else:
            cls.runServerProc()

        # works for Blender and 3ds Max, not Maya
        atexit.register(cls.stop)

    @classmethod
    def stop(cls):
        if cls.isThreaded:
            cls.killSubThreads()
        else:
            conn = HTTPConnection(getAppManagerHost(False))
            conn.request('GET', '/stop')
            response = conn.getresponse()
            if response.status != 200:
                printLog('ERROR', 'App Manager connection error: ' + response.reason)

    @classmethod
    def killSubThreads(cls):
        for srv in cls.servers:
            srv.stop()
        for thread in cls.subThreads:
            if thread.is_alive():
                printLog('INFO', 'Waiting app manager to finish')
                thread.join(3)

        cls.servers = []
        cls.subThreads = []

    @classmethod
    def compressLZMA(cls, srcPath, dstPath=None):
        # improves console readability
        srcPath = os.path.normpath(srcPath)
        dstPath = dstPath if dstPath else srcPath + '.xz'

        printLog('INFO', 'Compressing {} to LZMA'.format(os.path.basename(srcPath)))

        with open(srcPath, 'rb') as fin:
            conn = HTTPConnection(getAppManagerHost(False))
            headers = {'Content-type': 'application/octet-stream'}
            conn.request('POST', '/storage/lzma/', body=fin, headers=headers)
            response = conn.getresponse()

            if response.status != 200:
                printLog('ERROR', 'LZMA compression error: ' + response.reason)

            with open(dstPath, 'wb') as fout:
                fout.write(response.read())

    @classmethod
    def compressLZMABuffer(cls, data):
        conn = HTTPConnection(getAppManagerHost(False))
        headers = {'Content-type': 'application/octet-stream'}
        conn.request('POST', '/storage/lzma/', body=data, headers=headers)
        response = conn.getresponse()

        if response.status != 200:
            printLog('ERROR', 'LZMA compression error: ' + response.reason)

        return response.read()

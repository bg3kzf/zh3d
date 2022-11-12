from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from builtins import (ascii, bytes, chr, dict, filter, hex, input,
                      int, map, next, oct, open, pow, range, round,
                      str, super, zip)

import imghdr, os, platform, subprocess, sys, tempfile

from .path import getRoot, getPlatformBinDirName
from .log import printLog

try:
    from subprocess import CompletedProcess
except ImportError:
    # COMPAT: Python 2
    class CompletedProcess:

        def __init__(self, args, returncode, stdout=None, stderr=None):
            self.args = args
            self.returncode = returncode
            self.stdout = stdout
            self.stderr = stderr

        def check_returncode(self):
            if self.returncode != 0:
                err = subprocess.CalledProcessError(self.returncode, self.args, output=self.stdout)
                raise err
            return self.returncode

    def sp_run(*popenargs, **kwargs):
        input = kwargs.pop('input', None)
        check = kwargs.pop('handle', False)

        capture_output = kwargs.pop('capture_output', False)
        if capture_output:
            kwargs['stdout'] = subprocess.PIPE
            kwargs['stderr'] = subprocess.PIPE

        if input is not None:
            if 'stdin' in kwargs:
                raise ValueError('stdin and input arguments may not both be used.')
            kwargs['stdin'] = subprocess.PIPE
        process = subprocess.Popen(*popenargs, **kwargs)
        try:
            outs, errs = process.communicate(input)
        except:
            process.kill()
            process.wait()
            raise
        returncode = process.poll()
        if check and returncode:
            raise subprocess.CalledProcessError(returncode, popenargs, output=outs)
        return CompletedProcess(popenargs, returncode, stdout=outs, stderr=errs)

    subprocess.run = sp_run


class CompressionFailed(Exception):
    pass

def compressKTX2(srcPath='', srcData=None, dstPath='-', method='AUTO'):
    """
    srcPath/srcData are mutually exclusive
    """

    if srcData:
        # NOTE: toktx does not support stdin at the moment
        tmpImg = tempfile.NamedTemporaryFile(delete=False)
        tmpImg.write(srcData)
        tmpImg.close()
        srcPath = tmpImg.name

    imgType = imghdr.what(srcPath)

    params = [os.path.join(getRoot(), 'ktx', getPlatformBinDirName(), 'toktx')]

    params.append('--encode')
    if method == 'UASTC' or method == 'AUTO':
        params.append('uastc')
        params.append('--zcmp')
    else:
        params.append('etc1s')
        params.append('--clevel')
        params.append('2')
        params.append('--qlevel')
        params.append('255')

    params.append('--genmipmap')
    params.append(dstPath)
    params.append(srcPath)

    printLog('INFO', 'Compressing {0} to {1}'.format(os.path.basename(srcPath), params[2].upper()))

    if platform.system().lower() == 'windows':
        # disable popup console window
        si = subprocess.STARTUPINFO()
        si.dwFlags = subprocess.STARTF_USESHOWWINDOW
        si.wShowWindow = subprocess.SW_HIDE
        app = subprocess.run(params, capture_output=True, startupinfo=si)
    else:
        app = subprocess.run(params, capture_output=True)

    if srcData:
        os.unlink(srcPath)

    if app.stderr:
        printLog('WARNING', app.stderr.decode('utf-8').strip())
        raise CompressionFailed

    return app.stdout

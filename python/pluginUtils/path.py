from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from builtins import (ascii, bytes, chr, dict, filter, hex, input,
                      int, map, next, oct, open, pow, range, round,
                      str, super, zip)

import os, platform

def getRoot():
    baseDir = os.path.dirname(os.path.abspath(__file__))
    # NOTE: not working in python2
    #return (pathlib.Path(baseDir) / '..' / '..').resolve()
    return os.path.join(baseDir, '..', '..')

def getManualURL():
    return 'https://www.soft8soft.com/docs/manual/en/index.html'

def getAppManagerHost(includeScheme=True):
    if includeScheme:
        return 'http://localhost:8668/'
    else:
        return 'localhost:8668'

def findExportedAssetPath(srcPath):

    dirname, basename = os.path.split(srcPath)

    for ext in ['.gltf', '.glb']:

        gltfname = os.path.splitext(basename)[0] + ext

        for path in [os.path.join(dirname, gltfname),
                     os.path.join(dirname, 'export', gltfname),
                     os.path.join(dirname, 'exports', gltfname)]:

            if os.path.exists(path):
                return path

    return None

def getPlatformBinDirName():
    """
    linux_x86_64, windows_amd64, darwin_arm64, etc...
    """
    return platform.system().lower() + '_' + platform.machine().lower()

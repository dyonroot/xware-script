#!/usr/bin/env python3

import os

LOCAL_PATH = "/home/qweroot/Downloads/TDDownloads"
PROFILE_DIR = "/home/qweroot/.xware-desktop/profile"


def pathSplit(path):
    return list(filter(bool,path.split("/")))

def trySymlink(src, dest):
    # ignores the exception when dest is already there.
    try:
        os.symlink(src, dest)
    except FileExistsError:
        pass

def tryMkdir(pathstr):
    # mimics "mkdir -p"
    try:
        print("mkdir -p %s" % (pathstr))
        Path(pathstr).mkdir(parents = True)
    except FileExistsError:
        pass

def _mountBootstrap(localPath):

    backslashed = "\\".join(pathSplit(localPath))

    mntDir = os.path.join(PROFILE_DIR, "mnt", backslashed)

    tddownloadDir = os.path.join(mntDir, "TDDOWNLOAD")
    thunderdbDir = os.path.join(mntDir, "ThunderDB")

    # 
    # tryMkdir(thunderdbDir)
    # trySymlink(localPath, tddownloadDir)

    print("tddownloadDir=" + tddownloadDir)
    print("thunderdbDir=" + thunderdbDir)

    return mntDir


def main():
    mntPath = _mountBootstrap(LOCAL_PATH)

    buf = list()
    buf.append("{localPath} {mntPath} auto defaults,rw 0 0"
            .format(localPath=LOCAL_PATH, mntPath=mntPath))
    buf.append("")

    with open("mounts", "w", encoding="UTF-8") as mountFile:
        mountFile.writelines("\n".join(buf))

if __name__ == "__main__":
    main()

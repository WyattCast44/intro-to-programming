from pathlib import Path as PathLib


class Filesystem:

    """
    An 80% use-case wrapper around the Path library.
        Read More: https://docs.python.org/3/library/pathlib.html
    """

    @staticmethod
    def exists(path):
        return PathLib.exists(path)

    @staticmethod
    def touch(path, errorIfExists=True):
        PathLib(path).touch(exist_ok=not errorIfExists)

    @staticmethod
    def mkdir(path, makeParents=True, errorIfExists=True):
        PathLib(path).mkdir(parents=makeParents, exist_ok=not errorIfExists)

    @staticmethod
    def ensureFileExists(path, contents=None):
        Filesystem.touch(path, errorIfExists=False)

    @staticmethod
    def ensureDirectoryExists(path):
        Filesystem.mkdir(path, errorIfExists=False)

    @staticmethod
    def isDir(path):
        return PathLib.is_dir(path)

    @staticmethod
    def isFile(path):
        return PathLib.is_file(path)

    @staticmethod
    def isSymlink(path):
        return PathLib.is_symlink(path)

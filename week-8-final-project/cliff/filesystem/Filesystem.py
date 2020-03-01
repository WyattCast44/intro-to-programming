from pathlib import Path


class Filesystem:

    @staticmethod
    def ensureDirExists(fullPath):
        Filesystem.mkdir(fullPath, True, False)

    @staticmethod
    def mkdir(fullPath, makeParents=True, errorIfExists=False):
        Path(fullPath).mkdir(parents=makeParents, exist_ok=errorIfExists)

    @staticmethod
    def ensureFileExists(fullPath):
        Filesystem.touch(fullPath, errorIfExists=False)

    @staticmethod
    def touch(fullPath, errorIfExists=False):
        Path(fullPath).touch(exist_ok=errorIfExists)

    @staticmethod
    def writeLines(fullPath, lines):

        f = open(Path(fullPath), 'w')

        for line in lines:
            f.write(f'{line}\n')

        f.close()

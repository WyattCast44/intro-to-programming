from pathlib import Path


class Filesystem:

    @staticmethod
    def ensureDirExists(fullPath):
        Path(fullPath).mkdir(parents=True, exist_ok=True)

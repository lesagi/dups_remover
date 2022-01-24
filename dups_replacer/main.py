import fire

from .duplicates_remover import DuplicatesRemover
from .duplicates_scanner import DuplicatesScanner
from .file_system_adapter import FileSystemAdapter
from .files_registry import FileRegistry
from .hash_util import HashUtil


def remove_duplicates(path):
    if not path:
        raise Exception('You must provide a path argument')

    hash_util = HashUtil()
    registry = FileRegistry(hash_util)
    fs_adapter = FileSystemAdapter()
    duplicates_locator = DuplicatesRemover(fs_adapter, registry, path)
    duplicates_locator.scan_files_for_duplicates()


def identify_duplicates(path):
    if not path:
        raise Exception('You must provide a path argument')

    hash_util = HashUtil()
    registry = FileRegistry(hash_util)
    fs_adapter = FileSystemAdapter()
    duplicates_locator = DuplicatesScanner(fs_adapter, registry, path)
    duplicates_locator.scan_files_for_duplicates()


def main():
    fire.Fire()


if __name__ == '__main__':
    main()

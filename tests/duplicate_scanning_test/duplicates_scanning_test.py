import pytest

from dups_replacer.duplicates_scanner import DuplicatesScanner
from dups_replacer.files_registry import FileRegistry
from dups_replacer.hash_util import HashUtil
from tests.duplicate_scanning_test.mock_fs_adapter import MockFSAdapter


@pytest.fixture(scope='function')
def duplicates_scanner():
    return DuplicatesScanner(MockFSAdapter(), FileRegistry(HashUtil()), "/")


def test_identifying_duplicates(duplicates_scanner):
    duplicates_scanner.scan_files_for_duplicates()
    [duplicate_file_registry] = get_duplicate_files_registry(duplicates_scanner)
    duplicates_full_paths = get_duplicates_full_paths(duplicates_scanner, duplicate_file_registry)

    assert len(duplicate_file_registry['duplicates']) == 2
    assert duplicates_full_paths == ['/test/mock1/dir/filename1', '/test/mock2/dir/filename2', '/test/mock3/dir/filename1']


def get_duplicate_files_registry(duplicates_scanner):
    duplicates = []
    files_registry = duplicates_scanner.registry.registry
    for file_key in files_registry:
        if files_registry[file_key]['duplicates']:
            duplicates.append(files_registry[file_key])

    return duplicates


def get_duplicates_full_paths(scanner, registry):
    paths = []

    original_file_dir_path = registry['dir_path']
    original_file_filename = registry['filename']
    paths.append(scanner.fs_adapter.get_file_full_path(original_file_dir_path, original_file_filename))

    for duplicate in registry['duplicates']:
        paths.append(scanner.fs_adapter.get_file_full_path(duplicate['dir_path'], duplicate['filename']))

    return paths

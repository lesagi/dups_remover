import pytest

from dups_replacer.files_registry import FileRegistry
from dups_replacer.hash_util import HashUtil
from tests.utils.mocks_util import create_mock_file_from_text, reset_mock_file_read_pointer_position


@pytest.fixture(scope='function')
def registry_instance():
    return FileRegistry(HashUtil())


def test_file_registration(registry_instance):
    dir_path = "/root/test/path/"
    filename = "mock_filename.co"
    registry_key = "mock_registry_key"

    registry_instance.register_file(registry_key, dir_path, filename)

    file_registry = registry_instance.registry[registry_key]
    assert file_registry['dir_path'] == dir_path
    assert file_registry['filename'] == filename
    assert file_registry['duplicates'] == []


def test_key_generation_uniqueness(registry_instance):
    mock_file_1 = create_mock_file_from_text('This is a mock file data')
    mock_file_2 = create_mock_file_from_text('This is a different mock file data')

    registry_key_1 = registry_instance.get_file_key(mock_file_1)
    registry_key_2 = registry_instance.get_file_key(mock_file_2)

    assert registry_key_1 != registry_key_2


def test_key_generation_dependency_from_previous_files(registry_instance):
    mock_file_1 = create_mock_file_from_text('This is a mock file data')
    registry_key_1 = registry_instance.get_file_key(mock_file_1)

    mock_file_2 = create_mock_file_from_text('This is a different mock file data')
    registry_instance.get_file_key(mock_file_2)

    reset_mock_file_read_pointer_position(mock_file_1)
    registry_key_1_copy = registry_instance.get_file_key(mock_file_1)

    mock_file_2.close()
    mock_file_1.close()

    assert registry_key_1 == registry_key_1_copy




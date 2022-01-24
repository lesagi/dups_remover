import os

from tests.utils.mocks_util import create_mock_file_from_text

DUPLICATE_FILE_CONTENT = 'mock duplicate file content'
ORIGINAL_FILE_DIR_PATH = '/test/mock1/dir/'
ORIGINAL_FILE_NAME = 'filename1'

files_records = [
    {
        'dir_path': ORIGINAL_FILE_DIR_PATH,
        'filename': ORIGINAL_FILE_NAME,
        'content': DUPLICATE_FILE_CONTENT
    },
    {
        'dir_path': '/test/mock2/dir/',
        'filename': 'filename2',
        'content': DUPLICATE_FILE_CONTENT
    },
    {
        'dir_path': '/test/mock3/dir/',
        'filename': 'filename1',
        'content': DUPLICATE_FILE_CONTENT
    },
    {
        'dir_path': '/test/mock4/dir/',
        'filename': 'filename4',
        'content': 'random_content'
    },
    {
        'dir_path': '/test/mock5/dir/',
        'filename': 'filename5',
        'content': 'random_content 2'
    }
]


class MockFSAdapter:
    def __init__(self):
        self.files_list_by_path = self.get_files_list_by_path()

    def get_files_list(self, path):
        for file in files_records:
            yield file['dir_path'], file['filename']
        return

    def get_file_full_path(self, dir_path, filename):
        return os.path.join(dir_path, filename)

    def load_file(self, file_path):
        content = self.files_list_by_path[file_path]
        return create_mock_file_from_text(content)

    def close_file(self, file):
        file.close()

    def get_absolute_path(self, path):
        return path

    def get_path_basename(self, path):
        return os.path.basename(path)

    def get_path_dirname(self, path):
        return os.path.dirname(path)

    def is_link(self, file_path):
        return False

    def get_link_target(self, link_file):
        return ""

    def get_files_list_by_path(self):
        files_list = {}

        for file in files_records:
            abs_path = self.get_file_full_path(file['dir_path'], file['filename'])
            files_list[abs_path] = file['content']

        return files_list

import os
from pathlib import Path


class FileSystemAdapter:
    def get_files_list(self, path):
        for dir_path, dir_names, file_names in os.walk(path):
            abs_dir_path = self.get_absolute_path(dir_path)
            for filename in file_names:
                yield abs_dir_path, filename
        return

    def get_file_full_path(self, dir_path, filename):
        return os.path.join(dir_path, filename)

    def load_file(self, file_path):
        return open(file_path, 'rb')

    def close_file(self, file):
        file.close()

    def get_absolute_path(self, path):
        return os.path.abspath(path)

    def get_path_basename(self, path):
        return os.path.basename(path)

    def get_path_dirname(self, path):
        return os.path.dirname(path)

    def is_link(self, file_path):
        return os.path.islink(file_path)

    def get_link_target(self, link_file):
        return Path(link_file).resolve()

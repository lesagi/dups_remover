import os
from .duplicates_scanner import DuplicatesScanner


class DuplicatesRemover(DuplicatesScanner):
    def handle_duplicate(self, file_registry_key, duplicate_path):
        dir_path = self.fs_adapter.get_path_dirname(duplicate_path)
        filename = self.fs_adapter.get_path_basename(duplicate_path)
        self.registry.register_duplicate(file_registry_key, dir_path, filename)

        file_registry = self.registry.get_file_registry(file_registry_key)
        original_file_path = self.fs_adapter.get_file_full_path(file_registry['dir_path'], file_registry['filename'])

        os.remove(duplicate_path)
        os.symlink(original_file_path, duplicate_path)

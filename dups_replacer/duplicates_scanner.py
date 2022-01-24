class DuplicatesScanner:
    def __init__(self, fs_adapter, registry, path):
        self.fs_adapter = fs_adapter
        self.registry = registry
        self.path = path

    def scan_files_for_duplicates(self):
        for dir_path, filename in self.fs_adapter.get_files_list(self.path):
            file_path = self.fs_adapter.get_file_full_path(dir_path, filename)
            file = self.fs_adapter.load_file(file_path)
            file_registry_key = self.registry.get_file_key(file)
            self.fs_adapter.close_file(file)

            if self.fs_adapter.is_link(file_path):
                self.handle_link(file_registry_key, file_path)
            elif self.is_duplicate(file_registry_key):
                self.handle_duplicate(file_registry_key, file_path)
            else:
                self.register_file(file_registry_key, file_path)

    def is_duplicate(self, file_registry_key):
        return self.registry.get_file_registry(file_registry_key) is not None

    def register_file(self, file_registry_key, file_path):
        dir_path = self.fs_adapter.get_path_dirname(file_path)
        filename = self.fs_adapter.get_path_basename(file_path)
        self.registry.register_file(file_registry_key, dir_path, filename)

    def handle_link(self, file_registry_key, link_path):
        pass

    def handle_duplicate(self, file_registry_key, duplicate_path):
        dir_path = self.fs_adapter.get_path_dirname(duplicate_path)
        filename = self.fs_adapter.get_path_basename(duplicate_path)
        self.registry.register_duplicate(file_registry_key, dir_path, filename)

        file_registry = self.registry.get_file_registry(file_registry_key)
        original_file_path = self.fs_adapter.get_file_full_path(file_registry['dir_path'], file_registry['filename'])
        print(f"Duplicate found: %s and %s" % (original_file_path, duplicate_path))

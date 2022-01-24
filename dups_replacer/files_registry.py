class FileRegistry:
    registry = {}

    def __init__(self, hash_util):
        self.hash_util = hash_util

    def get_file_key(self, file):
        self.hash_util.reset()
        for chunk in self.read_file_in_chunks(file):
            self.hash_util.update(chunk)

        return self.hash_util.digest()

    def read_file_in_chunks(self, file, chunk_size=1024):
        """Generator that reads a file in chunks of bytes"""
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                return
            yield chunk

    def get_file_registry(self, file_registry_key):
        return self.registry.get(file_registry_key, None)

    def register_file(self, file_registry_key, dir_path, filename):
        self.registry[file_registry_key] = {"dir_path": dir_path, "filename": filename, "duplicates": []}

    def register_duplicate(self, file_registry_key, dir_path, filename):
        file_registry = self.get_file_registry(file_registry_key)
        file_registry['duplicates'].append({"dir_path": dir_path, "filename": filename})

    def register_link(self, file_registry_key, dir_path, filename):
        pass

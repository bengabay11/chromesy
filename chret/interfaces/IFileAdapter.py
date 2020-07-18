

class IFileAdapter(object):
    def write(self, data, output_file_path):
        raise NotImplementedError

    def read(self, path):
        raise NotImplementedError



class ObjectFactory(object):
    def __init__(self):
        self._builders = {}

    def register_builder(self, key, builder):
        self._builders[key] = builder

    def create(self, key, exception=ValueError, **kwargs):
        builder = self._builders.get(key)
        if not builder:
            raise exception(key)
        return builder(**kwargs)

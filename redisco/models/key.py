from six import PY3

if PY3:
    unicode = basestring = str

class Key(unicode):
    def __getitem__(self, key):
        return Key(u"%s:%s" % (self, key))

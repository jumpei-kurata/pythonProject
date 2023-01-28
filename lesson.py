import contextlib
import os

try:
    os.remove('somefile.tmp')
except FileNotFoundError:
    pass

with contextlib.suppress(FileNotFoundError):
    os.remove('somfile.tmp')

def tag(f):
    def _wrpper():
        print('<h2>')
        r = f()
        print('</h2>')
        return r
    return _wrpper()
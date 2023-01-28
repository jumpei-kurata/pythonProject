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



import sys
import logging

x = input('Enter:')
print(x)

for line in sys.stdin:
    print(line)

with open('stdout.log', 'w') as f:
    with contextlib.redirect_stdout(f):
    print('hello')
# sys.stdout.write('hello')

logging.error('Error!')
sys.stderr.write('Error!')


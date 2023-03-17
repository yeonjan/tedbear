import sys

try:
    no_start, no_end = sys.argv[1:]
    print(no_start, no_end)
except:
    print('error')

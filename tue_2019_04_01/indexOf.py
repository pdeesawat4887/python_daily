import re


def indexOf(string, pattern):
    p = re.compile(pattern)
    for m in p.finditer(string):
        print("Index of pattern in string: {}".format(m.start()))


indexOf('Hello World World', 'World')

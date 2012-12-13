### triangular.py
# server
source = dict(zip(range(100), range(100)))

def final(key, value):
    print key, value

# client
def mapfn(key, value):
    for i in range(value + 1):
        yield key, i

def reducefn(key, value):
    return sum(value)

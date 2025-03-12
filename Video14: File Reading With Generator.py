# source: https://stackoverflow.com/questions/519633/lazy-method-for-reading-big-file-in-python

def read_in_chunks(file_object, chunk_size=1024):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data


with open('romeonjuliet.txt') as f:
    for piece in read_in_chunks(f):
        print(piece)
        
        
# source: https://www.dataquest.io/blog/python-generators-tutorial/
data = "sample.csv"
lines = (line for line in open(data, encoding="ISO-8859-1"))
for line in lines:
    cells = line.split(",")
    for c in cells:
        print(c.strip(), end="\t")
    print("")

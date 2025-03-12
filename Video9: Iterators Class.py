class MyIterator:
    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        self.n += 1
        if self.n <= 10:
            return self.n
        else:
            raise StopIteration

obj = MyIterator()
it = iter(MyIterator())
for i in it:
    print(i)


class NewIterator:
    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        self.n += 1000
        if self.n <= 10000000000000:
            return list(range(self.n-1000,self.n))
        else:
            raise StopIteration

for stream_data in NewIterator():
    for data in stream_data:
        print(data)



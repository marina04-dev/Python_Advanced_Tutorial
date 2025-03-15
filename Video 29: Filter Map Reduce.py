# Map Function Example 
print(list(map(lambda x,y: x+y, [1,2,3], [4,5,6])))

print(dict(list(map(lambda x,y:
                    (x,y), [1,2,3],
                    ["one", "two", "three"]))))

print(list(map(lambda x,y,z:
               {"id": x, "name": y, "grade": z},
                    (i for i in range(1000)),
                    ["Bob", "Tom", "Pat"],
                    [5,8,2])))
                    
                    
                    
            
# Filter Example 
print([x for x in ["aba","anna","baba","aa","baa"] if x == x[::-1]])

print(list(filter(lambda x: x==x[::-1], ["aba","anna","baba","aa","baa"])))


# Reduce Example
from functools import reduce

students = [
    {
        "name": "Bob",
        "grade": 5,
    },
    {
        "name": "Pat",
        "grade": 7
    },
    {
        "name": "Tom",
        "grade": 2
    }
]



# students that passed
print(reduce(lambda x, y: x+[y["name"]] if y["grade"]>=5 else x, students, []))

# get the entries with just the names of students that passed
print(reduce(lambda x, y: x+[{"name": y["name"]}] if y["grade"]>=5 else x, students, []))

# student with lowest grade
print(reduce(lambda x, y: x if x["grade"] < y["grade"] else y,students, (students[0])))

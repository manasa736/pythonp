sample_dict = {
    "name": "manasa",
    "age": 25,
    "salary": 8000,
    "city": "new york"
}

#keys to remove
keys = ["name", "salary"]

d=dict()
for i in sample_dict.keys()-keys:
    d[i]=sample_dict[i]

print(d)

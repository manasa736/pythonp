sample_dict = {
    "name": "manasa",
    "age": 25,
    "salary": 8000,
    "city": "new york"
}

#keys to remove
keys = ["name", "salary"]



for k in keys:
    sample_dict.pop(k)
print(sample_dict)

sample_dict = {
    "name": "manasa",
    "age": 25,
    "salary": 8000,
    "city": "new york"}
keys = ["name", "salary"]


#newDict={}
res = dict()
for k in keys:
    res.update({k: sample_dict[k]})
print(res)

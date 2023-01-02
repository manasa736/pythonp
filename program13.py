sample_dict = {
    "name": "manasa",
    "age": 25,
    "salary": 8000,
    "city": "new york"
}

sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)

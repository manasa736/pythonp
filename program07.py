employees = ['Manohar', 'Prasad', 'Manasa']
default = {"designation": 'Developer', "salary": 80000}

data = dict.fromkeys(employees, default)
print(data)

print(data["Manasa"])

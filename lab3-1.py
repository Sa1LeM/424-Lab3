employees = {}
cont = True
while cont :
    name = input("Employee name:")
    if name == "no":
        cont = False
    else:
        employees[name] = int(input("Salary: "))


print(employees)
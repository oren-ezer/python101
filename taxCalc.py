def taxRequired(age):
    result = None
    if age >= 18 and age <= 65:
        result = True
    else:
        result = False
    return result


name = "yaniv"
age = 17

myResult = taxRequired(age)
if myResult:
    print(name + " is required to pay taxes")
else:
    print(name + " is NOT required to pay taxes")

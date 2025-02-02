sd = {"ID1":{"Name":"Bob","Grade":"3","Subjects":["Maths","English"]}, 
    "ID2":{"Name":"Jake","Grade":"2","Subjects":["Maths","English"]},
    "ID3":{"Name":"Jake","Grade":"2","Subjects":["Maths","English"]},
    "ID4":{"Name":"Jake","Grade":"2","Subjects":["Maths","English"]}}

result = {}

for key,value in sd.items():
    if value not in result.values():
        result[key] = value

print(result)

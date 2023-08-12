# DICTIONARY
person={"name":"Can", "language":["python","java"]}
result=person["name"]                    #prints Can
print(result)

# CHANGING THIS DICT TO STRING
#person_string ='{"name":"Can", "language":["python","java"]}'
#result=person("name")                  #it wont work anymore because person_string is not dictionary

# JSON STRING TO DICTIONARY
import json

person_string ='{"name":"Can", "language":["python","java"]}'
result= json.loads(person_string)         # Converts the string into a dictionary
result=person["name"]                     #prints Can
print(result)

#
with open("person.json") as f:
    data=json.load(f)         # json.load() function is used to read and parse JSON data from a file
    print(data)

# DICTIONARY TO JSON STRING

person_dict={"name":"can","languages": ["python","java"]}

result=json.dumps(person_string)            # Converts the string into a dictionary
print(result)

#
with open("person.json",'w') as f:
    json.dump(person_dict,f)


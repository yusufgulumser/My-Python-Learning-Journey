import requests
import json

result=results.get('https://jsonplaceholder.typicode.com/todos')  #Fetching json data from url and storing in a variable in python 
result=json.loads(result.text)

for i in result:
    print(i['title'])
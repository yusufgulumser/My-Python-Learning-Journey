import requests
import json

api_url = "https://api.exchangeratesapi.io/latest?base="

Converted_money = input("Converted money type: ")
received_money = input("received money type: ")
Amount = int(input(f"how much {Converted_money} you want to convert: "))

result = requests.get(api_url+Converted_money)          # appends USD or etc at the end of the url
result = json.loads(result.text)

print("1 {0} = {1} {2}".format(Converted_money, result["rates"][received_money], received_money))  # '0'=Converted money, '1'=conversion rate '2'= received money
print("{0} {1} = {2} {3}".format(Amount, Converted_money, Amount * result["rates"][received_money],received_money))
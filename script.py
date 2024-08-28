import requests

with open('Files/base64_files/test', 'r', encoding='utf-8') as file:
    encoded_data = file.read()

with open('Files/base64_files/test1', 'r', encoding='utf-8') as file:
    encoded_data1 = file.read()

with open('Files/base64_files/test2', 'r', encoding='utf-8') as file:
    encoded_data2 = file.read()

with open('Files/base64_files/test3', 'r', encoding='utf-8') as file:
    encoded_data3 = file.read()

with open('Files/base64_files/test4', 'r', encoding='utf-8') as file:
    encoded_data4 = file.read()

url = 'http://127.0.0.1:80'
payload = {
    'image_base64': encoded_data
}
headers = {
    'Content-Type': 'application/json'
}
response = requests.post(url, json=payload, headers=headers)
import requests

r = requests.get('http://127.0.0.1:5000/employee/jumpei')
print(r.text)

r = requests.post('http://127.0.0.1:5000/employee', data={'name': 'jumpei'})
print(r.text)

r = requests.put('http://127.0.0.1:5000/employee', data={'name': 'jumpei', 'new_name': 'kurata'})
print(r.text)

r = requests.delete('http://127.0.0.1:5000/employee', data={'name': 'jumpei'})
print(r.text)
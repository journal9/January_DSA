import requests
from urllib.parse import urljoin
import json
base_url = 'https://reqres.in/'

#get from api
get_url = urljoin(base_url,'api/users') 
query_params = {'page':1}
r = requests.get(url=get_url,params=query_params)
print(r.status_code)
print(r.text)
print("-------------------")
print(r.request)
print(r.request.headers)
# if r.raise_for_status:
#     print(r.raise_for_status)
# else:
#     print(False)

# #post from api
# post_url = urljoin(base_url,'api/users')
# create_data = {
#     "name": "morpheus",
#     "job": "leader"
# }
# p = requests.post(url=post_url,json=create_data)
# print(p.status_code)
# print(p.text)
# print(p.headers)
# print(p.encoding)
# print(p.content)
# print(p.json)
# if p.status_code == requests.codes.no_content:
#     print('hi')
# if p.status_code == requests.codes.created:
#     print('hello')    

# #update users api
# patch_url = urljoin(base_url,'api/users/864')
# headers = {'user-agent': 'my-app/0.0.1'}
# update_data = {
#     "name": "popoye",
#     "job": "bruno"
# }
# u = requests.patch(url=patch_url,json=update_data)
# print(u.content)
# print(u.headers)

s = requests.Session()
s.headers.update({'x-test1':'true'}) # persists
t = s.get('https://httpbin.org/cookies/set/sessioncookie/123456780',headers={'x-test2': 'true'})
#method level parameters override session parameters
print(t.text)

t = requests.Session()
w = t.get('https://httpbin.org/cookies',cookies={'from-my':'i-pad'})
print(w.text)
print(w.request) # a prepared request is returned
# PreparedRequest that was used. In some cases you may wish to do some extra
# work to the body or headers (or anything else really) before sending a request. 



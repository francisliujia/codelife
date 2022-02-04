import requests

# r = requests.get('https://xkcd.com/353/')
# r = requests.get('https://imgs.xkcd.com/comics/python.png')

# payload = {'page':2, 'count':25}
payload = {'username': 'corey', 'password': 'testing'}
# r = requests.get('https://httpbin.org/get', params=payload)
# r = requests.post('https://httpbin.org/post', data=payload)
# r = requests.get('https://httpbin.org/basic-auth/corey/testing',auth=('corey','testing'))
# r = requests.get('https://httpbin.org/basic-auth/corey/testing',timeout=(3))
r = requests.get('https://httpbin.org/delay/6',timeout=(3))

print(r)
# print(r.text)
# r_dict = r.json()

# print(r_dict['form'])
# print(r.json())
# print(r.url)


# print(r)

# print(dir(r))
# print(help(r))
# print(r.text)
# print(r.content)


# print(r.status_code)

# print(r.ok)
# print(r.headers)


# with open('comic.png', 'wb') as f:
# 	f.write(r.content)

# print(__file__('comic.png'))




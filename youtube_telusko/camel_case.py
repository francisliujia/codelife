import re


def camel_case(name):
  name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
  return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()


print(camel_case('myFirstName'))
print(camel_case('OnlineUsers'))
print(camel_case('Address'))
print(camel_case('validHTTPRequest'))
print(camel_case('Helloworld')) 
print(camel_case('validHTTPmel_case'))
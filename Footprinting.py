import requests
from tqdm import tqdm
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# testing availability of http method
url = input("Enter target URL => ")
http_list_method = ['GET','POST','PUT','DELETE','OPTIONS','TRACE','TEST']

print("finding http method.." )

for method in tqdm(http_list_method, desc='Progress'):
    req = requests.request(method,url)
    print(f'Method:{method},req.status_code: {req.status_code},req.reason: {req.reason}')

print("*"*50)

# footprinting of http headers
print('Finding Http headers...')
http_list_headers = ['Server','X-Powered-BY','X-Country-Code','Connection','Content-Length']
re = requests.get(url)
for head in http_list_headers:
    try:
        res = re.headers[head]
        print('%s:%s' % (head,res))
    except Exception as err:
        print('%s: No Details Found' % head)

#Testing vulnerabilities
print("*"*50)
print('Testing vulnerabilities...')
try:
    t_Xss = re.headers['X-XSS-Protection']
    if t_Xss != '1; mode=block':
        print(f'X-XSS-Protection not set properly. It may be vulnerable to XSS.')
except KeyError:
    print('X-XSS-Protection not set. It may be vulnerable to XSS.')


import requests

url = 'http://34.136.213.223/'

r = requests.get(url)

if __name__=='__main__':
    print(r.text)
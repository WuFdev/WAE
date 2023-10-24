import requests
from urllib.parse import urlparse

server = input("Python file to run: ")

def Include(includePath):
  parsed_url = urlparse(server)
  host_url = parsed_url.netloc
  exec(host_url + includePath)
  
response = requests.get(server)
content = response.text

print("running from:" + " " + server)
exec(content)


import requests as rq

def Net():
  url = 'https://www.google.com/'
  timeout = 5

  response = req.get(url, timeout=timeout)
  print(f'RESPONSE: {response}')
  return True

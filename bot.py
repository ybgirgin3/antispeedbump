from utils import headers
import requests
import json
import sys

url = "https://www.instagram.com/api/v1/users/web_profile_info/?username=kimkardashian"

data = requests.get(url, headers=headers).text
print(data)

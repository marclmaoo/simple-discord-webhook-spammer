import requests
import time

webhook_url = input("enter webhook url to be spammed: ")
message = input("enter msg:")
data = {"content": message}
interval = 0.1  # Time interval in seconds

while True:
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print("msg sent, made by marclmao")
    else:
        print(f"ur prolly being ratelimited, check the status code to be sure staus code: {response.status_code}")

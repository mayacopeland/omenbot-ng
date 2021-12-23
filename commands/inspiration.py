import requests

def inspire():
    return requests.get("https://inspirobot.me/api?generate=true").text
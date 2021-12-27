import requests

def inspire() -> str:
    return requests.get("https://inspirobot.me/api?generate=true").text
import requests
import json

class runtimes():
    def __init__(self, n, v, sh):
        self.name = n
        self.version = v
        self.short = sh

def create_classes():
    api_url = 'https://emkc.org/api/v2/piston/runtimes'
    res = requests.get(api_url)
    res_parsed = json.loads(res.content)
    runtime_classes = []
    for i in res_parsed:
        runtime = runtimes(i['language'], i['version'], i['aliases'])
        runtime_classes.append(runtime)
    return runtime_classes

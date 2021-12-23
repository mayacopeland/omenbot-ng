import requests
import json

def get_runtimes_api():
    api_url = 'https://emkc.org/api/v2/piston/runtimes'
    res = requests.get(api_url)
    res_parsed = json.loads(res.content)
    available_runtimes = []
    for i in res_parsed:
        available_runtimes.append(i['language'])
    runtimes_readable = ', '.join(available_runtimes)
    return f'The available runtimes are {runtimes_readable}.'


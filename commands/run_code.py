import requests

def run_code(args: [str], runtimes, random_reply) -> str:
    ticks = False
    if len(args) > 0 and '```' in args[0]:
        args = args[0].split("\n") + args[1:]
        ticks = True

    if len(args) == 0:
        return "Language cannot be empty"

    language = args[0]
    code = " ".join(args[1:]).replace("```", "")
    if ticks:
        code = code[1:]
    version = None

    if language == "javascript":
        version = "16.3.0"
    else:
        for i in runtimes:
            if i.name == language:
                version = i.version
    
    if "@" in code:
        return random_reply

    
    if version is None:
        return f"{language} does not exist as a runtime"

    request_params = {
            'language': language,
            'version': version,
            'files': [{'content': code}], 
            'args': '',
            'stdin':  "",
            'log': 0
    }
    piston_request = requests.post('https://emkc.org/api/v2/piston/execute',  json=request_params)
    request_json = piston_request.json()

    if "@" in request_json['run']['output']:
        return random_reply

    return request_json['run']['output'] if request_json['run']['output'] != "" else "Input is invalid (was it empty?)"
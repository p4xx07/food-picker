
import requests
import json

def execute(language, code):
    try:
        data = {"language": language, "source": code}
        body = json.dumps(data)
        response = requests.post("https://emkc.org/api/v1/piston/execute", data=body)
        jsonData = json.loads(response.text)
        stdout = jsonData["stdout"]
        if len(stdout) == 0:
            return "No stdout"
        return str(stdout)
    except Exception as e:
        print(e)
    return "Code not valid"

def execute_js(code):
    return execute("js", code)

def execute_c(code):
    return execute("c", code)

def execute_csharp(code):
    return execute("csharp", code)

def execute_python3(code):
    return execute("python3", code)

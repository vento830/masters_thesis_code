import requests
import json

url = "http://127.0.0.1:11434/api/chat"

payload = {
    "model": "llama3.2",
    "message": [{"role": "user", "content": "Who is the best Jedi"}]
}

response = requests.post(url, json=payload)#, stream=True)
print(response.status_code)
print(response)

if response.status_code == 200:
    print("Answer:")
    for line in response.iter_lines(decode_unicode=True):   
        if line:
            try:
                json_data = json.loads(line)
                if "message" in json_data and "content" in json_data["message"]:
                    print(json_data["message"]["content"])
            except json.JSONDecodeError:
                print("Error decoding JSON")
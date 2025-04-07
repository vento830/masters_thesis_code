from ollama import chat

# from pathlib import Path

# Pass in the path to the image
path = "/Users/marv/MAA/venv_pylon/final_setting.jpg"

# You can also pass in base64 encoded image data
# img = base64.b64encode(Path(path).read_bytes()).decode()
# or the raw bytes
# img = Path(path).read_bytes()

Vorlage ='

response = chat(
  model='llava',
  messages=[
    {
      'role': 'user',
      'content': 'please decribe this gear wheel',
      'images': [path],
    }
  ],
)

print(response.message.content)
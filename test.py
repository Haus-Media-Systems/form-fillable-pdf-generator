import requests

# API endpoint
url = "http://cl.imagineapi.dev/items/images/"

# Payload with the prompt
payload = {
    "prompt": "Cinematic Portrait, GodlyBeautiful french supermodel, dynamic lighting, [light + space of James Turrell + Bauhaus architectural forms], BeautyCore, Sharp Details --ar 21:9 --style raw"
}

# Replace <Your_API_Token> with your actual API token
headers = {
    'Authorization': 'Bearer k508t4wOkNFROc6QjuWVut3SJSpOS7EE',  # Your API token
    'Content-Type': 'application/json'
}

# Sending the request
response = requests.request("POST", url, headers=headers, json=payload)

# Printing the response from the API
print(response.text)
import requests
import time

# Hardcoded API URL and Key
API_URL = "https://api.runwayml.com/v1/generate"
API_KEY = "key_6c25811330d9f34d45665ffe8b1beebbe3774766f33c2739c33e640360933a3c6009caa6c76e481c505e53b29193e94c17b8c4ef39ab31314e2c10997a5b9ef9"

# Hardcoded headers
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Hardcoded prompt batch
prompts_batch = [
    {
        "prompt": "A dynamic close-up shot of the Space Ocean logo over a starry background, slowly pulling back to reveal a large space station orbiting Earth. The focus is on the sleek design and futuristic elements.",
        "length": 10,
        "parameters": {
            "dynamic_lens": "wide-angle",
            "set_design": "sleek",
            "camera_movement": "slow_zoom_out"
        }
    },
    {
        "prompt": "The SpaceX Starship 'PEZ' dispenser releases a PEZZtank into the void of space. The PEZZtank inflates gradually as it floats away, with Earth in the background.",
        "length": 8,
        "parameters": {
            "dynamic_lens": "medium-focus",
            "set_design": "cinematic",
            "camera_movement": "smooth_pan"
        }
    },
    {
        "prompt": "The PEZZtank in space being filled with water, slowly expanding. The visuals should highlight its form factor and fluid animation.",
        "length": 12,
        "parameters": {
            "dynamic_lens": "close-up",
            "camera_movement": "push-in"
        }
    },
    {
        "prompt": "A futuristic mission control room, with a team monitoring a PEZZtank mission. The screen displays live telemetry from space.",
        "length": 15,
        "parameters": {
            "camera_movement": "tracking",
            "set_design": "high-tech"
        }
    },
    {
        "prompt": "The Space Train flying through space, powered by a nuclear engine. The train moves steadily between Earth and Mars, with distant planets visible.",
        "length": 10,
        "parameters": {
            "camera_movement": "wide-shot",
            "set_design": "space_journey"
        }
    }
]

# Function to send batch requests with retry logic
def send_batch(prompts_batch, retries=3):
    for attempt in range(retries):
        response = requests.post(API_URL, headers=headers, json=prompts_batch)
        if response.status_code == 200:
            return response.json()  # Success
        else:
            print(f"Attempt {attempt + 1} failed. Retrying in 5 seconds...")
            time.sleep(5)
    return None  # If all retries fail

# Sending the hardcoded batch
results = send_batch(prompts_batch)
if results:
    print("Batch processed successfully:", results)
else:
    print("Failed after multiple attempts.")
import requests
import config

def getvoices():
    response = requests.get("https://api.elevenlabs.io/v1/voices")

    if response.status_code == 200:
        result0 = response.json()

        voice_ids = []
        names = []

        for voice in result0['voices']:
            voice_ids.append(voice['voice_id'])
            names.append(voice['name'])

        finaldata = dict(zip(names, voice_ids))
        return finaldata, names
    else:
        return f"Request failed with status code {response.status_code}"

voicemodels,_ = getvoices()

def genaudio(text, voice,):
    
    CHUNK_SIZE = 1024
    url = "https://api.elevenlabs.io/v1/text-to-speech/" + voicemodels[voice]

    headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": config.api_key
    }

    data = {
    "text": text,
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.3
    }
    }

    TTS_res = requests.post(url, json=data, headers=headers)
    if TTS_res.status_code == 200:
        # Convert audio content to bytes and return it
        return bytes(TTS_res.content)
    else:
        return None  # Handle the error appropriately in your code

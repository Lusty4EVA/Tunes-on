Greetings!


#project "Text Tunes"

Text Tunes is an AI-powered telegram bot designed to assist you in converting your text into audio.
This process, commonly referred to as text-to-speech technology, allows you to transform written content into spoken sound

## Disclaimer

Text Tunes is an independent project and is not affiliated with or sponsored by ElevenLabs. This project is purely for educational and entertainment purposes. All rights and credits for the underlying technology and APIs used in this project belong to their respective owners "elevenlabs.io" or "11.ai".

## Legal Notice

This project adheres to the guidelines set forth by the American copyright and intellectual property laws. It respects the rights of content creators and emphasizes fair use. The bot does not endorse, promote, or support any form of copyright infringement or unauthorized use of copyrighted material.
Use of this bot to generate audio content should comply with all relevant laws, including but not limited to the Digital Millennium Copyright Act (DMCA) and the Fair Use doctrine.
Remember that the responsibility for any content generated using this bot lies solely with the user. The developers of Text Tunes do not assume any liability for the use or misuse of the generated audio content.


## getting started

1. make sure you have installed git, python and pip
<pre>

sudo apt-get --upgrade


sudo apt-get install python3


sudo apt install pip

sudo apt-get install git

git clone https://github.com/Lusty4EVA/text-to-speech

</pre>

2. go to project dir and edit config.py with your info

<pre>

owner_id = [ ] 			 get this from Rose
api_key = " " 			 get this from elevenlabs.io/
api_id = 				 get this from my.telegram.org/apps
api_hash = ""			 get this from my.telegram.org/apps
bot_token = ""			 make your bot on t.me/BotFather and get the bot_token
bot_username = ""		 your bot's username
bot_name = ""			 your bot's name

</pre>

3. install all requirements
<pre>

pip install -r requirements.txt
```
</pre>

4. run main.py
<pre>

python3 main.py

</pre>
5. bot commands
<pre>

/start  - check if bot is deployed
/help	- to get into help section
/voices	- to get the all available voices (must set one)
/set	- to update the default voice
/say	- convert your text to speech

</pre>
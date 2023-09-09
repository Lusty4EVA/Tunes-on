from pyrogram import Client, filters
from pyrogram import types
import sys
import requests
import text_to_speech_api
import os
import config
import uuid
import io


bot = Client(
    config.bot_username, 
    api_id = config.api_id,
    api_hash = config.api_hash,
    bot_token = config.bot_token,
)
owner_ids = config.owner_id

@bot.on_message(filters.command('start'))
def command1(bot, message):
  welcomepic = config.welcomepic
  bot.send_photo(message.chat.id, welcomepic , caption=f'{config.welcometext}')


@bot.on_message(filters.command('help'))
def command1(bot, message):
  message.reply_text("🤔 this is the help section of the bot!\n\n type /voices to see the list of all available voices \n type /set to set the default voice of the bot used in text to speech \n  type /say following with your text to convert your text to audio \n type /help to see a list of available commands and their functions ")

groups = [-1001603453760,-1001764772937,-1001806950717,-1001233090829, -983045102]
msg = "welcome to the chat"
@bot.on_message(filters.chat(groups) & filters.new_chat_members)
def welcomebot(client , message):
  message.reply_text(msg)

@bot.on_message(filters.command('memes'))
def command3(bot, message):
  response = requests.get('https://meme-api.com/gimme')
  if response.status_code == 200:
    image = response.json()['preview'] [-1]
    bot.send_photo(message.chat.id, image)
  else:
    bot.send_message(message.chat.id, f"failed to fetch the image {response.status_code}")
    return None

@bot.on_message(filters.command('voices'))
def command1(bot, message):
  _,names = text_to_speech_api.getvoices()
  voices = '  , '.join(names)
  message.reply_text('Certainly, here is the current list of available voices. :)\n\n '+voices + '\n\n just type /set following with the voice name you want ;)')

@bot.on_message(filters.audio & filters.private)
def audio(bot , message):
  message.reply(message.audio.file_id)

@bot.on_message(filters.command('audio'))
def command4(bot, message):
  bot.send_audio(message.chat.id,"CQACAgUAAxkBAANxZLEd4rSfGe_VYrIM0HYu7xKwiVQAAvcLAAKCVZFV2c1Q0x0YXfoeBA")


input_data = "" 

@bot.on_message(filters.command('set'))
def set_voice_handler(bot, message):
    global input_data
    _, validnames = text_to_speech_api.getvoices()
    try:
      input_data = message.text.split("/set ", maxsplit=1)[1]
    except IndexError:
      return bot.send_message(message.chat.id, f"voice name cannot be empty")
    if not input_data:
        return bot.send_message(message.chat.id, f"set voice cannot be empty. Try again with a valid name: {input_data}")
    input_data = input_data.title()
    if input_data not in validnames:
        return bot.send_message(message.chat.id, f"{input_data} is not a valid name. Try again or get voice names just type /voices. ")
    else:
        bot.send_message(message.chat.id, f"default voice has been updated to {input_data}")


@bot.on_message(filters.command("say") & filters.text)
async def play_text_handler(_, msg):
  try:
      orig_text = msg.text.split("/say ", maxsplit=1)[1]
  except IndexError :
    return await bot.send_message(msg.chat.id, f"say command is empty try again with some text can you? :(")
  text1 = orig_text
  if not input_data:
    return await bot.send_message(msg.chat.id, f"Please set a voice first using the /set command before using the /say command")
  audio_data = text_to_speech_api.genaudio(text1, input_data)
  if audio_data is None:
        return await bot.send_message(msg.chat.id, f"Failed to generate audio. Please try again later.")

  audio_buffer = io.BytesIO(audio_data)
  audio_buffer.name = "output.mp3"

  await bot.send_audio(
      chat_id=msg.chat.id,
      audio=audio_buffer, 
      title="output.mp3"
  )

def is_owner(message):
    return message.from_user.id in owner_ids

@bot.on_message(filters.command("stop"))
def owner_command_handler(client, message):
    if is_owner(message):
        client.send_message(message.chat.id, "killswitch triggered!, all bot's processes has been terminated and the bot is shutting down \n cya soon I Guess :'( ")
        sys.exit()
    else:
        client.send_message(message.chat.id, "Sorry, this is an owner-only command. You are not authorized to use it.")


bot.run()
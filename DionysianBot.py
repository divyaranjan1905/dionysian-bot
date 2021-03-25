
"""
This is the bot for the Philosophy And Literature Group on Telegram. 
This document was first written on 11th Jan 2021 by Divya Ranjan, one of the admins of the group. 
This document would be undergoind several changes for months, with the support of other members/admins from the group. 
This was solely made for the purpose of administering the group and help the admins keep up with the intentions of the group 
"""
#Everything that we need for the metaphysical structure of this bot 
import os
import asyncio 
import math
import time
import pyrogram
import random 
import logging
import schedule  
from bs4 import BeautifulSoup 
from pyrogram import Client, filters , emoji  
from pyromod import listen
from config import api_id, api_hash , pw
from pyrogram.types import User, Chat, ChatMember, Message, Photo, MessageEntity, Audio, Document, Animation, Video, Voice, Thumbnail, Contact, Game, Location, Poll, ForceReply
from pyrogram.handlers import MessageHandler
from gtts import gTTS
from gtts.lang import tts_langs
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.schedulers.background import BackgroundScheduler
import emoji 
from libgen_api import LibgenSearch
from scihub import SciHub
from aphorisms import aphorisms
import wikipedia 

#Enable Logging

logging.basicConfig(
format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.DEBUG
                     )
logger = logging.getLogger(__name__)

app = Client("DionysianBot", api_id=api_id, api_hash=api_hash, bot_token= "1520740480:AAFmzNr57pNnWud7u5x7sFX0MDPi2kPA6Dw")

PhilosophyChat = "CorgitoReaders"
TestingBots = "TestingPhilosophicalBots"
User = "[{}](tg://user?id={})"


            
"""Testing aphorisms on BOT Testing Group"""
async def job():
    await app.send_message(chat_id='TestingPhilosophicalBots' , text = random.choice(aphorisms))

scheduler = AsyncIOScheduler()
scheduler.add_job(job, "interval", seconds=43200)

scheduler.start()

""""Send a random aphorism to CorgitoReaders"""
async def job():
    await app.send_message(chat_id='CorgitoReaders' , text = random.choice(aphorisms))

scheduler = AsyncIOScheduler()
scheduler.add_job(job, "interval", seconds=10800)

scheduler.start()


"""Send a message when the command /start is used """
@app.on_message(filters.command("start@DionysianBot", prefixes="/") | filters.command("start", prefixes="/")) 
async def start(client, message):
        await message.reply_text(text = "The Dionysian Ubermensch among @CorgitoReaders. I'd do anything for you if you bring me wine, so, when are we having a drink ? " + emoji.emojize(":clinking_glasses:") , quote = True )


"""Generate a random aphorism when /quote is used"""
@app.on_message(filters.command("quote", prefixes="/") | filters.command("quote@DionysianBot", prefixes="/"))
async def quote(client, message):
        await message.reply_text(text = "Here's something that can rack your brains : " + random.choice(aphorisms) , quote=True) 


#Welcoming members in a philosophical manner 
Welcome = [
            "Umhmmm...so somehow you made it until here, do you know how boring this chat is ? I hope you have something interesting. Meanwhile, wanna have a glass of wine ?" + emoji.emojize(":clinking_glasses:"),
            "Hello! fellow human, I'm a bot but I can drink wine does that make me less of a bot and more of a human ? Also how have you been lately ?" + emoji.emojize(":clinking_glasses:"),
            "Hmmm....what do you think about nihilism ? Do you think it's all meaningless ? I mean, maybe, but I'm sure that wine isn't meaningless, how can it be ?" + emoji.emojize(":wine_glass:"),
            "Do you know that your entry has made me so happy, that I'm gonna continue bullying Divya for the next hour or so ?"
            "Wittgenstein said __Whereof one cannot speak, thereof one must be silent.__. But I'm sure you can speak, right ? Say me something interesting about yourself." + emoji.emojize(":grapes:"),
            "Do you know that the fact that you joined right now to this group was something that was determined to happen ? It couldn't have been otherwise, you were destined to be with us. Now as you are with us, I hope we can have some wine together while discussing philosophy." + emoji.emojize(":clinking_glasses:"),
            "Do you like talking about philosophy and essentially exploring the underlying substructure behind everything ? You're at the right place, a lot of bored folkd here have nothing better to do other than, hopefully you can be one of them." +emoji.emojize(":clinking_glasses:") , 
            "What was the last dream you had ? Have you tried analyzing it ? If not, we've got a few psychoanalysis enthusiasts here, they might help you out and you might get to have some insight about them and yourself"
            ]          

"""Welcome someone with a cool message"""
@app.on_message(filters.chat([TestingBots, PhilosophyChat]) & filters.new_chat_members)
async def welcome(client, message):        
        await message.reply_text(random.choice(Welcome), quote=True)

norms = "<p>You&apos;ll be able to figure out everything else as you go, but just remember some of these : <br>1. Don&apos;t take any opinion as the greatest truth, question everything. <br>2. Don&apos;t be afraid or indulge into emotions while having conversations. <br>3. Be civil during conversations and respect the human you&apos;re talking to. <br>4. Always share content with context. <br>5. We appreciate that you tell us about your day, in fact we encourage you to do so, but try to maintain the topic in a more higher intellectual level.<br>6. Do not feed the trolls. <br>7. If you feel like insulted in some way, you can tell any admin present at the moment or use the #harsh tag. <br>8. Try to limit the use of bad words, you can use them, but try not to abuse. <br><br>We appreciate your stay in this sacred place. Thank you</p>"

"""Send the rules when /rules command is used in CorgitoReaders """
@app.on_message(filters.chat(PhilosophyChat) & filters.command("rules@DionysianBot", prefixes="/"))
async def rules(client, message):
        soup = BeautifulSoup(norms , features= "html.parser")
        better = soup.get_text('\n')
        await message.reply_text(better, quote=True)

"""Send an audio from gTTS using /speak command"""

@app.on_message(filters.command("speak", prefixes="/")) 
async def text(client, message):
           userid = str(message.chat.id)
           if not os.path.isdir(f"./DOWNLOADS/{userid}"):
              os.makedirs(f"./DOWNLOADS/{userid}") 

           language = await client.ask(
           message.chat.id,
           "Plz enter an language code\n suppourt languages[click here](https://www.google.com/url?sa=t&source=web&rct=j&url=https://cloud.google.com/text-to-speech/docs/voices&ved=2ahUKEwir4pPLlr7uAhWLwjgGHQAVAQAQFjACegQIDBAC&usg=AOvVaw3Q_9UBb0Xo-ljg87RGPX-8&cshid=1611821833928)",
           reply_markup=ForceReply(True),
        )  

           language_to_audio = language.text.lower()
           if language.text.lower() not in tts_langs():
            await message.reply_text(
             "Unsupported Language Code",
             quote=True,
             parse_mode="md"
        )
           else:
                 a = await message.reply_text(
                 "processing",
                   quote=True,
                   parse_mode="md"
           )
           new_file  = "./DOWNLOADS" + "/" + userid + message.text + ".mp3"
           
           myobj = gTTS(text=message.text, lang=language_to_audio, slow=False)   
           myobj.save(new_file)
           await message.reply_audio(new_file)
           await a.edit(random.choice(aphorisms))
           
"""Gets a paper from SciHub using the given DOI"""
@app.on_message(filters.command("sci",prefixes="/"))
def sci(client, message):
    filters.command("sci", "/")
    DOI = message.command[-1]
    sh = SciHub()
    result = sh.fetch(DOI)
    if result:
        with open('output.pdf', 'wb+') as fd:
            fd.write(result.pdf)


"""Gets a summary from Wiki"""
@app.on_message(filters.command("w",prefixes="/"))
def wiki (client,message):
    filters.command("w","/")
    word = message.command[-1]
    message.replyText(wikipedia.summary(word),quote=True)
    

app.run()



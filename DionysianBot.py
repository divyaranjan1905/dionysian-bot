
"""
This is the bot for the Philosophy And Literature Group (@CorgitoReaders) on Telegram.
This document was first written on 11th Jan 2021 by Divya Ranjan, one of the admins of the group.
This document would be undergoing several changes for months, with the support of other members/admins from the group.
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
import requests
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
from scihub import SciHub
from aphorisms import aphorisms
import wikipedia
import urllib3
from gpytranslate import Translator

#Enable Logging

logging.basicConfig(level=logging.INFO)

bot_token = "1520740480:AAH9ocvGX1Tq3f_EC8DsNPFbXL5kLx2NOt0"

app = Client("DionysianBot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

PhilosophyChat = "CorgitoReaders"
TestingBots = "TestingPhilosophicalBots"

"""Supressing INSECURE RREQUEST from urllib Python"""
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


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
        await message.reply_text(text = "The Dionysian Ubermensch among @CorgitoReaders. I'd do anything for you if you bring me wine, so, when are we having a drink? " + emoji.emojize(":clinking_glasses:") , quote = True )


"""Generate a random aphorism when /quote is used"""
@app.on_message(filters.command("quote", prefixes="/") | filters.command("quote@DionysianBot", prefixes="/"))
async def quote(client, message):
        await message.reply_text(text = "Here's something that can rack your brains : " + random.choice(aphorisms) , quote=True)


#Welcoming members in a philosophical manner
Welcome = [
            "Umhmmm...so somehow you made it until here, do you know how boring this chat is? I hope you have something interesting. Meanwhile, wanna have a glass of wine?" + emoji.emojize(":clinking_glasses:"),
            "Hello! fellow human, I'm a bot but I can drink wine does that make me less of a bot and more of a human? Also how have you been lately?" + emoji.emojize(":clinking_glasses:"),
            "Hmmm....what do you think about nihilism? Do you think it's all meaningless? I mean, maybe, but I'm sure that wine isn't meaningless, how can it be?" + emoji.emojize(":wine_glass:"),
            "Wittgenstein said __Whereof one cannot speak, thereof one must be silent.__. But I'm sure you can speak, right? Say me something interesting about yourself." + emoji.emojize(":grapes:"),
            "Do you know that the fact that you joined right now to this group was something that was determined to happen? It couldn't have been otherwise, you were destined to be with us. Now as you are with us, I hope we can have some wine together while discussing philosophy." + emoji.emojize(":clinking_glasses:"),
            "Do you like talking about philosophy and essentially exploring the underlying substructure behind everything? You're at the right place, a lot of boring folks here have nothing better to do other than that, hopefully you can be one of them." +emoji.emojize(":clinking_glasses:") ,
            "What was the last dream you had? Have you tried analyzing it? If not, we've got a few psychoanalysis enthusiasts here, they might help you out and you might get to have some insight about them and yourself",
            "Remember the mad Apollo? One of the famous maxims inscribed at his Temple in Delphi is __Know Thyself__. Do you think this has anything reasonable to it? How do you think one can start with 'knowing themselves'? And can we only do that with the Apollonian tools of reason? Doesn't being drunk on wine also help you 'know thyself', about something that reason could never reach? Anyways..who cares" + emoji.emojize(":clinking_glasses:") ,
            "Welcome to this sacred (aka boring) place! Here's a question for you from Nietzsche, my only true disciple : '__Are you genuine? or just a play-actor? A representative? or the actual thing represented? --Ultimately you are even just an imitation play-actor...__' Let's think through this together" + emoji.emojize(":clinking_glasses:"),
            "What do you think about the concept of dualism? Do yo believe that the mind and the consciousness exist in a world entirely different that from the material world? Does the material world exist without consciousness? Or would consciousness exist without the brain? Why not talk start discussing about it here?", 
            "Aha! So as you're finally here, have you tried wondering about __happiness__ and __pleasure__? Well there's certainly no __pleasure__ in being here, I can assure you that, but if you think about it sometimes we strive for __happiness__ with the unconscious assumption that it's actually __pleasure__. Do you think __pleasure__ is more fundamental than __happiness__, or the other way around? Can we ever get rid of the drive to __pleasure__ and at the same time can we ever achieve __happiness__ or __be happy__? Regardless, a glass of wine certainly promises pleasue for __me__, you wanna try one?" + emoji.emojize(":clinking_glasses:"),
            "Hmm...so you decided to join a __philosophy__ group somehow, do you think philosophy is the most fundamental field of knowledge from which every other field builds upon? Or do you think philosophy itself has to rely on something more fundamental? What can be more fundamental than examining the nature of human beings and their reality? Also, what do you think is the aim of philosophy, is it the Socratic concept of 'living an examined life' or the Skeptical aim of examining everything and 'knowing nothing'? Let's start discussing about it....over a glass of wine!" + emoji.emojize(":clinking_glasses:"),

            "Hmmm....you know what, I haven't seen a decent aphorism from anyone in here, because they are just downright boring. So on the occasion of your arrival here, why don't you share with us your favorite philosophical quote/aphorism? Nothin is more satisfying than trying to decipher the underlyig meaning of an aphorism over a glass of wine. Cheers" + emoji.emojize("clinking_glasses:")
        ]

"""Welcome someone with a cool philosohical message"""
@app.on_message(filters.chat([TestingBots, PhilosophyChat]) & filters.new_chat_members)
async def welcome(client, message):
        await message.reply_text(random.choice(Welcome), quote=True)

norms = "<p>You&apos;ll be able to figure out everything else as you go, but just remember some of these :&nbsp;</p><p>1. Don&apos;t take any opinion as the greatest truth, question everything.&nbsp;</p> <p>2. Don&apos;t be afraid or indulge into emotions while having conversations.&nbsp;</p> <p>3. Be civil during conversations and respect the human you&apos;re talking to.&nbsp;</p> <p>4. Always share content with context. Random posts about random things are discouraged, and would be deleted.&nbsp;</p> <p>5. We appreciate that you tell us about your day, in fact we encourage you to do so, but try to maintain the topic &nbsp;at more higher intellectual level.</p><p>6. Do not feed the trolls.&nbsp;</p><p>7. If you feel like insulted in some way, you can tell any admin present at the moment or use the #harsh tag.&nbsp;</p><p>8. Try to limit the use of bad words, you can use them, but try not to abuse. <br><br>9. Treat the chat as a place of impersonal discourse. Long rants on things that aren&apos;t necessarily philosophical are discouraged. Try to keep your posts, claims and critiques as impersonal as you can.</p><p>10. Divergence in discussions leading to unnecessary &nbsp;back and forth around a controversial topic are to be moderated and kept to the minimum. For the best, try not to lead into such directions, and when you do try to get back to something beyond it.</p> <p>We appreciate your stay in this sacred place. Thank you.</p>"

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
            
           l = len(message.text)
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
           new_file  = "./DOWNLOADS" + "/" + userid + "Audio"  + ".mp3"
           myobj = gTTS(text=message.text[6:l], lang=language_to_audio, slow=False)
           myobj.save(new_file)
           await message.reply_audio(new_file)
           await a.edit(random.choice(aphorisms))

"""Gets a paper from SciHub using the given DOI"""
@app.on_message(filters.command("sci",prefixes="/"))
async def sci(client, message):
      filters.command("sci", "/")
      DOI = message.command[-1]
      sh = SciHub()
      result = sh.fetch(DOI)
      if result:
          with open('output.pdf', 'wb+') as fd:
              await fd.write(result.pdf)


"""Gets a summary from Wiki"""
@app.on_message(filters.command("w",prefixes="/"))
async def wiki (client,message):
      filters.command("w","/")
      word = message.command[-1]
      await message.reply_text( text = wikipedia.summary(word) ,quote=True)

"""Gets a random episode from Existential Comics"""
@app.on_message(filters.command("ec", prefixes="/"))
async def comics(client, message):
    episode = str(random.randint(1,2703))
    if not os.path.isdir(f"./Existential Comics/{episode}"):
        os.makedirs(f"./Existential Comics/{episode}")

    url = 'https://www.existentialcomics.com/comic' + episode
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    img_tags = soup.find_all('img')
    img_urls = [img['src'] for img in img_tags]

    for img in img_urls:
        if 'http' not in img:
            img = '{}{}'.format(url, img)
        filename = os.path.join(f"./Existential Comics/{episode}", img.split("/")[-1])
        with open(filename, "wb") as f:
           response = requests.get(img)
           f.write(response.content)
    await app.send_media_group(TestingBots, [InputMediaPhoto(filename)], quote = True)

"""Translate messages using gpytranslate"""

@app.on_message(filters.command("tr", prefixes="/"))
async def translate(client, message):
    t = Translator()
    txt =  message.text
    l = len(txt)
    to_translate = txt[4:l]
    detect = await t.detect(to_translate)
    ask = await client.ask(message.chat.id, "What language do you want this to be tranaslated into? Here are the language [codes](https://cloud.google.com/translate/docs/languages)", reply_markup=ForceReply(True)) 
    to_language = ask.text.lower()
    translation = await t.translate(to_translate, targetlang=to_language)

    await message.reply_text(translation.text, quote=True)



app.run()

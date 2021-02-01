
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
from pyrogram import Client, filters
from pyromod import listen
from config import api_id, api_hash
from pyrogram.types import User, Chat, ChatMember, Message, Photo, MessageEntity, Audio, Document, Animation, Video, Voice, Thumbnail, Contact, Game, Location, Poll, ForceReply
from pyrogram.handlers import MessageHandler
from gtts import gTTS
from gtts.lang import tts_langs
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.schedulers.background import BackgroundScheduler

#Enable Logging

logging.basicConfig(
format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO
                     )
logger = logging.getLogger(__name__)

app = Client("DionysianBot", api_id=api_id, api_hash=api_hash, bot_token= "1520740480:AAFmzNr57pNnWud7u5x7sFX0MDPi2kPA6Dw")

aphorisms = [
            '__He who fights with monsters might take care lest he thereby becomes a monster. And if you gaze for long into an abyss, the abyss gazes also into you.__ ~Nietzsche' , 
            '__What does not kill me, makes me stronger__ ~Nietzsche' , 
            '__What is done out of love always takes place beyond good and evil.__ ~Nietzsche' , 
            '__Man does not strive for happiness; only the Englishman does that.__ ~Nietzsche' , 
            '__There are no facts, only interpretations.__ ~Nietzsche' , 
            '__There are two great European narcotics, alcohol and Christianity.__ ~Nietzsche' , 
            '__Become who you are!.__ ~Nietzsche' , 
            '__The true man wants two things: danger and play.__ ~Nietzsche' , 
            '__My formula for greatness in a human being is amor fati: that one wants nothing to be different, not forward, not backward, not in all eternity.__ ~Nietzsche' , 
            '__The lonely one offers his hand too quickly to whomever he encounters.__ ~Nietzsche', 
            '__There is more wisdom in your body than in your deepest philosophy.__ ~Nietzsche ' , 
            '__A living thing seeks above all to discharge its strength — life itself is will to power.__ ~Nietzsche' , 
            '__My formula for happiness: a Yes, a No, a straight line, a goal.__ ~Nietzsche',
            '__"It is not death  that a man should fear but he should fear  never beginning to live."__ — Marcus Aurelius.',
            '__“Keep this thought handy when you feel a bit of rage coming on—it isn’t manly to be enraged. Rather, gentleness and civility are more human, and therefore manlier. A real man doesn’t give way to anger and discontent, and such a person has strength, courage, and endurance—unlike the angry and complaining. The nearer a man comes to a calm mind, the closer he is to strength.”__ -Marcus Aurelius',
            '__“Death smiles at us all; all we can do is smile back at it.”__ ― Marcus Aurelius',
            '__Think of yourself as dead. You have lived your life. Now take what’s left and live it properly.__ ~ Marcus Aurelius',
            '__Wherever there is a human, there is an opportunity for kindness.__ ~Seneca',
            '__Self love is more cunning than the most cunning man in the world.__ ~Rochefoucald',
            '__Passion often renders the most clever man a fool, and even sometimes renders the most foolish man clever.__ ~Rochefoucald',
            '__Self-love is the greatest of flatterers.__ ~Rochefoucald',
            '__The moderation of those who are happy arises from the calm which good fortune bestows upon their temper.__ ~Rochefoucald',
            '__We have all sufficient strength to support the misfortunes of others.__ ~Rochefoucald',
            '__Philosophy triumphs easily over past evils and future evils; but present evils triumph over it.__ ~Rochefoucald'
            '__If we had no faults we should not take so much pleasure in noting those of others.__ ~Rochefoucald',
            '__To establish ourselves in the world we do everything to appear as if we were established.__ ~Rochefoucald',
            '__The happiness or unhappiness of men depends no less upon their dispositions than their fortunes.__ ~Rochefoucald',
            '__If there is a pure love, exempt from the mixture of our other passions, it is that which is concealed at the bottom of the heart and of which even our- selves are ignorant.__ ~Rochefoucald',
            '__It is more disgraceful to distrust than to be deceived by our friends.__ ~Rochefoucald',
            '__Those who know their minds do not necessarily know their hearts.__ ~Rochefoucald',
            '__One kind of flirtation is to boast we never flirt.__ ~Rochefoucald',
            '__A man would rather say evil of himself than say nothing.__ ~Rochefoucald',
            '__We often boast that we are never bored, but yet we are so conceited that we do not perceive how often we bore others.__ ~Rochefouclad',
            '__The refusal of praise is only the wish to be praised twice.__ ~Rochefoucald',
            '__There are some persons who only disgust with their abilities, there are persons who please even with their faults__ ~Rochefoucald',
            '__People who comprehend a thing to its very depths rarely stay faithful to it forever. For they have brought its depths into the light of day: and in the depths there is always much that is unpleasant to see.__ ~Nietzsche',
            '__The cure for love is still in most cases that ancient radical medicine: love in return.__ ~Nietzsche',
            '__Fortune cures us of many faults that reason could not.__ ~Rochefoucald',
            '__However rare true love is, true friendship is rarer.__~Rochefoucald',
            '__Timidity is a fault which is dangerous to blame in those we desire to cure of it__~Rochefoucald',
            '__We often go from love to ambition, but we never return from ambition to love.__~Rochefoucald',
            '__Sobriety is the love of health, or an in- capacity to eat much. ~Rochefoucald',
            '__We never forget things so well as when we are tired of talking of them__ ~Rochefoucald',
            '__We are very fond of reading others characters, but we do not like to be read ourselves__~Rochefoucald',
            '__The greatest skill of the least skilful is to know how to submit to the direction of another__~Rochefoucald',
            '__Why we cry out so much against maxims which lay bare the heart of man, is because we fear that our own heart shall be laid bare.__ ~Rochefoucald',
            '__The labour of the body frees us from the pains of the mind, and thus makes the poor happy__~Rochefoucald',
            '__Few things are needed to make a wise man happy; nothing can make a fool content; that is why most men are miserable.__~Rochefoucald',
            '__We trouble ourselves less to become happy, than to make others believe we are so__~Rochefoucald',
            '__Wisdom is to the soul what health is to the body.__ ~Rochefoucald',
            '__Before strongly desiring anything we should examine what happiness he has who possesses it.__ ~Rochefoucald',
            '__We commonly praise the good hearts of those who admire us. __~Rochefoucald',
            '__A man to whom no one is pleasing is much more unhappy than one who pleases nobody.__~Rochefoucald',
            '__A well regulated mind sees all things as they should be seen, appraises them at their proper value, turns them to its own advantage, and adheres firmly to its own opinions as it knows all their force and weight.__~Rochefoucald',
            '__There is a kind of love, the excess of which forbids jealous__~Rochefoucald',
            '__Infidelities should extinguish love, and we ought not to be jealous when we have cause to be so. No person can escape causing jealousy who are worthy of exciting it.__~Rochefoucald',
            "__Flirtation is at the bottom of woman's nature, although all do not practise it, some being restrained by fear, others by sense__~Rochefoucald",
            '__There are different kinds of curiosity: one springs from interest, which makes us desire to know everything that may be profitable to us; another from pride, which springs from a desire of knowing what others are ignorant of.__~Rochefoucald',
            '__As rivers are lost in the sea so are virtues in self__~Rochefoucald',
            '__Idleness and fear keeps us in the path of duty, but our virtue often gets the praise.__~Rochefoucald',
            '__However deceitful hope may be, yet she carries us on pleasantly to the end of life__~Rochefoucald',
            '__Pride will not owe, self-love will not pay.__~Rochefoucald',
            '__True love is like ghosts, which everybody talks about and few have seen.__~Rochefoucald',
            '__Envy is destroyed by true friendship, flirtation by true love__~Rochefoucald',
            '__We always fear to see those whom we love when we have been flirting with others.__~Rochefoucald',
            '__That which makes us believe so easily that others have defects is that we all so easily believe what we wish.__~Rochefoucald',
            '__There are those who avoid our jealousy, of whom we ought to be jealous. __~Rochefoucald',
            '__There is nothing more natural, nor more deceptive, than to believe that we are beloved.__~Rochefoucald',
            '__"All truth is simple" - Is that not a compound lie ?__~Nietzsche',
            '__The mason employed on the building of a house may be quite ignorant of its general design; or at any rate, he may not keep it constantly in mind. So it is with man: in working through the days and hours of his life, he takes little thought of its character as a whole.__~Schopenhauer ',
            '__An angry man opens his mouth and shuts his eyes.__~Cato, The Elder'
        
        ]

"""Testing aphorisms on BOT Testing Group"""
async def job():
    await app.send_message(chat_id='TestingPhilosophicalBots' , text = random.choice(aphorisms))

scheduler = AsyncIOScheduler()
scheduler.add_job(job, "interval", seconds=1800)

scheduler.start()

""""Send a random aphorism to CorgitoReaders"""
async def job():
    await app.send_message(chat_id='CorgitoReaders' , text = random.choice(aphorisms))

scheduler = AsyncIOScheduler()
scheduler.add_job(job, "interval", seconds=10800)

scheduler.start()


"""Send a message when the command /start is used """
@app.on_message(filters.command("start", prefixes="/")) 
async def start(client, message):
        await message.reply_text("Hello! I'm the official managing bot for the Philosophy and Literature group on Telegram(@CorgitoReaders)." , quote = True )


"""Generate a random aphorism when /quote is used"""
@app.on_message(filters.command("quote", prefixes="/"))
async def quote(client, message):
        await message.reply_text(text = "Here's something that can rack your brains : " + random.choice(aphorisms) , quote=True) 

norms = "<p>You&apos;ll be able to figure out everything else as you go, but just remember some of these : <br>1. Don&apos;t take any opinion as the greatest truth, question everything. <br>2. Don&apos;t be afraid or indulge into emotions while having conversations. <br>3. Be civil during conversations and respect the human you&apos;re talking to. <br>4. Always share content with context. <br>5. We appreciate that you tell us about your day, in fact we encourage you to do so, but try to maintain the topic in a more higher intellectual level.<br>6. Do not feed the trolls. <br>7. If you feel like insulted in some way, you can tell any admin present at the moment or use the #harsh tag. <br>8. Try to limit the use of bad words, you can use them, but try not to abuse. <br><br>We appreciate your stay in this sacred place. Thank you</p>"

"""Send the rules when /rules command is used or someone joins """
@app.on_message(filters.command("rules", prefixes="/") | filters.new_chat_members)
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
           "**Plz enter an language code\n suppourt languages**[click here](https://www.google.com/url?sa=t&source=web&rct=j&url=https://cloud.google.com/text-to-speech/docs/voices&ved=2ahUKEwir4pPLlr7uAhWLwjgGHQAVAQAQFjACegQIDBAC&usg=AOvVaw3Q_9UBb0Xo-ljg87RGPX-8&cshid=1611821833928)",
           reply_markup=ForceReply(True),
        )  

           language_to_audio = language.text.lower()
           if language.text.lower() not in tts_langs():
            await message.reply_text(
             "```Unsupported Language Code```",
             quote=True,
             parse_mode="md"
        )
           else:
                 a = await message.reply_text(
                 "```processing```",
                   quote=True,
                   parse_mode="md"
           )
           new_file  = "./DOWNLOADS" + "/" + userid + message.text + ".mp3"
           myobj = gTTS(text=message.text, lang=language_to_audio, slow=False)   
           myobj.save(new_file)
           await message.reply_audio(new_file)
           quotes = ['He who fights with monsters might take care lest he thereby becomes a monster. And if you gaze for long into an abyss, the abyss gazes also into you.' , 'What does not kills me, makes me stronger' , 'What is done out of love always takes place beyond good and evil.' , 'Man does not strive for happiness; only the Englishman does that. ' , 'There are no facts, only interpretations.' , 'There are two great European narcotics, alcohol and Christianity' , 'Become who you are!' , 'The true man wants two things: danger and play.' , 'My formula for greatness in a human being is amor fati: that one wants nothing to be different, not forward, not backward, not in all eternity.' , '**The lonely one offers his hand too quickly to whomever he encounters.**', 'There is more wisdom in your body than in your deepest philosophy' , 'A living thing seeks above all to discharge its strength — life itself is will to power' , 'My formula for happiness: a Yes, a No, a straight line, a goal']
           await a.edit(random.choice(quotes))



app.run()

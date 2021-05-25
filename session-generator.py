from pyrogram import Client
from config import api_id, api_hash, bot_token, pw

with Client(":DionysianBot:", api_id, api_hash) as app, open("session.txt", "w+") as s_file: 
    session_string = app.export_session_string()
    s_file.write(session_string)
    print("Session string has been saved to session.txt")

    print(session_string) 

import os 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from pyrogram import Client, filters
from pyrogram.types import Message
from Plugins.commands import commands
import time
import requests
from pytube import Playlist
import subprocess
import youtube_dl


START_TEXT, HELP_TEXT, UPLOAD_START, ABOUT_TEXT, START_BUTTONS, result_buttons, HELP_BUTTONS, ABOUT_BUTTONS, SOURCE_TEXT, SOURCE_BUTTONS, result_text = commands()

HB = Client(
    "YOUTUBE Bot",
    bot_token=os.environ.get("BOT_TOKEN", "6999401413:AAHgF1ZpUsCT5MgWX1Wky7GbegyeHvzi2AU"),
    api_id=int(os.environ.get("API_ID", "10471716")),
    api_hash=os.environ.get("API_HASH", "f8a1b21a13af154596e2ff5bed164860")
)

VIDEO_REGEX = r'(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/|(?:youtube\.com\/shorts\/))(?P<video_id>[a-zA-Z0-9_-]{11})'
PLAYLIST_REGEX = r'(.*)youtube.com/(.*)[&|?]list=(?P<playlist>[^&]*)(.*)'
start_time = time.time()




@HB.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.mention)
    reply_markup = START_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@HB.on_message(filters.command(["help"]))
async def help_message(bot, update):
    text = HELP_TEXT
    reply_markup = HELP_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@HB.on_message(filters.command(["about"]))
async def about_message(bot, update):
    text = ABOUT_TEXT
    reply_markup = ABOUT_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )






@HB.on_message(filters.regex(VIDEO_REGEX))
async def videodl(_, message):
    url = message.text
    video_title = subprocess.check_output(["youtube-dl", "--get-title", url]).decode("utf-8").strip()
    thumbnail_url = subprocess.check_output(["youtube-dl", "--get-thumbnail", url]).decode("utf-8").strip()
    
    result_buttons2 = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🎬 Download Video', callback_data='video')
        ]]
    )

    await message.reply_photo(
        photo=thumbnail_url,
        caption="🎬 TITLE : " + video_title + "\n\n📤 UPLOADED : " + url,
        reply_markup=result_buttons2,
        quote=True,
    )

@HB.on_callback_query()
async def cb_data(bot, update):
    if update.data == 'video':
        url = update.message.caption.split("\n\n")[1].split(" : ")[1]
        video_title = subprocess.check_output(["youtube-dl", "--get-title", url]).decode("utf-8").strip()
        video_file = f"{video_title}.mp4"
        subprocess.run(["youtube-dl", "-f", "best", "-o", video_file, url])
        
        await HB.send_video(
            chat_id=update.message.chat.id,
            video=video_file,
            caption=result_text,
            progress=progress_for_pyrogram,
            progress_args=(
                UPLOAD_START,
                update.message,
                start_time
            )
        )
        await update.message.delete()

@HB.on_message(filters.regex(PLAYLIST_REGEX))
async def playlistdl(_, update):
    purl = update.text
    pyt = Playlist(purl)
  
    for video in pyt.videos:
        video_title = subprocess.check_output(["youtube-dl", "--get-title", video]).decode("utf-8").strip()
        video_file = f"{video_title}.mp4"
        subprocess.run(["youtube-dl", "-f", "best", "-o", video_file, video])
        
        await HB.send_video(
            chat_id=update.chat.id, 
            caption=(f"⭕️ PLAYLIST : "+ pyt.title + "\n📥 DOWNLOADED " + "\n✅ JOIN @TELSABOTS" ),
            video=video_file,
        )


print("Private Botz On the Run HOHOHO *LOL 😂")
HB.run()

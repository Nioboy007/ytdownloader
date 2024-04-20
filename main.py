import os 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from pyrogram import Client, filters,emoji
from pyrogram.types import Message
import os
import math
from Plugins.commands import commands
import time
import requests
from pytube import YouTube
import time
import pytube
import re
from helpers.thumbnail import take_screen_shot
from pytube import Playlist

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



async def progress_for_pyrogram(
    current,
    total,
    ud_type,
    message,
    start
):
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        # if round(current / total * 100, 0) % 5 == 0:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)

        progress = "[{0}{1}] \n<b>• Percentage :</b> {2}%\n".format(
            ''.join([" ▰" for i in range(math.floor(percentage / 10))]),
            ''.join(["▱" for i in range(10 - math.floor(percentage / 10))]),
            round(percentage, 2))

        tmp = progress + "<b>✅ COMPLETED :</b> {0}\n<b>📂 SIZE :</b> {1}\n<b>⚡️ SPEED :</b> {2}/s\n<b>⏰ ETA :</b> {3}\n".format(
            humanbytes(current),
            humanbytes(total),
            humanbytes(speed),
            # elapsed_time if elapsed_time != '' else "0 s",
            estimated_total_time if estimated_total_time != '' else "0 s"
        )
        try:
            await message.edit(
                text="{}\n{}".format(
                    ud_type,
                    tmp
                )
            )
        except:
            pass

def format_bytes(size):
    # 2**10 = 1024
    power = 2**10
    n = 0
    power_labels = {0 : '', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return size, power_labels[n]+'B'

def humanbytes(size):
    # https://stackoverflow.com/a/49361727/4723940
    # 2**10 = 1024
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'Ki', 2: 'Mi', 3: 'Gi', 4: 'Ti'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'


def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "d, ") if days else "") + \
        ((str(hours) + "h, ") if hours else "") + \
        ((str(minutes) + "m, ") if minutes else "") + \
        ((str(seconds) + "s, ") if seconds else "") + \
        ((str(milliseconds) + "ms, ") if milliseconds else "")
    return tmp[:-2]




@HB.on_message(filters.regex(VIDEO_REGEX))
async def ytdl(_, message):
   l = message.text.split()
   global var
   global ythd
   global ytlow
   global yt
   global song
   global file
   global thumb
   global ytaudio
   var=message.text
   url= message.text
   yt = YouTube(url)
   chat_id =message.chat.id
   thumb = yt.thumbnail_url
   output_directory = "downloads/"
   ythd = yt.streams.get_highest_resolution()
   ytlow = yt.streams.get_by_resolution(resolution ='360p')
   ytaudio = yt.streams.filter(only_audio=True).first()
   download_path = ytaudio.download(output_path=output_directory, filename=f"{str(yt.title)}")
   rename = os.rename(download_path, f"{str(yt.title)}.mp3")
   audio_path = os.path.join(output_directory, f"{str(yt.title)}.mp3")
   audio_size = f"{int(format_bytes(ytaudio.filesize)[0]):.2f}{format_bytes(ytaudio.filesize)[1]}"
   hd = f"{int(format_bytes(ythd.filesize)[0]):.2f}{format_bytes(ythd.filesize)[1]}"
   low = f"{int(format_bytes(ytlow.filesize)[0]):.2f}{format_bytes(ytlow.filesize)[1]}"
   
   import requests
   result_buttons2 = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton('🎬720P ' +' ⭕️ '+ hd, callback_data='high'),
        InlineKeyboardButton('🎬 360p ' + '⭕️ ' +  low, callback_data='360p')
    ],[
        InlineKeyboardButton('🎧 AUDIO '+  '⭕️ ' +  audio_size , callback_data='audio')
    ],[
        InlineKeyboardButton('🖼THUMBNAIL🖼', callback_data='thumbnail')
    ]]
   )
   
   await message.reply_photo(
            photo=thumb,
            caption="🎬 TITLE : "+ yt.title +  "\n\n📤 UPLOADED : " + yt.author  + "\n\n📢 CHANNEL LINK " + f'https://www.youtube.com/channel/{yt.channel_id}',
            reply_markup=result_buttons2,
            quote=True,
    
    )
import time
start_time = time.time()


@HB.on_callback_query()
async def cb_data(bot, update):                     
    
    if update.data == 'high':
     try:
        await  HB.send_video(
            chat_id = update.message.chat.id, 
            video = ythd.download(),
            caption=result_text,
            reply_markup=result_buttons,
            progress=progress_for_pyrogram,
                    progress_args=(
                        UPLOAD_START,
                        update.message,
                        start_time
                    )
      )
        await update.message.delete()
     except:
        await HB.send_message(
            chat_id = update.message.chat.id,
            text="**😔 1080P QUALITY IS NOT AVAILABLE\n CHOOSE ANY OTHER QUALITIES**")    
    
    elif update.data == '360p':
     try:
      await  HB.send_video(
        chat_id = update.message.chat.id, 
        video = ytlow.download(),
        caption=result_text,
        reply_markup=result_buttons,
       progress=progress_for_pyrogram,
                    progress_args=(
                        UPLOAD_START,
                        update.message,
                        start_time
                    )
        )
      await update.message.delete()

     except:
        await HB.send_message(
            chat_id = update.message.chat.id,
            text="**😔 360P QUALITY IS NOT AVAILABLE \n CHOOSE ANY OTHER QUALITIES**") 
         
    audio_file_path = os.path.join("downloads", f"{yt.title}.mp3")
    elif update.data == 'audio':
        await  HB.send_audio(
        chat_id = update.message.chat.id,
        audio=audio_file_path,
        caption=result_text,
        duration=yt.length,
        reply_markup=result_buttons,
        progress=progress_for_pyrogram,
                    progress_args=(
                        UPLOAD_START,
                        update.message,
                        start_time
                    )
      )
        await update.message.delete()

    elif update.data == 'thumbnail':
        await HB.send_photo(
            chat_id = update.message.chat.id, 
            photo=thumb,
            caption="**JOIN @TELSABOTS**"
        )
        await update.message.delete()    

    elif update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    
    else:
        await update.message.delete()

@HB.on_message(filters.text & filters.private)
async def ytdl(_, update):
   purl=update.text
   pyt = Playlist(purl)
  
   for video in pyt.videos:
    phd =video.streams.get_highest_resolution()
    
    await  HB.send_video(
            chat_id = update.chat.id, 
            caption=(f"⭕️ PLAYLIST : "+ pyt.title + "\n📥 DOWNLOADED " + "\n✅ JOIN @TELSABOTS" ),
            video = phd.download(),
            
    )
        

print("Private Botz On the Run HOHOHO *LOL 😂")
HB.run()

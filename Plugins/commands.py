from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def commands():
    START_TEXT = """**
    HI {}, 
    I AM A  ADVANCED YOUTUBE DOWNLOADER BOT
    I CAN DOWNLOAD YOUTUBE VIDEOS ,THUMBNAIL
    AND PLAYLIST VIDEOS....
    ONE OF THE SPPEDEST YOUTUBE BOT 
    I CAN DOWNLOAD 911mb VIDEOS
    IN 1min 
    MADE BY @TELSABOTS**"""

    HELP_TEXT = """**
        YOUTUBE VIDEO
    SENT ANY URL .......
    THEN SELECT AVAILABLE QUALITY

        PLAYLIST
    SENT ANY URL .....
    THEN WAIT BOT WILL SENT
    VIDEOS IN HIGH QUALITY...

    MADE BY @TELSABOTS**
    """
    
    

    ABOUT_TEXT = """
     🤖<b>BOT :YOUTUBE DOWNLOADER </b>
     
     🧑🏼‍💻DEV🧑🏼‍💻: @ALLUADDICT
     
     📢<b>CHANNEL :</b>@TELSABOTS
     
     📝<b>Language :</b>  <a href='https://python.org/'>Python3</a>
     
     🧰<b>Frame Work :</b>  <a href='https://pyrogram.org/'>Pyrogram</a>
     
     🤩<b>SOURCE :</b>  <a href='https://youtu.be/xyW5fe0AkXo'>CLICK HERE</a>
     
     
    """

    UPLOAD_START = " <bold>Upload STARTED...</bold>"

    START_BUTTONS = InlineKeyboardMarkup(
            [[
            InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
            InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')
            ],[
            InlineKeyboardButton('🆘HELP🆘', callback_data='help'),
            InlineKeyboardButton('🤗ABOUT🤗', callback_data='about'),
            InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
            ]]
        )


    result_buttons = InlineKeyboardMarkup(
            [[
            InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
            InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')
            ],[
            InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
            ]]
        )
    HELP_BUTTONS = InlineKeyboardMarkup(
            [[
            InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
            InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')
            ],[
            InlineKeyboardButton('🏡HOME🏡', callback_data='home'),
            InlineKeyboardButton('🤗ABOUT🤗', callback_data='about'),
            InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
            ]]
        )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
            [[
            InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
            InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')
            ],[
            InlineKeyboardButton('🏡HOME🏡', callback_data='home'),
            InlineKeyboardButton('🆘HELP🆘', callback_data='help'),
            InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
            ]]
        )

    SOURCE_TEXT = """<b>PRESS SOURCE BUTTON \n WATCH MY VIDEO AND\nCHECK DESCRIPTION FOR SOURCE CODE</b>"""
    SOURCE_BUTTONS = InlineKeyboardMarkup(
            [[
            InlineKeyboardButton('✅SOURCE✅', url='https://youtu.be/xyW5fe0AkXo'),
            InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')
            ],[
            InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
            ]]
        )

    result_buttons = InlineKeyboardMarkup(
            [[
            InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
            InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')
            ],[
            InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
            ]]
        )

    result_text = """**JOIN @TELSABOTS**""" 

    return (START_TEXT, HELP_TEXT, ABOUT_TEXT, UPLOAD_START, START_BUTTONS, result_buttons, HELP_BUTTONS, ABOUT_BUTTONS, SOURCE_TEXT, SOURCE_BUTTONS, result_text)

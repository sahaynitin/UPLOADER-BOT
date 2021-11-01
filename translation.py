class Translation(object):
    START_TEXT = """Hey {}

I am Url Uploader Bot 

I can Upload Any Link in Media Form

Use Help Command to Know How to Use me.

Made With 💕 By @Tellybots_4u
"""

    HELP_USER = """Welcome to Help Menu
    
✪ Send a Custom Thumbnail to Save Thumbnail\n
✪ Please Send Any Link to Upload on Telegram.\n
✪ Use /delthumbnail to Delete Your Custom Thumbnail\n
✪ Use Any Button Below on Sending link\n
Its Recommended to Use A Custom Thumbnail Before Sending link
"""
    ABOUT_TEXT = """<b>🤖 𝐌𝐲 𝐍𝐚𝐦𝐞 : <a href='https://t.me/TeleRoid_Hotstar_Bot'> @𝐓𝐞𝐥𝐞𝐑𝐨𝐢𝐝_𝐇𝐨𝐭𝐬𝐭𝐚𝐫_𝐁𝐨𝐭 </a></b>

<b>👨‍💻 My Name:<a href='https://t.me/PredatorHackerzZ'>@𝐏𝐫𝐞𝐝𝐚𝐭𝐨𝐫𝐇𝐚𝐜𝐤𝐞𝐫𝐳𝐙</a></b>

<b>📝 language: Python3</b>

<b>📡 Server :<a href='https://www.heroku.com'> Heroku </a></b>

<b>📚 library : Pyrogram 1.0.7</b>

<b>📁 Source Code :<a href='https://github.com/PredatorHackerzZ/UPLOADER-BOT'>𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞</a></b>

<b>🤖 Update Channel :<a href='https://t.me/TeleRoid14'>@𝐓𝐞𝐥𝐞𝐑𝐨𝐢𝐝𝐒𝐮𝐩𝐩𝐨𝐫𝐭</a></b>

<b>📢 𝐁𝐨𝐭𝐬 𝐔𝐩𝐝𝐚𝐭𝐞𝐬: <a href='https://t.me/TeleRoidGroup'>@𝐓𝐞𝐥𝐞𝐑𝐨𝐢𝐝𝐆𝐫𝐨𝐮𝐩</a></b>

<b>👨‍🔧 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐁𝐨𝐭𝐥𝐢𝐬𝐭 : <a href='https://t.me/TGRobot_List'>@𝐓𝐆𝐑𝐨𝐛𝐨𝐭_𝐋𝐢𝐬𝐭</a></b>

<b>👨‍🔧 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲: <a href='https://t.me/MoviesFlixers_DL'>@𝐏𝐨𝐰𝐞𝐫𝐞𝐝_𝐋𝐢𝐬𝐭</a></b>"""
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    SET_CUSTOM_USERNAME_PASSWORD = """𝐈𝐟 𝐲𝐨𝐮 𝐰𝐚𝐧𝐭 𝐭𝐨 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐩𝐫𝐞𝐦𝐢𝐮𝐦 𝐯𝐢𝐝𝐞𝐨𝐬, 𝐩𝐫𝐨𝐯𝐢𝐝𝐞 𝐢𝐧 𝐭𝐡𝐞 𝐟𝐨𝐥𝐥𝐨𝐰𝐢𝐧𝐠 𝐟𝐨𝐫𝐦𝐚𝐭:
URL | filename | username | password"""
    DOWNLOAD_START = "📥𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐭𝐨 𝐌𝐲 𝐒𝐞𝐫𝐯𝐞𝐫....."
    UPLOAD_START = "📤𝐔𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐭𝐨 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦....."
    RCHD_TG_API_LIMIT = "𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐝 𝐢𝐧 {} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬.\n𝐃𝐞𝐭𝐞𝐜𝐭𝐞𝐝 𝐅𝐢𝐥𝐞 𝐒𝐢𝐳𝐞: {}\n𝐒𝐨𝐫𝐫𝐲. 𝐁𝐮𝐭, 𝐈 𝐜𝐚𝐧𝐧𝐨𝐭 𝐮𝐩𝐥𝐨𝐚𝐝 𝐟𝐢𝐥𝐞𝐬 𝐠𝐫𝐞𝐚𝐭𝐞𝐫 𝐭𝐡𝐚𝐧 𝟐𝐆𝐁 𝐝𝐮𝐞 𝐭𝐨 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐀𝐏𝐈 𝐥𝐢𝐦𝐢𝐭𝐚𝐭𝐢𝐨𝐧𝐬."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "𝐓𝐡𝐚𝐧𝐤𝐬 𝐟𝐨𝐫 𝐮𝐬𝐢𝐧𝐠 𝐭𝐡𝐞 𝐁𝐨𝐭 @TheTeleRoid\n\n<b>𝐉𝐨𝐢𝐧 : @MoviesFlixers_DL</b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐝 𝐢𝐧 {} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬.\n𝐔𝐩𝐥𝐨𝐚𝐝𝐞𝐝 in {} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬.\n\n@TheTeleRoid"
    SAVED_CUSTOM_THUMB_NAIL = "𝐂𝐮𝐬𝐭𝐨𝐦 𝐯𝐢𝐝𝐞𝐨 / 𝐟𝐢𝐥𝐞 𝐭𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐬𝐚𝐯𝐞𝐝. 𝐓𝐡𝐢𝐬 𝐢𝐦𝐚𝐠𝐞 𝐰𝐢𝐥𝐥 𝐛𝐞 𝐮𝐬𝐞𝐝 𝐢𝐧 𝐭𝐡𝐞 𝐯𝐢𝐝𝐞𝐨 / 𝐟𝐢𝐥𝐞."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ 𝐂𝐮𝐬𝐭𝐨𝐦 𝐭𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐜𝐥𝐞𝐚𝐫𝐞𝐝 𝐬𝐮𝐜𝐜𝐞𝐬𝐟𝐮𝐥𝐥𝐲."
    CUSTOM_CAPTION_UL_FILE = "{}"
    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = """𝐌𝐞𝐝𝐢𝐚 𝐀𝐥𝐛𝐮𝐦 𝐬𝐡𝐨𝐮𝐥𝐝 𝐜𝐨𝐧𝐭𝐚𝐢𝐧 𝐨𝐧𝐥𝐲 𝐭𝐰𝐨 𝐩𝐡𝐨𝐭𝐨𝐬. 𝐏𝐥𝐞𝐚𝐬𝐞 𝐫𝐞-𝐬𝐞𝐧𝐝 𝐭𝐡𝐞 𝐦𝐞𝐝𝐢𝐚 𝐚𝐥𝐛𝐮𝐦, 𝐚𝐧𝐝 𝐭𝐡𝐞𝐧 𝐭𝐫𝐲 𝐚𝐠𝐚𝐢𝐧, 𝐨𝐫 𝐬𝐞𝐧𝐝 𝐨𝐧𝐥𝐲 𝐭𝐰𝐨 𝐩𝐡𝐨𝐭𝐨𝐬 𝐢𝐧 𝐚𝐧 𝐚𝐥𝐛𝐮𝐦."
𝐘𝐨𝐮 𝐜𝐚𝐧 𝐮𝐬𝐞 /rename 𝐜𝐨𝐦𝐦𝐚𝐧𝐝 𝐚𝐟𝐭𝐞𝐫 𝐫𝐞𝐜𝐞𝐢𝐯𝐢𝐧𝐠 𝐟𝐢𝐥𝐞 𝐭𝐨 𝐫𝐞𝐧𝐚𝐦𝐞 𝐢𝐭 𝐰𝐢𝐭𝐡 𝐜𝐮𝐬𝐭𝐨𝐦 𝐭𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐬𝐮𝐩𝐩𝐨𝐫𝐭.
"""
    CANCEL_STR = "Your Process Cancelled ⛔"
    ZIP_UPLOADED_STR = "𝐔𝐩𝐥𝐨𝐚𝐝𝐞𝐝 {} 𝐟𝐢𝐥𝐞𝐬 𝐢𝐧 {} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬"
    SLOW_URL_DECED = "𝐆𝐨𝐬𝐡 𝐭𝐡𝐚𝐭 𝐬𝐞𝐞𝐦𝐬 𝐭𝐨 𝐛𝐞 𝐚 𝐯𝐞𝐫𝐲 𝐬𝐥𝐨𝐰 𝐔𝐑𝐋. 𝐒𝐢𝐧𝐜𝐞 𝐲𝐨𝐮 𝐰𝐞𝐫𝐞 𝐬𝐜𝐫𝐞𝐰𝐢𝐧𝐠 𝐦𝐲 𝐡𝐨𝐦𝐞, 𝐈 𝐚𝐦 𝐢𝐧 𝐧𝐨 𝐦𝐨𝐨𝐝 𝐭𝐨 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐭𝐡𝐢𝐬 𝐟𝐢𝐥𝐞. 𝐌𝐞𝐚𝐧𝐰𝐡𝐢𝐥𝐞, 𝐰𝐡𝐲 𝐝𝐨𝐧'𝐭 𝐲𝐨𝐮 𝐭𝐫𝐲 𝐭𝐡𝐢𝐬:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."

import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/e5c05d766a6fee1a50d18.jpg"
pm_caption = "`E.D.I.T.H.` **MODE ON**"
#@command(outgoing=True, pattern="^.on$")
@borg.on(admin_cmd(pattern=r"on"))
async def amireallyalive(on):
    chat = await alive.get_chat()
    await mode.delete()
    """ For .on command, check if the bot is running.  """
    await borg.send_file(mode.chat_id, PM_IMG,caption=pm_caption)
    await mode.delete() 

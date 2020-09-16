import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
PM_IMG = "https://telegra.ph/file/e5c05d766a6fee1a50d18.jpg"
pm_caption = "`E.D.I.T.H.` **MODE ON**"
#@command(outgoing=True, pattern="^.mode$")
@borg.on(admin_cmd(pattern=r"on"))
async def amireallyalive(mode):
    chat = await mode.get_chat()
    await mode.delete()
    """ For .mode command, check if the bot is running.  """
    await borg.send_file(mode.chat_id, PM_IMG,caption=pm_caption)
    await mode.delete() 

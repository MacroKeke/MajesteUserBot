# HerlockProjects Sakir Bey Herlock

import os
import re
from userbot.events import register
from userbot import (
    HEROKU_APPNAME,
    HEROKU_APIKEY,
    SUDO_ID,
    bot,
)
import heroku3
from telethon.tl.functions.users import GetFullUserRequest

Heroku = heroku3.from_key(HEROKU_APIKEY)
heroku_api = "https://api.heroku.com"
majestesudo = os.environ.get("SUDO_ID", None)

@register(outgoing=True,
          pattern=r"^.sudoekle")
async def addsudo(event):
    await event.edit("`Kullanıcı sudo olarak ayarlanıyor`...")
    majeste = "SUDO_ID"
    if HEROKU_APPNAME is not None:
        app = Heroku.app(HEROKU_APPNAME)
    else:
        await event.edit("HEROKU:" "\nLütfen **HEROKU_APPNAME** değerini tanımlayın.")
        return
    heroku_var = app.config()
    if event is None:
        return
    try:
        majestetext = await get_user(event)
    except Exception:
        await event.edit("`Lütfen bir kullanıcının mesajına cevap verin.`")
    if majestesudo:
        yenisudo = f"{majestesudo} {majestetext}"
    else:
        yenisudo = f"{majestetext}"
    await event.edit("`Kullanıcı sudo olarak ayarlandı.👌` \n`Botunuz yeniden başlatılıyor...`")
    heroku_var[majeste] = yenisudo


async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    herlocktext = replied_user.user.id
    return herlocktext

@register(outgoing=True,
          pattern=r"^.sudosil")
async def sudosil(event):
  Heroku = heroku3.from_key(HEROKU_APIKEY)
  app = Heroku.app(HEROKU_APPNAME)
  heroku_var = app.config()
  if not event.is_reply:
    return await event.edit("`Lütfen bir kullanıcının mesajına cevap verin.`")
  if event.is_reply:
    id = (await event.get_reply_message()).sender_id
    ad = (await bot.get_entity(id)).first_name
    op = re.search(str(id), str(majestesudo))
    if op:
      i = ""
      esudo = majestesudo.split(" ")
      esudo.remove(str(id))
      i += str(esudo)
      x = i.replace("[", "")
      xx = x.replace("]", "")
      xxx = xx.replace(",", "")
      hazir = xxx.replace("'", "")
      heroku_var["SUDO_ID"] = hazir
      await event.edit(f"`{ad}``Artık Sudo değil 👌.`\n`Botunuz yeniden başlatılıyor...`")
    else:
      await event.edit(f"`Kusura bakma,` `{ad}` `Zaten Bir Sudo Değil!`")
    if heroku_var["SUDO_ID"] == None:
       await event.edit(f"`Sudo Bulunmamaktadır!`") 
    
async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    majestet = replied_user.user.id
    return majestet
    
@register(incoming=True, from_users=SUDO_ID, pattern="^.salive$")
async def _(q):
    await q.client.send_message(q.chat_id,"`Hey Sudom ❤️ \nMajesteUserBot Çalışıyor...`")

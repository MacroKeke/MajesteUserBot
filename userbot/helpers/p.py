def e_(fayl_adi, name, slep, siyahi):
	f = open(f"./majesteuserbot{fayl_adi}.py", "x")
	f.write(f"""from userbot.events import register
from userbot.cmdhelp import CmdHelp
from time import sleep
from telethon import events
a={siyahi}
@register(outgoing=True, pattern="^.{name}$")
async def _(majeste):
	for i in a:
		await majeste.edit(' '+str(i))
		sleep({slep})
Help = CmdHelp("majesteuserbot{fayl_adi}")
Help.add_command("{name}", None, "Bu plugin @SakirBey2 tarafından hazırlanmıştır.")
Help.add()
								""")
	return f.close()

def a_(fayl_adi, name, siyahi, slep):
	f = open(f"./majesteuserbot{fayl_adi}.py", "x")
	f.write(f"""from userbot.events import register
from userbot.cmdhelp import CmdHelp
from time import sleep
from telethon import events
a={siyahi}
@register(outgoing=True, pattern="^.{name}$")
async def _(majeste):
	text= " "
	for i in a:
		text+=i+"\\n"
		await majeste.edit(text)
		sleep({slep})
Help = CmdHelp("majesteuserbot{fayl_adi}")
Help.add_command("{name}", None, "Bu plugin @sakirbey2 tarafından hazırlanmıştır.")
Help.add()
								""")
	return f.close()

def r_(fayl_adi, name, siyahi):
	f = open(f"./majesteuserbot{fayl_adi}.py", "x")
	f.write(f"""from userbot.events import register
from userbot.cmdhelp import CmdHelp
from telethon import events
from random import choice
a={siyahi}
@register(outgoing=True, pattern="^.{name}$")
async def _(majeste):
	random_ = choice(a)
	await majeste.client.send_file(majeste.chat_id, random_)
	await majeste.delete()
Help = CmdHelp("majesteuserbot{fayl_adi}")
Help.add_command("{name}", None, "Bu plugin @SakirBey2 tarafından hazırlanmıştır.")
Help.add()
		""")

def m_(fayl_adi, name, siyahi):
	f = open(f"./majesteuserbot{fayl_adi}.py", "x")
	f.write("""from telethon import events
import asyncio
from userbot.events import register
from userbot.cmdhelp import CmdHelp
import random
import os
IFACI = [{siyahi}]
@register(outgoing=True, pattern="^.{name}$")
async def majestemusic(majeste):
    
    
    await majeste.edit("`Sizin için  "+IFACI+"müziğini aktarıyorum`")
    try:
        results = await majeste.client.inline_query('deezermusicbot', '+IFACI+')
    except:
            await majeste.edit("`Bottan cevap alamadım`")
            return
    netice = False
    while netice is False:
            rast = random.choice(results)
            if rast.description == IFACI:
                await majeste.edit("`Müzik Yükleniyor!")
                yukle = await rast.download_media()
                await majeste.edit("`Yükleme tamamlandı!`")
                await majeste.client.send_file(majeste.chat_id, yukle, caption="@SakirBey2 sizin için `"+rast.description+" - "+rast.title+"` müziğini seçti iyi dinlemeler. :)")
                await event.delete()
                os.remove(yukle)
                netice = True
Help = CmdHelp("majesteuserbot{fayl_adi}")
Help.add_command("{name}", None, "Bu Plugin @SakirBey2 Taradındən Hazırlanmışdır..")
Help.add()
		""".format(
siyahi=siyahi,
name=name,
fayl_adi=fayl_adi
			))

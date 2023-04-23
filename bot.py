  from askpyro import Askclient
  from pyrogram import Client ,filters
  
  app = Client("my_account")
  read = Askclient(app)

  @app.on_message(filters.command("start"))
  async def start_pm(c: app, m: Message):
    answer = await read.ask(m, text)
    if answer.text:
     print(answer.text)
    await answer.reply("ɪ ɢᴏᴛ ᴀɴsᴡᴇʀ..")

  app.run()

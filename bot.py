from pyrogram import Client, Filters
import time
from pyrogram.errors import FloodWait
import asyncio
async def main():
 msg_ids = {}
 app = Client("my_account",800295,"3d6ffe66b0d34f2921b964da418d9931") 
 d = -1001328910368
 s = -1001262096355
 @app.on_message(Filters.chat(s) & Filters.text & ~Filters.edited)
 def forward(client,Message):
  words = ['dekho','TRUST','join','fix','😱','😳','👆','👇','☝️','https://','😂','🤔','pass','chase','link','suno','member','❓','loss','audio','open',"report",'paid','contact','baazigar','market','load','whatsapp','book','bhai','🐴','only','chut','tennis','teen','lavde','chutiya','bc','kya','LUND','WICKET LU','?','loda','telegram','chor',"kama","lakh",' id','स',"kitna"]
  for word in words:
   if word.casefold() in Message.text.casefold():
     return 
  z = client.send_message(d, "<b> " + Message.text.replace("🖲","🙇🏼‍♂").replace("📟","🎳").replace("🇩🇪","🇮🇶") + " </b>",parse_mode="html").message_id
  msg_ids[Message.message_id] = z
 @app.on_message(Filters.chat(s) & Filters.photo & ~Filters.edited)
 def forward(client,Message):
  if Message.caption:
   f = False
  else:
   f = True
  words = ['dekho','TRUST','join','fix','😱','😳','👆','👇','☝️','https://','😂','🤔','pass','chase','link','suno','member','❓','loss','audio','open',"report",'paid','contact','baazigar','market','load','whatsapp','book','bhai','🐴','only','chut','tennis','teen','lavde','chutiya','bc','kya','line','LUND','WICKET LU','?','loda','telegram','chor',"kama","lakh",' id','स',"kitna"]
  for word in words:
   if word.casefold() in Message.caption.casefold():
    f = True
  if not f:
   Message.forward(chat_id=d,as_copy = True)
 @app.on_message(Filters.chat(s) & Filters.text & Filters.edited)
 def forward(client,Message):
  if not Message.message_id in msg_ids:
   return
  try:
   client.edit_message_text(d,msg_ids[Message.message_id],"<b>" + Message.text.replace("🖲","🙇🏼‍♂").replace("📟","🎳").replace("🇩🇪","🇮🇶") + " </b>",parse_mode = "html") 
  except FloodWait as e:
   time.sleep(e.x)
 @app.on_deleted_messages(Filters.chat(s))
 def main(client, messages):
   for Message in messages:
    if not Message.message_id in msg_ids:
     return
    client.delete_messages(d,msg_ids[Message.message_id])
 app.run()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())

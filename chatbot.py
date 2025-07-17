import qrgen,whatsapp
def chatbot():
  print("""BOT :Welcome to Akshay's CHAT BOT ! 
  
  """)
  database()
  
def database():
  i=input("user :").lower()
  if "hi" in i:
    print("BOT: HELLO !")
    database()
  elif "name" in i:
    print("BOT: MY NAME IS CHAT BOT !")
    database()
  elif "whatsapp" in i:
    whatsapp.whatsapp()
    database()
  elif "qrgen" or "qrcode" in i:
    qrgen.qrgen()
    database()
  elif "help" in i:
    print("""
BOT: I AM A SIMPLE (BETA) CHAT BOT 
     I CAN HELP YOU WITH MY LIMTED POW
     If you need : [qrcode generator type "qrgen"]
                   [whatsapp message type "whatsapp"]
           """)
    database()
  else:
    print("BOT: command not find !")
    database()
  

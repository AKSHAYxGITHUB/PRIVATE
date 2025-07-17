def chatbot():
  print("Welcome to Akshay's CHAT BOT ! ")
  database()
  
def database(i):
  i=input("user :")
  if "hi" in i.lower():
    print("HELLO !")
    database()
  elif "name" in i.lower():
    print("MY NAME IS CHAT BOT !")
    database()
  else:
    database()
  

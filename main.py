import hello,qrgen,whatsapp,chatbot
from colorama import init, Fore, Style

def run():
  init(autoreset=True)
  print(Fore.GREEN +"="*87)
  print(Fore.YELLOW + "Select the program that you want to run :" + Style.RESET_ALL)
  print(Fore.CYAN + "  1)" + Fore.GREEN + " Print any thing !")
  print(Fore.CYAN + "  2)" + Fore.GREEN + " Qr generator")
  print(Fore.CYAN + "  3)" + Fore.GREEN + " Whatsapp Message Sender")
  print(Fore.CYAN + "  4)" + Fore.GREEN + " Chat BOT")
  print(Fore.CYAN + "  e)" + Fore.RED + " exit")
  a=input("Enter your choice :") 
  if a=='1':
    hello.hello()
    run()
  elif a=='2':
    qrgen.qrgen()
    run()
  elif a=='3':
    whatsapp.whatsapp()
    run()
  elif a=="4":
    chatbot.chatbot()
    run()
  elif a=='e':
    exit()
  else:
    run()
run()

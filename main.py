import hello,qrgen,whatsapp

def run():
  print("""
=======================================================================================
Select the program that you want to run :
  1) Hello print
  2) Qr generator
  3) Whatsapp Message Sender
  e) exit
  """)
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
  elif a=='e':
    exit()
  else:
    run()
run()

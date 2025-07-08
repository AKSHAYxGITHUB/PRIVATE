import hello,qrgen

def run():
  print("""Select the program that you want to run :
  1) hello print
  2) qr generator
  3) exit
  """)
  a=input("Enter your choice :") 
  if a==1:
    hello()
  elif a==2:
    qrgen()
  elif a==3:
    exit()
  else:
    run()
  

print("DO YOU WANT TO RUN ANY PROGRAMS ?")
a=input("(y/n) :")
if a=="y":
  run()
else :
  exit()

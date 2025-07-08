import hello,qrgen

def run():
  print("""Select the program that you want to run :
  1) hello print
  2) qr generator
  3) exit
  """)
  a=int(input("Enter your choice :") )
  if a==1:
    hello.hello()
    run()
  elif a==2:
    qrgen.qrgen()
    run()
  elif a==3:
    exit()
  else:
    run()
run()

import qrcode
def qrgen():
  a=input("Enter the link for creating qr code  :")
  img = qrcode.make(a)
  img.save("my_qr.png")
  print("QR CODE SAVED AS MY_QR.PNG ")

import qrcode
def qrgen():
  img = qrcode.make("https://github.com/akshaydev")
  img.save("my_qr.png")
  print("QR code saved as my_qr.png")

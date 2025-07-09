import pywhatkit as pwk
def whatsapp():
  phone_number=input("Enter the phone number (only suuports indian numbers) :")
  message=input("Enter the message you whant to send :")
  pwk.sendwhatmsg("+91"+phone_number,message)

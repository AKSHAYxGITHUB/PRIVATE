import pywhatkit as pwk
def whatsapp():
  phone_number=input("Enter the phone number (only suuports indian numbers) :")
  message=input("Enter the message you whant to send :")
 pwk.sendwhatmsg_instantly("+91"+phone_number, message, wait_time=10, tab_close=True)

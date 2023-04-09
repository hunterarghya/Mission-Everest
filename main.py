import pywhatkit as pw
import time

# Set the phone number of the recipient and the message to be sent
phone_number = "+917063783821"  # Replace with the phone number of the recipient
message = "ESCAPE ALERT!!!!!"
file_path= "violationImage/tester.jpg"

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)


curr2 = current_time.split(":")

hour= int(curr2[0])
minute= int(curr2[1])


# Send the message
pw.sendwhatmsg(phone_number, message, hour, minute+2)


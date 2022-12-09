from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


print(".....................Welcome To Gmail Terminal.........................")
print(".......................Creator-Farhan Habib............................")
print("........................................................................")
print("                    ............................                        ")
for i in range(2):
    print("\n"*i)
Object = MIMEMultipart()
Object['From'] = input("From:-")
Object['To'] = input('To:-')
Object['Subject']= input('Subject:- ')
text = input("Body:-")
text2 = input("As - Write down the type, Format- (text,csv,plain) \n :-")
Object.attach(MIMEText(text,text2))
try:
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        print("To send this Mail you have to log in a gmail account.\n Your normal gmail password does't allow for this mail system")
        print("You have to genarate a  App password from Google from here - https://bit.ly/3Hk8UVq")
        print("Don't worry this link is based on Google")
        ans = input("Y or N:-").lower()
        if ans == "y":
            email=input("Enter email\gmail:-")
            password = input("Enter Password(App Password):-")
            smtp.login(email,password)
            smtp.send_message(Object)
            print("Your mail has been sent")
        else:
            exit()

except:
    print("Something Wrong on your Input or You Select (N)")

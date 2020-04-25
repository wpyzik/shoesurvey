from email.mime.text import MIMEText
import smtplib

def send_email(Email, Shoe, average_shoe, count):
    from_email="pythoncource1@gmail.com"
    from_password="pythonCourse1"
    to_email=Email

    subject="Shoe data"
    message="Hey there, your shoe size is <strong>%s</strong>. Average shoe size of all is <strong>%s</strong> and this number is calculated out of <strong>%s</strong> samples. <br> Thank you for participation!" %(Shoe, average_shoe, count)

    msg=MIMEText(message, 'html') #we're doing it so that python treats the "message" as html, and therefore we can apply html commands to change it (like to bold -> <strong> methon)
    msg["Subject"]=subject
    msg["To"]=to_email
    msg["From"]=from_email

#you do those to login to your email and send email to the list created
    gmail=smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
#then in the google sign-in & security you need to allow for less secure apps be ON

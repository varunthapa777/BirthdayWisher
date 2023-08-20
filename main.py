import os
import smtplib

try:
    SECRET_TOKEN = os.environ["MY_SECRET_TOKEN"]
    EMAIL = os.environ["EMAIL"]
except KeyError:
    SOME_SECRET = "Token not available!"


connection = smtplib.SMTP("smtp.gmail.com")

connection.starttls()
connection.login(user=EMAIL, password=SECRET_TOKEN)

connection.sendmail(from_addr=EMAIL, to_addrs="varunthapa1920@gmail.com", msg="Subject:Hemlo!\n\nThis is Varunthapa")
connection.close()

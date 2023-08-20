import os
import smtplib

try:
    SOME_SECRET = os.environ["MY_SECRET_TOKEN"]
except KeyError:
    SOME_SECRET = "Token not available!"

MY_EMAIL = "varunthapa615@gmail.com"
PASSWORD = SOME_SECRET
connection = smtplib.SMTP("smtp.gmail.com")

connection.starttls()
connection.login(user=MY_EMAIL, password=PASSWORD)

connection.sendmail(from_addr=MY_EMAIL, to_addrs="varunthapa1920@gmail.com", msg="Subject:Hemlo!\n\nThis is Varunthapa")
connection.close()

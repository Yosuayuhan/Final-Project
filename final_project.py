import csv, smtplib, ssl

message = """Subject: Final Project Indonesia AI

Good Morning! """
from_address = "yosuayuhan.assistant@gmail.com"
password = input("Type your password and press enter: ")
message = "Hi!"
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(from_address, password)
    with open("receiver_list.txt") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for email in reader:
            print(f"Sending email to {email}")
            server.sendmail(
                from_address,
                email,
                message,
            )

#referensi 
# https://realpython.com/python-send-email/#sending-multiple-personalized-emails


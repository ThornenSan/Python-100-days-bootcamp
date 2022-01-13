import datetime as dt
import smtplib
from random import choice

MY_EMAIL = ""
PASSWORD = ""
quote = ""

# get current weekday
now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 2:
    try:
        with open("quotes.txt") as quotes:
            list_of_quotes = quotes.readlines()
    except FileNotFoundError:
        print("File not Found!")
    else:
        quote = choice(list_of_quotes)

    # Email sending
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # Make connection secure. TLS stands for Transport layer Security
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="NasenX404@yahoo.com",
            msg=f"Subject:Motivation Quote\n\n{quote}"
        )

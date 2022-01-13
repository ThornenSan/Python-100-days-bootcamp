import smtplib

my_email = ""
password = ""

with smtplib.SMTP("smtp.gmail.com") as connection:
    # Make connection secure. TLS stands for Transport layer Security
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, to_addrs="NasenX404@yahoo.com",
        msg="Subject:Hello\n\nThis is my content"
    )

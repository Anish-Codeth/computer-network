import smtplib, ssl

port = 587   
smtp_server = "smtp.gmail.com"
sender_email = "basaulaashish73@gmail.com"
receiver_email = "basaulaashish73@gmail.com"
password = ""
message = """\
Subject: Hi there

This Computer network test to capture email packet"""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()   
    server.starttls(context=context)
    server.ehlo()   
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
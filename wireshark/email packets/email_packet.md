# Capturing SMTP Packets with Wireshark

To capture SMTP packets using Wireshark, follow these steps:

1. **Open Wireshark**: Launch Wireshark on your computer.

2. **Start Capturing Packets**: Select your network interface and start capturing packets.

3. **Filter for SMTP Traffic**: Use the filter `smtp` to isolate SMTP traffic.

4. **Run the Python Script**: Execute the Python script provided. Replace the password placeholder with the actual password.

5. **Stop Capturing Packets**: Stop the capture after the email is sent.

6. **Analyze the SMTP Packet**: Find and analyze the SMTP packets related to the email.

![image](https://github.com/user-attachments/assets/2048adf2-af29-4062-92e3-57b928609d4c)
1. **TCP Connection Establishment**: The client and server establish a TCP connection using a three-way handshake (SYN, SYN-ACK, ACK) at the Transport Layer (Layer 4 of the OSI model).

2. **SMTP Server Greeting**: The SMTP server sends an SMTP 220 response code, indicating it is ready to proceed with communication.



## Code Explanation

Here's a brief explanation of each line of the code:

1. `import smtplib, ssl`: Imports the SMTP library for sending emails and SSL for secure connections.
2. `port = 587`: Sets the port number for SMTP with TLS.
3. `smtp_server = "smtp.gmail.com"`: Specifies the SMTP server address.
4. `sender_email = "basaulaashish73@gmail.com"`: Sets the sender's email address.
5. `receiver_email = "basaulaashish73@gmail.com"`: Sets the receiver's email address (same as sender in this case).
6. `password = ""`: Placeholder for the sender's email password (should be filled with the actual password).
7. `message = """\..."""`: Defines the email message content, including the subject and body.
8. `context = ssl.create_default_context()`: Creates a default SSL context for secure connection.
9. `with smtplib.SMTP(smtp_server, port) as server`: Connects to the SMTP server on the specified port.
10. `server.ehlo()`: Identifies the client to the SMTP server.
11. `server.starttls(context=context)`: Secures the SMTP connection using TLS.
12. `server.ehlo()`: Re-identifies the client after starting TLS.
13. `server.login(sender_email, password)`: Logs in to the SMTP server using the sender's email and password.
14. `server.sendmail(sender_email, receiver_email, message)`: Sends the email from the sender to the receiver with the specified message.

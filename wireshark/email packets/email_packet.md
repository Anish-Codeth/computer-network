# Capturing SMTP Packets with Wireshark

To capture SMTP packets using Wireshark, follow these steps:

1. **Open Wireshark**: Launch Wireshark on your computer.

2. **Start Capturing Packets**: Select your network interface and start capturing packets.

3. **Filter for SMTP Traffic**: Use the filter `smtp` to isolate SMTP traffic.

4. **Run the Python Script**: Execute the Python script provided. Replace the password placeholder with the actual password.

5. **Stop Capturing Packets**: Stop the capture after the email is sent.

6. **Analyze the SMTP Packet**: Find and analyze the SMTP packets related to the email.

![image](https://github.com/user-attachments/assets/18983e40-57be-4e53-bc6c-694fcc0058e6)

1. **TCP Connection Establishment**: The client and server establish a TCP connection using a three-way handshake (SYN, SYN-ACK, ACK) at the Transport Layer (Layer 4 of the OSI model).

2. **SMTP Server Greeting**: The SMTP server sends an SMTP 220 response code, indicating it is ready to proceed with communication.

![image](https://github.com/user-attachments/assets/ce7c1f91-6633-4eba-95b3-daa39342993d)
The EHLO command is used in SMTP (Simple Mail Transfer Protocol) to identify the client to the server. It stands for "Extended HELO" and is an enhanced version of the older HELO command. 

![image](https://github.com/user-attachments/assets/28449345-e2af-44a4-896c-cd171db6aa5c) 
1. **220 smtp.gmail.com**: The server's initial greeting, indicating it's ready to start the SMTP conversation.
2. **EHLO [client IP]**: The client's EHLO command, identifying itself and requesting the server's capabilities.
3. **250-smtp.gmail.com**: The server responds with a 250 code, listing its supported features.
4. **STARTTLS**: The client requests to start TLS(Transport Layer Security) encryption.
5. **220 2.0.0 Ready to start TLS**: The server confirms it's ready to begin the TLS session. 

 

![image](https://github.com/user-attachments/assets/f5de23c7-de3f-4fd0-a612-47189e403020)

 When the server receives the STARTTLS command, it responds with a message indicating that it's ready to proceed with the TLS handshake.

![image](https://github.com/user-attachments/assets/a1da97dd-1a72-48ad-88ae-4b71e32fcdba)
Mail is send using the encrypted channel .if the Transport layer security handshake is completed sucessfully.



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

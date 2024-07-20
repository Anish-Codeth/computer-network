# CAPTURING THE PACKET WHILE UPLOADING THE FILE IN LOCAL SERVER OF SIZE LESS THEN 10MB


## Steps to capture upload file


1. **Start Wireshark and Capture Traffic**

   - Open Wireshark.
   - Make sure Npcap is installed (if windows)
   - Select the network interface that the file upload will occur over.(if you have started the     server in your own machine then select the loopback interface)
   - Start capturing traffic by clicking the blue icon.

2.**Filter the traffic.**
    - In Filter tab search bar type 'http' .
    [HTTP Filter Image ]

3.**Locate Request**
    -Identify the post request .
    - The request will have large payload.

    [POST Request]
4.
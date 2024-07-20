# Capturing the Packet While Uploading a File to a Local Server (Size Less Than 10MB)

## Steps to Capture Upload File

### 1. Start Wireshark and Capture Traffic

- **Open Wireshark**
- **Install Npcap (if on Windows)**
- **Select Network Interface**
  - Choose the network interface that the file upload will occur over.
  - If you have started the server on your own machine, select the loopback interface.
- **Start Capturing Traffic**
  - Click the blue icon to begin capturing traffic.

### 2. Filter the Traffic

- **Apply HTTP Filter**
  - In the filter tab search bar, type `http` and apply the filter.
  ![HTTP Filter Image]

### 3. Locate Request

- **Identify the POST Request**
  - Look for the POST request which will have a large payload.
  ![POST Request]

### 4. Analyze the POST Request

- **Examine Packet Details**
  - Click on the identified POST request packet to examine its details.
- **Review the Payload**
  - Check the packet's payload to confirm it contains the data from your uploaded file. You should see the file content within the packet's data section.

---

Following these steps will help you capture and analyze the packet details while uploading a file to a local server.

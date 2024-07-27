# Capturing the Packet While Uploading a File to a Local Server (Size Less Than 10MB)

## Steps to Capture Upload File

### 1. Start Wireshark and Capture Traffic

- **Open Wireshark**
- **Install Npcap (if on Windows)**
- **Select Network Interface**
  - Choose the network interface that the file upload will occur over.
  - ![image](https://github.com/user-attachments/assets/9857c9f3-e8ad-4069-99c5-018b504f46ae)

  - If you have started the server on your own machine, select the loopback interface.
- **Start Capturing Traffic**
  - Click the blue icon to begin capturing traffic.

### 2. Filter the Traffic

- **Apply HTTP Filter**
  - In the filter tab search bar, type `http` and apply the filter.
    ![image](https://github.com/user-attachments/assets/785c917c-9cd2-482d-a0f6-9c70c7851d2a)

### 3. Locate Request

- **Identify the POST Request**
  - Look for the POST request which will have a large payload.
 ![image](https://github.com/user-attachments/assets/73f69b1e-2fd6-44df-a1dd-ed58ca196717)


### 4. Analyze the POST Request

- **Examine Packet Details**
  - Click on the identified POST request packet to examine its details.
  - ![image](https://github.com/user-attachments/assets/84474a9e-8d76-4e89-821f-d442a715bf7b)

- **Review the Payload**
  - Check the packet's payload to confirm it contains the data from your uploaded file. You should see the file content within the packet's data section.

---

Following these steps will help you capture and analyze the packet details while uploading a file to a local server.

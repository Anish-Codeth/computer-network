 
Launch the Cisco Packet Tracer application.
Create a Network Topology:

Drag and drop network devices such as a router, switch, and PCs onto the workspace.

2. Configure the Router as a DHCP Server


To set up automatic IP assignment using a DHCP server in Cisco Packet Tracer for connected PCs, follow these steps:

### 1. **Set Up the Network**

1. **Open Cisco Packet Tracer**:
   - Launch the Cisco Packet Tracer application.

2. **Create a Network Topology**:
   - Drag and drop network devices such as a router, switch, and PCs onto the workspace.

### 2. **Configure the Router as a DHCP Server**

1. **Configure the DHCP Pool**:
2. **Save the Configuration**:
   - Type `end` to exit global configuration mode.
   - Type `write memory` to save the configuration.

### 3. **Configure the PCs to Obtain an IP Address Automatically**

1. **Access the PC**:
   - Click on a PC and go to the "Desktop" tab.

2. **Set IP Configuration**:
   - Open the "IP Configuration" window.
   - Select the "DHCP" option to enable automatic IP assignment.

### 4. **Verify the Configuration**

1. **Check IP Address Assignment**:
   - Go to each PC and check the IP configuration to ensure they received an IP address from the DHCP server.

2. **Test Connectivity**:
   - Use the command prompt on the PCs to ping the default gateway or other PCs to verify network connectivity.

 
# Cisco Packet Tracer Project: Setting Up a DHCP Server

In this [project](dhcp_server.pkt), I configured a DHCP server to automatically assign IP addresses to hosts in the network.

## Steps Involved

1. **Set Up the Devices**:
   - Added a router, a switch, and several computers to the workspace.
   - Connected the computers to the switch, and the switch to the router.
   - Added a DHCP server to the network and connected it to the switch.

2. **Configure the DHCP Server**:
   - Opened the DHCP server configuration panel.
   - Enabled the DHCP service and configured the DHCP pool with the following settings:
     ```plaintext
     Network: 192.168.1.0
     Subnet Mask: 255.255.255.0
     Default Gateway: 192.168.1.1
     DNS Server: 8.8.8.8
     Starting IP Address: 192.168.1.2
     Ending IP Address: 192.168.1.100
     ```

3. **Configure the Router**:
   - Assigned an IP address to the router interface connected to the network.
     ```plaintext
     Interface 0/0: 192.168.1.1
     ```

4. **Configure the PCs**:
   - Set the IP configuration of each PC to DHCP mode, so they would automatically request an IP address from the DHCP server.

5. **Testing the Configuration**:
   - Observed the IP addresses assigned to each PC by opening the command prompt and using the `ipconfig` command:
     ```plaintext
     ipconfig
     ```
   - Verified that each PC received a unique IP address within the specified range and could communicate with other devices on the network.

## Conclusion

By setting up and configuring a DHCP server, I automated the process of IP address assignment for hosts in the network. This project demonstrated how DHCP simplifies network management by dynamically assigning IP addresses, reducing the need for manual configuration.


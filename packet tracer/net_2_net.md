# Different-Network Computer Ping in Packet Tracer

In this project, I set up a router to connect two different networks and successfully pinged a computer in one network from another network. The project file is linked [here](net2net_connection.pkt)

## Steps Involved

1. **Set Up the Devices**:
   - Placed a router in the workspace.
   - Added two switches and connected them to the router.
   - Added several computers to each switch.

2. **Configure the Router**:
   - Assigned IP addresses to the router interfaces connected to each network.
     ```plaintext
     Interface 0/0: 192.168.1.1
     Interface 0/1: 192.168.2.1
     ```

3. **Configure the PCs**:
   - Assigned IP addresses to the computers in each network.
     ```plaintext
     Network 1: 192.168.1.0/24
     PC1: 192.168.1.2
     PC2: 192.168.1.3
     
     Network 2: 192.168.2.0/24
     PC3: 192.168.2.2
     PC4: 192.168.2.3
     ```
   - Set the default gateway of the PCs to the IP address of the router interface for their respective networks.

4. **Testing Connectivity**:
   - Opened the command prompt on PC1 (192.168.1.2).
   - Pinging PC3 (192.168.2.2) using the command:
     ```plaintext
     ping 192.168.2.2
     ```
   - Observed successful ping replies, indicating that the router correctly routed the packets between the two networks.

## Conclusion

By configuring the router with appropriate IP addresses and setting the default gateways on the computers, I enabled communication between devices on different networks. This project demonstrated the basic principles of routing and network communication using Cisco Packet Tracer.

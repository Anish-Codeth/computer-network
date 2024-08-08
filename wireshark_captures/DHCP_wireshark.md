# DHCP Transactions Report

## Discover
**Frame Number:** 195  
**Frame Length:** 342 bytes (2736 bits)  
**Arrival Time:** Jul 28, 2024 09:19:08.560907000 +0545  
**Source:** Apple_8a:f1:31 (68:2f:67:8a:f1:31)  
**Destination:** Broadcast (ff:ff:ff:ff:ff:ff)

**Internet Protocol Version 4**  
- **Src Address:** 0.0.0.0  
- **Dst Address:** 255.255.255.255

**Dynamic Host Configuration Protocol (Discover)**  
- **Message Type:** Boot Request (1)  
- **Transaction ID:** 0x8cd05dfc  
- **Client MAC Address:** Apple_8a:f1:31 (68:2f:67:8a:f1:31)  
- **Host Name:** Sudhins-MBP

-[DHCP Discover] (https://github.com/Anish-Codeth/computer-network/blob/main/wireshark_captures/DHCP%20Discover.png)
---

## Offer
**Frame Number:** 196  
**Frame Length:** 590 bytes (4720 bits)  
**Arrival Time:** Jul 28, 2024 09:19:08.609482000 +0545  
**Source:** TPLink_1a:41:30 (00:5f:67:1a:41:30)  
**Destination:** Apple_8a:f1:31 (68:2f:67:8a:f1:31)

**Internet Protocol Version 4**  
- **Src Address:** 192.168.0.1  
- **Dst Address:** 192.168.0.103

**Dynamic Host Configuration Protocol (Offer)**  
- **Message Type:** Boot Reply (2)  
- **Transaction ID:** 0x8cd05dfc  
- **Your (client) IP Address:** 192.168.0.103  
- **DHCP Server Identifier:** 192.168.0.1

-[DHCP Offer] (https://github.com/Anish-Codeth/computer-network/blob/main/wireshark_captures/DHCP%20Offer.png)
---

## Request
**Frame Number:** 197  
**Frame Length:** 342 bytes (2736 bits)  
**Arrival Time:** Jul 28, 2024 09:19:09.612004000 +0545  
**Source:** Apple_8a:f1:31 (68:2f:67:8a:f1:31)  
**Destination:** Broadcast (ff:ff:ff:ff:ff:ff)

**Internet Protocol Version 4**  
- **Src Address:** 0.0.0.0  
- **Dst Address:** 255.255.255.255

**Dynamic Host Configuration Protocol (Request)**  
- **Message Type:** Boot Request (1)  
- **Transaction ID:** 0x8cd05dfc  
- **Client MAC Address:** Apple_8a:f1:31 (68:2f:67:8a:f1:31)

-[DHCP Request] (https://github.com/Anish-Codeth/computer-network/blob/main/wireshark_captures/DHCP%20Request.png)

---

## Acknowledge
**Frame Number:** 198  
**Frame Length:** 590 bytes (4720 bits)  
**Arrival Time:** Jul 28, 2024 09:19:09.612504000 +0545  
**Source:** TPLink_1a:41:30 (00:5f:67:1a:41:30)  
**Destination:** Apple_8a:f1:31 (68:2f:67:8a:f1:31)

**Internet Protocol Version 4**  
- **Src Address:** 192.168.0.1  
- **Dst Address:** 192.168.0.103

**Dynamic Host Configuration Protocol (Acknowledge)**  
- **Message Type:** Boot Reply (2)  
- **Transaction ID:** 0x8cd05dfc  
- **Your (client) IP Address:** 192.168.0.103  
- **DHCP Server Identifier:** 192.168.0.1  
- **Lease Time:** 2 hours (7200 seconds)

- [DHCP Acknowledge] (https://github.com/Anish-Codeth/computer-network/blob/main/wireshark_captures/DHCP%20Acknowledge.png)


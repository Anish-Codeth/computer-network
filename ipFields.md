
# IPV4 packet analysis
\- By Sunil Sapkota
A packet following IPv4 was captured on Wireshark for analysis. Here's its breakdown.

**_byte stream of packet_** : 45 00 00 43 f0 e5 00 00 40 11 a8 7a c0 a8 10 92 08 08 08 08

* **_version_** : 
   - field length = 4 bits
   - value = 4, indicating it uses ipv4 protocol
* **_Header length (IHL)_** : 
   - field length = 4 bits
   - value = 5, indicating that header length is 5 * (4 bytes or 32 bits)
* **_Differentiated Services Code Point (DSCP)_** : 
   - field length : 6 bits
   - Represents the Quality of Service (QoS) requirement for packet
   - value = 0, meaning that the type of service expected should be of "Best Effort"
* **_Explicit Congestion Notification (ENC)_** : 
   - field length = 2 bits 
   - valye = 0, meaning = (Not ECN-Capable Transport, Not-ECT)
* **_Total Length_** : 
   - field length = 16 bits 
   - value = 0x00(0) 0x43(67)
    * **_Identification_** : 0xf0 0xe5
    * **_Flags_** : 0x0
        * Reserved Bit : 0
        * Don't Fragment : 0
        * More Fragments : 0
    * **_Fragment offset_** : 0x0000
* **_Time to Live_** : 
   - field length = 8 bits
   - value = 0x40 (64)
* **_Protocol_** : 
   - field length = 8 bits
   - value = 0x11 (UDP) 
* **_Header Checksum_** :
   - field length = 16 bits
   - value = 0xa87a
* **_Source address_** :
   - field length = 32 bits
   - value = c0 a8 10 92 = 192.168.16.146
* **_Destination address_** :
   - field length = 32 bits
   - value 08 08 08 08 = 8.8.8.8


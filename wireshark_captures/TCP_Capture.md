# Packet Capture Summary

## Frame Details
- **Frame Number**: 8
- **Frame Length**: 66 bytes (528 bits)
- **Capture Length**: 66 bytes (528 bits)
- **Interface**: en0 (Wi-Fi)
- **Arrival Time**: Aug  9, 2024 08:20:04.166796000 +0545
- **UTC Arrival Time**: Aug  9, 2024 02:35:04.166796000 UTC
- **Epoch Arrival Time**: 1723170904.166796000
- **Protocols in Frame**: eth:ethertype:ip:tcp
- **Coloring Rule Name**: TCP SYN/FIN
- **Coloring Rule String**: tcp.flags & 0x02 || tcp.flags.fin == 1

## Ethernet II
- **Destination**: TPLink_1a:41:30 (00:5f:67:1a:41:30)
  - Address: TPLink_1a:41:30 (00:5f:67:1a:41:30)
  - LG bit: Globally unique address (factory default)
  - IG bit: Individual address (unicast)
- **Source**: Apple_8a:f1:31 (68:2f:67:8a:f1:31)
  - Address: Apple_8a:f1:31 (68:2f:67:8a:f1:31)
  - LG bit: Globally unique address (factory default)
  - IG bit: Individual address (unicast)
- **Type**: IPv4 (0x0800)

## Internet Protocol Version 4
- **Source Address**: 192.168.0.102
- **Destination Address**: 74.125.24.109
- **Version**: 4
- **Header Length**: 20 bytes (5)
- **Differentiated Services Field**: 0x00 (DSCP: CS0, ECN: Not-ECT)
- **Total Length**: 52
- **Identification**: 0x0000 (0)
- **Flags**: 0x2, Don't fragment
  - Reserved bit: Not set
  - Don't fragment: Set
  - More fragments: Not set
- **Fragment Offset**: 0
- **Time to Live**: 64
- **Protocol**: TCP (6)
- **Header Checksum**: 0x16cc [validation disabled]

## Transmission Control Protocol (TCP)
- **Source Port**: 51808
- **Destination Port**: 993
- **Sequence Number**: 95 (relative sequence number)
- **Acknowledgment Number**: 336 (relative ack number)
- **Header Length**: 32 bytes (8)
- **Flags**: 0x011 (FIN, ACK)
- **Window Size**: 44
- **Checksum**: 0x7b02 [unverified]
- **Urgent Pointer**: 0
- **Options**: (12 bytes), No-Operation (NOP), No-Operation (NOP), Timestamps

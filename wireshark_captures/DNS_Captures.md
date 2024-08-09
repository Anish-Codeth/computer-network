# Frame 71 Summary

## Frame Overview
- **Frame Length**: 127 bytes (1016 bits)
- **Capture Length**: 127 bytes (1016 bits)
- **Protocols in Frame**: Ethernet, IPv4, UDP, DNS
- **Coloring Rule Name**: UDP
- **Coloring Rule String**: udp

## Ethernet II Header
- **Source MAC Address**: TPLink_1a:41:30 (00:5f:67:1a:41:30)
- **Destination MAC Address**: Apple_8a:f1:31 (68:2f:67:8a:f1:31)
- **Type**: IPv4 (0x0800)

## Internet Protocol Version 4
- **Source Address**: 192.168.0.1
- **Destination Address**: 192.168.0.102
- **Header Length**: 20 bytes
- **Differentiated Services Field**: 0xb8 (DSCP: EF PHB, ECN: Not-ECT)
  - **DSCP**: Expedited Forwarding (46)
  - **ECN**: Not ECN-Capable Transport (0)
- **Total Length**: 113 bytes
- **Identification**: 0x2f6d (12141)
- **Flags**: 0x0
  - **Don't Fragment**: Not set
- **Fragment Offset**: 0
- **Time to Live**: 54
- **Protocol**: UDP (17)
- **Header Checksum**: 0xd29f (unverified)

## User Datagram Protocol
- **Source Port**: 53
- **Destination Port**: 59983
- **Length**: 93 bytes
- **Checksum**: 0x80d2 (unverified)

## DNS (Domain Name System) Response
- **Transaction ID**: 0x254c
- **Flags**: 0x8180 (Standard query response, No error)
- **Questions**: 1
- **Answer RRs**: 2
- **Authority RRs**: 0
- **Additional RRs**: 0

### DNS Details
- **Queries**: [Not displayed in this capture]
- **Answers**: [Not displayed in this capture]

- **Request In**: Frame 70
- **Time**: 0.041190000 seconds (from previous frame)

## Notes
- **Frame Number**: 71
- **Arrival Time**: Aug 9, 2024 08:20:07.762878000 +0545
- **Epoch Arrival Time**: 1723170907.762878000
- **Time Delta from Previous Captured Frame**: 0.041190000 seconds

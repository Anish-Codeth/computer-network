# Packet Capture Summary

## Frame Details
- **Frame Number**: 1
- **Frame Length**: 162 bytes (1296 bits)
- **Capture Length**: 162 bytes (1296 bits)
- **Interface**: en0 (Wi-Fi)
- **Arrival Time**: Aug  9, 2024 08:20:03.878169000 +0545
- **UTC Arrival Time**: Aug  9, 2024 02:35:03.878169000 UTC
- **Epoch Arrival Time**: 1723170903.878169000
- **Protocols in Frame**: eth:ethertype:ip:tcp:tls
- **Coloring Rule Name**: TCP
- **Coloring Rule String**: tcp

## Ethernet II
- **Destination**: Apple_8a:f1:31 (68:2f:67:8a:f1:31)
  - Address: Apple_8a:f1:31 (68:2f:67:8a:f1:31)
  - LG bit: Globally unique address (factory default)
  - IG bit: Individual address (unicast)
- **Source**: TPLink_1a:41:30 (00:5f:67:1a:41:30)
  - Address: TPLink_1a:41:30 (00:5f:67:1a:41:30)
  - LG bit: Globally unique address (factory default)
  - IG bit: Individual address (unicast)
- **Type**: IPv4 (0x0800)

## Internet Protocol Version 4
- **Source Address**: 74.125.24.109
- **Destination Address**: 192.168.0.102
- **Version**: 4
- **Header Length**: 20 bytes (5)
- **Differentiated Services Field**: 0x00 (DSCP: CS0, ECN: Not-ECT)
- **Total Length**: 148
- **Identification**: 0xa0e1 (41185)
- **Flags**: 0x0
  - Reserved bit: Not set
  - Don't fragment: Not set
  - More fragments: Not set
- **Fragment Offset**: 0
- **Time to Live**: 54
- **Protocol**: TCP (6)
- **Header Checksum**: 0xbf8a [validation disabled]

## Transmission Control Protocol
- **Source Port**: 993
- **Destination Port**: 51808
- **Sequence Number**: 1 (relative sequence number)
- **Acknowledgment Number**: 1 (relative ack number)
- **Header Length**: 32 bytes (8)
- **Flags**: 0x018 (PSH, ACK)
- **Window**: 261
- **Checksum**: 0x2832 [unverified]
- **Urgent Pointer**: 0
- **Options**: (12 bytes), No-Operation (NOP), No-Operation (NOP), Timestamps

## Payload
- **TCP Payload**: 96 bytes

## Transport Layer Security
- **TLSv1.2 Record Layer**: Application Data Protocol: Internet Message Access Protocol
  - **Content Type**: Application Data (23)
  - **Version**: TLS 1.2 (0x0303)
  - **Length**: 91 bytes
  - **Encrypted Application Data**: 
    ```
    000000000000000105fd6b5506ab1432a5a03f5c42e5003f71cf8a82016a71d00156f7dda533cf3ba4552441f116025fa1178c07826ca9f31a3537ee1293f7730b1434fd9cbdecdc27e4a55ed8e2bb13aa032c2e4afa4ccadfd0d3
    ```
  - **Application Data Protocol**: Internet Message Access Protocol

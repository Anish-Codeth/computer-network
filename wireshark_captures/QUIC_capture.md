# Packet Capture Summary

## Frame Details
- **Frame Number**: 39
- **Frame Length**: 1392 bytes (11136 bits)
- **Capture Length**: 1392 bytes (11136 bits)
- **Interface**: en0 (Wi-Fi)
- **Arrival Time**: Aug  9, 2024 08:20:07.517578000 +0545
- **UTC Arrival Time**: Aug  9, 2024 02:35:07.517578000 UTC
- **Epoch Arrival Time**: 1723170907.517578000
- **Protocols in Frame**: eth:ethertype:ip:udp:quic:tls
- **Coloring Rule Name**: UDP
- **Coloring Rule String**: udp

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
- **Destination Address**: 17.253.18.227
- **Version**: 4
- **Header Length**: 20 bytes (5)
- **Differentiated Services Field**: 0x01 (DSCP: CS0, ECN: ECT(1))
  - Differentiated Services Codepoint: Default (0)
  - Explicit Congestion Notification: ECN-Capable Transport codepoint '01' (1)
- **Total Length**: 1378
- **Identification**: 0x0000 (0)
- **Flags**: 0x2, Don't fragment
  - Reserved bit: Not set
  - Don't fragment: Set
  - More fragments: Not set
- **Fragment Offset**: 0
- **Time to Live**: 64
- **Protocol**: UDP (17)
- **Header Checksum**: 0x4f9c [validation disabled]

## User Datagram Protocol (UDP)
- **Source Port**: 50835
- **Destination Port**: 443
- **Length**: 1358
- **Checksum**: 0xd004 [unverified]
- **Stream Index**: 1

## QUIC Packet Details
- **Packet Length**: 1350 bytes
- **Header Form**: Long Header (1)
- **Fixed Bit**: True
- **Packet Type**: Initial (0)
- **Reserved**: 0
- **Packet Number Length**: 1 byte (0)

## Connection Information
- **Version**: 1 (0x00000001)
- **Destination Connection ID Length**: 8 bytes
- **Destination Connection ID**: 507886c63db93da5
- **Source Connection ID Length**: 8 bytes
- **Source Connection ID**: b6326d971ad0b891
- **Token Length**: 0 bytes
- **Length**: 1324 bytes
- **Packet Number**: 0
## Payload (Truncated)
- **Payload**: dccb0af5d67deb005569374b915db935d44dd2013a26e3b8c4f826271b04c2d1f6708b730fdb82808de57abe4f302349d868bfef8b7df272b7ba31c0d4e5c58597e2924da1ab7dd6b0690204df9dcef2decbe04684bf74f4a5a828963d28336e046407266c10a57eabf2be854f

## CRYPTO
- **Padding Length**: 1009 bytes

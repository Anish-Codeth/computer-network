# Packet Capture Summary

## Frame Details
- **Frame Number**: 10
- **Frame Length**: 217 bytes (1736 bits)
- **Capture Length**: 217 bytes (1736 bits)
- **Interface**: en0 (Wi-Fi)
- **Arrival Time**: Aug  9, 2024 08:20:04.171124000 +0545
- **UTC Arrival Time**: Aug  9, 2024 02:35:04.171124000 UTC
- **Epoch Arrival Time**: 1723170904.171124000
- **Protocols in Frame**: eth:ethertype:ip:udp:ssdp
- **Coloring Rule Name**: UDP
- **Coloring Rule String**: udp

## Ethernet II
- **Destination**: IPv4mcast_7f:ff:fa (01:00:5e:7f:ff:fa)
  - Address: IPv4mcast_7f:ff:fa (01:00:5e:7f:ff:fa)
  - LG bit: Globally unique address (factory default)
  - IG bit: Group address (multicast/broadcast)
- **Source**: Apple_8a:f1:31 (68:2f:67:8a:f1:31)
  - Address: Apple_8a:f1:31 (68:2f:67:8a:f1:31)
  - LG bit: Globally unique address (factory default)
  - IG bit: Individual address (unicast)
- **Type**: IPv4 (0x0800)

## Internet Protocol Version 4
- **Source Address**: 192.168.0.102
- **Destination Address**: 239.255.255.250
- **Version**: 4
- **Header Length**: 20 bytes (5)
- **Differentiated Services Field**: 0x00 (DSCP: CS0, ECN: Not-ECT)
- **Total Length**: 203
- **Identification**: 0x67fe (26622)
- **Flags**: 0x0
  - Reserved bit: Not set
  - Don't fragment: Not set
  - More fragments: Not set
- **Fragment Offset**: 0
- **Time to Live**: 1
- **Protocol**: UDP (17)
- **Header Checksum**: 0xa01b [validation disabled]

## User Datagram Protocol
- **Source Port**: 65472
- **Destination Port**: 1900
- **Length**: 183
- **Checksum**: 0x6418 [unverified]

## UDP Payload
- **Length**: 175 bytes

## Simple Service Discovery Protocol (SSDP)
- **Request Line**: M-SEARCH * HTTP/1.1\r\n
  - **Request Method**: M-SEARCH
  - **Request URI**: *
  - **Request Version**: HTTP/1.1
- **HOST**: 239.255.255.250:1900\r\n
- **MAN**: "ssdp:discover"\r\n
- **MX**: 1\r\n
- **ST**: urn:dial-multiscreen-org:service:dial:1\r\n
- **USER-AGENT**: Google Chrome/127.0.6533.73 Mac OS X\r\n
- **End of Request**: \r\n

# IPV4 Field on captured packet
    :: 45 00 00 43 f0 e5 00 00 40 11 a8 7a c0 a8 10 92 08 08 08 08 ::

    * version : 4 bits : 4
    * Header length (IHL) : 4 bits : 5
    * Differentiated Services Code Point (DSCP) : 6 bits : 0  : meaning (Best Effort) // QoS requirement for packet
    * Explicit Congestion Notification (ENC) : 2 bits : 0 : meaning (Not ECN-Capable Transport, Not-ECT)
    * Total Length : 16 bits : 0x00 0x43 : 67
        * Identification : 0xf0 0xe5
        * Flags : 0x0
            * Reserved Bit : 0
            * Don't Fragment : 0
            * More Fragments : 0
        * Fragment offset : 0x0000
    * Time to Live : 0x40
    * Protocol : UDP ( 0x11)
    * Header Checksum : 0xa87a [validation disabled]  : status -> unverified
    * Source address : c0 a8 10 92 : 192.168.16.146
    * Destination address : 08 08 08 08 : 8.8.8.8


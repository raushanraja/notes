Kamailio® is an open-source SIP server with powerful features for VoIP and real-time communications. Here are some of its key features:
+ Scalability: Kamailio can handle thousands of call setups per second, making it ideal for large platforms.
+ Versatility: Kamailio can be used to build platforms for presence, WebRTC, instant messaging, and other applications. It can also be used for scaling up SIP-to-PSTN gateways, PBX systems, or media servers like Asterisk™, FreeSWITCH™, or SEMS.
+ Security: Kamailio supports secure communication via TLS for voice, video, and text, as well as WebSocket support for WebRTC.
+ Compatibility: Kamailio supports both IPv4 and IPv6.
+ Instant Messaging and Presence: Kamailio supports SIMPLE instant messaging and presence with embedded XCAP server and MSRP relay.
+ Asynchronous Operations: Kamailio supports asynchronous TCP, UDP, and SCTP, as well as asynchronous operations for improved performance.
+ IMS Extensions: Kamailio has IMS extensions for VoLTE.
+ Routing: Kamailio supports DID and least cost routing, load balancing, and routing fail-over.
+ Backend Systems: Kamailio supports many backend systems such as MySQL, Postgres, Oracle, Radius, LDAP, Redis, Cassandra, MongoDB, and Memcached.
+ Control Interface: Kamailio supports Json and XMLRPC control interface.
+ Monitoring: Kamailio supports SNMP monitoring.

### Possible Conditions for setting the flags when dealing with SIP and Websocket
1. If the request is from a NATed client
2. If the request can handle both IPv4 and IPv6
3. If the request is from a SIP client
4. If the request is from a SIP client and the call is incoming
5. If the request is from a SIP client and the call is outgoing
6. If the request is for a bridged RTP stream:
- NATed client
- IPv4 --> IPv6
- IPv6 --> IPv4
- SIP --> Web
- Web --> SIP
- Web --> Web
- SIP --> SIP

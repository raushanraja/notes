### Protocols Categoriztion
- Protocols can be categorized in various ways based on
    - Purpose
    - Architecture
    - Communication characteristics
- Some of these categories are given below


#### 1. Purpose-Based Categoriztion
| Protocol Categoriztion              | Descriptoin| Examples|
|-------------------------------------|------------|---------|
|`Communication Protocols`        |Facilitates Communication and data exchange between systems.               | TCP/IP, FTP, HTTP   |
|`Routing Protocols`              |Helps in determing optimal path for data to travel on network.             | OSPF, BGP           |
|`Application Layer Protocols`    |Designed for specific application level task, like email, web browsing     | POP, SMTP, HTTP, FPT|


#### 2. Architecture-Based Categoriztion
| Protocol Categoriztion              | Descriptoin| Examples|
|-------------------------------------|------------|---------|
|`Client-Server Protocols`            |One entity(client) request resource from another entity(server)        | FTP, HTTP   |
|`Peer-to-Peer Protocols`             |Enables Communication between two entity without a central server      | Bittorrent  |
|`Layered Protocols`                  |Protocols are part of layered architecture, such as OSI Layer          | TCP, IP     |



# Rough
    Transport Layer Protocols:
        Connection-Oriented Protocols: These protocols, like TCP, establish a reliable connection between sender and receiver before data transfer, ensuring data integrity and order.
        Connectionless Protocols: Protocols like UDP do not establish a connection and provide minimal error checking. They are often used for real-time applications where speed is more critical than reliability.

    Stateful vs. Stateless Protocols:
        Stateful Protocols: These protocols maintain session state information, often requiring both parties to keep track of the current communication status. Examples include FTP and SIP.
        Stateless Protocols: Stateless protocols do not store session information, and each message or request is processed independently. HTTP is a common example.

    Text-Based vs. Binary Protocols: As discussed earlier, protocols can be categorized as text-based (using human-readable text) or binary (using machine-readable binary data) based on how they represent data.

    Secure vs. Non-Secure Protocols:
        Secure Protocols: These protocols incorporate encryption and authentication mechanisms to ensure the confidentiality and integrity of data. Examples include HTTPS (secure HTTP) and SSH (secure shell).
        Non-Secure Protocols: Protocols without built-in security measures may transmit data in plaintext. Examples include HTTP and Telnet.

    Wireless vs. Wired Protocols:
        Wireless Protocols: These are designed for communication over wireless networks, like Wi-Fi or cellular networks. Examples include Wi-Fi (802.11) protocols and 4G/5G protocols.
        Wired Protocols: These are designed for communication over physical wired connections, such as Ethernet (IEEE 802.3).

    Network Layer Protocols:
        Internet Layer Protocols: Protocols used for routing and forwarding data between networks, such as IP (IPv4 and IPv6).
        Link Layer Protocols: Protocols used for data framing, addressing, and error handling at the data link layer, like Ethernet and PPP.

    Operating System-Specific Protocols:
        Some protocols are designed specifically for use with particular operating systems or platforms, such as NetBIOS for Windows networking.

These are just some of the ways to categorize protocols. The choice of categorization depends on the context and the specific criteria you want to emphasize when discussing or studying network protocols.

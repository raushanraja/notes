## OSI Model - Open Source InterConnection Model
### Layers Of OSI Model:
+ Application Layer - Manages data from the actual application
+ Persentation Layer - Encode and decode data as per requirement
+ Session Layer - Attaches session information to data
+ Transport Layer - Breaks the data into segments  and adds dest and source port
+ Network Layer - Attaches source and destination IP address to each packet
+ Data Layer - Breaks the packets into frames and add MAC address to each frame
+ Physical Layer - Transmit the data as bits over network  

#### PDU (Protocol Data Unit)
- The unit of data at different layer of OSI(Open Standard Interconnection) model is reffered as PDU.
- At different layers of OSI the PDU is reffered as following:
    - Transport Layer   -> Segment
    - Network Layer     -> Packet
    - Data-Link Layer   -> Frame
- All of three `Segment`, `Packet` and `Frame` is unit of data at given layer.




#### Layers and commonly used protocols 
Layer # |OSI NAME       |SNA Name      | COMMON PROTOCOL OR USE   | PDU NAME
------- |-------------- |------------- | ------------------------ | ------------------------
Layer 1 |Physical       |Physical      | Transceiver              | bits, or a physical signal
Layer 2 |Datalink       |Datalink      | Ethernet                 | frame
Layer 3 |Network        |Path Control  | IP                       | packet
Layer 4 |Transport      |Transmission  | TCP, UDP                 | segment, datagram 
Layer 5 |Session        |Data Flow     | SIP                      | data, request, or response
Layer 6 |Presentation   |Presentation  | Encryption/compression   | data, request, or response
Layer 7 |Application    |Application   | HTTP                     | data, request, or response




#### Notes:
- SNA: System Network Architecture, A data communitaion Architecture established by IBM.

#### References:
- https://www.baeldung.com/cs/osi-packets-vs-frames
- https://www.geeksforgeeks.org/difference-between-segments-packets-and-frames/
- https://www.baeldung.com/cs/networking-packet-fragment-frame-datagram-segment
- https://www.educative.io/blog/osi-model-layers

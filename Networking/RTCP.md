#### RTCP
- RTCP is primarily used for quality monitoring and control in real-time multimedia streaming sessions. 
- It operates alongside RTP (Real-Time Transport Protocol) to provide feedback on the quality of the media transmission.
- Including metrics such as 
    - packet loss, 
    -  jitter, 
    - and round-trip time. 
- RTCP packets are periodically exchanged between participants in a session to gather and report this feedback information.

##### Use cases for RTCP:
- Quality monitoring and analysis of real-time media streams
- Synchronization of multimedia streams
- Participant control and management in conferencing applications


#### RTSP
- RTSP is a network control protocol designed for establishing and controlling media sessions between a client and a server. 
- It provides the framework for client-server interaction to facilitate the control of streaming media
- Including 
    - session setup, 
    - media description exchange, 
    - and control commands such as play, 
    - pause, and stop. 
- RTSP is commonly used for managing live streaming sessions, video-on-demand services, and interactive multimedia applications.

##### Use cases for RTSP:
- Session setup and control for streaming media
- Media server communication and control
- Interactive multimedia applications

#### Summary, RTCP  vs RTSP
- RTCP  is primarily focused on monitoring and control of real-time media streams, providing feedback on quality metrics. 
- RTSP is used for session control and management of streaming media, allowing clients to establish, control, and interact with media sessions on servers. 
- The choice between RTCP and RTSP depends on the specific requirements and objectives of the real-time communication application or service being implemented.


#### A comparision between RTCP, RTSP and Similarity with HTTP  
| Aspect                                | RTSP                                 | RTCP                                 | HTTP                                 |
|---------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|
| Protocol Purpose                      | Session control and coordination     | Control and monitoring of media      | Data transfer and resource retrieval |
| Header Format                         | Line-by-line text-based              | Binary                               | Line-by-line text-based              |
| Port Number                           | Default: 554                         | N/A (Uses same port as RTP)          | Default: 80                          |
| Message Structure                     | Request and response messages        | Packet-based                         | Request and response messages        |
| URI Scheme                            | rtsp://                              | N/A                                  | http:// or https://                  |
| Transport Layer                       | Typically over TCP                   | Typically over UDP                   | Typically over TCP                   |
| Media Transport                       | Not responsible for media transport  | Not responsible for media transport  | Not responsible for media transport  |
| Control Information                   | Session setup, play, pause, teardown | Quality feedback, control statistics | N/A                                  |
| Session Management                    | Yes                                  | N/A                                  | N/A                                  |
| Data Transfer                         | No                                   | No                                   | Yes                                  |
| Authentication and Security Mechanism | Supported                            | N/A                                  | Supported                            |

#### A Visual representation of RTCP and RTSP Packet
- RTCP
    ```  
          0                   1                   2                   3
          0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
         +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
         |V=2|P|    RC   |   PT=RR=201   |             length            |
         +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
         |                     SSRC of sender                            |
         +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
         |                         SSRC_1                                |
         +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
         | fraction lost |       cumulative number of packets lost       |
         +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
         |           extended highest sequence number received           |
         +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
         |                      interarrival jitter                      |
         +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
         |                         last SR (LSR)                         |
         +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
         |                   delay since last SR (DLSR)                  |
         +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
         |                          (optional)                           |
         |                  feedback control information                 |
         |                          (optional)                           |
         +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    ```

- RTSP
    ```
    RTSP/1.0 200 OK
    CSeq: 1
    Date: Wed, 26 Jan 2022 10:30:00 GMT
    Content-Length: 0
    Session: 12345678
    ```

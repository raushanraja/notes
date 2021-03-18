## SIP : Session Initial Protocal

### Introduction:
+ It is one of the most common protocol for VOIP technology.
+ It is an application layer signalling protocol.
+ This protocol is used to create, modify and terminate a multimedia session over IP.
+ It embodies `client-server` architecture and uses `URI`, `URL` from HTTP & header Style from `SMTP`.
+ It uses the `SDP (Session Description Protocol` and `RTP (Real Time Transport Protocol)` for delivering multimedia protocol network.
+ It supports both unicast and multicast communication.
+ It is defined in RFC 3261.


<figure align="center">
  <img src="OSI-SIP-Architecture.jpg" alt="SIP Protocol Architecture" >
  <figcaption>SIP Protocol Architecture</figcaption>
</figure> 

----------


### 2. SIP Network elements
+ To create a communication network SIP requires following elements:
  + User Agent
  + Proxy Server
  + Registrar Server
  + Redirect Server
  + Location Server

#### 2.1 User Agent
+ User Agents are end-point devices such as softphone, mobile or laptop.
+ There are divided into two parts:
  + User Agent Client(UAC) : Sends a request to UAS
  + User Agent Server(UAS) : Sends reponse based on request

#### 2.2 Proxy Server
+ Proxy Server sits between two User Agents &
+ It forwards the request from on UA to another based on URI.
+ There can be max 70 proxy server between source & destination.
+ Types of proxy server:
  + Stateless: Simply forwads the request % not store any information about the call transaction
  + Statefil: Forwards the call and keep track of each request and response received.



#### 2.3 Registrar Server
+ The registrar server accepts registration requests from user agents.
+ It helps users to authenticate themselves within the network.
+ It stores the URI and the location of users in a database to help other SIP servers within the same domain.
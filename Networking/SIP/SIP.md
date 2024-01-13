
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
+ It forwards the request from on UA to another party based on URI.
+ There can be max 70 proxy server between source & destination.
+ Types of proxy server:
  + Stateless: Simply forwads the request % not store any information about the call transaction
  + Statefil: Forwards the call and keep track of each request and response received.



#### 2.3 Registrar Server
+ The registrar server accepts registration requests from user agents.
+ It helps users to authenticate themselves within the network.
+ It stores the URI and the location of users in a database to help other SIP servers within the same domain.



#### 2.4 Redirect Server
+ It is mainly used to redirect a request to the other party.
+ Redirect Server, upon receiving a requests looks for intended recipient in database.
+ Upon finding a recipient, the server responds with 3xx ( Redirect response) to requester.
+ The intended recipient's location in database is created when a user completes the registration.


#### 2.5 Location Server
+ Location server provides possible location of a caller.
+ A Proxy or Registration Server can request a location server for the caller's location.


### 3. SIP Core Methods:
+ INVITE
+ BYE
+ REGISTER
+ CANCEL
+ ACK
+ OPTIONS
+ SUBSCRIBE
+ NOTIFY
+ PUBLISH
+ INFO
+ REFER
+ MESSAGE
+ UPDATE

#### 3.1: Transaction VS Non- Transactional Methods

#### 3.1.1 Transaction Methods
+ Transactional methods in SIP are those methods that involve establishing or modifying a session between two endpoints. 
+ These methods are typically used to initiate or modify a session, and the sequence of SIP messages exchanged between endpoints follows a specific transactional model.

#### 3.1.2 Non-Transaction Methods
+ In contrast, non-INVITE transactions are those that do not involve session establishment or modification. 
+ These include methods such as OPTIONS, REGISTER, INFO, and NOTIFY. 
+ Non-INVITE transactions typically involve a single request and a single response message, without any intermediate provisional responses.

![[basic 2023-05-09 19.50.35.excalidraw.png]]

							Fig1. Transactional VS Non-Transactional Methods


#### 3.2 Request VS Response methods

#### 3.2.1 Request Methods
+ Request methods are used by SIP user agents to initiate a transaction with another user agent. 
+ The most commonly used request method is INVITE, which is used to initiate a session between two endpoints. 
+ Some of the methods are described below:
    + INVITE: Requests that a user or service be invited to participate in a session.
    + ACK: Confirms that the client has received a final response to an INVITE request.
    + OPTIONS: Requests information about the capabilities of a server or the status of a connection.
    + BYE: Terminates a session between two users or services.
    + CANCEL: Cancels a pending request that has not yet received a final response.
    + REGISTER: Registers the user's current location and contact information with a server.
    + SUBSCRIBE: Requests that a user or service be notified of a specified event or state change.
    + NOTIFY: Sends a notification to a subscriber indicating that an event or state has occurred.
    + MESSAGE: Sends an instant message between two users or services.


#### 3.2.1 Response Methods
+ Response methods are used to respond to a request made by another SIP user agent. 
+ For example, replyting with 100 Trying message to an INVITE request. 
+ Some of these methods are:
    + 1xx: Provisional responses, indicating that the server has received the request and is processing it.
    + 2xx: Success responses, indicating that the request was successfully completed.
    + 3xx: Redirection responses, indicating that the request should be sent to a different server or location.
    + 4xx: Client error responses, indicating that the request was malformed or invalid.
    + 5xx: Server error responses, indicating that the server encountered an error while processing the request.
    + 6xx: Global error responses, indicating that the request cannot be completed due to some global condition.


![[a.png]]

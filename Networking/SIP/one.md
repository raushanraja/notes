### Abbreviatioins:
  - UAC: User Agent Client




### SIP Tags:
  - SIP uses tags to make a dialog unique, even in case of call forking
  - There are two types of tags: local (From) and remote (To).
  - The UAC puts its tag in the From header, and the UAS puts its tag in the To header.
  - The UAC puts the tag in the From when creating a new SIP Message
  - When a UAS responds to a message, it adds a tag to the To header.
  - Multiple clients can receive the same message, but they will all add their own unique tag values.
  - This results in the same From tag and different To tags depending on who is responding.




### SIP VIA header:
  - A Via header
    - protocol
    - version
    - transpor types
    - IP address, and 
    - port used for the request.

  - When a Sender UAC creates a SIP request, it must include a Via before Sending it.
  - If a Via header already in the message, the UAC adds the new one at the top of the list before sending it to the next hop.
  - The recipient of the request removes the top Via header and sends the response to the indicated party, and this process continues until the response reaches the original sender.
  - The Via header contains a unique "branch" parameter that identifies the request across space and time and is used to facilitate its use as a transaction ID.
  - The uniqueness of the branch parameter (beginning with "z9hG4bK.") is used to identify that the branch was created in accordance with RFC 3261 and not the older RFC 2543.


### Sending SIP Messages through proxy

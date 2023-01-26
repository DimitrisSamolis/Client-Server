# Client-Server
Communication Between Server-Client





Education                                                     D. Samolis
Internet-Draft                                     University of Piraeus
Intended status: Informational                             June 13, 2022
Expires: December 15, 2022


                       Semester project for 2022
                     draft-samolis-unipi-project-00

Abstract

   The purpose of this document is to describe our project in the
   Internet Protocols subject.

Status of This Memo

   This Internet-Draft is submitted in full conformance with the
   provisions of BCP 78 and BCP 79.

   Internet-Drafts are working documents of the Internet Engineering
   Task Force (IETF).  Note that other groups may also distribute
   working documents as Internet-Drafts.  The list of current Internet-
   Drafts is at https://datatracker.ietf.org/drafts/current/.

   Internet-Drafts are draft documents valid for a maximum of six months
   and may be updated, replaced, or obsoleted by other documents at any
   time.  It is inappropriate to use Internet-Drafts as reference
   material or to cite them other than as "work in progress."

   This Internet-Draft will expire on December 15, 2022.

Copyright Notice

   Copyright (c) 2022 IETF Trust and the persons identified as the
   document authors.  All rights reserved.

   This document is subject to BCP 78 and the IETF Trust's Legal
   Provisions Relating to IETF Documents
   (https://trustee.ietf.org/license-info) in effect on the date of
   publication of this document.  Please review these documents
   carefully, as they describe your rights and restrictions with respect
   to this document.  Code Components extracted from this document must
   include Simplified BSD License text as described in Section 4.e of
   the Trust Legal Provisions and are provided without warranty as
   described in the Simplified BSD License.






Samolis                 Expires December 15, 2022               [Page 1]

Internet-Draft          Semester project for 2022              June 2022


Table of Contents

   1.  Introduction  . . . . . . . . . . . . . . . . . . . . . . . .   2
     1.1.  Requirements Language . . . . . . . . . . . . . . . . . .   2
   2.  What messages are included  . . . . . . . . . . . . . . . . .   3
   3.  What are the header's fields  . . . . . . . . . . . . . . . .   3
     3.1.  Protocol Header Format  . . . . . . . . . . . . . . . . .   3
       3.1.1.  First header  . . . . . . . . . . . . . . . . . . . .   3
       3.1.2.  Second header . . . . . . . . . . . . . . . . . . . .   4
   4.  Server's Port . . . . . . . . . . . . . . . . . . . . . . . .   5
   5.  IANA Considerations . . . . . . . . . . . . . . . . . . . . .   5
   6.  Security Considerations . . . . . . . . . . . . . . . . . . .   5
   7.  Informative References  . . . . . . . . . . . . . . . . . . .   5
   Author's Address  . . . . . . . . . . . . . . . . . . . . . . . .   5

1.  Introduction

   The purpose of this document is simple.  To describe my own Protocol
   that I have created.  This Protocol is based on Server-Client
   connection and it can calculate 2 numbers from the Client side and
   appear the total.  Also, we have made this Protocol Multi-Client
   which means that one Server can connect with many Clients (max=5).

   This document follows the keyword use as specified in RFC2119
   [RFC2119].

   This document uses the following terms:

      Protocol - A pre-approved communication language between two end
      systems.

      Server - The part of the communication protocol that receives the
      request.  In this project the server is an endpoint for
      calculator.

      Client - The part of the communication protocol that starts the
      request.  In this project the client has to insert two numbers and
      a calculating method.

      byte - An 8-bit octet

1.1.  Requirements Language

   The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
   "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this
   document are to be interpreted as described in RFC2119 [RFC2119].





Samolis                 Expires December 15, 2022               [Page 2]

Internet-Draft          Semester project for 2022              June 2022


2.  What messages are included

   1.First of all, Server sends a message when it is ready to receive
   attributes.

   2.Then, when a client joins the Server it sends a message with the
   port and the IP address and also in which thread it is because a
   server connects in many threads.

   3.When the connection is succed Client gets a message to input 2
   numbers and the calculating method that is prefered.

   4.Finally, it returns the total of the calculation to the Server and
   the connection shuts down for this Client.

   Figure 1

                        Server                            Client
                        |                                  |
                        |             Ready(1)             |
                        | -------------------------------> |
                        |                                  |
                        |            Connects              |
                        | <------------------------------- |
                        |                                  |
                        |               (2)                |
                        | -------------------------------> |
                        |                                  |
                        |               (3)                |
                        | <------------------------------- |
                        |                                  |
                        |               (4)                |
                        | -------------------------------> |
                        |                                  |


                        Figure 1: Message Exchange

3.  What are the header's fields

3.1.  Protocol Header Format

3.1.1.  First header

   This is the first message sent by the Client to initiate the
   communication process...

   The following figure shows the message format.



Samolis                 Expires December 15, 2022               [Page 3]

Internet-Draft          Semester project for 2022              June 2022


       0                   1                   2                   3
       0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
      |        Message Type           |           Length              |
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
      |                               ID                              |
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
      |        Number 1               |           Number2             |
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
      |                      Calculating Method                       |
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+


                         Figure 2: A Header Format

   o  Message Type - 16 bits unsigned integer: The message type.  For
      this message, the message type MUST be 0.

   o  Number1,Number2,calculatingMethod - 2 bits unsigned short integer.

   o  Length - 16 bits unsigned integer.  The value for this message
      MUST be 8.

   o  ID- transaction ID.

3.1.2.  Second header

   This is the message sent by the Server to send back the total of the
   calculation...

   The following figure shows the message format.

       0                   1                   2                   3
       0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
      |        Message Type           |           Final               |
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
      |                               ID                              |
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+


                         Figure 3: A Header Format

   o  Message Type - 16 bits unsigned integer: The message type.  For
      this message, the message type MUST be 0.

   o  Final - 2 bits unsigned short integer: The outcome of the
      calculation



Samolis                 Expires December 15, 2022               [Page 4]

Internet-Draft          Semester project for 2022              June 2022


   o  ID- transaction ID.

4.  Server's Port

   The server receive messages at port 12345

5.  IANA Considerations

   This memo makes no requests to IANA.

6.  Security Considerations

   There is no security in this specification.  This is a prototype and
   all messages should be sent in cleartext over the wire.

   This is a VERY unsecure protocol.  Please do not implement.

7.  Informative References

   [RFC2119]  Bradner, S., "Key words for use in RFCs to Indicate
              Requirement Levels", BCP 14, RFC 2119,
              DOI 10.17487/RFC2119, March 1997,
              <https://www.rfc-editor.org/info/rfc2119>.

Author's Address

   Dimitrios Samolis
   University of Piraeus
   Department of Digital Systems
   Piraeus  18534
   Greece

   Email: dimitrissamolis2001@gmail.com


















Samolis                 Expires December 15, 2022               [Page 5]

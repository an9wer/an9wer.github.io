.. meta::
    :robots: noindex

Mail
====

Port 587 is used for communication between an MUA and an MSA.

Port 25 is used for communication between MTAs, or from an MSA to an MTA. (Port
25 may be blocked by ISP or cloud server provider)

::

    MUA -> MSA -> MTA -> MTA -> ... -> MTA -> MDA -> MUA

Message submission agent (MSA)
------------------------------

Message submission agent or mail submission agent is a computer program or
software agent that receives electronic mail messages from a mail user agent
(MUA) and cooperates with a mail transfer agent (MTA) for delivery of the mail.

Message transfer agent (MTA)
----------------------------

Message transfer agent or mail transfer agent or mail relay is software that
transfers electronic mail messages from one computer to another using SMTP.

Message transfer agent receives mail from either another MTA, a mail
submission agent (MSA), or a mail user agent (MUA). 

Mail retrieval agent (MRA)
--------------------------

Mail retrieval agent (MRA) is a computer application that retrieves or fetches
e-mail from a remote mail server and works with a mail delivery agent to
deliver mail to a local or remote email mailbox.

MRAs may be external applications by themselves or be built into a bigger
application like an MUA.  Significant examples of standalone MRAs include
fetchmail and getmail.

Message delivery agent (MDA)
----------------------------

Mail delivery agent or message delivery agent (MDA) is a computer software
component that is responsible for the delivery of e-mail messages to a local
recipient's mailbox.

References
----------

`Wikipedia: MSA
<https://en.wikipedia.org/wiki/Message_submission_agent>`_

`Wikipedia: MTA
<https://en.wikipedia.org/wiki/Message_transfer_agent>`_

`Wikipedia: MRA
<https://en.wikipedia.org/wiki/Mail_retrieval_agent>`_

`Wikipedia: MDA
<https://en.wikipedia.org/wiki/Mail_delivery_agent>`_

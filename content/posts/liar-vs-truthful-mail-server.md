--- 
draft: false
date: 2009-03-01T00:00:00+08:00
title: "Liar vs Truthful Mail Server"
tags: [mail,mailserver]
---

Once upon a time, when spam was not yet an "in thing", mail servers where all truthful. A mail server that sends an email to another for a non-existing address always receives a notice from its peer that says "Sorry buddy, I can't find it in my address list." Years later, the demons(spammers) found out about sending junk mails or spam. So, the IT gods(email admin) brainstormed on how to contain the inbox chaos.

Many ideas where submitted but only two suggestions emerged with the most number of supporters:

A. Accept all mails but throw away those destined for a non-existing inbox
B. Still send the "mail not found error" and wait for the spammers to change heart.

Both proposals have valid points. Proposal A supporters contends that they should never make the demon's job easier by telling them which address exist on a mail server and which one does not. Proposal B supporters though points out that it's against the mail server standard not to reply appropriately.

The two groups where not able to come to terms and so, we have today mail servers that don't tell the truth.

So, how do you know which type of mail server it is that you're dealing with? It's fairly easy.
Using some of the tools online that checks for mail server responses, like [neustar Email Server Test](https://www.ultratools.com/tools/emailTest): 

Check how the mail server responds to a random email address such as "asdfa3q2xcy53c323das4yux@casimpan.com" or asdf3s6ydq34xy7wec23572@casimpan.com (please replace casimpan.com with the domain name of the email you are checking, the one after the @)

If the mail server responds with something like "email address ok" to random email addresses you used in #1, then, that's a liar mail server. Otherwise, it's truthful.

<small>NOTE: First published in my [now defunct blog](https://web.archive.org/web/20100927055819/http://www.buggedtech.com:80/).</small>

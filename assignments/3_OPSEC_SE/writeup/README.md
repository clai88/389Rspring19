# Writeup 3 - Operational Security and Social Engineering

Name: Christopher Lai
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Christopher Lai

## Assignment Writeup

### Part 1 (40 pts)

In order to collect the necessary information, I would pose as a bank employee who needs to investigate an issue with her account requiring her immediate attention.  I would create a fake persona and run my voice through a voice changer to give me a Dutch accent, since that is where she is from.  Before calling her, I would look through all the personal information that I have alredy collected in order familiarize myself with her.  Luckily, I already have the username she uses for most of her accounts, along with her address and some of her close contact information.  Using this pretext, I should easily be able to extract her mother's maiden name, her birth city, and the name of her first pet.  These are all common security questions, so she should not become suspicious when I ask her for them.  For her browser I would need be a little more sneaky, as to not raise any suspicion.  I would direct her to a website that errors out and then prints the current browser and version number.  I would then ask her to read aloud this message.  For the pin number, I could pretend that the current PIN registered to her account has been leaked and that I advise that she changes it.  In order to do so, I would need her to verify her original PIN and then have her give me a new one.  This way, I have access to her actual PIN and another PIN that she is likely to use in the future.  If at any time she becomes suspicious, I would put on an official sounding voice and maybe name drop a few of her friends, showing that I indeed know about her.

### Part 2 (60 pts)

##### 1. Weak Password
The first thing that I would change about the bank's webserver is the weak password.  You should not use common passwords that can be found in wordlists, because this way they can be easily bruteforced.  She should change her password to something at least 10 characters long, with a mix of upper and lowercase letters, numbers, and passwords.  She should also make sure that there are no common words in her password or if there are, to convert it to "leetspeak". (cat -> c@t).  After the attacker finds her ip and port number, the only things currently stopping them from accessing all of 1337bank's internal server is a weak password, so this is definitely a major priority.

##### 2.  Open Ports
I was able to break into their system because I could nmap their system to see all the available ports.  In order to stop this they could have the port change periodically, or stop nmap scans altogether.  As mentioned in class, nmap scans are extremely noisy, so whoever is running the server could simply open up wireshark and blacklist any ip that is sending them repeated packets.  This method is effective, because if attackers do not know which port to exploit, then they will have an extremely tough time actually accessing the system.

##### 3. No Intrusion Detection System
There was obviously no intrusion detection system (IDS) on the 1337bank server, because 30 students were able to brute their way in and look through the system.  The bank should set up an IDS so that they can be warned when unathorized users or ip addresses attempt to connect to the system.  This way, they can take appropriate action such as blacklisting the ip's before they manage to bruteforce their way in.  The IDS can monitor the incoming traffic to the server and alert users of any breakins.  This is extremely important, as it allows them to see if any unauthorized users are on or attempting to get on their network.



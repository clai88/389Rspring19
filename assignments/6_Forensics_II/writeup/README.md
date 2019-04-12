# Writeup 6 - Forensics

Name: Christopher Lai
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Christopher Lai

## Assignment Writeup

### Part 1 (45 Pts)

1. Warmup: what IP address has been attacked? 

- 142.93.136.81 (1337bank.money)

2. What kind of assessment tool(s) were the attackers using against the victim machine? List the name(s) of the tool(s) as well.

- looks like some sort of tcp scan (nmap)

3. What are the hackers' IP addresses, and where are they connecting from?

- 159.203.113.181
- Clifton, New Jersey, 07014

4. What port are they using to steal files on the server?

- 20

5. Which file did they steal? What kind of file is it? Provide all metadata on the file. Specifically,

    a) What kind of file is it?
     - jpeg image called find_me.jpeg

    b) Where was this photo taken? Provide a country and city in your answer.
    - Punta del Este, Uraguay

    c) When was this photo taken? Provide a timestamp in your answer.
    - 12/23/2018 5:16PM

    d) What kind of camera took this photo?
    - Apple iphone 8

    e) How high up was this photo taken? Provide an answer in meters.
    - 4.572631836 meters below sea level

6. Which file did the attackers leave on the server?
- greetz.fpff

7. What is a countermeasure to prevent this kind of intrusion from happening again? Note: disabling the vulnerable service is *not* an option.
- allowing only authorized users from certain ip addresses to connect to the server.  Also blacklisting any ips they catch performing a port scan

### Part 2 (55 Pts)

2. Parse `greetz.fpff`, and report the following information:
    1. When was `greetz.fpff` generated?
    - ```2019-03-27 00:15:05```
    2. Who authored `greetz.fpff`?
    - ```f1inch```
    4. List each section, giving us the data in it *and* its type.
    ```
        ------- HEADER -------
    MAGIC: 0x8badf00d
    VERSION: 1
    TIMESTAMP: 1553660105 (2019-03-27 00:15:05)
    AUTHOR: fl1nch
    SECTION: 5
    -------  BODY  -------
    Section Type: 1
    Section Length: 24
    ASCII: Hey you, keep looking :)
    Section Type: 6
    Section Length: 16
    Coordinates: (52.336035, 4.880673)
    Section Type: 8
    Section Length: 202776
    PNG saved to embedded_png.png
    Section Type: 1
    Section Length: 44
    ASCII: }R983CSMC_perg_tndid_u0y_yllufep0h{-R983CSMC
    Section Type: 1
    Section Length: 80
    ASCII: CMSC389R-{hey_h3y_y0U_you_I_dont_like_your_base64_encoding}
    ```
    5. Report *at least* one flag hidden in `greetz.fpff`. Any other flag found will count as bonus points towards the *competition* portion of the syllabus.

    - ```CMSC389R-{h0pefully_y0u_didnt_grep_CMSC389R}```

    - ```CMSC389R-{hey_h3y_y0U_you_I_dont_like_your_base64_encoding}```

    - ```CMSC389R-{w3lc0me_b@ck_fr0m_spr1ng_br3ak}```




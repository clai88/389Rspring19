# Writeup 2 - OSINT

Name: Christopher Lai

Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Christopher Lai

## Assignment Writeup

### Part 1 

1. Elizabeth Moffet

2. Banking CEO at 13/37 National Bank  (http://1337bank.money) 

3.  - Twitter handle: ```@v0idcache```.  Discovered by searching the online usertag.

    - Email: ```v0idcache@protonmail.com```.  Went to the company website and went to the about page.  Email was located on the bottom.

    - Twitter Followers: ```@umdcsec```.  Located in the following section of twitter

    - Twitter Like: ```@CacheDev0id```.  Commented and liked some of her posts.

    - Github: ```v0idcache```.  User has no public repos, followers, or stars.  Has one commit on February 6th, 2019.

    - Dehashed had some information about the email, but I needed an an active subscription to view the data found ![dehashed error message](https://i.imgur.com/GYC1MTU.png)

4. 142.93.136.81 Digital Ocean in Noord-Holland, Netherlands.

    Here is the full traceroute scan.

    ```TRACEROUTE (using port 139/tcp)
    HOP RTT       ADDRESS
    1   3.20 ms   192.168.1.1
    2   4.10 ms   172.24.116.1
    3   5.86 ms   24-104-71-65-ip-static.hfc.comcastbusiness.net (24.104.71.65)
    4   3.49 ms   68.87.129.1
    5   3.22 ms   68.85.67.181
    6   4.42 ms   68.85.130.149
    7   4.41 ms   ae-13-ar01.capitolhghts.md.bad.comcast.net (68.87.168.61)
    8   19.22 ms  be-33657-cr02.ashburn.va.ibone.comcast.net (68.86.90.57)
    9   12.18 ms  be-10142-pe01.ashburn.va.ibone.comcast.net (68.86.86.34)
    10  15.56 ms  ash-b1-link.telia.net (62.115.149.64)
    11  95.60 ms  ash-bb4-link.telia.net (62.115.143.120)
    12  129.97 ms ldn-bb4-link.telia.net (62.115.122.60)
    13  111.51 ms adm-bb4-link.telia.net (62.115.134.26)
    14  101.83 ms adm-b1-link.telia.net (62.115.137.65)
    15  115.21 ms digitalocean-ic-335925-adm-b1.c.telia.net (213.248.68.169)
    16  ...
    17  121.54 ms 142.93.136.81
    
5. I looked in robots.txt and found the flag ```CMSC389R-{h1ding_fil3s_in_r0bots_L0L}```.

6. Result from nmap scan of first 10,000 ports. 

    ```PORT     STATE SERVICE
    22/tcp   open  ssh
    53/tcp   open  domain
    80/tcp   open  http
    1337/tcp open  waste```

7. Werkzeug/0.14.1 Python/3.7.2.  I used an online webserver application.

8.  - CMSC389R-{h1dd3n_1n_plain_5ight}. 

### Part 2 :


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

    - Pastebin: Found this conversation between v0idcache and fl1nch:

    ```
    [+] fl1nch joined
    [+] v0idcache joined
    [v0idcache] u there?
    [fl1nch] hi
    [v0idcache] what time are we doing this
    [v0idcache] i have a meeting with the board of directors and they're not going to like this
    [fl1nch] 1400
    [v0idcache] ugh i have to get a flight out of here asap
    [fl1nch] lol
    [fl1nch] you worry too much
    [v0idcache] u would too if you were in as much trouble as i am
    [v0idcache] whats the file you need called
    [fl1nch] AB4300.txt
    [fl1nch] thx - we owe you
    [v0idcache] thank me later
    [-] v0idcache left
    [-] fl1nch left 
    ```

    - Dehashed had some information about the email, but I needed an an active subscription to view the data found ![dehashed error message](https://i.imgur.com/GYC1MTU.png)

4. IP address is: 142.93.136.81 Digital Ocean in Noord-Holland, Netherlands.

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
    1337/tcp open  waste 
    ```

7. Werkzeug/0.14.1 Python/3.7.2.  I used an online webserver application.

8. Additional Flags

    - CMSC389R-{h1dd3n_1n_plain_5ight}.
    - CMSC389R-{brut3_f0rce_m4ster}
    - CMSC389R-{YWX4H3d3Bz6dx9lG32Odv0JZh}


### Part 2 :

My program is named ```bruteforce.py``` and can be run using ```python3 bruteforce.py```.

For this part I crafted formatted bytestrings for the username and password and used s.send() to send them to the server.  I iterated over all of the passwords and checked the server response to see if my password worked.

I did attempt to use a multithreaded version by putting all the passwords in a queue and spawning threads to speed up the checking process.  This one is ```bruteforce_multi.py```.


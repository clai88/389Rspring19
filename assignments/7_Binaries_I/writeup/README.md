# Writeup 7 - Binaries I

Name: Christopher Lai
Section: 0101

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Christopher Lai

## Assignment Writeup

### Part 1 (90 Pts)

*Put your code here as well as in main.c*
```
#include <stdio.h>

int main(){
    int a = 0x1ceb00da;
    int b = 0xfeedface;

    printf("a = %d\n", a);
    printf("b = %d\n", b);

    b = a ^ b;

    a = a ^ b;

    b = a ^ b;

    printf("a = %d\n", a);
    printf("b = %d\n", b);

    return 0;
}

```

### Part 2 (10 Pts)

This program starts with 2 hex values and prints out their initial values as a decimal.  It then uses a series of xors to swap their values without needing a third variable.  We then print the result.

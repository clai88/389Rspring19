/*
 * Name: Christopher Lai
 * Section: 0101
 *
 * I pledge on my honor that I have not given or received any unauthorized
 * assistance on this assignment or examination.
 *
 * Digital acknowledgement: Christopher Lai
 */

/* your code goes here */

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

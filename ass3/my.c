#include<stdio.h>

int main()
{
    int a = 15, b = 51;

    a ^= b;
    b ^= a;
    a ^= b;

    printf("%d %d\n", a, b);
}
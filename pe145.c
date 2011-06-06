#include <stdio.h>
#include <memory.h>

#define N  1000000000

int bits[10];

int isReversible(long long x)
{
    if(x%10 == 0) return -1;
    memset(bits, -1, sizeof(bits));
    int nb=0;
    while(x){
        bits[nb++] = x%10; x /=10;
    }
    int i, c=0, d;
    for(i=0; i<nb; ++i){
        d = bits[i] + bits[nb-i-1] + c;
        if(d%2 == 0) return -1;
        c = d>=10 ? 1 : 0;
    }
    return 0;
}

int main()
{
    long long ret = 0, i=10;
    while( i++ < N){
        if(isReversible(i)==0) ++ret;        
    }
    printf("ans is %lld\n", ret);
    return 0;
}

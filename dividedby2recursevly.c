#include <stdio.h>
int div(int);
int main()
{ 
    int m,k;
    scanf("%d",&m);
    k=div(m);
    printf("%d",k);
	return 0;
}
int div(int num)
{
    if(num%2==0)
    {
        num=num/2;
        return div(num);
    }
    else
    {
        return num;
    }
    
}

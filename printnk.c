#include<stdio.h>
int main()
{
int a,b,i,m=1;
printf("enter the values:");
scanf("%d%d",&a,&b);
for(i=0;i<b;i++)
{
m=m*a;
}
printf("%d",m);
return 0;
}

#include<stdio.h>
int main(void)
{
   int k,rem=0,rev=0,count=0,i;
   scanf("%d",&n);
   while(k!='\0')
   {
       rem=k%10;
       
       rev=(rev*10)+rem;
       k=k/10;
}
n=rev;

while(k!='\0')
{
    rem=k%10;
    printf("%d ",rem);
    k=k/10;
}
   
}

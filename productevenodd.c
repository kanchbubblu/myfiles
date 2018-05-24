#include<stdio.h>
int main()
{
 int n1,n2,product;
 printf("get the two numbers:");
 scanf("%d%d",&n1,&n2);
 product=n1*n2;
 if(product%2==0)
 {
   printf("this is even number=%d",product);
   }
   return 0;
   }

#include<stdio.h>
void main()
{
int k[10],i,j,temp,n;
printf("enter the number");
scanf("%d",&n);
printf("enter the number");
for(i=0;i<n;i++)
{
scanf("%d",&k[i]);
}
for(i=0;i<n;i++)
{
for(j=i+1;j<n;j++)
{
if(k[i]>k[j])
{
temp=k[i];
k[i]=k[j];
k[j]=temp;
}
}
}
for(i=0;i<n;i++)
{
printf("%d",k[i]);
}
}

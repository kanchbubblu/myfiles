#include<stdio.h>
int main()
{
char str[20];
int k,i,sum=0;
printf("Enter the string");
scanf("%s",str);
k=strlen(str);
for(i=0;i<k;i++)
{
  if(str[i]=='@'||str[i]=='*'||str[i]=='.'||str[i]=='#'||str[i]=='&'||str[i]=='^')
  {
    sum=sum+1;
  }
}
printf("Special character:%d",sum);
return 0;
}

#include<stdio.h>
#include<conio.h>
void main()
{
int a;
clrscr();
printf("Enter a:");
scanf("%d",&a);
if(a&1)
{
printf("\nodd");
}
else
{
printf("\neven");
}
getch();
}

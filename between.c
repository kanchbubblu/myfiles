#include<stdio.h>
void main()
{
  int n,l,r;
  printf("Enter the number");
  scanf("%d",&n);
  printf("Enter he value for L and R");
  scanf("%d\n%d",&l,&r);
  if(n>=l&&n<=r)
  {
    printf("yes");
  }
  else 
  {
    printf("no");
  }
  return 0;
}

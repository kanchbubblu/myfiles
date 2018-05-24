#include <stdio.h>

int main(void) 
{
	int m;

	scanf("%d",&m);
	m+=1;
	while(m%10!=0)
	{
		m=m+1;
	}
	printf("\m%d",m);
	return 0;
}

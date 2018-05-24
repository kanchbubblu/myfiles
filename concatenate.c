#include <stdio.h>
#include <string.h>
 
void concatenate(char [], char []); 
 
int main()
{
  	char Str1[100], Str2[100];
 
  	printf("\n Please Enter the First String :  ");
  	gets(Str1);
  	
  	printf("\n Please Enter the Second String :  ");
  	gets(Str2);
  	
  	concatenate(Str1, Str2);
 
  	printf("\n String after the Concatenate = %s", Str1);
  	
  	return 0;
}
 
void concatenate(char s11[], char s22[])
{
	int i, j;
	
	i = 0;
	while( s11[i]!='\0')
	{
		i++;
	}
	
  	j = 0;
  	while( s22[j]!='\0')
  	{
  		s11[i] = s22[j];
  		i++;
  		j++;
  	}
  	s11[i] = '\0';
}

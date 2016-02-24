#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void pick_colour(char* colour) {
  while (1) {
    printf("pick a colour (red, blue, green, or orange):\n");
    scanf("%s", colour);
    if (
      strcmp(colour, "red") == 0 || 
      strcmp(colour, "blue") == 0 || 
      strcmp(colour, "green") == 0 || 
      strcmp(colour, "orange") == 0) {
    
      printf("you have selected: %s\n", colour);
      break;
    } else {
      printf("you have not selected a valid colour: %s\n", colour);
    }     
  }
}

int pick_number(int* num) {
  while (1) {
    char temp[10];
    int num;
    printf("pick a number (between 1 and 8):\n");
    scanf("%s", temp);
    num = atoi(temp);
    if (num>0 && num<9) {
       printf("you have selected: %d\n", num);
       break;
    } else {
       printf("you have not selected a valid number: %s\n", temp);
    }
  }
}

int main()
{
  char colour[10];
  int num1, num2;
  pick_colour(colour);
  pick_number(&num1);
  printf("And one more...\n");
  pick_number(&num2);

  if (strcmp(colour, "red") == 0 && num1 == 1 && num2 == 8) printf("Be kind.\n");
  else if (strcmp(colour, "blue") == 0 && num1 == '2' && num2 == '7') printf("Be encouraging.\n");
  else if (strcmp(colour, "green") == 0 && num1 == '3' && num2 == '6') printf("Be thoughtful.\n");
  else if (strcmp(colour, "orange") == 0 && num1 == '4' && num2 == '5') printf("Be gentle.\n");
  else printf("Be positive.\n");

  return 0;
}

#include <stdio.h>

main() {
    printf("Hello World!\n");

    char rays[100];

    int a, b, c;
    a = 5;
    b = 7;
    c = a + b;
    printf("%d + %d = %d\n", a, b, c);
    printf ( "Line1\nLine2\nLine3\n" );
   
    dog();
    tellmeloc();
    recusiverun();

    return 0;
}



// really all you need is 1 script to make a random, then run the recursive runs etc on the unique script



int dog(){

int x = 33;
  int y = 12;
  int z = 8;
   printf ( "Line69\nLine2\nLine3\n" );

  foo_function(&x, &y, &z);
}

int foo_function(int* x, int* y, int* z) {
  int g;
  *x = *y * *z;
  int f = *x;
  g = *x + *y + *z;
  printf("%d be talkin shit about that sum: %d\n",f ,g);
  return 0;
}

int tellmeloc(){
  char command[100];
  int count = 0;
  while (count < 4)
  {
  printf("THIS IS THE NUMBER %d copy!!",count);

  system("ls -a");
  sprintf(command, "cp hi.c demo%d.c",count);

  // rays[count] = ("demo%d.c",count);


  system(command);
  count++;
  }
  return 0;

}

int recusiverun(){
// ghetto way to access copies

	char command[100];
	char commander[100];
  int count = 0;
  while (count < 4)
  {
  sprintf(command, "gcc demo%d.c -o demo%d",count,count);

  // rays[count] = ("demo%d.c",count);
  sprintf(commander, "./demo%d",count);


  system(command);
  system(commander);
  count++;
  }
  return 0;
}



int gen_random(char *s, const int len) {
    static const char alphanum[] =
        "0123456789"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz";

    for (int i = 0; i < len; ++i) {
        s[i] = alphanum[rand() % (sizeof(alphanum) - 1)];
    }

    s[len] = 0;
}















// lool


// business foundation certificate !!!! look into this

/*
char drive[1];
printf("Target drive is: ");
scanf("%s", drive);
printf("\nOkay, using %s: as target drive...\n", drive);
system("dir %s:", drive);
system("PAUSE");

==========
==========
==========
==========
==========

char input[10], drive[10];
char command[100];
 
printf("Target drive is: ");
fgets(input, 10, stdin);
if (scanf(input, "%s", drive) != 1)
{
  printf("Error entering target drive.");
  return EXIT_FAILURE;
}
printf("\nOkay, using %s: as target drive...\n", drive);
sprintf(command, "dir %s:", drive);
system(command);
system("PAUSE");
*/



// printf("command = \"%s\"\n", command); /* debugging */
    // $ make
        // gcc hi.c -o randomtitle 
    // $ ./hello-c-world
    // $ ./hello-cpp-world
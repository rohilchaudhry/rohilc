#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

void compute_flag(int a, int b) {
    
    //super secure security trapdoor!
    int x = a / b; //This will give a SIGFPE in case of no optimizations , but will let it pass through if optimization used 

    x = a + b;

    if(x == 1337)
    {
        //give out the flag if x = 1337
        char *flag = getenv("FLAG");
        if (!flag) {
            perror("Environment variable FLAG not set");
            exit(1);
        }
        printf("%s",flag);
        fflush(stdout);
    }
}

int main(int argc, char *argv[]) {
    setbuf(stdout, NULL);
    
    int user_input;

    printf("Enter a number: ");
    fflush(stdout);
    // Get user input
    if (scanf("%d", &user_input) != 1) {
        printf("Invalid input. Please enter a valid integer.\n");
        fflush(stdout);
        return 1; // Exit if input is invalid
    }

    // Call the vulnerable function with user-supplied input
    compute_flag(user_input,0);

    return 0;
}

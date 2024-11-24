#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

char* read_flag_from_env() {
    // Get the flag from the environment variable "FLAG"
    char *flag = getenv("FLAG");
    if (!flag) {
        perror("Environment variable FLAG not set");
        exit(1);
    }
    return flag;
}

void initialize_offset(int *offsets, int length, int start_offset) {
    // Generate "random" sequence starting from `start_offset`
    offsets[0] = start_offset;
    offsets[1] = start_offset + 11;

    for (int i = 2; i < length; i++) {
        offsets[i] = offsets[i - 1] + 11+i+1;
    }
}

void super_service(char *input) {
    char cmd[10];             // Command buffer of size 10 (for overflow)
    char replybuf[1000];      // Large reply buffer containing scattered flag characters

    // Initialize replybuf with dots for clarity
    memset(replybuf, '.', sizeof(replybuf));

    // Fetch the flag to be distributed character by character
    const char *flag = read_flag_from_env();

    // Calculate the offsets for each character in the flag
    int flag_length = strlen(flag);
    int fib_offsets[flag_length];
    initialize_offset(fib_offsets, flag_length, 21);

    // Place each character of the flag in replybuf
    for (int i = 0; i < flag_length; i++) {
        replybuf[fib_offsets[i]] = flag[i];
    }

    // Vulnerable copying of input to cmd without bounds checking
    // This can cause an overflow if input is longer than cmd's size (10 bytes)
    strcpy(cmd, input);

    // Attempt to simulate command processing based on cmd buffer content
    char *base = cmd;
    if (*base != 0) {
            while (!isspace((unsigned char)*base++) && *base != '\0');
            while (isspace((unsigned char)*base++) && *base != '\0');

            // Potentially dangerous access if base goes out of bounds
            printf("Processing command: %s\n", cmd);
            if (*base != 0) {
                printf("Some garbage: %c\n", *base); //This would give out an random char until overflown!
            } else {
                printf("End of command reached\n");
            }
    } else {
        printf("Empty input.\n");
    }
}

int main(int argc, char *argv[]) {
    char input[1000];  // Buffer to hold user input, with a fixed size to prevent overflow

    if (fgets(input, sizeof(input), stdin) == NULL) {
        printf("Error reading input.\n");
        return 1;
    }

    // Remove the newline character from fgets
    input[strcspn(input, "\n")] = 0;

    // Call the vulnerable function with user-supplied input
    super_service(input);

    return 0;
}

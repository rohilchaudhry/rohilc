import os
import subprocess

# Paths
source_file = "chal.c"  # The C source file
binary_file = "ctf_challenge"    # Name of the output binary to be run

def compile_code(optimization_level):
    """Compiles the C code with the specified GCC optimization level."""
    print(f"Compiling with optimization level: {optimization_level}", flush=True) #Will help the students to think into compiler optimizations!
    compile_command = [
        "gcc", source_file, "-o", binary_file,
        f"-{optimization_level}", "-Wall", "-Wextra", "-Wno-div-by-zero"
    ]
    try:
        result = subprocess.run(compile_command, check=True, capture_output=True)
        print("Compilation successful!", flush=True)
    except subprocess.CalledProcessError as e:
        print("Compilation failed!", flush=True)
        print(e.stderr.decode())
        exit(1)

def run_binary():
    """Runs the compiled binary and allows user interaction."""
    if not os.path.exists(binary_file):
        print("Error: Binary file not found. Compile it first!",flush=True)
        return

    print("\nRunning the binary... Enter input as prompted.", flush=True)
    try:
        print("Enter a number: ", flush=True)
        # Start the binary and allow interaction
        result = subprocess.run(f"./{binary_file}", shell=True, capture_output=True)
        error_output = result.stderr.decode()
        if error_output != "":
            print(error_output, flush=True)
        else:
            print(result.stdout.decode(), flush=True)
    except Exception as e:
        print(f"Error while running the binary: {e}", flush=True)

def main():
    print("=== Welcome to the most awsome challenge! ===", flush=True)
    print("Give the compilation command , and leave the rest to us!", flush=True)

    while True:
        user_command = input("\nEnter your compilation command: ").strip()
        
        #take input from user
        if ("gcc" not in user_command) or (any(char in ";,/\:'" for char in user_command)):
            print("Please provide a valid GCC command")
        elif ("-O" not in user_command) or ("-O0" in user_command):
            compile_code("O0")
            run_binary()
        elif ("-O1"  in user_command):
            compile_code("O1")
            run_binary()
        elif ("-O2"  in user_command):
            compile_code("O2")
            run_binary()
        elif ("-O3"  in user_command):
            compile_code("O3")
            run_binary()
        elif ("-Ofast"  in user_command):
            compile_code("Ofast")
            run_binary()
        else:
            print("Please provide a valid GCC command", flush=True)
            
if __name__ == "__main__":
    main()

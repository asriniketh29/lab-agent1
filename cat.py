'''
This program prints stdin to the screen using O(1) memory.
'''
import sys

BUFFER_SIZE = 64 * 1024  # 64KB buffer

def cat(file):
    while True:
        chunk = file.read(BUFFER_SIZE)
        if not chunk:
            break
        sys.stdout.buffer.write(chunk)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "rb") as f:
                cat(f)
    else:
        cat(sys.stdin.buffer)

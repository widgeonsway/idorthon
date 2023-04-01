import sys

if len(sys.argv) != 2:
    print("Usage: python wordlist_generator.py <num>")
    sys.exit(1)

try:
    num = int(sys.argv[1])
except ValueError:
    print("Error: <num> must be an integer")
    sys.exit(1)

with open("wordlist.txt", "w") as f:
    for i in range(num+1):
        f.write(str(i) + "\n")

print("Wordlist generated successfully")

import sys
import re
if len(sys.argv) !=3:
    print("ERROR 1: You should enter a two arguments")
    sys.exit()
else:
    try:
        s = sys.argv[1]
        n = int(sys.argv[2])
        word = re.sub(r'[^\w\s]', ' ', s)
        word = word.split()
        wordsInRange = [i for i in word if len(i) > n]
        print(wordsInRange)
    except ValueError:
        print("ERROR 2: First argument should be a string and second one a integer.")
        sys.exit()
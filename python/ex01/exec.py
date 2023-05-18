import sys

def adding_args(args):
    args = sys.argv[1:]
    x = " ".join(args)
    x = x.swapcase()
    return x

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print()
    elif len(sys.argv) > 1:
        print(adding_args(sys.argv)[::-1], end="\n\n")


    
 
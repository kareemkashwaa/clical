import sys


def calc(expr):
    try:
        return eval(expr)
    except:
        print("An error occured")
        return None
    
def main():
    if len(sys.argv) < 2:
        print("Usage clical expression")
        return
    expr = "".join(sys.argv[1:])
    print(calc(expr))

if __name__ == "__main__":
    main()
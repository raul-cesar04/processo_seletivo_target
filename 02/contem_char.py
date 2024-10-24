def verify(string: str)->int:
    return string.lower().count("a")


def main():
    string: str = input()
    occur: int = verify(string)
    
    if(occur == 0):
        print("A letra 'a' não ocorre nenhuma vez na string "+string)
        return
    
    print("A letra 'a' ocorre {x} vezes na string {string}".format(x=occur, string=string))

if __name__ == "__main__":
    main()
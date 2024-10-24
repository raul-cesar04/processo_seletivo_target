def fibonacci(n):
    a: int = 0
    b: int  = 1

    for i in range(n):
        if(i < 2):
            print(i)
            continue
        next_number: int = a + b

        print(next_number)
        
        a = b
        b = next_number
        

def nth_impar(n)->int:
    x: int = 1
    i: int = 0
    while(i < n):
        x = x + 2

        i = i+1
    return x

def impares(n):
    for i in range(n):
        print(nth_impar(i))

def dobradas(n):
    i: int = 1
    x: int = 1
    while(i < n):
        x = x * 2
        i = i+1
        print(x)

def soma_impar(n):
    x: int = 0
    for i in range(n):
        x = x + nth_impar(i)
        print(x)
    pass

def oitavos(n):
    x: int = 4
    k: int = 12
    step: int = 8
    for i in range(n):
        print(x)
        x = x + (k+step*i)


def main():
    #dobradas(10)       ### A
    #impares(10)        ### B
    #soma_impar(10)     ### C
    #oitavos(10)         ### D
    #fibonacci(10)       ### E
    # 2, 10,12,16,17,18,19,200 -> Todas começam com a letra D
    pass


if __name__ == "__main__":
    main()
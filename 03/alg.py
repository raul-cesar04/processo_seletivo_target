def main():
    index: int = 12
    sum: int = 0
    k: int = 1

    while(k < index):
        k = k + 1
        sum = sum + k
    
    print(sum) # Resultado: 77

if __name__ == "__main__":
    main()
n = int(input("Enter the number of rows:"))
for i in range(1, n + 1):
    print(" "*(i-1),(str(n+1-i)+"")*(n+1-i))





#ex2
    
n = int(input("Enter the number of rows:"))
for i in range(1, n + 1):
    print(" " * (i - 1), end="")
    for j in range(1, n + 2 - i):
        print(j, end="")
    print()
#ex3


n = int(input("Enter the number of rows:"))
for i in range(1, n + 1):
        print(" " * (i - 1),(str(chr(65 + n - i)) + "") * (n + 1 - i))


#ex4        



n = int(input("Enter the number of rows:"))
for i in range(1, n + 1):
    print(" " * (i - 1), end=" ")
    for j in range(0, n + 1 - i):
        print(n + 1 - i, end=" ")
        for k in range(1, n + 1 - i):
            print(n + 1 - i, end=" ")
        print()

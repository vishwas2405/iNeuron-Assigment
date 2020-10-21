'''

# Q2

String = input("Enter the String")
Rev_String = String[::-1]
print(Rev_String)


'''

# Q1

n = 5
for i in range(n):
    for j in range(0,i+1):
        print("* ",end = "")
    print("\n")
    
for i in range(n,0,-1):
    for j in range(0,i-1):
        print("* ",end = "")
    print("\n")
    



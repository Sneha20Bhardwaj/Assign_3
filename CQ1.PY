#CALCULATING FACTORIAL USING LOOP AND RECURSION
#USING LOOP
'''n1=int(input("Enter a number : "))
def recursion1(n):
    fact=1

    for i in range(n,1,-1):
        fact=fact*i
    print("Factorial of",n1,"is :",fact)

recursion1(n1)'''
#USING RECURSION

def recursion2(n):
     if n==1 or n==0:
         return 1
     fact=n*recursion2(n-1)
     return fact
n2=int(input("Enter a number : "))   
result= recursion2(n2)
print("Factorial of",n2,"is :",result)
num=int(input("enter number :"))

if num > 1:
    for i in range(2,num):
        if (num % i)==0:
            print(num,"not a prime number.")
            break

    else:
            print(num,"prime number.")
else:
        print(num,"is not a prime")

        
        
            

       
        
 

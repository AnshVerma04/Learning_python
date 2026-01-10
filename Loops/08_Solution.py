Number = int(input("Enter a number: "))
is_prime = True
if Number >1:
    for i in range(2,Number):
        if(Number%i)==0:
            is_prime = False
            break
    
    print("Number:",is_prime)
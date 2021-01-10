#Iteration wit some Python
houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]

def deliver_presents_iteratively():
    for house in houses:
        print("Delivering presents to", house)
#deliver_presents_iteratively()

#each function call represents an elf doing his work 
def deliver_presents_recursively(houses):
    print("len of houses: ", len(houses))
    #worker elf doing their work
    if len(houses) == 1:
        print("in if statement")
        house = houses[0]
        print("Delivering presents to", house)

    #Manager elf doing his work
    else:
        mid = len(houses) // 2 #which means divide by 2 and find the floor of the result
        print("mid: ", mid)
        first_half = houses[:mid]  
        second_half = houses[mid:]

        #Divides work among 2 elves
        deliver_presents_recursively(first_half)
        deliver_presents_recursively(second_half)

#deliver_presents_recursively(houses)

#factorial recursion
def factorial_recursive(n):
    print("n", n)
    
    #base case: 1! = 1
    if n == 1:
        return 1
    #recursive case: n! = n * (n-1)!
    
    else:
        return n * factorial_recursive(n-1)
#stores to stack, only at the very end, when n == 1 do we multiply entire stack together
print(factorial_recursive(5))
        

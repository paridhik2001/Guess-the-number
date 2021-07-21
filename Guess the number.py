n = 56
i=0
print("You have 10 gueses")
while(1):
    i=i+1
    print("Guess No. ",i)
    print("Guess the number")
    x=int(input())
    if x<n:
        print(x," is lesser than the number!! Try Again!")
    elif x==n:
        print("You Won!! This is the number")
        break
    else:
        print(x," is larger than the number!! Try Again!")
    if i>10:
        print("Game Over")
        break





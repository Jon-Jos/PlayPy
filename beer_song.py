word = 'bottles'
bottle_num = input("Enter the number of bottle to start:\t")
for bottle_num in range(100,0,-1):
    print(bottle_num, word, "of beer on the wall")
    print(bottle_num, word, "of beer")
    print("Take one down.")
    print("Pass it around")
    
    if bottle_num == 1:
        print("\nOut of bottles!")
    else:
        temp_num = bottle_num -1
        if temp_num == 1:
            word = 'bottle'
            print(temp_num, word, "of beer on the wall")
    print()




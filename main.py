largest = None
smallest = None
while True:

    try:
        num = input("Enter a number: ")
        if num == "done":
         break
        num = int(num)

        if largest == None or smallest == None:
            largest = num
            smallest = num
        elif largest < num:
            largest = num
        elif smallest > num:
            smallest = num

    except:
        print("Invaild input")

print("Maximum is ", largest)
print("Minimum is ", smallest)
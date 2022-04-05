while True:
    try:
        first_num = int(input('What is the first number you wanr to add?'))
        second_num = int(input('What is the second number you wanr to add?'))
        sum = first_num + second_num
        print("The sum of your two numbers is", sum)
        break
    except:
        print("Your so silly. That's not an integer")
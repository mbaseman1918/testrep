def averagenumbers():
    num_list = []
    user = "0"
    total = 0
    while user not in ["done","Done"] and user.isdigit():
        user = input("Enter a number, or done: ")
        if user.isdigit():
            num_list.append(int(user))
    for i in num_list:
        total += i
    print("Average = {}".format(total/len(num_list)))

averagenumbers()

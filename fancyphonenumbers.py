phone = input("Please enter an all digits phone number: ")
while len(phone) != 10 or phone.isdigit() != True:
    phone = input("Please enter an all digits phone number (number must be 10 digits): ")

print("({}) {}-{}".format(phone[0:3],phone[3:6],phone[6:]))

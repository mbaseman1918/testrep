time = input("When are you eating your meal? ")
hour = int(time[:-2])
meridian = time[-2:].lower()
if hour in [7,8,9] and meridian == "am":
    print("You are eating breakfast.")
elif hour in [12,1,2] and meridian == "pm":
    print("You are eating lunch.")
elif hour in [7,8,9] and meridian == "pm":
    print("You are eating dinner.")
elif (hour in [10,11] and meridian == "pm") or (hour in [12,1,2,3,4] and meridian == "am"):
    print("STOP, HAMMERTIME!")
else:
    print("What are you doing with your life?")

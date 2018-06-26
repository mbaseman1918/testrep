import datetime
import math
def getrain():
    with open("rain.txt", "r+") as f:
        rain = f.readlines()
        ref_rain = []
        final_rain_list = []
        for i in rain:
            ref_rain.append(i[0:19])
        for i in ref_rain:
            final_rain_list.append(i.split())
        raindata = {}
        return final_rain_list

def getmean(x):
    data = []
    numbers = []
    for i in x:
        data.append(i[1])
    for i in data:
        if i.isdigit():
            numbers.append(int(i))
    return(sum(numbers)/len(numbers))


def getvariance(x, mean):
    data = []
    numbers = []
    variance = []
    for i in x:
        data.append(i[1])
    for i in data:
        if i.isdigit():
            numbers.append(int(i))
    for i in numbers:
        variance.append((i - mean)**2)
    return math.sqrt(sum(variance)/len(variance))

def getmaxday(x):
    data = []
    numbers = []
    for i in x:
        data.append(i[1])
    for i in data:
        if i.isdigit():
            numbers.append(int(i))
    for i in x:
        if i[1] == str(max(numbers)):
            answer = i
    return answer



def getmaxyear(x):
    year_dict = {}
    year_dict_average = {}
    average_list = []
    for i in range(21):
        year_dict[1998 + i] = []
        year_dict_average[1998 + i] = []
    for i in x:
        date = datetime.datetime.strptime(i[0], "%d-%b-%Y")
        if i[1].isdigit():
            year_dict[date.year].append(int(i[1]))
    for i in year_dict:
        year_dict_average[i] = (sum(year_dict[i])/len(year_dict[i]))
    for i in year_dict_average:
        average_list.append(year_dict_average[i])
    for i in year_dict_average:
        if year_dict_average[i] == max(average_list):
            answer = i
    return "{} had the highest averaga rain with {}.".format(answer,max(average_list))


print(getmaxday(getrain()))
print(getmean(getrain()))
y = getmean(getrain())
print(getvariance(getrain(), y))
print(getmaxyear(getrain()))

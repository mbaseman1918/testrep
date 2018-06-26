def peaks(lst):
    c = 0
    peaks = []
    for i in lst:
        if c > 0 and c < (len(lst)-1):
            if lst[c] > lst[c-1] and lst[c] > lst[c+1]:
                peaks.append(c)
        c += 1
    return peaks

def valleys(lst):
    c = 0
    peaks = []
    for i in lst:
        if c > 0 and c < (len(lst)-1):
            if lst[c] < lst[c-1] and lst[c] < lst[c+1]:
                peaks.append(c)
        c += 1
    return peaks

def peaksandvalleys(lst):
    comb_list = peaks(lst) + valleys(lst)
    final_list = sorted(comb_list)
    return final_list

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
print(peaks(data))
print(valleys(data))
print(peaksandvalleys(data))

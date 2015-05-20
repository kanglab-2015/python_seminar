import sum

cal=sum.Cal()
cal.cal_sum(int(raw_input())+1)
print cal.sum

from sum import Cal

cal2=Cal()
cal2.cal_sum(int(raw_input())+1)
print cal2.sum
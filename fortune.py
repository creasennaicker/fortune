import random

fort = open('fortunedat.txt', 'r')

q = []

line = ''


fortunes = fort.readlines()

for x in fortunes:
    if x != "%\n":
        line = line + x
    elif x == "%\n":
        q.append(line)
        line = ''

quote_num = len(q)
rq = random.randint(5, quote_num)

print("\n"+q[rq])
fort.close()






#! /usr/bin/python

freq = [0,0,0,0,0,0,0]

# een commentaar toegevoegd
for i in range(0,200,10):
	day = (3 + i + i // 4 ) % 7
	print(1900 + i, day)
	freq[day] = freq[day] + 1
print(freq)


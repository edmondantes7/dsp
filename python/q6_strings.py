# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
	if count < 10:
		print("Number of donuts: %r" % count)
	else:
		print("Number of donuts: many")


list1 = [4, 11, 25, 3, 5]

for i in range(0,5):
	donuts(list1[i])


def both_ends(s):
	a = len(s)
	if a > 2:
		new = s[0]+s[1]+s[-2]+s[-1]
	else:
		new = ''
	print(new)


list2 = ['John', 'Spring', 're', 'Tom', 'jennifer', 'Bill', 'a']

for i in range(0,7):
	both_ends(list2[i])


def fix_start(s):
 	a = word[0]
	print(type(a))
	b = len(word)
	for i in word:
		if i == a:
			word = word.replace(i, "*")
	word = word.replace(word[0], a, 1)
	print(word)		
	return word
	
list3 = ['daddy', 'babble', 're', 'Tom', 'jennifer', 'Bill', 'a']
for i in range(0,5,2):
	fix_start(list3[i])


def mix_up(a, b):
	x = len(a)
	y = len(b)
	ss1 = a[-x:-x+2]
	ss2 = b[-y:-y+2]
	new1 = ss1 + b[2:]
	new2 = ss2 + a[2:]
	print(new2)
	print(new1)

list4 = ['mix', 'pod', 'Dog', 'Dinner', 'gnash', 'sport']

for i in range(0,5,2):
	mix_up(list4[i], list4[i+1])


def verbing(s):
	b = len(s)
	if b > 3 and s[-3:] == 'ing':
		s = s +'ly'
		#s = s.replace('ing',"ly",1)
	elif b > 3:
		s = s +'ing'
	else:
		pass
    print(s)

list5 = ['hail', 'swimming', 'do']

for i in range(0,3):
	verbings(list5[i])


def not_bad(s):
	b = s.find('bad')
	c = s.find('not')
	if (b == -1):
		s = s 
	elif (c < b): 
		s = s.replace(s[c:],"good")
    print(s)

list6 = ['This movie is not so bad', 'This dinner is not that bad!','This tea is not hot', "It's bad not yet"]

for i in range(0,4):
	not_bad(list6[i])


def front_back(a, b):
	c = len(a)
	d = len(b)
	if c%2 == 0:
		c1 = c/2
	else:
		c1 = c/2 + 1
	if d%2 == 0:
		d1 = d/2
	else:
		d1 = d/2 + 1
	new = a[:c1] + b[:d1] + a[c1:] + b[d1:]
	print(new)

list7 = ['abcd','xy','abcde','xyz','Kitten','Donut']

for i in range(0,6,2):
	front_back(list7[i], list7[i+1])

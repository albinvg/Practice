s1 = list('garden')
s2 = list('danger')

if len(s1) != len(s2):
	print('not Anagram')

#take first char of s1 and check if s2 has that string. If yes, pop char out of s2. If no, then Not Anagram
#increase the index pointer of s1

else:
	for i in s1:
		if i in s2:
			s2.remove(i)
		else:
			print ('not Anagram')
	print ('Anagram')

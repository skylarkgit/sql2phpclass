def dtfParse(fName):
	data={}
	type={}
	f = open(fName,'r')
	l=f.readline()
	while l:
		l=l.split(" ")
		print(l[1])
		if l[0] in data:
			data[l[0]].append(l[1])
			type[l[0]].append(l[2])
		else:
			data[l[0]]=[l[1]]
			type[l[0]]=[l[2]]
		l=f.readline()
	f.close()
	return [data,type]
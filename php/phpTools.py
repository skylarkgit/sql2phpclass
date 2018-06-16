def beautify(fName):
	finalPhp=""
	indentLevel=0;
	f = open(fName,'r')
	l=f.readline()
	while l:
		if l[:-1].endswith('}'):
			indentLevel-=1
		finalPhp+=('\t'*indentLevel)+l
		if l[:-1].endswith('{'):
			indentLevel+=1
		l=f.readline()
	f.close()
	return finalPhp
	

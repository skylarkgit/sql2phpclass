class Column:
	def __init__(self, name, type, keyType=None, keyReference=None):
		self.name=name
		self.type=type
		self.isKey=(keyType!=None and keyType!="AUTO")
		self.keyType=keyType
		self.isAUTO=(keyType=="AUTO" or keyReference=="AUTO")
		#print("name="+name+" keyType="+str(keyType)+" keyReference="+str(keyReference))
		self.keyReference=keyReference

class Table:
	def __init__(self, name,varList=[]):
		self.name=name
		self.varList=varList
	def append(self,col):
		if self.varList==[]:
			self.varList=[col]
		else:
			self.varList.append(col)
	def getKeys(self):
		keySet={}
		for v in self.varList:
			if v.isKey==True and v.keyType=="PRI":
				keySet[v.name]=v.type
		return keySet
	def getAutoKey(self):
		autoKey=None
		for v in self.varList:
			if v.isKey and v.isAUTO:
				autoKey=v.name
		return autoKey
	def getSettable(self):
		settables={}
		for v in self.varList:
			if v.isAUTO==False:
				settables[v.name]=v.type
		return settables
	def getVars(self):
		varl={}
		for v in self.varList:
			varl[v.name]=v.type
		return varl
				
def dtfParse(fName):
	data={}
	f = open(fName,'r')
	l=f.readline()
	while l:
		l=l.split(" ")
		l.append(None);l.append(None)
		print(l[1])
		if l[0] in data:
			data[l[0]].append(Column(l[1],l[2],l[3],l[4]))
		else:
			data[l[0]]=Table(l[0])
			data[l[0]].append(Column(l[1],l[2],l[3],l[4]))
		l=f.readline()
	f.close()
	return data
	
#def trimAUTO(varList,isAUTO):
#	for i in range(len(isAUTO))
		
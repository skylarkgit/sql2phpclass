import csv

class Column:
	def __init__(self, name, type, keyType, keyReference,validType,lengthConstraint):
		self.name=name
		self.alias=name
		self.type=type
		self.isKey=(keyType!="" and keyType!="AUTO")
		self.keyType=keyType
		self.isAUTO=(keyType=="AUTO" or keyReference=="AUTO")
		#print("name="+name+" keyType="+str(keyType)+" keyReference="+str(keyReference))
		self.validType=validType
		self.lenConstraint=(lengthConstraint!="")
		if(self.lenConstraint==True):
			lens=lengthConstraint.split("-")
			self.minLen=lens[0]
			self.maxLen=lens[1]
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
				keySet[v.name]=v
		return keySet
	def getForiegnKeys(self):
		keySet={}
		for v in self.varList:
			if v.isKey==True and v.keyType=="FOR":
				keySet[v.name]=v
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
				settables[v.name]=v
		return settables
	def getVars(self):
		varl={}
		for v in self.varList:
			varl[v.name]=v
		return varl

def unifyKeys(keySet1,keySet2):
	newSet={}
	for v in keySet1:
		newSet[v.name]=v
	for v in keySet2:
		newSet[v.name]=v
	return newSet
		
def dtfParse(fName):
	rows=[]
	with open(fName, 'r') as csvfile:
		csvreader = csv.reader(csvfile)
		for row in csvreader:
			rows.append(row)
	data={}
	for l in rows:
		print(",".join(l))
		if l[0] in data:
			data[l[0]].append(Column(l[1],l[3],l[4],l[5],l[6],l[7]))
		else:
			data[l[0]]=Table(l[0])
			data[l[0]].append(Column(l[1],l[3],l[4],l[5],l[6],l[7]))
	return data
	
#def trimAUTO(varList,isAUTO):
#	for i in range(len(isAUTO))
		
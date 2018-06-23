import csv

class Column:
	def __init__(self, name, type, keyType, keyReference,validType,lengthConstraint,params=None):
		self.name=name
		self.alias=name
		self.type=type
		self.isKey=(keyType!="")
		self.keyType=keyType
		self.isAUTO=(keyReference=="AUTO")
		#print("name="+name+" keyType="+str(keyType)+" keyReference="+str(keyReference))
		self.validType=validType
		self.lenConstraint=(lengthConstraint!="")
		if self.lenConstraint==True:
			lens=lengthConstraint.split("-")
			self.minLen=lens[0]
			self.maxLen=lens[1]
		if keyType=='FOR':
			self.relationType=params[8]
		self.keyReference=keyReference

class Table:
	def __init__(self, name,varList={}):
		self.name=name
		self.alias=name
		self.varList=varList
	def append(self,col):
		self.varList[col.name]=col
	def getKeys(self):
		keySet={}
		for v in self.varList.values():
			if v.isKey==True and v.keyType=="PRI":
				keySet[v.name]=v
		return keySet
	def getForiegnKeys(self):
		keySet={}
		for v in self.varList.values():
			if v.isKey==True and v.keyType=="FOR":
				keySet[v.name]=v
		return keySet
	def getForiegnOTMKeys(self):
		keySet={}
		for v in self.varList.values():
			if v.isKey==True and v.keyType=="FOR" and v.relationType=="OTM":
				keySet[v.name]=v
		return keySet
	def getForiegnOTOKeys(self):
		keySet={}
		for v in self.varList.values():
			if v.isKey==True and v.keyType=="FOR" and v.relationType=="OTO":
				keySet[v.name]=v
		return keySet
	def getAutoKey(self):
		autoKey=None
		for v in self.varList.values():
			if v.isKey and v.isAUTO:
				autoKey=v
		return autoKey
	def getSettable(self):
		settables={}
		for v in self.varList.values():
			if v.isAUTO==False:
				settables[v.name]=v
		return settables
	def getVars(self):
		varl={}
		for v in self.varList.values():
			varl[v.name]=v
		return varl

def unifyKeys(keySet1,keySet2):
	newSet={}
	for v in keySet1.values():
		newSet[v.name]=v
	for v in keySet2.values():
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
		#print(",".join(l))
		if l[0] in data:
			data[l[0]].append(Column(l[1],l[3],l[4],l[5],l[6],l[7],l))
		else:
			data[l[0]]=Table(l[0],{})
			data[l[0]].append(Column(l[1],l[3],l[4],l[5],l[6],l[7],l))
	return data

#def trimAUTO(varList,isAUTO):
#	for i in range(len(isAUTO))

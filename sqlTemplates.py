insertTemplate		=	"INSERT INTO ~ (@) VALUES (^)"
selectTemplate		=	"SELECT ~ FROM @"
whereTemplate		=	" WHERE ~"

def getAndClause(varList):
	clause=[]
	for d in varList:
		if clause==[]:
			clause=[d+"=:"+d]
		else:
			clause.append(d+"=:"+d)
	return " AND ".join(clause)

def getWhereClause(clause):
	return whereTemplate.replace("~",clause)
	
def getInsertQuery(tableName,varList):
	iQry=insertTemplate.replace('~',tableName)
	iQry=iQry.replace('@',",".join(varList))
	iQry=iQry.replace('^',":"+",:".join(varList))
	return iQry

def getSelectQuery(tableName,varList):
	sQry=selectTemplate.replace('@',tableName)
	sQry=sQry.replace('~',",".join(varList))
	return sQry
	

insertTemplate		=	"INSERT INTO ~ (@) VALUES (^)"
updateTemplate		=	"UPDATE ~ SET @"
selectTemplate		=	"SELECT ~ FROM @"
joinTemplate			=	" ~ INNER JOIN @ ON"
whereTemplate		=	" WHERE ~"

def getEqualList(varList):
	el=[]
	for d in varList:
		if el==[]:
			el=[d+"=:"+d]
		else:
			el.append(d+"=:"+d)
	return el
	
def getAndClause(varList):
	return " "+" AND ".join(getEqualList(varList))

def getEqualClause(varList):
	return " "+" AND ".join(getEqualList(varList))

def getJoinClause(table1,table2):
	clause=joinTemplate.replace('~',table1)
	return clause.replace('@',table2)

def getJoinSelect(varList,table1,table2,clause):
	return getSelectQuery(getJoinClause(table1,table2),varList)+clause
	
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
	
def getUpdateQuery(tableName,varList,clause):
	uQry=updateTemplate.replace('~',tableName)
	uQry=uQry.replace('@',",".join(getEqualList(varList)))+clause
	return uQry
	
def getSelectById(tableSurface):
	tableName=tableSurface.name
	varList=tableSurface.getVars()
	return getSelectQuery(tableName,varList)+getWhereClause(getEqualClause(tableSurface.getKeys()))

def getGlobalById(tableSurface,globalSpace):
	tableName=tableSurface.name
	varList=tableSurface.getVars()
	forKeys=tableSurface.getForiegnKeys()
	return getJoinSelect(varList,table1,table2,getAndClause(key))

def getUpdateById(tableName,varList,clauseVar):
	return getUpdateQuery(tableName,varList,getWhereClause(getEqualClause(clauseVar)))

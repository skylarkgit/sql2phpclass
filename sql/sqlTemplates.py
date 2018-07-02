insertTemplate		=	"INSERT INTO {} ({}) VALUES ({})"
updateTemplate		=	"UPDATE {} SET {}"
selectTemplate		=	"SELECT {} FROM {}"
joinTemplate		=	" INNER JOIN {} ON {}"
whereTemplate		=	" WHERE {}"
sqlMemberTemplate	=	"{obj}.{mem}"
sqlEqlClauseTemplate=	"{}={}"
sqlSelectTemplate	=	"SELECT {vars} FROM {tables}"
sqlWhereTemplate	=	" WHERE {clause}"
sqlAndTemplate		=	" {code1} AND {code2}"

def SQLAND(code1,code2):
	if code1=='': return code2
	if code2=='': return code1
	return sqlAndTemplate.format(code1=code1,code2=code2)

def SQLSELECT(vars,tables):
	return sqlSelectTemplate.format(vars=vars,tables=tables)

def SQLWHERE(clause):
	if(clause==''): return clause
	return sqlWhereTemplate.format(clause=clause)

def SQLEQL(one,two):
	return sqlEqlClauseTemplate.format(one,two)

def SQLMEM(obj,mem):
	return sqlMemberTemplate.format(obj=obj,mem=mem)

def JOIN(tableName1,tableName2,todisp,clause):
	return selectTemplate.format(todisp,tableName1)+joinTemplate.format(to,clause)

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
	return clause.format(table1,table2)

def getJoinSelect(varList,table1,table2,clause):
	return getSelectQuery(getJoinClause(table1,table2),varList)+clause

def getWhereClause(clause):
	return whereTemplate.format(clause)

def getInsertQuery(tableName,varList):
	return insertTemplate.format(tableName,",".join(varList),":"+",:".join(varList))

def getSelectQuery(tableName,varList):
	return selectTemplate.format(",".join(var.name+" as "+var.alias for var in varList.values()),tableName)

def getUpdateQuery(tableName,varList,clause):
	return updateTemplate.format(tableName,",".join(getEqualList(varList)))+clause

def getSelectById(tableSurface):
	tableName=tableSurface.name
	varList=tableSurface.getVars()
	return getSelectQuery(tableName,varList)+getWhereClause(getEqualClause(tableSurface.getKeys()))

#def getGlobalById(tableSurface,globalSpace):
#	tableName=tableSurface.name
#	varList=tableSurface.getVars()
#	forKeys=tableSurface.getForiegnKeys()
#	return getJoinSelect(varList,table1,table2,getAndClause(key))

def getUpdateById(tableName,varList,clauseVar):
	return getUpdateQuery(tableName,varList,getWhereClause(getEqualClause(clauseVar)))

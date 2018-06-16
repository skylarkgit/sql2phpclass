from dtfParser import *
from sqlTemplates import *
from phpTemplates import *
from phpsupport import *

def is_empty(struct):
	if struct:
		return False
	else:
		return True

def getPostArgsFunction(tableSurface):
	varList=tableSurface.getVars()
	return FUNCTION("initFromPost","",localizeAliases(varList));

def getNulledConstructor(tableSurface):
	varList=tableSurface.getVars()
	str="function __construct(){\n"
	return FUNCTION("__construct",""," ".join(THIS(var)+"=NULL;" for var in varList)+"\n");

def getConstructor(tableSurface):
	varList=tableSurface.getSettable()
	str=""
	for d in varList:
		str+=(THIS(d)+"="+VAR(d)+";")
	return FUNCTION("__construct",getNulledArgs(varList),str+"\n");

def getAddFunction(tableSurface):
	tableName=tableSurface.name
	varList=tableSurface.getSettable()
	str=getValidations(varList)
	str+=PREPARE(getInsertQuery(tableName,varList))
	str+=getBindings(varList)
	str+=EXEC(tableName+" : INSERT")
	str+="$retObj=NULL;\n"
	key=tableSurface.getAutoKey()
	allKeys=tableSurface.getKeys()
	if key!=None:
		str+="$this->"+key.name+"="+lastInsertId;
		str+=PREPARE(getSelectQuery(tableName,{key.name:key}))
		str+=getBindings({key.name:key})
		str+=EXEC(tableName+" : SELECT AUTO")
		str+="$retObj"+"="+fetchObj
	elif len(allKeys)>0:
		str+=PREPARE(getSelectQuery(tableName,allKeys))
		str+=getBindings(allKeys)
		str+=EXEC(tableName+" : SELECT PRIME")
		str+="$retObj"+"="+fetchObj
	str+=returnSuccess
	return FUNCTION("add","",str)

def getUpdateByIdFunction(tableSurface):
	tableName=tableSurface.name
	varList=tableSurface.getKeys()
	allSettables=tableSurface.getSettable()
	str=getValidations(varList)
	str+=getValidations(allSettables)
	str+=PREPARE(getUpdateById(tableName,allSettables,varList))
	str+=getBindings(varList)
	str+=getBindings(allSettables)
	str+=EXEC(tableName+" : UPDATE LOCAL BY ID")
	str+="$retObj"+"="+fetchObj
	str+=returnSuccess
	return FUNCTION("getUpdateById","",str)

def getSelectLocalByIdFunction(tableSurface):
	tableName=tableSurface.name
	varList=tableSurface.getKeys()
	str=getArgsToLocal(varList)
	str+=getValidations(varList)
	str+=PREPARE(getSelectById(tableSurface))
	str+=getBindings(varList)
	str+=EXEC(tableName+" : SELECT LOCAL BY ID")
	str+="$retObj"+"="+fetchObj
	str+=returnSuccess
	return FUNCTION("getLocalById",getArgs(varList),str)

def getSelectByIdFunction(tableSurface):
	tableName=tableSurface.name
	varList=tableSurface.getKeys()
	str=getArgsToLocal(varList)
	str+=getValidations(varList)
	str+=PREPARE(getSelectById(tableSurface))
	str+=getBindings(varList)
	str+=EXEC(tableName+" : SELECT LOCAL BY ID")
	str+="$retObj"+"="+fetchObj
	str+=returnSuccess
	return str
	return FUNCTION("getLocalById",getArgs(varList),str)

def getForiegnAdd(var):
	str=EQUAL(VAR("retObj"),CALLIN("Add::"+var.keyReference,"$db"))
	str+=IF(ISEQUAL(VAR("retObj->status"),"'ERROR'"),RETURN(VAR('retObj')))
	str+=EQUAL(POST(var.alias),MEMBER(VAR('retObj->data'),var.alias))
	return str+"\n"

def getAdd(table):
	str=EQUAL(VAR(table.name),"new "+CALLIN(table.name,""))
	str+=MEMBER(VAR(table.name),SETDB(VAR('db')))
	str+=MEMBER(VAR(table.name),CALL('initFromPost',""))
	str+=EQUAL(VAR('retObj'),MEMBER(VAR(table.name),CALLIN('add',"")))
	str+=IF(ISEQUAL(VAR("retObj->status"),"'ERROR'"),RETURN(VAR('retObj')))
	return str+"\n"

def getAddAllFunction(tableSurface):
	tableName=tableSurface.name
	varList=tableSurface.getForiegnKeys()
	str=""
	for v in varList:
		if varList[v].relationType=='OTO':
			str+=getForiegnAdd(varList[v])
	str+=getAdd(tableSurface)
	str+=returnSuccess
	return FUNCTION(tableName,"$db",str)

def getForiegnGet(key):
	str=EQUAL(VAR("retObjTwo"),CALLIN("Get::"+key.keyReference,"$db,$retObj->"+key.alias))
	str+=IF(ISEQUAL(VAR("retObjTwo->status"),"'ERROR'"),RETURN(VAR('retObjTwo')))
	str+=CALL('array_merge',"$result,(array)$retObjTwo->data")
	return str+"\n"

def getGet(table):
	keySet=table.getKeys()
	str=getArgsToLocal(keySet)
	str+=EQUAL(VAR(table.name),"new "+CALLIN(table.name,""))
	str+=MEMBER(VAR(table.name),SETDB(VAR('db')))
	str+=EQUAL(VAR('retObj'),MEMBER(VAR(table.name),CALLIN('getLocalById',getArgs(keySet))))
	str+=IF(ISEQUAL(VAR("retObj->status"),"'ERROR'"),RETURN(VAR('retObj')))
	return str+"\n"

def getGetAllFunction(tableSurface):
	tableName=tableSurface.name
	varList=tableSurface.getForiegnKeys()
	keySet=tableSurface.getKeys()
	if is_empty(keySet):
		return ""
	str="$result=array();\n"
	str+=getGet(tableSurface)
	for v in varList:
		str+=getForiegnGet(varList[v])
	str+="$retObj=(object)$result;\n"
	str+=returnSuccess
	return FUNCTION(tableName,"$db,"+getArgs(keySet),str)

def getForiegnUpdate(var):
	str=EQUAL(VAR("retObj"),CALLIN("Update::"+var.keyReference,"$db"))
	str+=IF(ISEQUAL(VAR("retObj->status"),"'ERROR'"),RETURN(VAR('retObj')))
	str+=EQUAL(POST(var.alias),MEMBER(VAR('retObj->data'),var.alias))
	return str+"\n"

def getUpdate(table):
	str=EQUAL(VAR(table.name),"new "+CALLIN(table.name,""))
	str+=MEMBER(VAR(table.name),SETDB(VAR('db')))
	str+=MEMBER(VAR(table.name),CALL('initFromPost',""))
	str+=EQUAL(VAR('retObj'),MEMBER(VAR(table.name),CALLIN('updateLocalById',"")))
	str+=IF(ISEQUAL(VAR("retObj->status"),"'ERROR'"),RETURN(VAR('retObj')))
	return str+"\n"

def getUpdateAllFunction(tableSurface):
	tableName=tableSurface.name
	varList=tableSurface.getForiegnKeys()
	str=""
	for v in varList:
		if varList[v].relationType=='OTO':
			str+=getForiegnUpdate(varList[v])
	str+=getUpdate(tableSurface)
	str+=returnSuccess
	return FUNCTION(tableName,"$db",str)

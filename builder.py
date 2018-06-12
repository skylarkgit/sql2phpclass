from dtfParser import *
from sqlTemplates import *
from phpTemplates import *
from phpsupport import *

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
		str+="$this->"+key+"="+lastInsertId;
		str+=PREPARE(getSelectQuery(tableName,[key]))
		str+=getBindings([key])
		str+=EXEC(tableName+" : SELECT AUTO")
		str+="$retObj"+"="+fetchObj
	elif len(allKeys)>0:
		str+=PREPARE(getSelectQuery(tableName,allKeys))
		str+=getBindings(allKeys)
		str+=EXEC(tableName+" : SELECT PRIME")
		str+="$retObj"+"="+fetchObj
	str+=returnSuccess
	return FUNCTION("add","",str)

def getSelectByIdFunction(tableSurface):
	tableName=tableSurface.name
	varList=tableSurface.getKeys()
	str=getArgsToLocal(varList)
	str+=PREPARE(getSelectById(tableSurface))
	str+=getBindings(varList)
	str+=EXEC(tableName+" : SELECT LOCAL BY ID")
	str+="$retObj"+"="+fetchObj
	str+=returnSuccess
	return str
	return FUNCTION("getLocalById",getArgs(varList),str)
	
def getUpdateByIdFunction(tableSurface):
	tableName=tableSurface.name
	varList=tableSurface.getKeys()
	allSettables=tableSurface.getSettable()
	str=getArgsToLocal(varList)
	str+=getArgsToLocal(allSettables)
	str+=PREPARE(getUpdateById(tableName,allSettables,varList))
	str+=getBindings(varList)
	str+=getBindings(allSettables)
	str+=EXEC(tableName+" : UPDATE LOCAL BY ID")
	str+="$retObj"+"="+fetchObj
	str+=returnSuccess
	return FUNCTION("getUpdateById",getArgs(varList),str)

def getSelectLocalByIdFunction(tableSurface):
	tableName=tableSurface.name
	varList=tableSurface.getKeys()
	str=getArgsToLocal(varList)
	str+=PREPARE(getSelectById(tableSurface))
	str+=getBindings(varList)
	str+=EXEC(tableName+" : SELECT LOCAL BY ID")
	str+="$retObj"+"="+fetchObj
	str+=returnSuccess
	return FUNCTION("getLocalById",getArgs(varList),str)

import sys
sys.path.append("..")
from phpBuilds.phpTemplates import *
from phpBuilds.phpTools import *
from dtfParser import *
from sql.sqlTemplates import *

def getValidate(var):
	return VALIDATE(THIS(var.alias),var.validType)

def getSanitize(var):
	return SANITIZE(THIS(var.alias),var.validType)

def getValidations(varlist):
	str=""
	for d in varlist.values():
		cond=ISEQUAL(getValidate(d),"false")
		if (d.lenConstraint==True):
			cond+=" || "+ISEQUAL(lenCheck(d),"false")
		str+=IF(cond,INVALID(d.alias))
		str+=THIS(d.alias)+"="+getSanitize(d)
	return str

def lenCheck(var):
	return LENCHECK(THIS(var.alias),var.minLen,var.maxLen)

def getArgsToLocal(varList):
	str=""
	for d in varList.values():
		str+=(THIS(d.alias)+"="+VAR(d.alias)+";")
	return str+"\n"

def localizeAliases(varList):
	str=""
	for d in varList.values():
		str+=("if (isset($_POST['"+d.alias+"'])) $this->"+d.alias+"=$_POST['"+d.alias+"'];")
		str+=("else $this->"+d.alias+"=NULL;\n")
	return str

def getBindings(paramList):
	bindings="";
	for p in paramList.values():
		bindings+=BIND(p.alias,"this->"+p.alias)
	return bindings

def getDeclarations(tableSurface):
	varList=tableSurface.getVars();
	return "".join("public "+VAR(x.alias)+";" for x in varList.values())+"\n";

def getArgs(varList):
	return ",".join(VAR(x.alias) for x in varList.values())

def getNulledArgs(varList):
	return ",".join(VAR(x.alias)+"=NULL" for x in varList.values())

def writePHP(fname,code):
	phpStr	=PHP(code)
	phpFile =open(fname, "w")
	phpFile.write(phpStr)
	phpFile.close()
	finalPhp=beautify(fname)
	phpFile	=open(fname, "w")
	phpFile.write(finalPhp)
	phpFile.close()

def getVarDependency(varName,elsecase):
	return IF(ISSET(POST(varName)),VAR(varName)+"="+POST(varName)+";\n")+ELSE(elsecase)

def getVarDependencies(varList):
	code=""
	for v in varList.values():
		code+=IF(ISSET(POST(v.alias)),VAR(v.alias)+"="+POST(v.alias)+";\n")+ELSE(INVALIDRESPONSE(VAR('res'),v.alias)+ECHO(GETRESPONSE(VAR('res')))+DIE())
	return code

def APICALLS(type,tableSurface):
	tableName=tableSurface.alias
	keys=tableSurface.getKeys()
	return apiCallsTemplates[type].format(tableName=tableName,vars=getArgs(keys))

def getAPIcase(type,tableSurface):
	tableName=tableSurface.alias
	return CASE(tableName,APICALLS(type,tableSurface))

def getTransactionBody(db,var,code):
	finalcode=VAR(db)+"="+CALL('createConnection','')
	finalcode+=BEGINTRANSACTION(VAR(db))
	finalcode+=code
	finalcode+=IF(ISEQUAL(MEMBER(VAR(var),'status'),'"OK"'),COMMIT(VAR(db)))
	finalcode+=ELSE(ROLLBACK(VAR(db)))
	finalcode+=ECHO(GETRESPONSE(VAR(var)))
	return finalcode

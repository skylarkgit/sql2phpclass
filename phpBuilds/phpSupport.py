import sys
sys.path.append("..")
from phpBuilds.phpTemplates import *
from phpBuilds.phpTools import *
from dtfParser import *
from sql.sqlTemplates import *

def getValidate(var):
	return VALIDATE(THIS(var.name),var.validType)

def getSanitize(var):
	return SANITIZE(THIS(var.name),var.validType)

def getValidations(varlist):
	str=""
	for d in varlist.values():
		cond=ISEQUAL(getValidate(d),"false")
		if (d.lenConstraint==True):
			cond+=" || "+ISEQUAL(lenCheck(d),"false")
		str+=IF(cond,INVALID(d.alias))
		str+=THIS(d.name)+"="+getSanitize(d)
	return str

def lenCheck(var):
	return LENCHECK(THIS(var.name),var.minLen,var.maxLen)

def getArgsToLocal(varList):
	str=""
	for d in varList:
		str+=(THIS(d)+"="+VAR(d)+";")
	return str+"\n"

def localizeAliases(varList):
	str=""
	for d in varList.values():
		str+=("if (isset($_POST['"+d.alias+"'])) $this->"+d.name+"=$_POST['"+d.alias+"'];")
		str+=("else $this->"+d.name+"=NULL;\n")
	return str

def getBindings(paramList):
	bindings="";
	for p in paramList:
		bindings+=BIND(p,"this->"+p)
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

def APICALLS(type,tableSurface):
	tableName=tableSurface.alias
	keys=tableSurface.getKeys()
	return apiCallsTemplates[type].format(tableName=tableName,vars=getArgs(keys))

def getAPIcase(type,tableSurface):
	tableName=tableSurface.alias
	return CASE(tableName,APICALLS(type,tableSurface))

def getTransactionBody(db,var,code):
	finalcode=VAR(db)+"="+CALL('createConnection','')
	finalcode+=BEGINTRANSACTION(db)
	finalcode+=code
	finalcode+=IF(ISEQUAL(MEMBER(VAR(var),'status'),'OK'),COMMIT(VAR(db)))
	finalcode+=ELSE(ROLLBACK(VAR(db)))
	finalcode+=ECHO(GETRESPONSE(VAR(var)))
	return finalcode

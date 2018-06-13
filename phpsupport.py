from phpTemplates import *
from dtfParser import *
from phpTools import *
from sqlTemplates import *


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
	return "public $"+";public $".join(varList)+";\n";

def getArgs(varList):
	return "$"+",$".join(varList)

def getNulledArgs(varList):
	return "$"+"=NULL,$".join(varList)+"=NULL"

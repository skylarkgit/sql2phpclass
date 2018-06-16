import sys
sys.path.append("..")
from php.phpTemplates import *
from php.phpTools import *
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
	return "".join("public "+VAR(x)+";" for x in varList)+"\n";

def getArgs(varList):
	return ",".join(VAR(x) for x in varList)

def getNulledArgs(varList):
	return ",".join(VAR(x)+"=NULL" for x in varList)

def writePHP(fname,code):
	phpStr	=PHP(code)
	phpFile =open(fname, "w")
	phpFile.write(phpStr)
	phpFile.close()
	finalPhp=beautify(fname)
	phpFile	=open(fname, "w")
	phpFile.write(finalPhp)
	phpFile.close()

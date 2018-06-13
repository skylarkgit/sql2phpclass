#TEMPLATES
from dtfParser import *
from sqlTemplates import *

prepareTemplate		=	"$stmt=$this->db->prepare('{}');\n"
bindTemplate		=	"$stmt->bindParam(':{}',${});\n"
execTemplate		=	"if($stmt->execute()==false) {{\n$this->errorLog($stmt->errorInfo()[2]);\nreturn new RESPONSE(null,'{}','ERROR');\n}}\n"
lastInsertId		=	"$this->db->lastInsertId();\n"
fetchObj			=	"$stmt->fetch(PDO::FETCH_OBJ);\n"
returnSuccess		=	"return new RESPONSE($retObj,'SUCCESS','OK');\n"
returnInvalid		=	"return new RESPONSE('BAD-{}','INVALID','ERROR');\n"
requireOnce			=	"require_once('{}');\n"
ifTemplate			=	"if({}) {}\n"
elseTemplate		=	"else {}}\n"
elseifTemplate		=	"elseif({}) @\n"
functionTemplate	=	"function {}({}){{\n{}}}\n"
strlenTemplate		=	"strlen(''.{})"
strInRangeTemplate	=	"strInRange({},{},{})"
equalityTemplate	=	"({}=={})"
validateTemplate	=	"validate({},'{}')"
sanitizeTemplate	=	"sanitize({},'{}');\n"

def VALIDATE(var,varclass):
	return validateTemplate.format(var,varclass)

def SANITIZE(var,varclass):
	return sanitizeTemplate.format(var,varclass)

def IF(cond,do):
	return ifTemplate.format(cond,do)

def ISEQUAL(va,vb):
	return equalityTemplate.format(va,vb)

def STRLEN(varname):
	return strlenTemplate.format(varname)

def INVALID(reason):
	return returnInvalid.format(reason)

def REQUIRE_ONCE(fname):
	return requireOnce.format(fname)

def POST(varname):
	return "$_POST['"+var.name+"']"

def FUNCTION(name,args,body):
	return functionTemplate.format(name,args,body)

def THIS(varname):
	return "$this->"+varname

def BIND(inQry,outQry):
	return bindTemplate.format(inQry,outQry)

def EXEC(varMsg):
	return execTemplate.format(varMsg)

def PREPARE(varQ):
	return prepareTemplate.format(varQ)

def VAR(varname):
	return "$"+varname;

def LENCHECK(varname,minl,maxl):
	return strInRangeTemplate.format(varname,minl,maxl);
#-------------

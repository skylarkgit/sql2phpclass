#TEMPLATES
from dtfParser import *
from sqlTemplates import *

bindTemplate		=	"$stmt->bindParam(':{}',${});\n"
callTemplate		=	"{}({});\n"
callinTemplate		=	"{}({})"
classTemplate		=	"class {}{{\n{}}}\n"
commitTemplate		=	"{}->commit();\n"
equalTemplate		=	"{}={};\n"
execTemplate		=	"if($stmt->execute()==false) {{\n$this->errorLog($stmt->errorInfo()[2]);\nreturn new RESPONSE(null,'{}','ERROR');\n}}\n"
elseTemplate		=	"else {}}\n"
elseifTemplate		=	"elseif({}) @\n"
equalityTemplate	=	"({}=={})"
functionTemplate	=	"function {}({}){{\n{}}}\n"
fetchObj			=	"$stmt->fetch(PDO::FETCH_OBJ);\n"
ifTemplate			=	"if({}) {{\n{}}}\n"
lastInsertId		=	"$this->db->lastInsertId();\n"
memberTemplate		=	"{}->{}"
nonEqualityTemplate	=	"({}!={})"
prepareTemplate		=	"$stmt=$this->db->prepare('{}');\n"
phpTemplate			=	"<?php\n{}?>"
returnSuccess		=	"return new RESPONSE($retObj,'SUCCESS','OK');\n"
requireOnce			=	"require_once('{}');\n"
responseTemplate	=	"new RESPONSE({},{},{})"
returnInvalid		=	"return new RESPONSE('BAD-{}','INVALID','ERROR');\n"
returnTemplate		=	"return {};\n"
rollbackTemplate	=	"{}->rollback();\n"
sanitizeTemplate	=	"sanitize({},'{}');\n"
setdbTemplate		=	"setdb({});\n"
strlenTemplate		=	"strlen(''.{})"
strInRangeTemplate	=	"strInRange({},{},{})"
validateTemplate	=	"validate({},'{}')"

def MEMBER(obj,mem):
	return memberTemplate.format(obj,mem)

def RETURN(response):
	return returnTemplate.format(response)

def RESOPNSE(response,msg,status):
	return responseTemplate.format(response,msg,status)

def CALL(var,var2):
	return callTemplate.format(var,var2)

def CALLIN(var,var2):
	return callinTemplate.format(var,var2)

def EQUAL(var,var2):
	return equalTemplate.format(var,var2)

def SETDB(var):
	return setdbTemplate.format(var)

def ROLLBACK(var):
	return rollbackTemplate.format(var)

def COMMIT(var):
	return commitTemplate.format(var)

def PHP(code):
	return phpTemplate.format(code)

def CLASS(classname,code):
	return classTemplate.format(classname,code)

def VALIDATE(var,varclass):
	return validateTemplate.format(var,varclass)

def SANITIZE(var,varclass):
	return sanitizeTemplate.format(var,varclass)

def IF(cond,do):
	return ifTemplate.format(cond,do)

def ISEQUAL(va,vb):
	return equalityTemplate.format(va,vb)

def ISNOTEQUAL(va,vb):
	return nonEqualityTemplate.format(va,vb)

def STRLEN(varname):
	return strlenTemplate.format(varname)

def INVALID(reason):
	return returnInvalid.format(reason)

def REQUIRE_ONCE(fname):
	return requireOnce.format(fname)

def POST(varname):
	return "$_POST['"+varname+"']"

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

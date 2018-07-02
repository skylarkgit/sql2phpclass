#TEMPLATES
import sys
sys.path.append("..")
from dtfParser import *
from sql.sqlTemplates import *

beginTransaction	=	"{var}->beginTransaction();\n"
bindTemplate		=	"$stmt->bindParam(':{}',${});\n"
callTemplate		=	"{}({});\n"
callinTemplate		=	"{}({})"
caseTemplate		=	"case '{match}': {code}break;\n"
classTemplate		=	"class {}{{\n{}}}\n"
commitTemplate		=	"{}->commit();\n"
equalTemplate		=	"{}={};\n"
execTemplate		=	"if($stmt->execute()==false) {{\n$this->errorLog($stmt->errorInfo()[2]);\nreturn new RESPONSE(null,'{}','ERROR');\n}}\n"
elseTemplate		=	"else {{\n{code}}}\n"
elseifTemplate		=	"elseif({cond}) {{{code}}}\n"
echoTemplate		=	"echo {var};\n"
equalityTemplate	=	"({}=={})"
fetchObj			=	"$stmt->fetch(PDO::FETCH_OBJ);\n"
fetchAll			=	"$stmt->fetchAll(PDO::FETCH_ASSOC);\n"
functionTemplate	=	"function {}({}){{\n{}}}\n"
getResponseTemplate	=	"{var}->getResponse()"
ifTemplate			=	"if({}) {{\n{}}}\n"
issetTemplate		=	"isset({var})"
invalidResponse		=	"{var}=new RESPONSE('BAD-{msg}','INVALID','ERROR');\n"
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
rollbackTemplate	=	"{}->rollBack();\n"
sanitizeTemplate	=	"sanitize({},'{}');\n"
setdbTemplate		=	"setdb({});\n"
strlenTemplate		=	"strlen(''.{})"
strInRangeTemplate	=	"strInRange({},{},{})"
switchTemplate		=	"switch({var}){{\n{code}}}\n"
validateTemplate	=	"validate({},'{}')"
apiCallsTemplates	=	{
'ADD': 'return Add::{tableName}($db);',
'UPDATE': 'return Update::{tableName}($db);',
'GET': '$obj=new {tableName}();return $obj->getAllGlobal($db);',
'SELECT': '$obj=new {tableName}();return $obj->getAllLocal($db);',
'FETCH': '$obj=new {tableName}();return $obj->getByIdGlobal($db);'
}

def ELSE(code):
	return elseTemplate.format(code=code)

def BEGINTRANSACTION(varName):
	return beginTransaction.format(var=varName)

def DIE():
	return "die();\n"

def GETRESPONSE(var):
	return getResponseTemplate.format(var=var)

def ECHO(var):
	return echoTemplate.format(var=var)

def INVALIDRESPONSE(var,msg):
	return invalidResponse.format(var=var,msg=msg)

def ISSET(var):
	return issetTemplate.format(var=var)

def CASE(match,code):
	return caseTemplate.format(match=match,code=code)

def SWITCH(var,code):
	return switchTemplate.format(var=var,code=code)

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

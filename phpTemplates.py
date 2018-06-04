#TEMPLATES
from dtfParser import *
from sqlTemplates import *

prepareTemplate	=	"$stmt=$this->db->prepare('~');\n"
bindTemplate			=	"$stmt->bindParam(':~',$@);\n"
execTemplate		=	"if($stmt->execute()==false) {\n$this->errorLog($stmt->errorInfo()[2]);\nreturn new RESPONSE(null,'~','ERROR');\n}\n"
lastInsertId			=	"=$this->db->lastInsertId();\n"
fetchObj				=	"=$stmt->fetch(PDO::FETCH_OBJ);\n"
returnSuccess		=	"return new RESPONSE($retObj,'SUCCESS','OK');\n"
def getBind(inQry,outQry):
	return bindTemplate.replace("~",inQry).replace("@",outQry)

def getArgsToLocal(varList):
	str=""
	for d in varList:
		str+=("$this->"+d+"=$p"+d+";")
	return str+"\n"
		
def getPrepare(varQ):
	return prepareTemplate.replace("~",varQ)
	
def getArgs(varList):
	return "$p"+",$p".join(varList)
	
def getExec(varMsg):
	return execTemplate.replace("~",varMsg)

def getBindings(paramList):
	bindings="";
	for p in paramList:
		bindings+=getBind(p,"this->"+p)
	return bindings

def getDeclarations(tableSurface):
	varList=tableSurface.getVars();
	return "public $"+";public $".join(varList)+";\n";
	
def getSelectLocalByIdFunction(tableSurface):
	tableName=tableSurface.name
	varList=tableSurface.getKeys()
	str="function getLocalById("+getArgs(varList)+"){\n"
	str+=getArgsToLocal(varList)
	str+=getPrepare(getSelectById(tableSurface))
	str+=getBindings(varList)
	str+=getExec(tableName+" : SELECT LOCAL BY ID")
	str+="$retObj"+fetchObj
	str+=returnSuccess
	str+="}\n"
	return str
	
def getUpdateByIdFunction(tableSurface):
	tableName=tableSurface.name
	varList=tableSurface.getKeys()
	allSettables=tableSurface.getSettable()
	str="function getUpdateById("+getArgs(varList)+"){\n"
	str+=getArgsToLocal(varList)
	str+=getArgsToLocal(allSettables)
	str+=getPrepare(getUpdateById(tableName,allSettables,varList))
	str+=getBindings(varList)
	str+=getBindings(allSettables)
	str+=getExec(tableName+" : SELECT LOCAL BY ID")
	str+="$retObj"+fetchObj
	str+=returnSuccess
	str+="}\n"
	return str

def getSelectGlobalByIdFunction(tableSurface):
	tableName=tableSurface.name
	varList=tableSurface.getKeys()
	str="function getGlobalById("+getArgs(varList)+"){\n"
	str+=getArgsToLocal(varList)
	str+=getPrepare(getSelectById(tableSurface))
	str+=getBindings(varList)
	str+=getExec(tableName+" : SELECT GLOBAL BY ID")
	str+="$retObj"+fetchObj
	str+=returnSuccess
	str+="}\n"
	return str

def getSelectByIdFunction(tableSurface):
	tableName=tableSurface.name
	varList=tableSurface.getKeys()
	str="function getLocalById("+getArgs(varList)+"){\n"
	str+=getArgsToLocal(varList)
	str+=getPrepare(getSelectById(tableSurface))
	str+=getBindings(varList)
	str+=getExec(tableName+" : SELECT LOCAL BY ID")
	str+="$retObj"+fetchObj
	str+=returnSuccess
	str+="}\n"
	return str
	
def getAddFunction(tableSurface):
	tableName=tableSurface.name
	varList=tableSurface.getSettable()
	str="function add(){\n"
	str+=getPrepare(getInsertQuery(tableName,varList))
	str+=getBindings(varList)
	str+=getExec(tableName+" : INSERT")
	str+="$retObj=NULL;\n"
	key=tableSurface.getAutoKey()
	allKeys=tableSurface.getKeys()
	if key!=None:
		str+="$this->"+key+lastInsertId;
		str+=getPrepare(getSelectQuery(tableName,[key]))
		str+=getBindings([key])
		str+=getExec(tableName+" : SELECT AUTO")
		str+="$retObj"+fetchObj
	elif len(allKeys)>0:
		str+=getPrepare(getSelectQuery(tableName,allKeys))
		str+=getBindings(allKeys)
		str+=getExec(tableName+" : SELECT PRIME")
		str+="$retObj"+fetchObj
	str+=returnSuccess
	#str+="$"getLastInserted()
	str+="}\n"
	return str

def getConstructor(tableSurface):
	varList=tableSurface.getSettable()
	str="function __construct("+getArgs(varList)
	str+="){\n"
	for d in varList:
		str+=("$this->"+d+"=$p"+d+";")
	str+="\n}\n"
	return str
	
def getNulledConstructor(tableSurface):
	varList=tableSurface.getVars()
	str="function __construct(){\n"
	str+="$this->"+"=NULL;$this->".join(varList)+"=NULL;"
	str+="\n}\n"
	return str
	
#-------------


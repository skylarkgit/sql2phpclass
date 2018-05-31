#TEMPLATES

prepareTemplate	=	"$stmt=$this->db->prepare('~');\n"
bindTemplate			=	"$stmt->bindParam(':~',$~);\n"
execTemplate		=	"if($stmt->execute()==false) {\n$this->errorLog($stmt->errorInfo()[2]);\nreturn new RESPONSE(null,'~','ERROR');\n}\n"
insertTemplate		=	"INSERT INTO ~ (@) VALUES (^)"

def getBind(var):
	return bindTemplate.replace("~",var)
	
def getPrepare(varQ):
	return prepareTemplate.replace("~",varQ)
	
def getExec(varMsg):
	return execTemplate.replace("~",varMsg)

def getBindings(paramList):
	bindings="";
	for p in paramList:
		bindings+=getBind(p)
	#print(bindings+"|||||||||||");
	return bindings

def getVars(varList):
	varDec="public $"
	varDec+=",$".join(varList)+";\n"
	return varDec
#def getClass():

def getInsertQuery(varTable,varList):
	iQry=insertTemplate.replace('~',varTable)
	iQry=iQry.replace('@',",".join(varList))
	iQry=iQry.replace('^',":"+",:".join(varList))
	return iQry

def getAddFunction(tableName,varList):
	str="function add(){\n"
	str+=getPrepare(getInsertQuery(tableName,varList))
	str+=getBindings(varList)
	str+=getExec(tableName+" : INSERT")
	str+="}\n"
	return str
	
def getConstructor(varList):
	str="function __construct($p"
	str+=",$p".join(varList)
	str+="){\n"
	for d in varList:
		str+=("$"+d+"=$p"+d+";")
	str+="\n}\n"
	return str
#-------------


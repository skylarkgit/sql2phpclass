import sys
sys.path.append('..')
from jsBuilds.jsTemplates import *
from jsBuilds.jsSupport import *
from lib.fileOps import *
import jsbeautifier

tables=None
DEPENDENCIES="$scope,archonAPI,ToolBag,$http,$window,$filter,$mdDialog"

def getSelectServices(tableSurface):
	tableName=tableSurface.alias
	varList=tableSurface.getForiegnOTMKeys()
	code=""
	for v in varList.values():
		code+=(ARCHONCALL('select',tables[v.keyReference].alias,'',POSTSUBMISSION(SCOPE(v.alias+"Select")+'=response.data.data;',ONFAILURE('"NO ENTRIES IN '+tableName+' FOUND"'))))
	varList=tableSurface.getForiegnOTOKeys()
	for v in varList.values():
		code+=getSelectServices(tables[v.keyReference])
	return code

def getAllSettables(tableSurface,NV={}):
    varList=tableSurface.getSettable()
    print(tableSurface.name+" ----- "+','.join(varList))
    for v in varList.values():
        if v.isKey and v.keyType=="FOR" and v.relationType=="OTO":
            NV=getAllSettables(tables[v.keyReference],NV)
        else:
            NV[v.name]=v
    return NV

def setTables(tableSurfaces):
	global tables
	tables=tableSurfaces

def getSubmission(tableSurface):
	#code="var obj={"+createObjFromScope(tableSurface.getSettable())+"};\n"
	NV=getAllSettables(tableSurface,{})
	print(",".join(NV))
	code=SUBMISSION('"add"',CALL('ToolBag.objToCallArgs',createObjFromScope(NV)),"'"+tableSurface.alias+"'",POSTSUBMISSION(ONSUCCESS('"Data Saved"'),ONFAILURE('response.data.data')))
	return code

def createController(tableSurface):
	tableName=tableSurface.alias
	varList=tableSurface.getSettable()
	code=SCOPE(VALIDITY(SCOPE('add'+tableName+'Controller')))
	code+=getSelectServices(tableSurface)
	code+=getSubmission(tableSurface)
	return OBJ('app',CONTROLLER(CONTROLLERNAME('add',tableName),DEPENDENCIES,code))

def buildControllers(tableSurfaces):
	global tables
	tables=tableSurfaces
	code=""
	touchd('js')
	for t in tables.values():
		code+=createController(t)
	f=open('js\controllers.js','w')
	f.write(jsbeautifier.beautify(code))

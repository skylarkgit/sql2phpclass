import sys
sys.path.append('..')
from jsBuilds.jsTemplates import *
from jsBuilds.jsSupport import *
from lib.fileOps import *
from dtfSupport import *
import jsbeautifier

tables=None
DEPENDENCIES="$scope,archonAPI,ToolBag,$http,$window,$filter,$mdDialog"

def getSelectServices(tableSurface):
	tableName=tableSurface.alias
	varList=tableSurface.getForiegnOTMKeys()
	code=""
	for v in varList.values():
		code+=(ARCHONCALL('select',tables[v.keyReference].alias,'',POSTSUBMISSION(SCOPE(v.alias+"Select")+'=response.data.data;',ONFAILURE('"COULDN\'t FETCH DATA FROM '+tableName+' : "+response.data.data'))))
	varList=tableSurface.getForiegnOTOKeys()
	for v in varList.values():
		code+=getSelectServices(tables[v.keyReference])
	return code

def getShowService(tableSurface):
	tableName=tableSurface.alias
	varList=tableSurface.getForiegnOTMKeys()
	code=ARCHONCALL('Get',tableName,'',POSTSUBMISSION(SCOPE(tableName+"Data")+'=response.data.data;',ONFAILURE('"COULDN\'t FETCH DATA FROM '+tableName+' : "+response.data.data')))
	return code

def setTables(tableSurfaces):
	global tables
	tables=tableSurfaces

def getSubmission(tableSurface):
	#code="var obj={"+createObjFromScope(tableSurface.getSettable())+"};\n"
	NV=getAllSettables(tables,tableSurface,{})
	print(",".join(NV))
	code=SUBMISSION('"add"',CALL('ToolBag.objToCallArgs',createObjFromScope(NV)),"'"+tableSurface.alias+"'",POSTSUBMISSION(ONSUCCESS('"Data Saved"'),ONFAILURE('response.data.data')))
	return code

def createAddController(tableSurface):
	tableName=tableSurface.alias
	varList=tableSurface.getSettable()
	code=SCOPE(VALIDITY(SCOPE('add'+tableName+'Controller')))
	code+=SCOPE('showAdvanced')+'=ToolBag.showAdvanced;\n'
	code+=getSelectServices(tableSurface)
	code+=getSubmission(tableSurface)
	return OBJ('app',CONTROLLER(CONTROLLERNAME('add',tableName),DEPENDENCIES,code))

def buildShowController(tableSurface):
	tableName=tableSurface.alias
	code=SCOPE('showAdvanced')+'=ToolBag.showAdvanced;\n'
	code+=getShowService(tableSurface)
	return OBJ('app',CONTROLLER(CONTROLLERNAME('show',tableName),DEPENDENCIES,code))

def buildControllers(tableSurfaces):
	global tables
	tables=tableSurfaces
	code=""
	pc=""
	touchd('js')

	for t in tables.values():
		code+=createAddController(t)
		pc+=CASE("'"+CONTROLLERNAME('add',t.alias)+"'",'return '+CONTROLLERNAME('add',t.alias)+';')
	for t in tables.values():
		code+=buildShowController(t)
		pc+=CASE("'"+CONTROLLERNAME('show',t.alias)+"'",'return '+CONTROLLERNAME('show',t.alias)+';')
	pc=SWITCH('ctrl',pc)
	pc='obj.controllerProvider=function(ctrl){{{code}}}'.format(code=pc)
	f=open('js\controllers.js','w')
	f.write(jsbeautifier.beautify(pc+code))

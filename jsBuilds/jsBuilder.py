import sys
sys.path.append('..')
from jsBuilds.jsTemplates import *
from jsBuilds.jsSupport import *
tables=None

def getFetchServices(tableSurface):
	tableName=tableSurface.alias
	varList=tableSurface.getForiegnOTMKeys()
	code=""
	for v in varList.values():
		code+=FETCHSERVICE('select'+tableName,"")
	varList=tableSurface.getForiegnOTMKeys()
	for v in varList.values():
		code+=getFetchServices(tables[v.keyReference])
	return code

def getSubmission(tableSurface):
	code=SUBMISSION("","")
	return code

def createController(tableSurface):
	tableName=tableSurface.alias
	varList=tableSurface.getSettable()
	arr=varsToAliasArr(varList)
	code=SCOPE(VALIDITY(SCOPE('add'+tableName+'Controller')))
	code+=getFetchServices(tableSurface)
	code+=getSubmission(tableSurface)
	controller=CONTROLLER(CONTROLLERNAME(tableName),DEPENDENCIES,code)

def buildControllers(tableSurfaces):
	global tables
	tables=tableSurfaces
	code=""
	touchd('js')
	for t in tables:
		code+=createController(t)
	f=open('controllers.js','w')
	f.write(code)

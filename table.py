import sys
from htmlBuilds.htmlBuilder import *
from phpBuilds.phpTemplates import *
from dtfParser import *
from phpBuilds.phpTools import *
from phpBuilds.phpBuilder import *
from jsBuilds.jsBuilder import *
from lib.fileOps import *

print("Parsing.........")

tableSurfaces=dtfParse("table.dtf")

for t in tableSurfaces.values():
	print(t.name+"-----"+(','.join(t.varList)))

print("Finished Parsing")

touchd('php')
touchd('htmlTemplates')
touchd('js')

#setTables(tableSurfaces)
#NV=getAllSettables(tableSurfaces['patients'])
#print(",".join(NV))
#sys.exit()
#CLASSES.php
createPHPClasses(tableSurfaces)
#ADD.php
createAddFunctions(tableSurfaces)
createAddAPI(tableSurfaces)
#GET.php
createGetFunctions(tableSurfaces)
createSelectAPI(tableSurfaces)
#UPDATE.php
createUpdateFunctions(tableSurfaces)
#ADD.tpl
createHTMLTemplates(tableSurfaces)
#controllers.js
buildControllers(tableSurfaces)

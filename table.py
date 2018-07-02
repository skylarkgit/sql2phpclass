import sys
import pprint
from dtfParser import *
from lib.fileOps import *
from sql.sqlBuilder import *
from phpBuilds.phpTools import *
from jsBuilds.jsBuilder import *
from phpBuilds.phpBuilder import *
from htmlBuilds.htmlBuilder import *
from phpBuilds.phpTemplates import *
print("Parsing.........")

tableSurfaces=dtfParse("table.dtf")

for t in tableSurfaces.values():
	print(t.name+"-----"+(','.join(t.varList)))

print("Finished Parsing")

touchd('php')
touchd('htmlTemplates')
touchd('js')

#CLASSES.php
createPHPClasses(tableSurfaces)

#ADD.php
createAddFunctions(tableSurfaces)
createAddAPI(tableSurfaces)

#GET.php
createGetFunctions(tableSurfaces)
createSelectAPI(tableSurfaces)
createGetAPI(tableSurfaces)
createUpdateAPI(tableSurfaces)
createFetchAPI(tableSurfaces)

#UPDATE.php
createUpdateFunctions(tableSurfaces)

#ADD.tpl
createHTMLTemplates(tableSurfaces)

#controllers.js
buildControllers(tableSurfaces)

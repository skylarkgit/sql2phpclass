import sys
from htmlBuilds.htmlBuilder import *
from php.phpTemplates import *
from dtfParser import *
from php.phpTools import *
from builder import *

print("Parsing.........")

tableSurfaces=dtfParse("table.dtf")

print("Finished Parsing")

#sys.exit()
#CRUD
#CLASSES.php
phpStr=REQUIRE_ONCE("dbconn.php")+REQUIRE_ONCE("toolbag.php")
for a in tableSurfaces:
	str=getDeclarations(tableSurfaces[a])
	str+=getConstructor(tableSurfaces[a])
	#str+=getNulledConstructor(tableSurfaces[a])
	str+=getAddFunction(tableSurfaces[a])
	str+=getSelectLocalByIdFunction(tableSurfaces[a])
	str+=getUpdateByIdFunction(tableSurfaces[a])
	str+=getPostArgsFunction(tableSurfaces[a])
	#print(str)
	phpStr+=CLASS(a+" extends dbconn",str)

writePHP("classes.php",phpStr)

#ADD.php
phpStr=REQUIRE_ONCE("dbconn.php")+REQUIRE_ONCE("toolbag.php")+REQUIRE_ONCE("classes.php")+REQUIRE_ONCE("auth.php")
fncs=""
for a in tableSurfaces:
	fncs+="static "+getAddAllFunction(tableSurfaces[a])
#print(fncs)
phpStr+=CLASS("Add",fncs)
writePHP("add.php",phpStr)

#GET.php
phpStr=REQUIRE_ONCE("dbconn.php")+REQUIRE_ONCE("toolbag.php")+REQUIRE_ONCE("classes.php")+REQUIRE_ONCE("auth.php")
fncs=""
for a in tableSurfaces:
	fncs+="static "+getGetAllFunction(tableSurfaces[a])
#print(fncs)
phpStr+=CLASS("Get",fncs)
writePHP("get.php",phpStr)


#UPDATE.php
phpStr=REQUIRE_ONCE("dbconn.php")+REQUIRE_ONCE("toolbag.php")+REQUIRE_ONCE("classes.php")+REQUIRE_ONCE("auth.php")
fncs=""
for a in tableSurfaces:
	fncs+="static "+getUpdateAllFunction(tableSurfaces[a])
#print(fncs)
phpStr+=CLASS("Update",fncs)
writePHP("update.php",phpStr)

#ADD.tpl
createHTMLTemplates(tableSurfaces)

buildControllers(tableSurfaces)

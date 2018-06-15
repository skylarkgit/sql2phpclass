import sys
import numpy as np
from phpTemplates import *
from dtfParser import *
from phpTools import *
from builder import *

print("Parsing.........")

tableSurfaces=dtfParse("table.dtf")

print("Finished Parsing")

#sys.exit()
#CRUD
#CLASSES.php
phpStr=REQUIRE_ONCE("dbconn.php")
phpStr+=REQUIRE_ONCE("toolbag.php")
for a in tableSurfaces:
	str=getDeclarations(tableSurfaces[a])
	str+=getConstructor(tableSurfaces[a])
	#str+=getNulledConstructor(tableSurfaces[a])
	str+=getAddFunction(tableSurfaces[a])
	str+=getSelectLocalByIdFunction(tableSurfaces[a])
	str+=getUpdateByIdFunction(tableSurfaces[a])
	str+=getPostArgsFunction(tableSurfaces[a])
	print(str)
	phpStr+=CLASS(a+" extends dbconn",str)

phpStr	=	PHP(phpStr)
phpFile = 	open("classes.php", "w")
phpFile.write(phpStr)
phpFile.close()

finalPhp=	beautify("classes.php")

phpFile	= 	open("classes.php", "w")
phpFile.write(finalPhp)
phpFile.close()

#ADD.php
phpStr=REQUIRE_ONCE("dbconn.php")
phpStr+=REQUIRE_ONCE("toolbag.php")
phpStr+=REQUIRE_ONCE("classes.php")
phpStr+=REQUIRE_ONCE("auth.php")
fncs=""
for a in tableSurfaces:
	fncs+=getAddAllFunction(tableSurfaces[a])

print(fncs)

phpStr+=CLASS("Add",fncs)

phpStr	=	PHP(phpStr)
phpFile = 	open("add.php", "w")
phpFile.write(phpStr)
phpFile.close()

finalPhp=	beautify("add.php")

phpFile	= 	open("add.php", "w")
phpFile.write(finalPhp)
phpFile.close()

#GET.php
phpStr=REQUIRE_ONCE("dbconn.php")
phpStr+=REQUIRE_ONCE("toolbag.php")
phpStr+=REQUIRE_ONCE("classes.php")
phpStr+=REQUIRE_ONCE("auth.php")
fncs=""
for a in tableSurfaces:
	fncs+=getGetAllFunction(tableSurfaces[a])

print(fncs)

phpStr+=CLASS("Get",fncs)

phpStr	=	PHP(phpStr)
phpFile = 	open("get.php", "w")
phpFile.write(phpStr)
phpFile.close()

finalPhp=	beautify("get.php")

phpFile	= 	open("get.php", "w")
phpFile.write(finalPhp)
phpFile.close()

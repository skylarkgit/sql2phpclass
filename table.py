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

phpStr="<?php\n"
phpStr+=REQUIRE_ONCE("dbconn.php")
phpStr+=REQUIRE_ONCE("toolbag.php")
for a in tableSurfaces:
	str="class "+a+" extends dbconn{\n";
	str+=getDeclarations(tableSurfaces[a])
	str+=getConstructor(tableSurfaces[a])
	#str+=getNulledConstructor(tableSurfaces[a])
	str+=getAddFunction(tableSurfaces[a])
	str+=getSelectLocalByIdFunction(tableSurfaces[a])
	str+=getUpdateByIdFunction(tableSurfaces[a])
	str+=getPostArgsFunction(tableSurfaces[a])
	str+="}\n"
	print(str)
	phpStr+=str+"\n"

phpStr+="?>"
phpFile = open("classes.php", "w")
phpFile.write(phpStr)
phpFile.close()

finalPhp=beautify("classes.php")

phpFile = open("classes.php", "w")
phpFile.write(finalPhp)
phpFile.close()

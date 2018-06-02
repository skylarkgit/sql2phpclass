import numpy as np
from phpTemplates import *
from dtfParser import *
from phpTools import *

print("Parsing.........")

data=dtfParse("table.dtf")

print("Finished Parsing")

phpStr="<?php\n"

for a in data:
	str="class "+a+" implements dbconn{\n";
	str+=getDeclarations(data[a])
	str+=getConstructor(data[a])
	str+=getNulledConstructor(data[a])
	str+=getAddFunction(data[a])
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

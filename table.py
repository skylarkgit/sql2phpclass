import numpy as np
from phpTemplates import *
from dtfParser import *
from phpTools import *

[data,type]=dtfParse("tables.dtf")

phpStr="<?php\n"

for a in data:
	str="class "+a+" implements dbconn{\n";
	str+=getConstructor(data[a])
	str+=getAddFunction(a,data[a])
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

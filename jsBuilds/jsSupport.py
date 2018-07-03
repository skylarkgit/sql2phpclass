import sys
sys.path.append('..')
from jsBuilds.jsTemplates import *

def args(varList):
    return ','.join(varList)

def reqData(varList):
    return '+"&"+'.join('"'+x+'="obj.'+x for x in varList)

def objFormation(varlist):
    return ','.join(x+':'+SCOPE(x) for x in varList)

def varsToAliasArr(varList):
    arr={}
    for v in varList.values():
        arr[v.alias]=v
    return arr

def createObjFromScope(varList):
    return '{'+(','.join(v.alias+":"+PARSER(v.validType,SCOPE(v.alias)) for v in varList.values()))+'}'

def responseToScope(varList):
    return ''.join(SCOPE() for v in varList.values())

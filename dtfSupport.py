from  dtfParser import *

def getAllVars(tables,tableSurface,NV={}):
    varList=tableSurface.getVars()
    for v in varList.values():
        if v.isKey and v.keyType=="FOR" and v.relationType=="OTO":
            NV=getAllVars(tables,tables[v.keyReference],NV)
        else:
            NV[v.name]=v
    return NV

def getAllOTOLinks(tables,tableSurface,NV={}):
    varList=tableSurface.getForiegnOTOKeys()
    for v in varList.values():
        NV=getAllOTOLinks(tables,tables[v.keyReference],NV)
        NV[v.keyReference]={'tableName':tableSurface.name,'via':v.name,'parent':v.keyReference}
    return NV

def getAllOTOLinkedTables(tables,tableSurface,list=[]):
    varList=tableSurface.getForiegnOTOKeys()
    list.append(tableSurface.name)
    for v in varList.values():
        list=getAllOTOLinkedTables(tables,tables[v.keyReference],list)
    return list

import sys
sys.path.append('..')
import pprint
from sql.sqlTemplates import *
from dtfSupport import *

def getJoinQueryOld(tableSurface1,varList2,refcolname,code,aliasNum=1):
    tableName1=tableSurface1.name
    tableName2='a'+aliasNum
    varList1=tableSurface1.getVars()
    clause=SQLEQL(SQLMEM(tableName2,varList2[refcolname]),tableName1.refcolname)
    todisp2=','.join(MEM(tableName2,v.alias)+' as '+v.alias for v in varList2.values())
    todisp1=','.join(MEM(tableName1,v.name)+' as '+v.alias for v in varList1.values())
    JOIN(tableName1,tableName2,todisp1.todisp2,code)

def getJoinQuery(tables,tableSurface):
    varList=getAllVars(tables,tableSurface,{})
    allLinks=getAllOTOLinks(tables,tableSurface,{})
    allTables=getAllOTOLinkedTables(tables,tableSurface,[])
    varsStr=','.join(SQLMEM(v.tableName,v.name)+" as "+v.alias for v in varList.values())
    allTalbesStr=','.join(allTables)
    #pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(allLinks)
    NVstr=' AND '.join(SQLEQL(SQLMEM(n['tableName'],n['via']),SQLMEM(n['parent'],n['via'])) for n in allLinks.values())
    return SQLSELECT(varsStr,allTalbesStr)+SQLWHERE(NVstr)

def getJoinByIdQuery(tables,tableSurface):
    keys=tableSurface.getKeys()
    varList=getAllVars(tables,tableSurface,{})
    allLinks=getAllOTOLinks(tables,tableSurface,{})
    allTables=getAllOTOLinkedTables(tables,tableSurface,[])
    varsStr=','.join(SQLMEM(v.tableName,v.name)+" as "+v.alias for v in varList.values())
    allTalbesStr=','.join(allTables)
    #pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(allLinks)
    NVstr=[keys]
    NVstr=(' AND '.join(SQLEQL(SQLMEM(n['tableName'],n['via']),SQLMEM(n['parent'],n['via'])) for n in allLinks.values()))

    NVstr=SQLAND(' AND '.join(SQLEQL(SQLMEM(tableSurface.name,k.name),':'+k.alias) for k in keys.values()),NVstr)
    return SQLSELECT(varsStr,allTalbesStr)+SQLWHERE(NVstr)

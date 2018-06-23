import sys
sys.path.append('..')
from htmlBuilds.htmlTemplates import *
from htmlBuilds.mytemplate import *
from lib.fileOps import *
import bs4
table=None

def getHTMLAdd(tableSurface,column,type=None):
    return getInputCode(tableSurface,column,type)

def getHTMLAllAdd(ownerTableSurface,tableSurface=None):
    if tableSurface==None:
        tableSurface=ownerTableSurface
    varList=tableSurface.getSettable()
    code='<md-divider md-inset ng-if="!$last"></md-divider>\n'
    for v in varList.values():
        if v.isKey and v.keyType=="FOR" and v.relationType=='OTO':
            #print(v.name+"----"+ownerTableSurface.name+"----"+tableSurface.name+"-----"+v.keyReference)
            code+=getHTMLAllAdd(ownerTableSurface,table[v.keyReference])
        elif v.isKey and v.keyType=="FOR" and v.relationType=='OTM':
            code+=getForeignAdd(ownerTableSurface,v,table[v.keyReference])
        else :
            code+=getHTMLAdd(ownerTableSurface,v)
    return code

def buildHTMLTemplate(tableSurface):
    code=getHTMLAllAdd(tableSurface)
    return getFormBodyCode(tableSurface,code)

def createHTMLTemplates(tables):
    global table
    table=tables
    touchd('htmlTemplates')
    for t in table:
        print(t)
    for t in table:
        f=open("htmlTemplates/add"+table[t].alias+".html.tpl",'w')
        f.write(bs4.BeautifulSoup(buildHTMLTemplate(table[t]), "html5lib").prettify())
        f.close()

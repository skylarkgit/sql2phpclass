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
    code=""
    for v in varList:
        if varList[v].isKey and varList[v].keyType=="FOR" and varList[v].relationType=='OTO':
            code+=getHTMLAllAdd(ownerTableSurface,table[varList[v].keyReference])
        elif varList[v].isKey and varList[v].keyType=="FOR" and varList[v].relationType=='OTM':
            code+=getForeignAdd(ownerTableSurface,varList[v],table[varList[v].keyReference])
        else :
            code+=getHTMLAdd(ownerTableSurface,varList[v])
    return code+'<md-divider md-inset ng-if="!$last"></md-divider>'

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

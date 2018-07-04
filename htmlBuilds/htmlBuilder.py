import sys
sys.path.append('..')
from htmlBuilds.htmlTemplates import *
from htmlBuilds.mytemplate import *
from htmlBuilds.htmlSupport import *
from lib.fileOps import *
from dtfSupport import *
import bs4
import html
table=None

def getHTMLAdd(tableSurface,column,type=None):
    return getInputCode(tableSurface,column,type)

def getHTMLAllAdd(ownerTableSurface,tableSurface=None):
    if tableSurface==None:
        tableSurface=ownerTableSurface
    varList=tableSurface.getSettable()
    code1=''
    code2=''
    for v in varList.values():
        if v.isKey and v.keyType=="FOR" and v.relationType=='OTO':
            #print(v.name+"----"+ownerTableSurface.name+"----"+tableSurface.name+"-----"+v.keyReference)
            code2+=getHTMLAllAdd(ownerTableSurface,table[v.keyReference])
        elif v.isKey and v.keyType=="FOR" and v.relationType=='OTM':
            code1+=getForeignAdd(ownerTableSurface,v,table[v.keyReference])
        else :
            code1+=getHTMLAdd(ownerTableSurface,v)
    code=HEADING(tableSurface.alias,code1)+code2
    return code

def getHTMLShowTable(tables,tableSurface):
    varList=getAllReal(tables,tableSurface,{})
    headings=''.join(ITAG('th',v.alias.title()) for v in varList.values())+ITAG('th','ACTION')
    data=''.join(ITAG('td',TABLEDATA(tableSurface,v)) for v in varList.values())+ITAG('td',UPDATEBUTTON(tableSurface))
    code=DATATABLE(tableSurface,headings,data)
    return code

def buildHTMLAddTemplate(tableSurface):
    code=getHTMLAllAdd(tableSurface)+SUBMIT('add',tableSurface)
    return wrapForm(getFormBodyCode(tableSurface,code))

def buildHTMLShowTemplate(tables,tableSurface):
    code=getHTMLShowTable(tables,tableSurface)
    return TAG('div',code,"class='archonShowTable'")

def createHTMLTemplates(tables):
    global table
    table=tables
    touchd('htmlTemplates')
    for t in table:
        f=open("htmlTemplates/add"+table[t].alias+".html.tpl",'w')
        f.write(html.unescape(bs4.BeautifulSoup(buildHTMLAddTemplate(table[t]), "html5lib").prettify()))
        f.close()
    for t in table:
        f=open("htmlTemplates/show"+table[t].alias+".html.tpl",'w')
        f.write(html.unescape(bs4.BeautifulSoup(buildHTMLShowTemplate(tables,table[t]), "html5lib").prettify()))
        f.close()

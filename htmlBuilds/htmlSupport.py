import sys
sys.path.append("..")
from htmlBuilds.htmlTemplates import *
from htmlBuilds.mytemplate import *
from lib.fileOps import *

def wrapForm(code):
    return TAG('div',code,ATTR('class','archonFormWrapper'))

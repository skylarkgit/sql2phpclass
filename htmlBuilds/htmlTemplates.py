#Templates
tagTemplate         =   "<{name} {attributes}>\n{code}\n</{name}>\n"
inlineTagTemplate   =   "<{name} {attributes}>{code}</{name}>\n"
attributesTemplate  =   "{name}='{value}'"

def TAG(tname,tcode,tattributes=""):
    return tagTemplate.format(name=tname,code=tcode,attributes=tattributes)

def ITAG(tname,tcode,tattributes=""):
    return inlineTagTemplate.format(name=tname,code=tcode,attributes=tattributes)

def ATTR(tname,tval):
    return attributesTemplate.format(name=tname,value=tval)

def COMBINE(attrs):
    return " ".join(attrs)

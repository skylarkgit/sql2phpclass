archonAPIcallTemplate   =   'archonAPI.call({type},{fname},{args}).then(function(response){{{code}}});'
callendTemplate         =   '{fname}({args});\n'
callTemplate            =   '{fname}({args})'
controllerTemplate      =   'controller("{name}",{name});function {name}({dependencies}){{\n{code}\n}}\n'
controllerNameTemplate  =   '{func}{table}Controller'
fetchServiceTemplate    =   'FetchService.get("{name}").then(function(response){{\n{code}\n}})'
functionTemplate        =   'function({args}){{\n{code}\n}}\n'
objTemplate             =   '{parent}.{obj}'
onFailureTemplate       =   'toastr.error({message},"Error");\n'
onSuccessTemplate       =   'toastr.success({message},"Success");\n'
postSubmissionTemplate  =   'if(response.data.status=="OK") {{{success}}}\nelse {{{failure}}}'
scopeTemplate           =   '$scope.{obj}'
statementTemplate       =   '{statement};\n'
submissionTemplate      =   '$scope.submission=function(){{\nvar args={code};\narchonAPI.call({type},{fname},args).then(function(response){{{todo}}});\n}}\n'
validityTemplate        =   'checkValidity=function(){{\nreturn {toCheck}.$invalid;\n}}\n'
switchTemplate          =   'switch({expression}){{{code}}}'
caseTemplate            =   'case {case}: {code} break;'
parserTemplates={
'date':
'$filter("date")({var}, "yyyy-MM-dd")',
'default':'{var}'
}

def SWITCH(expression,code):
    return switchTemplate.format(expression=expression,code=code)

def CASE(case,code):
    return caseTemplate.format(case=case,code=code)

def PARSER(type,var):
    if type in parserTemplates:
        return parserTemplates[type].format(var=var)
    else:
        return parserTemplates['default'].format(var=var)

def ARCHONCALL(type,fname,args,code):
    return archonAPIcallTemplate.format(type=type,fname=fname,args=args,code=code)

def CONTROLLERNAME(func,table):
    return controllerNameTemplate.format(func=func,table=table)

def CALLEND(fname,args):
    return callendTemplate.format(fname=fname,args=args)

def CALL(fname,args):
    return callTemplate.format(fname=fname,args=args)

def CONTROLLER(name,dependencies,code):
    return controllerTemplate.format(name=name,dependencies=dependencies,code=code)

def FETCHSERVICE(name,code):
    return fetchServiceTemplate.format(name=name,code=code)

def FUNCTION(pArgs,pCode):
    return functionTemplate.format(args=pArgs,code=pCode)

def OBJ(pParent,pObj):
    return objTemplate.format(parent=pParent,obj=pObj)

def ONFAILURE(message):
    return onFailureTemplate.format(message=message)

def ONSUCCESS(message):
    return onSuccessTemplate.format(message=message)

def POSTSUBMISSION(onSuccess,onFailure):
    return postSubmissionTemplate.format(success=onSuccess,failure=onFailure)
#def (p):
#    return .format(=p)

def SCOPE(pObj):
    return scopeTemplate.format(obj=pObj)

def STATEMENT(pStatement):
    return statementTemplate.format(statement=pStatement)

def SUBMISSION(type,objFormation,fname,pTodo):
    return submissionTemplate.format(type=type,code=objFormation,fname=fname,todo=pTodo)

def VALIDITY(pToCheck):
    return validityTemplate.format(toCheck=pToCheck)

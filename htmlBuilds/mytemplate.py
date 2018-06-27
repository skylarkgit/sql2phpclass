inputTemplates={
'string':
'<md-input-container class="md-block" flex-gt-sm>\
    <label>{label}</label>\
    <input name="{name}" ng-model="{model}" id="{id}" {extensions}/>\
      <div ng-messages="{form}.{name}.$touched && {form}.{name}.$error">\
        <div ng-messages-include="validationMessages.html"></div>\
      </div>\
</md-input-container>',
'date':
'<md-input-container class="md-block" flex-gt-sm>\
    <label>{label}</label>\
    <md-datepicker name="{name}" ng-model="{model}" id="{id}" {extensions}></md-datepicker>\
      <div ng-messages="{form}.{name}.$touched && {form}.{name}.$error">\
        <div ng-messages-include="validationMessages.html"></div>\
      </div>\
</md-input-container>',
'number':
'<md-input-container class="md-block" flex-gt-sm>\
    <label>{label}</label>\
    <input type="number" name="{name}" ng-model="{model}" id="{id}" {extensions}/>\
      <div ng-messages="{form}.{name}.$touched && {form}.{name}.$error">\
        <div ng-messages-include="validationMessages.html"></div>\
      </div>\
</md-input-container>',
'float':
'<md-input-container class="md-block" flex-gt-sm>\
    <label>{label}</label>\
    <input type="number" name="{name}" ng-model="{model}" id="{id}"/>\
      <div ng-messages="{form}.{name}.$touched && {form}.{name}.$error">\
        <div ng-messages-include="validationMessages.html"></div>\
      </div>\
</md-input-container>',
'percent':
'<md-input-container class="md-block" flex-gt-sm>\
    <label>{label}</label>\
    <input type="number" name="{name}" ng-model="{model}" id="{id}" ng-pattern="/^[0-9]{{2}}+(\.[0-9]{{1,2}})?$/" step="0.01" {extensions}/>\
      <div ng-messages="{form}.{name}.$touched && {form}.{name}.$error">\
        <div ng-messages-include="validationMessages.html"></div>\
      </div>\
</md-input-container>',
'phone':
'<md-input-container class="md-block" flex-gt-sm>\
    <label>{label}</label>\
    <input name="{name}" ng-model="{model}" id="{id}" ng-pattern="/^[0-9]{{10}}$/" {extensions}/>\
    <div class="hint">10 digits</div>\
      <div ng-messages="{form}.{name}.$touched && {form}.{name}.$error">\
        <div ng-messages-include="validationMessages.html"></div>\
      </div>\
</md-input-container>',
'aadhar':
'<md-input-container class="md-block" flex-gt-sm>\
    <label>{label}</label>\
    <input name="{name}" ng-model="{model}" id="{id}" ng-pattern="/^[0-9]{{12}}$/" {extensions}/>\
    <div class="hint">12 digits</div>\
      <div ng-messages="{form}.{name}.$touched && {form}.{name}.$error">\
        <div ng-messages-include="validationMessages.html"></div>\
      </div>\
</md-input-container>',
'email':
'<md-input-container class="md-block" flex-gt-sm>\
    <label>{label}</label>\
    <input type="email" name="{name}" ng-model="{model}" id="{id}" {extensions}/>\
      <div ng-messages="{form}.{name}.$touched && {form}.{name}.$error">\
        <div ng-messages-include="validationMessages.html"></div>\
      </div>\
</md-input-container>',
'discountType':
'<md-input-container layout="row" class="md-block" flex-gt-sm>\
    <md-radio-group name="{name}" ng-model="{model}">\
        <md-radio-button value="P" class="md-primary">Percent</md-radio-button>\
        <md-radio-button value="A">Amount</md-radio-button>\
    </md-radio-group>\
</md-input-container>',
'profileType':
'<md-input-container layout="row" class="md-block" flex-gt-sm>\
    <md-radio-group name="{name}" ng-model="{model}">\
        <md-radio-button value="D" class="md-primary">Doctor</md-radio-button>\
        <md-radio-button value="E">Employee</md-radio-button>\
    </md-radio-group>\
</md-input-container>',
'exchangeType':
'<md-input-container class="md-block" flex-gt-sm>\
    <md-radio-group name="{name}" layout="row" ng-model="{model}">\
        <md-radio-button value="C" class="md-primary">Credit</md-radio-button>\
        <md-radio-button value="D">Debit</md-radio-button>\
    </md-radio-group>\
</md-input-container>',
'transactionType':
'<md-input-container class="md-block" flex-gt-sm>\
    <md-radio-group name="{name}" layout="row" ng-model="{model}">\
        <md-radio-button value="C" class="md-primary">Credit</md-radio-button>\
        <md-radio-button value="D">Debit</md-radio-button>\
    </md-radio-group>\
</md-input-container>',
'genderType':
'<md-input-container class="md-block" flex-gt-sm>\
    <md-radio-group name="{name}" layout="row" ng-model="{model}">\
        <md-radio-button value="F" class="md-primary">Female</md-radio-button>\
        <md-radio-button value="M">Male</md-radio-button>\
        <md-radio-button value="O">Other</md-radio-button>\
    </md-radio-group>\
</md-input-container>',
'bloodGroupType':
'<md-input-container>\
    <label>Blood Group</label>\
    <md-select name="{name}" ng-model="{model}">\
        <md-option value="Ap">A+</md-option>\
        <md-option value="Bp">B+</md-option>\
        <md-option value="An">A-</md-option>\
        <md-option value="Bn">B-</md-option>\
        <md-option value="ABp">AB+</md-option>\
        <md-option value="ABn">AB-</md-option>\
        <md-option value="Op">O+</md-option>\
        <md-option value="On">O-</md-option>\
    </md-select>\
</md-input-container>',
'foreign':
'<md-input-container layout="row">\
    <label>{label}</label>\
    <md-select ng-model="{model}" md-on-close="clearSearchTerm(\'search{model}\')" data-md-container-class="selectdemoSelectHeader" required>\
        <md-select-header class="demo-select-header">\
            <input ng-model="searchTerm{model}" type="search" placeholder="Search for a {name}.." class="demo-header-searchbox md-text">\
        </md-select-header>\
        <md-optgroup label="{label}">\
            <md-option value="{{{{{model}Var.{model}}}}}" ng-repeat="{model}Var in {model}Select | filter:searchTerm{model}">{{{{{model}Var.{model}}}}}</md-option>\
        </md-optgroup>\
    </md-select>\
    <md-button title="Add some" aria-label="{label}" class="md-icon-button launch md-primary md-raised" ng-click="ToolBag.showAdvanced(\'htmlTemplates\\add{reference}.html.tpl\')">\
        <md-icon md-font-icon="fa fa-plus-circle"></md-icon>\
    </md-button>\
</md-input-container>',
'submit':
'<div>\
    <md-button ng-disabled="{form}.$invalid" type="submit" class="md-raised md-primary">Submit</md-button>\
</div>',
'default':
'<md-input-container>\
    <label>{label}</label>\
    \
</md-input-container>'
}

sectionTemplate         =   '<section class="archonSection">\n<md-subheader>{heading}</md-subheader>\n{code}</section>\n'
contentTemplate         =   '<md-content>{code}</md-content>'
headingTemplate         =   '<div class="archonHeading">{heading}</div>'

def HEADING(heading,code):
    if code=='':
        return code
    return headingTemplate.format(heading=heading.title())+CONTENT(code)

def SECTION(heading,code):
    if code=='':
        return code
    return sectionTemplate.format(heading=heading.title(),code=code)

def CONTENT(code,theme="altTheme"):
    if code=='':
        return code
    return contentTemplate.format(code=code,theme=theme)

def SUBMIT(func,tableSurface):
    tableName=tableSurface.alias
    return inputTemplates['submit'].format(form=func+tableName+"Form")

formBodyTemplate=\
'<form ng-submit="{submit}" name="{form}" method="{method}" ng-controller="{controller}" class="archonFormBody">\
{code}\
</form>'
onsubmit="submission()"
def getInputCode(tableSurface,column,type=None):
    if type==None:
        type=column.validType
    tableName=tableSurface.name
    if type not in inputTemplates:
        type='default'
    #print(tableName+" "+column.alias+" "+type)
    return inputTemplates[type].format(model=column.alias,controller=tableName+"Controller",label=column.alias.title(),form=tableName+"Form",id=tableName+column.alias+'ID',name=tableName+column.alias,extensions='required')

def getFormBodyCode(tableSurface,filler,func='add',tmethod="POST"):
    tableName=tableSurface.name
    return formBodyTemplate.format(form=func+tableName+"Form",controller=func+tableName+"Controller",method=tmethod,submit=onsubmit,code=filler)

def getForeignAdd(tableSurface,column,referenceTable):
    tableName=tableSurface.name
    return inputTemplates['foreign'].format(model=column.alias,controller="add"+tableName+"Controller",label=column.alias.title(),form=tableName+"Form",id=tableName+column.alias+'ID',name=tableName+column.alias,extensions='',reference=referenceTable.alias)

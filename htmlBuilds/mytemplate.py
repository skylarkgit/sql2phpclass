inputTemplates={
'string':
'<md-input-container class="md-block" flex-gt-sm>\
    <label>{label}</label>\
    <input name="{name}" ng-model="{controller}.{model}" id="{id}" {extensions}/>\
      <div ng-messages="{form}.{name}.$touched && {form}.{name}.$error">\
        <div ng-messages-include="validationMessages.html"></div>\
      </div>\
</md-input-container>',
'date':
'<md-input-container class="md-block" flex-gt-sm>\
    <label>{label}</label>\
    <md-datepicker name="{name}" ng-model="{controller}.{model}" id="{id}" {extensions}></md-datepicker>\
      <div ng-messages="{form}.{name}.$touched && {form}.{name}.$error">\
        <div ng-messages-include="validationMessages.html"></div>\
      </div>\
</md-input-container>',
'number':
'<md-input-container class="md-block" flex-gt-sm>\
    <label>{label}</label>\
    <input type="number" name="{name}" ng-model="{controller}.{model}" id="{id}" {extensions}/>\
      <div ng-messages="{form}.{name}.$touched && {form}.{name}.$error">\
        <div ng-messages-include="validationMessages.html"></div>\
      </div>\
</md-input-container>',
'float':
'<md-input-container class="md-block" flex-gt-sm>\
    <label>{label}</label>\
    <input type="number" name="{name}" ng-model="{controller}.{model}" id="{id}"/>\
      <div ng-messages="{form}.{name}.$touched && {form}.{name}.$error">\
        <div ng-messages-include="validationMessages.html"></div>\
      </div>\
</md-input-container>',
'percent':
'<md-input-container class="md-block" flex-gt-sm>\
    <label>{label}</label>\
    <input type="number" name="{name}" ng-model="{controller}.{model}" id="{id}" ng-pattern="/^[0-9]{{2}}+(\.[0-9]{{1,2}})?$/" step="0.01" {extensions}/>\
      <div ng-messages="{form}.{name}.$touched && {form}.{name}.$error">\
        <div ng-messages-include="validationMessages.html"></div>\
      </div>\
</md-input-container>',
'phone':
'<md-input-container class="md-block" flex-gt-sm>\
    <label>{label}</label>\
    <input name="{name}" ng-model="{controller}.{model}" id="{id}" ng-pattern="/^[0-9]{{10}}$/" {extensions}/>\
    <div class="hint">(+91) ##-##-######</div>\
      <div ng-messages="{form}.{name}.$touched && {form}.{name}.$error">\
        <div ng-messages-include="validationMessages.html"></div>\
      </div>\
</md-input-container>',
'email':
'<md-input-container class="md-block" flex-gt-sm>\
    <label>{label}</label>\
    <input type="email" name="{name}" ng-model="{controller}.{model}" id="{id}" {extensions}/>\
      <div ng-messages="{form}.{name}.$touched && {form}.{name}.$error">\
        <div ng-messages-include="validationMessages.html"></div>\
      </div>\
</md-input-container>',
'discountType':
'<md-input-container layout="row" class="md-block" flex-gt-sm>\
    <md-radio-group name={name} ng-model="{controller}.{model}">\
        <md-radio-button value="P" class="md-primary">Percent</md-radio-button>\
        <md-radio-button value="A">Amount</md-radio-button>\
    </md-radio-group>\
</md-input-container>',
'exchangeType':
'<md-input-container class="md-block" flex-gt-sm>\
    <md-radio-group name={name} layout="row" ng-model="{controller}.{model}">\
        <md-radio-button value="C" class="md-primary">Credit</md-radio-button>\
        <md-radio-button value="D">Debit</md-radio-button>\
    </md-radio-group>\
</md-input-container>',
'transactionType':
'<md-input-container class="md-block" flex-gt-sm>\
    <md-radio-group name={name} layout="row" ng-model="{controller}.{model}">\
        <md-radio-button value="C" class="md-primary">Credit</md-radio-button>\
        <md-radio-button value="D">Debit</md-radio-button>\
    </md-radio-group>\
</md-input-container>',
'genderType':
'<md-input-container class="md-block" flex-gt-sm>\
    <md-radio-group name={name} layout="row" ng-model="{controller}.{model}">\
        <md-radio-button value="F" class="md-primary">Female</md-radio-button>\
        <md-radio-button value="M">Male</md-radio-button>\
        <md-radio-button value="O">Other</md-radio-button>\
    </md-radio-group>\
</md-input-container>',
'bloodGroupType':
'<md-input-container>\
    <label>Blood Group</label>\
    <md-select name={name} ng-model="{controller}.{model}">\
        <md-option ng-repeat="blood in {controller}.{model}Data" ng-value="blood">\
            {{blood}}\
        </md-option>\
    </md-select>\
</md-input-container>',
'foreign':
'<md-input-container layout="row">\
    <label>{label}</label>\
    <md-select ng-model="{model}" md-on-close="clearSearchTerm(\'search{model}\')" data-md-container-class="selectdemoSelectHeader">\
        <md-select-header class="demo-select-header">\
            <input ng-model="searchTerm{model}" type="search" placeholder="Search for a {name}.." class="demo-header-searchbox md-text">\
        </md-select-header>\
        <md-optgroup label="{label}">\
            <md-option ng-value="{model}Var.val" ng-repeat="{model}Var in {model}Select | filter:searchTerm{model}">{model}Var.display</md-option>\
        </md-optgroup>\
    </md-select>\
    <md-button title="Add some" aria-label="{label}" class="md-icon-button launch md-primary md-raised" ng-click="showAdvanced("htmlTemplates\add{reference}.htmp.tpl")">\
        <md-icon md-font-icon="fa fa-plus-circle"></md-icon>\
    </md-button>\
</md-input-container>',
'default':
'<md-input-container>\
    <label>{label}</label>\
    \
</md-input-container>'
}
formBodyTemplate=\
'<form ng-submit="{submit}" name="{form}" method="{method}" ng-controller="{controller}">\
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
    return inputTemplates[type].format(model=column.alias,controller=tableName+"Controller",label=column.alias.title(),form=tableName+"Form",id=tableName+column.alias+'ID',name=tableName+column.alias,extensions='')

def getFormBodyCode(tableSurface,filler,func='add',tmethod="POST"):
    tableName=tableSurface.name
    return formBodyTemplate.format(form=func+tableName+"Form",controller=tableName+"Controller",method=tmethod,submit=onsubmit,code=filler)

def getForeignAdd(tableSurface,column,referenceTable):
    tableName=tableSurface.name
    return inputTemplates['foreign'].format(model=column.alias,controller="add"+tableName+"Controller",label=column.alias.title(),form=tableName+"Form",id=tableName+column.alias+'ID',name=tableName+column.alias,extensions='',reference=referenceTable.alias)

HTMLadd={
'string':
'<div class="form-group col-md-6">\
    <label class="form-control-label" for="{id}">{label}</label>\
    <input type="text" class="form-control" name="{name}" id="{id}" ng-model="{model}" placeholder="" autocomplete="on" {extensions} required/>\
    <div class="help-block" ng-messages="{controller}.{model}.$touched && {controller}.{model}.$error">\
        <div ng-messages-include="validationMessages.html"></div>\
    </div>\
</div>',
'date':
'<div class="form-group col-md-6">\
    <label class="form-control-label" for="{id}">{label}</label>\
    <div class="input-group">\
        <span class="input-group-addon"><i class="icon wb-calendar" aria-hidden="true"></i></span>\
        <input type="date" class="form-control" name="{name}" id="{id}" ng-model="{model}" placeholder="" autocomplete="on"  {extensions} required/>\
    </div>\
    <div class="help-block" ng-messages="{controller}.{model}.$touched && {controller}.{model}.$error">\
        <div ng-messages-include="validationMessages.html"></div>\
    </div>\
</div>',
'number':
'<div class="form-group col-md-6">\
    <label class="form-control-label" for="{id}">{label}</label>\
    <input type="number" class="form-control" name="{name}" id="{id}" ng-model="{model}" ng-minLength="{minLength}" ng-maxLength="{maxLength}" placeholder="" autocomplete="on" {extensions} required/>\
    <div class="help-block" ng-messages="{controller}.{model}.$touched && {controller}.{model}.$error">\
        <div ng-messages-include="validationMessages.html"></div>\
    </div>\
</div>',
'phone':
'<div class="form-group col-md-6">\
    <label class="form-control-label" for="{id}">{label}</label>\
    <input type="number" class="form-control" name="{name}" id="{id}" ng-model="{model}" ng-minLength="{minLength}" ng-maxLength="{maxLength}" placeholder="" autocomplete="on" {extensions} required/>\
    <div class="help-block" ng-messages="{controller}.{model}.$touched && {controller}.{model}.$error">\
        <div ng-messages-include="validationMessages.html"></div>\
    </div>\
</div>',
'email':
'<div class="form-group col-md-6">\
    <label class="form-control-label" for="{id}">{label}</label>\
    <input type="email" class="form-control" name="{name}" id="{id}" ng-model="{model}" placeholder="" autocomplete="on"  {extensions} required/>\
    <div class="help-block" ng-messages="{controller}.{model}.$touched && {controller}.{model}.$error">\
        <div ng-messages-include="validationMessages.html"></div>\
    </div>\
</div>',
'date':
'<div class="form-group col-md-6">\
    <label class="form-control-label" for="{id}">{label}</label>\
    <input type="date" class="form-control date-input-style" name="{name}" id="{id}" ng-model="{model}" placeholder="" autocomplete="on"  {extensions} required/>\
    <div class="help-block" ng-messages="{controller}.{model}.$touched && {controller}.{model}.$error">\
        <div ng-messages-include="validationMessages.html"></div>\
    </div>\
</div>',
'default':
'<div class="form-group col-md-6">\
    <label class="form-control-label" for="{id}">{label}</label>\
    <input type="text" class="form-control" name="{name}" id="{id}" ng-model="{model}" placeholder="" autocomplete="on" {extensions} required/>\
    <div class="help-block" ng-messages="{controller}.{model}.$touched && {controller}.{model}.$error">\
        <div ng-messages-include="validationMessages.html"></div>\
    </div>\
</div>'
}

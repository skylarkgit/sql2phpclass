from htmlTemplate import *

HTMLadd={
'string':
'<div class="form-group col-md-6">\
    <label class="form-control-label" for="{id}">{label}</label>\
    <input type="text" class="form-control" name="{name}" id="{id}" ng-model="{model}" placeholder="" autocomplete="on" {} required/>\
    <div class="help-block" ng-messages="{controller}.{model}.$touched && {controller}.{model}.$error">\
        <div ng-messages-include="validationMessages.html"></div>\
    </div>\
</div>',
'number':
'<div class="form-group col-md-6">\
    <label class="form-control-label" for="{id}">{label}</label>\
    <div class="input-group">\
        <span class="input-group-addon"><i class="icon wb-calendar" aria-hidden="true"></i></span>\
        <input type="number" class="form-control" name="{name}" id="{id}" ng-model="{model}" placeholder="" autocomplete="on"  {} required/>\
    </div>\
    <div class="help-block" ng-messages="{controller}.{model}.$touched && {controller}.{model}.$error">\
        <div ng-messages-include="validationMessages.html"></div>\
    </div>\
</div>',
'date':
'<div class="form-group col-md-6">\
    <label class="form-control-label" for="{id}">{label}</label>\
    <input type="date" class="form-control date-input-style" name="{name}" id="{id}" ng-model="{model}" placeholder="" autocomplete="on"  {} required/>\
    <div class="help-block" ng-messages="{controller}.{model}.$touched && {controller}.{model}.$error">\
        <div ng-messages-include="validationMessages.html"></div>\
    </div>\
</div>',
'date':
'<div class="form-group col-md-6">\
    <label class="form-control-label" for="{id}">{label}</label>\
    <input type="date" class="form-control date-input-style" name="{name}" id="{id}" ng-model="{model}" placeholder="" autocomplete="on"  {} required/>\
    <div class="help-block" ng-messages="{controller}.{model}.$touched && {controller}.{model}.$error">\
        <div ng-messages-include="validationMessages.html"></div>\
    </div>\
</div>',
'date':
'<div class="form-group col-md-6">\
    <label class="form-control-label" for="{id}">{label}</label>\
    <input type="date" class="form-control date-input-style" name="{name}" id="{id}" ng-model="{model}" placeholder="" autocomplete="on"  {} required/>\
    <div class="help-block" ng-messages="{controller}.{model}.$touched && {controller}.{model}.$error">\
        <div ng-messages-include="validationMessages.html"></div>\
    </div>\
</div>',
'default':
'<div class="form-group col-md-6">\
    <label class="form-control-label" for="{id}">{label}</label>\
    <input type="text" class="form-control" name="{name}" id="{id}" ng-model="{model}" placeholder="" autocomplete="on" {} required/>\
    <div class="help-block" ng-messages="{controller}.{model}.$touched && {controller}.{model}.$error">\
        <div ng-messages-include="validationMessages.html"></div>\
    </div>\
</div>'
}

def getHTMLAdd(column):


<div class="form-group col-md-8">
    <input type="text" class="form-control" name="doctorName" placeholder="Name"
    autocomplete="off" ng-model='name' required/>
</div>
<div class="form-group  col-md-8">
    <div class="radio-custom radio-default radio-inline">
        <input value="M" type="radio" id="inputDoctorMale" name="inputRadioGender" ng-model='sex' required/>
        <label for="inputLabelMale">Male</label>
    </div>
    <div class="radio-custom radio-default radio-inline">
        <input value="F" type="radio" id="inputDoctorFemale" name="inputRadioGender" ng-model='sex' checked />
        <label for="inputLabelFemale">Female</label>
    </div>
</div>
<div class="form-group  col-md-8">
    <!--label class="form-control-label" for="doctorEmail">UsernameEmail</label-->
    <input type="email" class="form-control" id="doctorEmail" name="doctorEmail"
    placeholder="Email" autocomplete="off" ng-model='email' required/>
</div>
<div class="col-md-6">
    <!-- Example Default Datepicker -->
    <div class="example-wrap">
        <div class="example">
            <div class="input-group">
                <span class="input-group-addon">Date Of Birth <i class="icon wb-calendar" aria-hidden="true"></i>
                </span>
                <input type="date" class="form-control date-input-style" name="doctorDoB" placeholder="Date of Birth" ng-model='dob' required>
            </div>
        </div>
    </div>
    <!-- End Example Default Datepicker -->
</div>
<div class="col-md-6">
    <!-- Example Default Datepicker -->
    <div class="example-wrap">
        <div class="example">
            <div class="input-group">
                <span class="input-group-addon">
                Since
                    <i class="icon wb-calendar" aria-hidden="true"></i>
                </span>
                <input type="date" class="form-control date-input-style" name="doctorExp" placeholder="Practicing Since" ng-model='experience' required>
            </div>
        </div>
    </div>
    <!-- End Example Default Datepicker -->
</div>
<div class="form-group col-md-6">
    <div class="input-group">
        <span class="input-group-addon">Salary ₹</span>
        <input type="number" class="form-control" placeholder="Salary" ng-model='salary' required>
    </div>
</div>
<div class="form-group col-md-6">
    <div class="input-group">
        <span class="input-group-addon">Fees ₹</span>
        <input type="number" class="form-control" placeholder="Fees" ng-model='fees' required>
    </div>
</div>
<div class="form-group  col-md-8">
    <!--label class="form-control-label" for="doctorEmail">UsernameEmail</label-->
    <div class="input-group">
        <span class="input-group-addon">+91</span>
        <input type="number" ng-minlength="10" ng-maxlength="10" class="form-control" id="doctorContact" name="doctorContact"
        placeholder="Contact" autocomplete="off" ng-model="contact" required/>
    </div>
</div>
<div class="form-group  col-md-8">
    <div class="input-group">
        <!--label class="form-control-label" for="doctorEmail">UsernameEmail</label-->
        <span class="input-group-addon">+91</span>
        <input type="number" ng-minlength="10" ng-maxlength="10" class="form-control" id="doctorContact1" name="doctorContact1"
        placeholder="Contact 2" autocomplete="off" ng-model="contact1" required/>
    </div>
</div>
<div class="form-group col-md-8">
    <!--label class="form-control-label" for="doctorPassword">Password</label-->
    <input type="password" class="form-control" id="doctorPassword" name="doctorPassword"
    placeholder="Password" autocomplete="off" ng-model="password" required/>
</div>

<div class="form-group col-md-8">
    <!--label class="form-control-label" for="doctorConfirmPassword">Confirm Password</label-->
    <input type="password" class="form-control" id="doctorConfirmPassword" name="doctorConfirmPassword"
    placeholder="Confirm Password" autocomplete="off" ng-model="confirmPassword" required/>
    <span style="color:red" ng-show="addDoctor.doctorConfirmPassword.$touched && confirmPassword!=password">Passwords Doesn't Match</span>
</div>
<div class="form-group col-md-12">
    <textarea class="form-control" name="doctorAddress" placeholder="Address" ng-model="address" required></textarea>
</div>
<div class="form-group col-md-4">
    <select ng-init="cid='jp'" class="form-control" ng-model="cid" required>
        <option ng-repeat="city in cities" value="{{city.cid}}">{{city.name}}</option>
    </select>
</div>
<div class="form-group col-md-4">
    <select ng-init="spec='Srgn'" class="form-control" ng-model="spec" required>
        <option ng-repeat="specs in specializations" value="{{specs.code}}">{{specs.name}}</option>
    </select>
</div>
<div class="form-group  col-md-4">
    <input ng-disabled="addDoctor.$invalid" type="submit" class="btn btn-primary"></input>
</div>

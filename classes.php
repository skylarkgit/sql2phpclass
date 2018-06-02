<?php
class address implements dbconn{
	public $street;public $city;public $state;public $PIN;public $addrid;
	function __construct($pstreet,$pcity,$pstate,$pPIN){
		$this->street=$pstreet;$this->city=$pcity;$this->state=$pstate;$this->PIN=$pPIN;
	}
	function __construct(){
		$this->street=NULL;$this->city=NULL;$this->state=NULL;$this->PIN=NULL;$this->addrid=NULL;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO address (street,city,state,PIN) VALUES (:street,:city,:state,:PIN)');
		$stmt->bindParam(':street',$this->street);
		$stmt->bindParam(':city',$this->city);
		$stmt->bindParam(':state',$this->state);
		$stmt->bindParam(':PIN',$this->PIN);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'address : INSERT','ERROR');
		}
		$retObj=NULL;
		$this->addrid=$this->db->lastInsertId();
		$stmt=$this->db->prepare('SELECT addrid FROM address');
		$stmt->bindParam(':addrid',$this->addrid);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'address : SELECT AUTO','ERROR');
		}
		$retObj=$stmt->fetch(PDO::FETCH_OBJ);
		return new RESPONSE($retObj,'SUCCESS','OK');
	}
}

class bill implements dbconn{
	public $chartId;public $exchangeId;public $billId;
	function __construct($pchartId,$pexchangeId){
		$this->chartId=$pchartId;$this->exchangeId=$pexchangeId;
	}
	function __construct(){
		$this->chartId=NULL;$this->exchangeId=NULL;$this->billId=NULL;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO bill (chartId,exchangeId) VALUES (:chartId,:exchangeId)');
		$stmt->bindParam(':chartId',$this->chartId);
		$stmt->bindParam(':exchangeId',$this->exchangeId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'bill : INSERT','ERROR');
		}
		$retObj=NULL;
		$this->billId=$this->db->lastInsertId();
		$stmt=$this->db->prepare('SELECT billId FROM bill');
		$stmt->bindParam(':billId',$this->billId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'bill : SELECT AUTO','ERROR');
		}
		$retObj=$stmt->fetch(PDO::FETCH_OBJ);
		return new RESPONSE($retObj,'SUCCESS','OK');
	}
}

class categories implements dbconn{
	public $name;public $categoryId;
	function __construct($pname){
		$this->name=$pname;
	}
	function __construct(){
		$this->name=NULL;$this->categoryId=NULL;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO categories (name) VALUES (:name)');
		$stmt->bindParam(':name',$this->name);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'categories : INSERT','ERROR');
		}
		$retObj=NULL;
		$this->categoryId=$this->db->lastInsertId();
		$stmt=$this->db->prepare('SELECT categoryId FROM categories');
		$stmt->bindParam(':categoryId',$this->categoryId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'categories : SELECT AUTO','ERROR');
		}
		$retObj=$stmt->fetch(PDO::FETCH_OBJ);
		return new RESPONSE($retObj,'SUCCESS','OK');
	}
}

class charts implements dbconn{
	public $availId;public $sessionId;public $status;public $exchangeId;public $chartId;
	function __construct($pavailId,$psessionId,$pstatus,$pexchangeId){
		$this->availId=$pavailId;$this->sessionId=$psessionId;$this->status=$pstatus;$this->exchangeId=$pexchangeId;
	}
	function __construct(){
		$this->availId=NULL;$this->sessionId=NULL;$this->status=NULL;$this->exchangeId=NULL;$this->chartId=NULL;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO charts (availId,sessionId,status,exchangeId) VALUES (:availId,:sessionId,:status,:exchangeId)');
		$stmt->bindParam(':availId',$this->availId);
		$stmt->bindParam(':sessionId',$this->sessionId);
		$stmt->bindParam(':status',$this->status);
		$stmt->bindParam(':exchangeId',$this->exchangeId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'charts : INSERT','ERROR');
		}
		$retObj=NULL;
		$this->chartId=$this->db->lastInsertId();
		$stmt=$this->db->prepare('SELECT chartId FROM charts');
		$stmt->bindParam(':chartId',$this->chartId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'charts : SELECT AUTO','ERROR');
		}
		$retObj=$stmt->fetch(PDO::FETCH_OBJ);
		return new RESPONSE($retObj,'SUCCESS','OK');
	}
}

class contact implements dbconn{
	public $email;public $phone1;public $phone2;public $contactId;
	function __construct($pemail,$pphone1,$pphone2){
		$this->email=$pemail;$this->phone1=$pphone1;$this->phone2=$pphone2;
	}
	function __construct(){
		$this->email=NULL;$this->phone1=NULL;$this->phone2=NULL;$this->contactId=NULL;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO contact (email,phone1,phone2) VALUES (:email,:phone1,:phone2)');
		$stmt->bindParam(':email',$this->email);
		$stmt->bindParam(':phone1',$this->phone1);
		$stmt->bindParam(':phone2',$this->phone2);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'contact : INSERT','ERROR');
		}
		$retObj=NULL;
		$this->contactId=$this->db->lastInsertId();
		$stmt=$this->db->prepare('SELECT contactId FROM contact');
		$stmt->bindParam(':contactId',$this->contactId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'contact : SELECT AUTO','ERROR');
		}
		$retObj=$stmt->fetch(PDO::FETCH_OBJ);
		return new RESPONSE($retObj,'SUCCESS','OK');
	}
}

class doctors implements dbconn{
	public $userId;public $profileId;public $doctorId;
	function __construct($puserId,$pprofileId){
		$this->userId=$puserId;$this->profileId=$pprofileId;
	}
	function __construct(){
		$this->userId=NULL;$this->profileId=NULL;$this->doctorId=NULL;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO doctors (userId,profileId) VALUES (:userId,:profileId)');
		$stmt->bindParam(':userId',$this->userId);
		$stmt->bindParam(':profileId',$this->profileId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'doctors : INSERT','ERROR');
		}
		$retObj=NULL;
		$this->doctorId=$this->db->lastInsertId();
		$stmt=$this->db->prepare('SELECT doctorId FROM doctors');
		$stmt->bindParam(':doctorId',$this->doctorId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'doctors : SELECT AUTO','ERROR');
		}
		$retObj=$stmt->fetch(PDO::FETCH_OBJ);
		return new RESPONSE($retObj,'SUCCESS','OK');
	}
}

class employees implements dbconn{
	public $userId;public $profileId;public $empId;
	function __construct($puserId,$pprofileId){
		$this->userId=$puserId;$this->profileId=$pprofileId;
	}
	function __construct(){
		$this->userId=NULL;$this->profileId=NULL;$this->empId=NULL;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO employees (userId,profileId) VALUES (:userId,:profileId)');
		$stmt->bindParam(':userId',$this->userId);
		$stmt->bindParam(':profileId',$this->profileId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'employees : INSERT','ERROR');
		}
		$retObj=NULL;
		$this->empId=$this->db->lastInsertId();
		$stmt=$this->db->prepare('SELECT empId FROM employees');
		$stmt->bindParam(':empId',$this->empId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'employees : SELECT AUTO','ERROR');
		}
		$retObj=$stmt->fetch(PDO::FETCH_OBJ);
		return new RESPONSE($retObj,'SUCCESS','OK');
	}
}

class exchange implements dbconn{
	public $type;public $amount;public $discount;public $discountType;public $exchangeId;public $net;
	function __construct($ptype,$pamount,$pdiscount,$pdiscountType,$pnet){
		$this->type=$ptype;$this->amount=$pamount;$this->discount=$pdiscount;$this->discountType=$pdiscountType;$this->net=$pnet;
	}
	function __construct(){
		$this->type=NULL;$this->amount=NULL;$this->discount=NULL;$this->discountType=NULL;$this->exchangeId=NULL;$this->net=NULL;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO exchange (type,amount,discount,discountType,net) VALUES (:type,:amount,:discount,:discountType,:net)');
		$stmt->bindParam(':type',$this->type);
		$stmt->bindParam(':amount',$this->amount);
		$stmt->bindParam(':discount',$this->discount);
		$stmt->bindParam(':discountType',$this->discountType);
		$stmt->bindParam(':net',$this->net);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'exchange : INSERT','ERROR');
		}
		$retObj=NULL;
		$this->exchangeId=$this->db->lastInsertId();
		$stmt=$this->db->prepare('SELECT exchangeId FROM exchange');
		$stmt->bindParam(':exchangeId',$this->exchangeId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'exchange : SELECT AUTO','ERROR');
		}
		$retObj=$stmt->fetch(PDO::FETCH_OBJ);
		return new RESPONSE($retObj,'SUCCESS','OK');
	}
}

class expenditures implements dbconn{
	public $expenseId;public $exchangeId;public $expenditureId;
	function __construct($pexpenseId,$pexchangeId){
		$this->expenseId=$pexpenseId;$this->exchangeId=$pexchangeId;
	}
	function __construct(){
		$this->expenseId=NULL;$this->exchangeId=NULL;$this->expenditureId=NULL;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO expenditures (expenseId,exchangeId) VALUES (:expenseId,:exchangeId)');
		$stmt->bindParam(':expenseId',$this->expenseId);
		$stmt->bindParam(':exchangeId',$this->exchangeId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'expenditures : INSERT','ERROR');
		}
		$retObj=NULL;
		$this->expenditureId=$this->db->lastInsertId();
		$stmt=$this->db->prepare('SELECT expenditureId FROM expenditures');
		$stmt->bindParam(':expenditureId',$this->expenditureId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'expenditures : SELECT AUTO','ERROR');
		}
		$retObj=$stmt->fetch(PDO::FETCH_OBJ);
		return new RESPONSE($retObj,'SUCCESS','OK');
	}
}

class expenses implements dbconn{
	public $name;public $cost;public $expenseId;
	function __construct($pname,$pcost){
		$this->name=$pname;$this->cost=$pcost;
	}
	function __construct(){
		$this->name=NULL;$this->cost=NULL;$this->expenseId=NULL;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO expenses (name,cost) VALUES (:name,:cost)');
		$stmt->bindParam(':name',$this->name);
		$stmt->bindParam(':cost',$this->cost);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'expenses : INSERT','ERROR');
		}
		$retObj=NULL;
		$this->expenseId=$this->db->lastInsertId();
		$stmt=$this->db->prepare('SELECT expenseId FROM expenses');
		$stmt->bindParam(':expenseId',$this->expenseId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'expenses : SELECT AUTO','ERROR');
		}
		$retObj=$stmt->fetch(PDO::FETCH_OBJ);
		return new RESPONSE($retObj,'SUCCESS','OK');
	}
}

class groups implements dbconn{
	public $groupName;public $groupId;
	function __construct($pgroupName){
		$this->groupName=$pgroupName;
	}
	function __construct(){
		$this->groupName=NULL;$this->groupId=NULL;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO groups (groupName) VALUES (:groupName)');
		$stmt->bindParam(':groupName',$this->groupName);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'groups : INSERT','ERROR');
		}
		$retObj=NULL;
		$this->groupId=$this->db->lastInsertId();
		$stmt=$this->db->prepare('SELECT groupId FROM groups');
		$stmt->bindParam(':groupId',$this->groupId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'groups : SELECT AUTO','ERROR');
		}
		$retObj=$stmt->fetch(PDO::FETCH_OBJ);
		return new RESPONSE($retObj,'SUCCESS','OK');
	}
}

class lab implements dbconn{
	public $serviceId;public $paramId;public $cost;public $labId;
	function __construct($pserviceId,$pparamId,$pcost){
		$this->serviceId=$pserviceId;$this->paramId=$pparamId;$this->cost=$pcost;
	}
	function __construct(){
		$this->serviceId=NULL;$this->paramId=NULL;$this->cost=NULL;$this->labId=NULL;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO lab (serviceId,paramId,cost) VALUES (:serviceId,:paramId,:cost)');
		$stmt->bindParam(':serviceId',$this->serviceId);
		$stmt->bindParam(':paramId',$this->paramId);
		$stmt->bindParam(':cost',$this->cost);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'lab : INSERT','ERROR');
		}
		$retObj=NULL;
		$this->labId=$this->db->lastInsertId();
		$stmt=$this->db->prepare('SELECT labId FROM lab');
		$stmt->bindParam(':labId',$this->labId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'lab : SELECT AUTO','ERROR');
		}
		$retObj=$stmt->fetch(PDO::FETCH_OBJ);
		return new RESPONSE($retObj,'SUCCESS','OK');
	}
}

class params implements dbconn{
	public $paramId;public $paramString;
	function __construct($pparamString){
		$this->paramString=$pparamString;
	}
	function __construct(){
		$this->paramId=NULL;$this->paramString=NULL;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO params (paramString) VALUES (:paramString)');
		$stmt->bindParam(':paramString',$this->paramString);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'params : INSERT','ERROR');
		}
		$retObj=NULL;
		$this->paramId=$this->db->lastInsertId();
		$stmt=$this->db->prepare('SELECT paramId FROM params');
		$stmt->bindParam(':paramId',$this->paramId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'params : SELECT AUTO','ERROR');
		}
		$retObj=$stmt->fetch(PDO::FETCH_OBJ);
		return new RESPONSE($retObj,'SUCCESS','OK');
	}
}

class patientgroups implements dbconn{
	public $groupId;public $patientId;
	function __construct($pgroupId,$ppatientId){
		$this->groupId=$pgroupId;$this->patientId=$ppatientId;
	}
	function __construct(){
		$this->groupId=NULL;$this->patientId=NULL;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO patientgroups (groupId,patientId) VALUES (:groupId,:patientId)');
		$stmt->bindParam(':groupId',$this->groupId);
		$stmt->bindParam(':patientId',$this->patientId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'patientgroups : INSERT','ERROR');
		}
		$retObj=NULL;
		return new RESPONSE($retObj,'SUCCESS','OK');
	}
}

class patients implements dbconn{
	public $userId;public $patientId;
	function __construct($puserId){
		$this->userId=$puserId;
	}
	function __construct(){
		$this->userId=NULL;$this->patientId=NULL;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO patients (userId) VALUES (:userId)');
		$stmt->bindParam(':userId',$this->userId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'patients : INSERT','ERROR');
		}
		$retObj=NULL;
		$this->patientId=$this->db->lastInsertId();
		$stmt=$this->db->prepare('SELECT patientId FROM patients');
		$stmt->bindParam(':patientId',$this->patientId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'patients : SELECT AUTO','ERROR');
		}
		$retObj=$stmt->fetch(PDO::FETCH_OBJ);
		return new RESPONSE($retObj,'SUCCESS','OK');
	}
}

class personalinfo implements dbconn{
	public $name;public $gender;public $bloodGroup;public $dob;public $aadhar;public $infoId;
	function __construct($pname,$pgender,$pbloodGroup,$pdob,$paadhar){
		$this->name=$pname;$this->gender=$pgender;$this->bloodGroup=$pbloodGroup;$this->dob=$pdob;$this->aadhar=$paadhar;
	}
	function __construct(){
		$this->name=NULL;$this->gender=NULL;$this->bloodGroup=NULL;$this->dob=NULL;$this->aadhar=NULL;$this->infoId=NULL;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO personalinfo (name,gender,bloodGroup,dob,aadhar) VALUES (:name,:gender,:bloodGroup,:dob,:aadhar)');
		$stmt->bindParam(':name',$this->name);
		$stmt->bindParam(':gender',$this->gender);
		$stmt->bindParam(':bloodGroup',$this->bloodGroup);
		$stmt->bindParam(':dob',$this->dob);
		$stmt->bindParam(':aadhar',$this->aadhar);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'personalinfo : INSERT','ERROR');
		}
		$retObj=NULL;
		$this->infoId=$this->db->lastInsertId();
		$stmt=$this->db->prepare('SELECT infoId FROM personalinfo');
		$stmt->bindParam(':infoId',$this->infoId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'personalinfo : SELECT AUTO','ERROR');
		}
		$retObj=$stmt->fetch(PDO::FETCH_OBJ);
		return new RESPONSE($retObj,'SUCCESS','OK');
	}
}

class profiles implements dbconn{
	public $type;public $name;public $description;public $profileId;
	function __construct($ptype,$pname,$pdescription){
		$this->type=$ptype;$this->name=$pname;$this->description=$pdescription;
	}
	function __construct(){
		$this->type=NULL;$this->name=NULL;$this->description=NULL;$this->profileId=NULL;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO profiles (type,name,description) VALUES (:type,:name,:description)');
		$stmt->bindParam(':type',$this->type);
		$stmt->bindParam(':name',$this->name);
		$stmt->bindParam(':description',$this->description);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'profiles : INSERT','ERROR');
		}
		$retObj=NULL;
		$this->profileId=$this->db->lastInsertId();
		$stmt=$this->db->prepare('SELECT profileId FROM profiles');
		$stmt->bindParam(':profileId',$this->profileId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'profiles : SELECT AUTO','ERROR');
		}
		$retObj=$stmt->fetch(PDO::FETCH_OBJ);
		return new RESPONSE($retObj,'SUCCESS','OK');
	}
}

class service implements dbconn{
	public $name;public $cost;public $description;public $categoryId;public $serviceId;
	function __construct($pname,$pcost,$pdescription,$pcategoryId){
		$this->name=$pname;$this->cost=$pcost;$this->description=$pdescription;$this->categoryId=$pcategoryId;
	}
	function __construct(){
		$this->name=NULL;$this->cost=NULL;$this->description=NULL;$this->categoryId=NULL;$this->serviceId=NULL;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO service (name,cost,description,categoryId) VALUES (:name,:cost,:description,:categoryId)');
		$stmt->bindParam(':name',$this->name);
		$stmt->bindParam(':cost',$this->cost);
		$stmt->bindParam(':description',$this->description);
		$stmt->bindParam(':categoryId',$this->categoryId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'service : INSERT','ERROR');
		}
		$retObj=NULL;
		$this->serviceId=$this->db->lastInsertId();
		$stmt=$this->db->prepare('SELECT serviceId FROM service');
		$stmt->bindParam(':serviceId',$this->serviceId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'service : SELECT AUTO','ERROR');
		}
		$retObj=$stmt->fetch(PDO::FETCH_OBJ);
		return new RESPONSE($retObj,'SUCCESS','OK');
	}
}

class serviceavailed implements dbconn{
	public $patientId;public $serviceId;public $exchangeId;public $taxId;public $availId;
	function __construct($ppatientId,$pserviceId,$pexchangeId,$ptaxId){
		$this->patientId=$ppatientId;$this->serviceId=$pserviceId;$this->exchangeId=$pexchangeId;$this->taxId=$ptaxId;
	}
	function __construct(){
		$this->patientId=NULL;$this->serviceId=NULL;$this->exchangeId=NULL;$this->taxId=NULL;$this->availId=NULL;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO serviceavailed (patientId,serviceId,exchangeId,taxId) VALUES (:patientId,:serviceId,:exchangeId,:taxId)');
		$stmt->bindParam(':patientId',$this->patientId);
		$stmt->bindParam(':serviceId',$this->serviceId);
		$stmt->bindParam(':exchangeId',$this->exchangeId);
		$stmt->bindParam(':taxId',$this->taxId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'serviceavailed : INSERT','ERROR');
		}
		$retObj=NULL;
		$this->availId=$this->db->lastInsertId();
		$stmt=$this->db->prepare('SELECT availId FROM serviceavailed');
		$stmt->bindParam(':availId',$this->availId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'serviceavailed : SELECT AUTO','ERROR');
		}
		$retObj=$stmt->fetch(PDO::FETCH_OBJ);
		return new RESPONSE($retObj,'SUCCESS','OK');
	}
}

class servicecategories implements dbconn{
	public $name;public $categoryId;
	function __construct($pname){
		$this->name=$pname;
	}
	function __construct(){
		$this->name=NULL;$this->categoryId=NULL;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO servicecategories (name) VALUES (:name)');
		$stmt->bindParam(':name',$this->name);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'servicecategories : INSERT','ERROR');
		}
		$retObj=NULL;
		$this->categoryId=$this->db->lastInsertId();
		$stmt=$this->db->prepare('SELECT categoryId FROM servicecategories');
		$stmt->bindParam(':categoryId',$this->categoryId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'servicecategories : SELECT AUTO','ERROR');
		}
		$retObj=$stmt->fetch(PDO::FETCH_OBJ);
		return new RESPONSE($retObj,'SUCCESS','OK');
	}
}

class session implements dbconn{
	public $timeStamp;public $dateAndTime;public $duration;public $sessionId;
	function __construct($ptimeStamp,$pdateAndTime,$pduration){
		$this->timeStamp=$ptimeStamp;$this->dateAndTime=$pdateAndTime;$this->duration=$pduration;
	}
	function __construct(){
		$this->timeStamp=NULL;$this->dateAndTime=NULL;$this->duration=NULL;$this->sessionId=NULL;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO session (timeStamp,dateAndTime,duration) VALUES (:timeStamp,:dateAndTime,:duration)');
		$stmt->bindParam(':timeStamp',$this->timeStamp);
		$stmt->bindParam(':dateAndTime',$this->dateAndTime);
		$stmt->bindParam(':duration',$this->duration);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'session : INSERT','ERROR');
		}
		$retObj=NULL;
		$this->sessionId=$this->db->lastInsertId();
		$stmt=$this->db->prepare('SELECT sessionId FROM session');
		$stmt->bindParam(':sessionId',$this->sessionId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'session : SELECT AUTO','ERROR');
		}
		$retObj=$stmt->fetch(PDO::FETCH_OBJ);
		return new RESPONSE($retObj,'SUCCESS','OK');
	}
}

class taxes implements dbconn{
	public $taxName;public $percent;public $taxId;
	function __construct($ptaxName,$ppercent){
		$this->taxName=$ptaxName;$this->percent=$ppercent;
	}
	function __construct(){
		$this->taxName=NULL;$this->percent=NULL;$this->taxId=NULL;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO taxes (taxName,percent) VALUES (:taxName,:percent)');
		$stmt->bindParam(':taxName',$this->taxName);
		$stmt->bindParam(':percent',$this->percent);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'taxes : INSERT','ERROR');
		}
		$retObj=NULL;
		$this->taxId=$this->db->lastInsertId();
		$stmt=$this->db->prepare('SELECT taxId FROM taxes');
		$stmt->bindParam(':taxId',$this->taxId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'taxes : SELECT AUTO','ERROR');
		}
		$retObj=$stmt->fetch(PDO::FETCH_OBJ);
		return new RESPONSE($retObj,'SUCCESS','OK');
	}
}

class transactions implements dbconn{
	public $type;public $status;public $exchangeId;public $txnId;
	function __construct($ptype,$pstatus,$pexchangeId){
		$this->type=$ptype;$this->status=$pstatus;$this->exchangeId=$pexchangeId;
	}
	function __construct(){
		$this->type=NULL;$this->status=NULL;$this->exchangeId=NULL;$this->txnId=NULL;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO transactions (type,status,exchangeId) VALUES (:type,:status,:exchangeId)');
		$stmt->bindParam(':type',$this->type);
		$stmt->bindParam(':status',$this->status);
		$stmt->bindParam(':exchangeId',$this->exchangeId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'transactions : INSERT','ERROR');
		}
		$retObj=NULL;
		$this->txnId=$this->db->lastInsertId();
		$stmt=$this->db->prepare('SELECT txnId FROM transactions');
		$stmt->bindParam(':txnId',$this->txnId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'transactions : SELECT AUTO','ERROR');
		}
		$retObj=$stmt->fetch(PDO::FETCH_OBJ);
		return new RESPONSE($retObj,'SUCCESS','OK');
	}
}

class users implements dbconn{
	public $infoId;public $contactId;public $addrId;public $userId;
	function __construct($pinfoId,$pcontactId,$paddrId){
		$this->infoId=$pinfoId;$this->contactId=$pcontactId;$this->addrId=$paddrId;
	}
	function __construct(){
		$this->infoId=NULL;$this->contactId=NULL;$this->addrId=NULL;$this->userId=NULL;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO users (infoId,contactId,addrId) VALUES (:infoId,:contactId,:addrId)');
		$stmt->bindParam(':infoId',$this->infoId);
		$stmt->bindParam(':contactId',$this->contactId);
		$stmt->bindParam(':addrId',$this->addrId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'users : INSERT','ERROR');
		}
		$retObj=NULL;
		$this->userId=$this->db->lastInsertId();
		$stmt=$this->db->prepare('SELECT userId FROM users');
		$stmt->bindParam(':userId',$this->userId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'users : SELECT AUTO','ERROR');
		}
		$retObj=$stmt->fetch(PDO::FETCH_OBJ);
		return new RESPONSE($retObj,'SUCCESS','OK');
	}
}

?>
<?php
class address implements dbconn{
	function __construct($pstreet,$pcity,$pstate,$pPIN,$paddrid){
		$street=$pstreet;$city=$pcity;$state=$pstate;$PIN=$pPIN;$addrid=$paddrid;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO address (street,city,state,PIN,addrid) VALUES (:street,:city,:state,:PIN,:addrid)');
		$stmt->bindParam(':street',$street);
		$stmt->bindParam(':city',$city);
		$stmt->bindParam(':state',$state);
		$stmt->bindParam(':PIN',$PIN);
		$stmt->bindParam(':addrid',$addrid);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'address : INSERT','ERROR');
		}
	}
}

class bill implements dbconn{
	function __construct($pchartId,$pexchangeId,$pbillId){
		$chartId=$pchartId;$exchangeId=$pexchangeId;$billId=$pbillId;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO bill (chartId,exchangeId,billId) VALUES (:chartId,:exchangeId,:billId)');
		$stmt->bindParam(':chartId',$chartId);
		$stmt->bindParam(':exchangeId',$exchangeId);
		$stmt->bindParam(':billId',$billId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'bill : INSERT','ERROR');
		}
	}
}

class charts implements dbconn{
	function __construct($pavailId,$psessionId,$pstatus,$pexchangeId,$pchartId){
		$availId=$pavailId;$sessionId=$psessionId;$status=$pstatus;$exchangeId=$pexchangeId;$chartId=$pchartId;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO charts (availId,sessionId,status,exchangeId,chartId) VALUES (:availId,:sessionId,:status,:exchangeId,:chartId)');
		$stmt->bindParam(':availId',$availId);
		$stmt->bindParam(':sessionId',$sessionId);
		$stmt->bindParam(':status',$status);
		$stmt->bindParam(':exchangeId',$exchangeId);
		$stmt->bindParam(':chartId',$chartId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'charts : INSERT','ERROR');
		}
	}
}

class contact implements dbconn{
	function __construct($pemail,$pphone1,$pphone2,$pcontactId){
		$email=$pemail;$phone1=$pphone1;$phone2=$pphone2;$contactId=$pcontactId;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO contact (email,phone1,phone2,contactId) VALUES (:email,:phone1,:phone2,:contactId)');
		$stmt->bindParam(':email',$email);
		$stmt->bindParam(':phone1',$phone1);
		$stmt->bindParam(':phone2',$phone2);
		$stmt->bindParam(':contactId',$contactId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'contact : INSERT','ERROR');
		}
	}
}

class doctors implements dbconn{
	function __construct($puserid,$pprofileId,$pdoctorId){
		$userid=$puserid;$profileId=$pprofileId;$doctorId=$pdoctorId;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO doctors (userid,profileId,doctorId) VALUES (:userid,:profileId,:doctorId)');
		$stmt->bindParam(':userid',$userid);
		$stmt->bindParam(':profileId',$profileId);
		$stmt->bindParam(':doctorId',$doctorId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'doctors : INSERT','ERROR');
		}
	}
}

class employees implements dbconn{
	function __construct($puserId,$pprofileId,$pempId){
		$userId=$puserId;$profileId=$pprofileId;$empId=$pempId;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO employees (userId,profileId,empId) VALUES (:userId,:profileId,:empId)');
		$stmt->bindParam(':userId',$userId);
		$stmt->bindParam(':profileId',$profileId);
		$stmt->bindParam(':empId',$empId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'employees : INSERT','ERROR');
		}
	}
}

class exchange implements dbconn{
	function __construct($ptype,$pamount,$pdiscount,$pdiscountType,$pexchangeId,$pnet){
		$type=$ptype;$amount=$pamount;$discount=$pdiscount;$discountType=$pdiscountType;$exchangeId=$pexchangeId;$net=$pnet;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO exchange (type,amount,discount,discountType,exchangeId,net) VALUES (:type,:amount,:discount,:discountType,:exchangeId,:net)');
		$stmt->bindParam(':type',$type);
		$stmt->bindParam(':amount',$amount);
		$stmt->bindParam(':discount',$discount);
		$stmt->bindParam(':discountType',$discountType);
		$stmt->bindParam(':exchangeId',$exchangeId);
		$stmt->bindParam(':net',$net);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'exchange : INSERT','ERROR');
		}
	}
}

class expenditures implements dbconn{
	function __construct($pexpenseId,$pexchangeId,$pexpenditureId){
		$expenseId=$pexpenseId;$exchangeId=$pexchangeId;$expenditureId=$pexpenditureId;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO expenditures (expenseId,exchangeId,expenditureId) VALUES (:expenseId,:exchangeId,:expenditureId)');
		$stmt->bindParam(':expenseId',$expenseId);
		$stmt->bindParam(':exchangeId',$exchangeId);
		$stmt->bindParam(':expenditureId',$expenditureId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'expenditures : INSERT','ERROR');
		}
	}
}

class expenses implements dbconn{
	function __construct($pname,$pcost,$pexpenseId){
		$name=$pname;$cost=$pcost;$expenseId=$pexpenseId;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO expenses (name,cost,expenseId) VALUES (:name,:cost,:expenseId)');
		$stmt->bindParam(':name',$name);
		$stmt->bindParam(':cost',$cost);
		$stmt->bindParam(':expenseId',$expenseId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'expenses : INSERT','ERROR');
		}
	}
}

class groups implements dbconn{
	function __construct($pgroupName,$pgroupId){
		$groupName=$pgroupName;$groupId=$pgroupId;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO groups (groupName,groupId) VALUES (:groupName,:groupId)');
		$stmt->bindParam(':groupName',$groupName);
		$stmt->bindParam(':groupId',$groupId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'groups : INSERT','ERROR');
		}
	}
}

class lab implements dbconn{
	function __construct($pserviceId,$pparamId,$pcost,$plabId){
		$serviceId=$pserviceId;$paramId=$pparamId;$cost=$pcost;$labId=$plabId;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO lab (serviceId,paramId,cost,labId) VALUES (:serviceId,:paramId,:cost,:labId)');
		$stmt->bindParam(':serviceId',$serviceId);
		$stmt->bindParam(':paramId',$paramId);
		$stmt->bindParam(':cost',$cost);
		$stmt->bindParam(':labId',$labId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'lab : INSERT','ERROR');
		}
	}
}

class params implements dbconn{
	function __construct($pparamId,$pparamString){
		$paramId=$pparamId;$paramString=$pparamString;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO params (paramId,paramString) VALUES (:paramId,:paramString)');
		$stmt->bindParam(':paramId',$paramId);
		$stmt->bindParam(':paramString',$paramString);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'params : INSERT','ERROR');
		}
	}
}

class patientgroups implements dbconn{
	function __construct($pgroupId,$ppatientId){
		$groupId=$pgroupId;$patientId=$ppatientId;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO patientgroups (groupId,patientId) VALUES (:groupId,:patientId)');
		$stmt->bindParam(':groupId',$groupId);
		$stmt->bindParam(':patientId',$patientId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'patientgroups : INSERT','ERROR');
		}
	}
}

class personalinfo implements dbconn{
	function __construct($pname,$pgender,$pbloodGroup,$pdob,$paadhar,$pinfoId){
		$name=$pname;$gender=$pgender;$bloodGroup=$pbloodGroup;$dob=$pdob;$aadhar=$paadhar;$infoId=$pinfoId;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO personalinfo (name,gender,bloodGroup,dob,aadhar,infoId) VALUES (:name,:gender,:bloodGroup,:dob,:aadhar,:infoId)');
		$stmt->bindParam(':name',$name);
		$stmt->bindParam(':gender',$gender);
		$stmt->bindParam(':bloodGroup',$bloodGroup);
		$stmt->bindParam(':dob',$dob);
		$stmt->bindParam(':aadhar',$aadhar);
		$stmt->bindParam(':infoId',$infoId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'personalinfo : INSERT','ERROR');
		}
	}
}

class profiles implements dbconn{
	function __construct($ptype,$pname,$pdescription,$pprofileId){
		$type=$ptype;$name=$pname;$description=$pdescription;$profileId=$pprofileId;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO profiles (type,name,description,profileId) VALUES (:type,:name,:description,:profileId)');
		$stmt->bindParam(':type',$type);
		$stmt->bindParam(':name',$name);
		$stmt->bindParam(':description',$description);
		$stmt->bindParam(':profileId',$profileId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'profiles : INSERT','ERROR');
		}
	}
}

class service implements dbconn{
	function __construct($pname,$pcost,$pdescription,$pcategoryId,$pserviceId){
		$name=$pname;$cost=$pcost;$description=$pdescription;$categoryId=$pcategoryId;$serviceId=$pserviceId;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO service (name,cost,description,categoryId,serviceId) VALUES (:name,:cost,:description,:categoryId,:serviceId)');
		$stmt->bindParam(':name',$name);
		$stmt->bindParam(':cost',$cost);
		$stmt->bindParam(':description',$description);
		$stmt->bindParam(':categoryId',$categoryId);
		$stmt->bindParam(':serviceId',$serviceId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'service : INSERT','ERROR');
		}
	}
}

class serviceavailed implements dbconn{
	function __construct($ppatientId,$pserviceId,$pexchangeId,$ptaxId,$pavailId){
		$patientId=$ppatientId;$serviceId=$pserviceId;$exchangeId=$pexchangeId;$taxId=$ptaxId;$availId=$pavailId;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO serviceavailed (patientId,serviceId,exchangeId,taxId,availId) VALUES (:patientId,:serviceId,:exchangeId,:taxId,:availId)');
		$stmt->bindParam(':patientId',$patientId);
		$stmt->bindParam(':serviceId',$serviceId);
		$stmt->bindParam(':exchangeId',$exchangeId);
		$stmt->bindParam(':taxId',$taxId);
		$stmt->bindParam(':availId',$availId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'serviceavailed : INSERT','ERROR');
		}
	}
}

class servicecategories implements dbconn{
	function __construct($pname,$pcategoryId){
		$name=$pname;$categoryId=$pcategoryId;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO servicecategories (name,categoryId) VALUES (:name,:categoryId)');
		$stmt->bindParam(':name',$name);
		$stmt->bindParam(':categoryId',$categoryId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'servicecategories : INSERT','ERROR');
		}
	}
}

class session implements dbconn{
	function __construct($ptimeStamp,$pdateAndTime,$pduration,$psessionId){
		$timeStamp=$ptimeStamp;$dateAndTime=$pdateAndTime;$duration=$pduration;$sessionId=$psessionId;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO session (timeStamp,dateAndTime,duration,sessionId) VALUES (:timeStamp,:dateAndTime,:duration,:sessionId)');
		$stmt->bindParam(':timeStamp',$timeStamp);
		$stmt->bindParam(':dateAndTime',$dateAndTime);
		$stmt->bindParam(':duration',$duration);
		$stmt->bindParam(':sessionId',$sessionId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'session : INSERT','ERROR');
		}
	}
}

class taxes implements dbconn{
	function __construct($ptaxName,$ppercent,$ptaxId){
		$taxName=$ptaxName;$percent=$ppercent;$taxId=$ptaxId;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO taxes (taxName,percent,taxId) VALUES (:taxName,:percent,:taxId)');
		$stmt->bindParam(':taxName',$taxName);
		$stmt->bindParam(':percent',$percent);
		$stmt->bindParam(':taxId',$taxId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'taxes : INSERT','ERROR');
		}
	}
}

class transactions implements dbconn{
	function __construct($ptype,$pstatus,$pexchangeId,$ptxnId){
		$type=$ptype;$status=$pstatus;$exchangeId=$pexchangeId;$txnId=$ptxnId;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO transactions (type,status,exchangeId,txnId) VALUES (:type,:status,:exchangeId,:txnId)');
		$stmt->bindParam(':type',$type);
		$stmt->bindParam(':status',$status);
		$stmt->bindParam(':exchangeId',$exchangeId);
		$stmt->bindParam(':txnId',$txnId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'transactions : INSERT','ERROR');
		}
	}
}

class users implements dbconn{
	function __construct($pinfoId,$pcontactId,$paddrId,$puserId){
		$infoId=$pinfoId;$contactId=$pcontactId;$addrId=$paddrId;$userId=$puserId;
	}
	function add(){
		$stmt=$this->db->prepare('INSERT INTO users (infoId,contactId,addrId,userId) VALUES (:infoId,:contactId,:addrId,:userId)');
		$stmt->bindParam(':infoId',$infoId);
		$stmt->bindParam(':contactId',$contactId);
		$stmt->bindParam(':addrId',$addrId);
		$stmt->bindParam(':userId',$userId);
		if($stmt->execute()==false) {
			$this->errorLog($stmt->errorInfo()[2]);
			return new RESPONSE(null,'users : INSERT','ERROR');
		}
	}
}

?>
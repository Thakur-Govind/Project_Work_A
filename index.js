var log_or_reg=0;
var user='Consumer';
function initialload(){
  document.getElementsByClassName('user')[0].style.display = 'none';
  document.getElementsByClassName('register')[0].style.display = 'none';
  document.getElementsByClassName('login')[0].style.display='none';
}

function reg_log_option(a,b,c){
  if(log_or_reg==2){
    document.getElementsByClassName('register')[0].style.display='block';
    document.getElementsByClassName('login')[0].style.display='none';
    document.getElementsByClassName('consumer')[0].style.display=a;
    document.getElementsByClassName('farmer')[0].style.display=b;
    document.getElementsByClassName('seller')[0].style.display=c;
    document.getElementsByClassName('reg_head')[0].innerHTML=user+' Registration';
  }
  else {
    document.getElementsByClassName('login')[0].style.display='block';
    document.getElementsByClassName('register')[0].style.display='none';
    document.getElementsByClassName('log_head')[0].innerHTML=user+' Login';
  }

}

function useroption(f){

  var x=document.getElementsByClassName('user')[0];
  x.style.display = 'block';
  log_or_reg=f;

    document.getElementsByClassName('login')[0].style.display='none';
    document.getElementsByClassName('register')[0].style.display='none';
    document.getElementById(user).checked=false;
}



function chooseradio(clicked_id){
  //user=document.getElementsByClassName('user')[0].elements.user.value;
  user = document.getElementById(clicked_id).value;
  if(user=='Consumer'){
  reg_log_option('block','none','none');
  }
  if(user=='Farmer'){
    reg_log_option('none','block','none');
  }
  if(user=='Seller'){
  reg_log_option('none','none','block');
  }

}

function validation(){
  event.preventDefault();
  var adhar = document.getElementById("txtaadhar").value;
  var firstname = document.getElementById("firstname").value;
  var middlename = document.getElementById("middlename").value;
  var lastname = document.getElementById("lastname").value;
  var dob = document.getElementById("DOB").value;
  var panno =  document.getElementById("PAN").value;
  var mobile = document.getElementById("Mobile").value;
  var adharcard = /^\d{12}$/;
  var adharsixteendigit = /^\d{16}$/;
  var pancard = /[A-Z]{5}[0-9]{4}[A-Z]{1}/;
  var mobileno = /^\d{10}$/;
  var userID = document.getElementById("userID").value;
  var pass = document.getElementById("password_reg").value;
  var conf_pass = document.getElementById("conf_password_reg").value;
  if (adhar != '' && firstname!='' && middlename!=''&& lastname!='' && dob!='' && panno!='' && mobile!='' && userID!='' && pass!='' && conf_pass!=''){
       if (adhar.match(adharcard) || adhar.match(adharsixteendigit))
       {
          if(panno.match(pancard)){
              if(mobile.match(mobileno)){
                if(pass == conf_pass){
                  alert("Success");
                }
                else{
                  alert("Password do not match with confirm password field.");
                }

              }
              else{
                alert("Invalid Phone");
              }
          }
          else{
            alert("Invalid PAN");
          }
       }
       else{
         alert("Invalid Aadhar Number");
       }
   }
   else{
     alert("Enter all fields.");
   }

   // if (adhar != '')
   // {
   //     if(!adhar.match(adharsixteendigit))
   //     {
   //         alert("Invalid Aadhar Number");
   //         return false;
   //     }
   // }

}

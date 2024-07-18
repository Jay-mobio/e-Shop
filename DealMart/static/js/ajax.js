function ReSendOTP(email, mess_id) {
	
	mess = document.getElementById(mess_id);
	mess.innerText = "Sending...";
	// url = "authetication:resend_otp"
	$.ajax({
		type: 'POST',
		url: '/resend_otp/',
		data: {usr:email},
		success: function(req){
			mess.innerText = "Resend";

		}
	})
}
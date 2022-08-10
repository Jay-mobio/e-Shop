// $(document).ready(function(){
//     $('.send_otp').submit(function(){
//         url = $(this).attr('action')
//         mess = document.getElementById("resendOTPmess");
//         mess.innerText = "Sending...";
//         $.ajax({
//             url: url,
//             type: 'POST',
//             data: $(".send_otp").serialize(),
//             success: function(data){
//                 // mess.innerText = data;
//                 alert('otp is sent successfully!')

//             }
//         })
//     })  
// })


// function resend_otp(email) {
// 	url = $('.send_otp').attr('href')
//     // console.log(email);
//     // console.log(url)
// 	mess = document.getElementById("resendOTPmess");
// 	mess.innerText = "Sending...";
// 	$.ajax({
// 		url: url,
// 		type: 'POST',
// 		data: JSON.stringify({'usr':email}),
// 		success: function(data){
// 			mess.innerText = data;

// 		}
// 	})
// }

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
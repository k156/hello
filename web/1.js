
  function checkLogin() {
	var uid = get('userid'),
		upw = get('userpw');
  
	var frm = document.getElementById('frm'),
		msg = document.getElementById('msg'),
		err = document.getElementById('err');
	if (uid === 'a' && upw === '1') {
	  window.location.href = "2.html";
	} else {
	  err.style.display = 'block'; 
	  frm.style.display = 'block';
	}
  
  }
  function get(id) {
	return document.getElementById(id).value;
  }
  
  
  function sign_in(user) {
	var x = document.getElementById(user);
	if (user.style.display === "none") {
	  user.style.display = "block";
	} else {
	  user.style.display = "none";
	}
  }
//  Profile Script


var savebutton = document.getElementById('save');
var readonly = true;
var inputs = document.querySelectorAll('.edit-text');
savebutton.addEventListener('click',function(){
    
     for (var i=0; i<inputs.length; i++) {
     inputs[i].toggleAttribute('readonly');
     };

    if (savebutton.innerHTML == "Save Changes") {
      savebutton.innerHTML = "Edit Profile";
         } else {
      savebutton.innerHTML = "Save Changes";
      }
    });
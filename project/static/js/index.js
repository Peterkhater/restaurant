$(document).ready(function() {

    $(`[unique-script-id="w-w-dm-id"] .btn-box`).click(function() {
      $(this).parent().children(".overlay").show();
  
    });
  
  
    $(`[unique-script-id="w-w-dm-id"] .close`).click(function() {
      $(".overlay").hide();
    });
  });
  function sendMessage() {
    // Get form values
    const fullName = document.getElementById("fullName").value.trim();
    const subject = document.getElementById("subject").value.trim();
    const message = document.getElementById("message").value.trim();

    // Check if all fields are filled
    if (!fullName || !subject || !message) {
      alert("Veuillez remplir tous les champs.");
      return;
    }

    // Format the WhatsApp message
    const whatsappMessage = `Nom et prénom: ${fullName}\nSujet: ${subject}\nMessage: ${message}`;


    const phoneNumber = "+96181121347"; 
    const whatsappURL = `https://wa.me/${phoneNumber}?text=${encodeURIComponent(whatsappMessage)}`;

    // Open WhatsApp URL in a new tab
    window.open(whatsappURL, "_blank");
  }

  let img_cont = document.getElementById('img_cont')
  let img_cont_2 = document.getElementById('img_cont2')
  let fade_overlay_id = document.getElementById("fade_overlay_id")
  let fade_overlay_id2 = document.getElementById('fade_overlay_id2')

  img_cont.onmouseenter=function(){
    fade_overlay_id.style.height="80%";   
  }
  
  img_cont.onmouseleave=function(){
    fade_overlay_id.style.height="50%"
  }
  
  
  img_cont_2.onmouseenter=function(){
    fade_overlay_id2.style.height="80%";
  }

  img_cont_2.onmouseleave=function(){
    fade_overlay_id2.style.height="50%"
  }
  
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
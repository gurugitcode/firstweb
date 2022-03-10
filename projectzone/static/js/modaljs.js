"{% load static %}"
$('#contect-form').on('submit', function(event) {
    event.preventDefault();
    output = "";
    var name = $("#inputName4").val();
    console.log(name);
    var email = $("#inputEmail4").val();
    console.log(email);
    var subject = $("#inputSubject").val();
    console.log(subject);
    var message = $("#idmessege").val();
    console.log(message);
    var gridCheck = $("#gridCheck").val();
    console.log(gridCheck);
    var csr = $("input[name=csrfmiddlewaretoken]").val();
    console.log(csr);
    // console.log("form submitted!") // sanity check
    if (name == "") {
        console.log("please enter name");
    } else if (email == "") {
        console.log("please enter email");
    } else if (subject == "") {
        console.log("please enter subject");
    } else if (message == "") {
        console.log("please enter message");
    } else if (gridCheck == "") {
        console.log("please click check out gridCheck");
    } else {
        mydata = {
            name: name,
            email: email,
            subject: subject,
            message: message,
            csrfmiddlewaretoken: csr
        };

        console.log(mydata);
        $.ajax({

            method: "POST",
            data: mydata,
            url: "{% url 'contectdata' %}",
            success: function(data) {
                $("#inputName4").val(data.name)
                $("#inputEmail4").val(data.email);
                $("#inputSubject").val(data.subject);
                $("#idmessege").val(data.message);
                console.log(data);
                x = data.status;
                if (data.status == "Save") {

                    $("#msg").text("Form Submitted Successfily");
                    $("#msg").show();
                    var data = document.getElementById("successmsg");
                    console.log('yesy', data.status, data)
                        // data.innerHTML = "<p id='msg' class='alert alert-success'>Your message has been sent. Thank you!</p>"
                    data.innerHTML = "<div class='alert alert-info alert-dismissible d-flex align-items-center fade show' role='alert'><i class='bi-check-circle-fill'></i> <strong></strong> Your message has been sent. Thank you! <button type='button' id='over' class='close' data-dismiss='alert' aria-label='Close'> <span aria-hidden='true'>&times;</span></button></div>"
                        // alert("Your message has been sent. Thank you!")
                        // $('.alert').alert()
                    $('.alert').mousemove('closed.bs.alert', function() {
                        // do something…
                        var data = document.getElementById("successmsg");
                        data.innerHTML = "<p id='msg' class='alert alert-success'>Your message has been sent. Thank you!</p>"
                            // data.innerHTML = ""
                    })
                    $("form")[0].reset();
                }
                if (data.status == 0) {
                    $("#msg").text("Unable to Form Submitted Successfily");
                    $("#msg").show();

                    $("form")[0].reset();
                    // console.log("Unable to save Form");
                }
            }
        })
    }
});

// var button = document.getElementById("clickme"),
//     count = 0;
// button.onclick = function() {
//     var x = document.getElementById("address0");
//     // document.getElementById("id_serial_no").innerHTML = x;
//     console.log(x);
//     count += 1;
//     button.innerHTML = "Click me: " + count;
// };
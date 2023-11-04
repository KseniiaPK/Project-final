$(document).ready(function() {
    $("#loginCard").hide().slideDown(800);

    $("#passwordEye").click(function() {
        if ($("#passwordEye").html() == "visibility_off") {
            $("#passwordEye").html("visibility");
            $("#passwordInput").attr('type', 'text');
        } else {
            $("#passwordEye").html("visibility_off");
            $("#passwordInput").attr('type', 'password');
        }
    });

    $("#confirmPasswordEye").click(function() {
        if ($("#confirmPasswordEye").html() == "visibility_off") {
            $("#confirmPasswordEye").html("visibility");
            $("#confirmPasswordInput").attr('type', 'text');
        } else {
            $("#confirmPasswordEye").html("visibility_off");
            $("#confirmPasswordInput").attr('type', 'password');
        }
    });

    $("#oldPasswordEye").click(function() {
        if ($("#oldPasswordEye").html() == "visibility_off") {
            $("#oldPasswordEye").html("visibility");
            $("#oldPasswordInput").attr('type', 'text');
        } else {
            $("#oldPasswordEye").html("visibility_off");
            $("#oldPasswordInput").attr('type', 'password');
        }
    });

    $("#newPasswordEye").click(function() {
        if ($("#newPasswordEye").html() == "visibility_off") {
            $("#newPasswordEye").html("visibility");
            $("#newPasswordInput").attr('type', 'text');
        } else {
            $("#newPasswordEye").html("visibility_off");
            $("#newPasswordInput").attr('type', 'password');
        }
    });

    $("#confirmNewPasswordEye").click(function() {
        if ($("#confirmNewPasswordEye").html() == "visibility_off") {
            $("#confirmNewPasswordEye").html("visibility");
            $("#confirmNewPasswordInput").attr('type', 'text');
        } else {
            $("#confirmNewPasswordEye").html("visibility_off");
            $("#confirmNewPasswordInput").attr('type', 'password');
        }
    });

});


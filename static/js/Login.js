// Login.js

function validarInicioSesion() {
    var form1Example1 = document.getElementById("form1Example1").value;
    var form1Example2 = document.getElementById("form1Example2").value;

    // Realiza tus validaciones aquí
    if (form1Example1 === "" || form1Example2 === "") {
        alert("Debes completar los campos requeridos.");
        return false;
    }

    // Si las validaciones son exitosas, puedes enviar el formulario
    return true;
}

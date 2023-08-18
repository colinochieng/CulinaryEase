function validateForm() {
    const fname = document.getElementById('fname').value;
    const sname = document.getElementById('sname').value;

    document.getElementById('fnameError').innerText = '';
    document.getElementById('snameError').innerText = '';

    if (fname.trim() === '')
    {
        document.getElementById('fnameError').innerText = 'First Name required';
        return false; 
    }
    if (sname.trim() === '')
    {
        document.getElementById('snameError').innerText = 'Surname is required';
        return false;
    }

    if (! checkPasswordMatch())
    {
        return false;
    }
}

function checkPasswdStrength(password) {
    console.log(password)
    console.log(password.length)

    if (password.length >= 8) {
        const specialCharacterRegex = /[!@#$%^&*(),.?":{}|<>]/;
        let state = specialCharacterRegex.test(password);

        if (state) {
            return 'strong';
        }
        else {
            return 'Must contain special characters';
        }
    }
    else {
        return 'Password Weak';
    }
}

document.getElementById('password').addEventListener('input', (e) => {
    const inputValue = checkPasswdStrength(e.target.value)
    if (inputValue === 'strong') {
        document.getElementById("password-strength").innerText = inputValue;
        document.getElementById("password-strength").style.color = 'green';
    } else {
        document.getElementById("password-strength").style.color = 'red';
        document.getElementById("password-strength").innerText = inputValue;
    }
});

function checkPasswordMatch() {
    const password = document.getElementById("password").value;
    const confirm = document.getElementById("confirm").value;
    const passwordMatchElement = document.getElementById("password-match");

    if (password === confirm) {
        passwordMatchElement.innerHTML = "Passwords match!";
        return true
    } else {
        passwordMatchElement.innerHTML = "Passwords do not match!";
        return false
    }
}

export function imgValidate(inputId, spanId) {
  const imageInput = document.querySelector(inputId);
  const selectedImageName = document.querySelector(spanId);
  const allowedExtensions = ["png", "jpg", "jpeg", "gif"];

  imageInput.addEventListener("change", function () {
    const fileName = this.files[0].name;

    const isValidFile = allowedExtensions.includes(
      fileName.split(".").slice(-1)[0].toLowerCase()
    );

    if (isValidFile) {
      selectedImageName.textContent = fileName.substring(0, 27) + "...";
      return 1;
    } else {
      selectedImageName.textContent = "Only png, jpg, jpeg or gif allowed";
      return -1;
    }
  });
}

document.addEventListener("DOMContentLoaded", function () {
  imgValidate("#user-image", "#selectedFileName");

  // validate if the username or the email already exists

  function validateForm(username, email, password) {
    let isValidForm = true;
    const unameError = document.getElementById("unameError");
    const emailError = document.getElementById("emailError");
    const passwordError = document.getElementById("password-strength");
    const bios = document.getElementById("bios");
    const biosError = document.getElementById("biosError");

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (username.value.trim() === "") {
      unameError.textContent = "Username is required";
      isValidForm = false;
    } else {
      unameError.textContent = "";
    }

    if (email.value.trim() === "") {
      emailError.textContent = "Email is required";
      isValidForm = false;
    } else {
      if (emailRegex.test(email.value)) {
        emailError.textContent = "";
      } else {
        isValidForm = false;
        emailError.textContent = "Invalid email";
      }
    }

    if (password.value.trim() === "") {
      passwordError.textContent = "Password cannot be empty";
      console.log(password.value.trim());
      isValidForm = false;
    } else if (password.value.length < 8) {
      passwordError.textContent = "Password must be at least 8 characters long";
      isValidForm = false;
    } else {
      passwordError.textContent = "";
    }

    if (bios.value.trim() === "") {
      biosError.textContent = "Bios is required";
      isValidForm = false;
    } else {
      biosError.textContent = "";
    }

    /**
         * Validation of the country tables which can't be empty
        === Used Ids=============
         * country countryError
         * state, stateError
         * city, cityError
         * */

    const country = document.querySelector("#country").value;
    const countryError = document.querySelector("#countryError");
    const state = document.querySelector("#state").value;
    const stateError = document.querySelector("#stateError");
    const city = document.querySelector("#city").value;
    const cityError = document.querySelector("#cityError");

    if (country.trim() === "") {
      countryError.textContent = "Country name required";
      isValidForm = false;
    } else {
      countryError.textContent = "";
    }

    if (state.trim() === "") {
      stateError.textContent = "State name required";
      isValidForm = false;
    } else {
      stateError.textContent = "";
    }

    if (city.trim() === "") {
      cityError.textContent = "City name required";
      isValidForm = false;
    } else {
      cityError.textContent = "";
    }

    return isValidForm;
  }

  const signupForm = document.getElementsByClassName("sigup-form")[0];
  signupForm.addEventListener("submit", function (event) {
    event.preventDefault();

    const username = document.getElementById("uname");
    const email = document.getElementById("emailCode");
    const password = document.getElementById("passcode");
    let userSignupValid = false;

    fetch("http://192.168.0.13:5000/usernames", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username: username.value.toLowerCase(),
        email: email.value.toLowerCase(),
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        let isValidForm = validateForm(username, email, password);

        if (data.username === null) {
          if (data.email === null) {
            userSignupValid = true;
          } else {
            emailError.textContent = "Account with the email already exists";
            isValidForm = false;
          }
        } else {
          unameError.textContent = "User name already taken";
          isValidForm = false;
        }
        console.log(data);

        if (isValidForm && userSignupValid) {
          this.submit();
        }
      })
      .catch((error) => {
        console.log(error);
      });
  });

  /**
   * Validating login data
   */
  const loginEmail = document.getElementById("email");
  const loginPass = document.getElementById("password");
  const emailLoginError = document.getElementById("emailLoginError");
  const passLoginError = document.getElementById("passLoginError");
  const loginForm = document.querySelector(".login-form");

  loginForm.addEventListener("submit", function (event) {
    event.preventDefault();
    let loginIsvalid = true;

    if (loginEmail.value.trim() === "") {
      emailLoginError.textContent = "Email cannot be empty";
      loginIsvalid = false;
    } else {
      emailLoginError.textContent = "";
    }

    if (loginPass.value.trim() === "") {
      passLoginError.textContent = "Passcode cannot be empty";
      loginIsvalid = false;
    } else {
      passLoginError.textContent = "";
    }

    if (loginIsvalid) {
      let xhr = new XMLHttpRequest();

      xhr.onreadystatechange = () => {
        if (xhr.readyState === XMLHttpRequest.DONE) {
          if (xhr.status === 200) {
            const jsonResponse = JSON.parse(xhr.responseText);

            const { email } = jsonResponse;

            if (email) {
              this.submit();
            } else {
              // No account with such an email consider to login
              console.log(jsonResponse);
              emailLoginError.textContent = "Account doesn't exist";
            }
          } else if (xhr.status === 404) {
            // inavlid password or email
            const textResponse = xhr.responseText;

            if (textResponse.endsWith("email")) {
              // No account with such an email consider to login
              emailLoginError.textContent = "Account doesn't exist";
            }

            if (textResponse.endsWith("password")) {
              passLoginError.textContent = textResponse;
            } else {
              passLoginError.textContent = "";
            }
          } else {
            console.error(xhr.stateError);
          }
        }
      };

      xhr.open("POST", "http://192.168.0.13:5000/logcheck", false);
      xhr.setRequestHeader("Content-Type", "application/json");

      const dataSent = { email: loginEmail.value, password: loginPass.value };
      xhr.send(JSON.stringify(dataSent));
    }
  });
});

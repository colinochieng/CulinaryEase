window.addEventListener('load', function() {
    let loginBtn = document.getElementById('loginBtn');
    let popup = document.querySelector('.popup');
    let closeLogin = document.getElementsByClassName('closeLogin')[0]

    loginBtn.style.cursor = 'pointer';
    closeLogin.style.cursor = 'pointer';

    popup.addEventListener('click', (event) => {
        if (event.target === popup) {
          popup.style.display = 'none';
        }
      });

      closeLogin.addEventListener('click', (event) => {
          popup.style.display = 'none';
      });

    let signUpBtn = document.getElementById('signUpBtn');
    const popupSignup = document.querySelector('.signup-popup');
    const closeSignup = document.querySelector('.closeSignup');
    closeSignup.style.cursor = 'pointer';

    signUpBtn.style.cursor = 'pointer';

    loginBtn.addEventListener('click', () => {
        if (popupSignup.style.display === 'flex') {
            popupSignup.style.display = 'none';
        }
        popup.style.display = 'flex';
    });

    signUpBtn.addEventListener('click', () => {
        if (popup.style.display === 'flex') {
            popup.style.display = 'none';
        }
        popupSignup.style.display = 'flex';
    })

    popupSignup.addEventListener('click', (event) => {
        if (event.target === popupSignup) {
          popupSignup.style.display = 'none';
        }
      });

      closeSignup.addEventListener('click', (event) => {
        popupSignup.style.display = 'none';
    });


    const toLoginFromSignUp = document.getElementById('to_login');
    const toSignupFromLogin = document.getElementById('to_signin');

    toLoginFromSignUp.addEventListener('click', () => {
        popupSignup.style.display = 'none';
        popup.style.display = 'flex';
    });

    toSignupFromLogin.addEventListener('click', () => {
        popup.style.display = 'none';
        popupSignup.style.display = 'flex';
    });
});
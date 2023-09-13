window.addEventListener("DOMContentLoaded", function() {
    /**
     * likes
     */
    let likes = document.getElementsByClassName('like-button')[0];
    let likesValue = document.getElementById('like-value');

    likesValue.textContent = likes.value;

    likes.addEventListener('click', (event) => {
      if (event.currentTarget.classList.contains('like'))
      {
        event.currentTarget.classList.toggle('like', false);
        likesValue.textContent = parseInt(likesValue.textContent) - 1;
      }
      else {
        event.currentTarget.classList.toggle('like', true);
        likesValue.textContent = parseInt(likesValue.textContent) + 1;
      }
    });

    /**
     * comments
     */
    let commentsPopupBtn = document.querySelector('.comment-popup-button');
    const commentPopup = document.getElementById('commentPopup');
    const username = document.getElementById('comments-username');
    const email = document.getElementById('comments-email')
    const commentsText = document.getElementById('comments-text');
    // const errorMessages = document.getElementById('errorMessages');


    commentsPopupBtn.addEventListener('click', function() {
        commentPopup.style.display = 'flex';
    });

    document.querySelector('.send-comment').addEventListener('submit', function (event) {
        // errorMessages.innerHTML = '';
        event.preventDefault();
        console.log(username.value)

        if (username.value.length < 8 || username.value.length > 20) {
            displayError('Username must be between 8 and 20 characters.');
        } else if (commentsText.value.length < 50 || commentsText.value.length > 250) {
            displayError('Comment must be between 50 and 250 characters.');
        } else if (!isValidEmail(email.value)) {
            displayError('Invalid email address.');
        } else {
            this.submit();
            commentPopup.style.display = 'none';
        }
    });

    document.querySelector('.close-comment').addEventListener('click', function() {
        commentPopup.style.display = 'none';
    });

    function isValidEmail(email) {
        const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
        return emailPattern.test(email);
    }

    function displayError(message) {
        // const errorMessage = document.createElement('div');
        // errorMessage.textContent = message;
        // errorMessages.appendChild(errorMessage);
        alert(message);
        commentPopup.style.display = 'flex';
    }
});

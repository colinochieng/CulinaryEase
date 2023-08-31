/*
===========================
Responsive Nav-bar
===========================
*/

let navIcon = document.querySelector('.menu-bar');
let navElem = document.querySelector('.nav-elem');

navIcon.addEventListener('click',showNav);

function showNav() {
  navElem.classList.toggle('active');
  if(navElem.classList.contains('active')) {
    navIcon.innerHTML = '<i class="fa-solid fa-xmark"></i>';
  }
  else {
    navIcon.innerHTML = '<i class="fa-solid fa-bars"></i>';
  }
}
/*
===========================
Dark Mode Settings
===========================
*/
const modeIcon = document.querySelector('.mode');
let bodyElem = document.body;

modeIcon.onclick = () => {
  modeIcon.classList.toggle('active');
  if(modeIcon.classList.contains('active')){
    modeIcon.innerHTML = '<i class="fa-solid fa-sun"></i>';
    modeIcon.style.color = 'orange';
    bodyElem.classList.add('active')
  }
  else {
    modeIcon.innerHTML = '<i class="fa-regular fa-moon"></i>';
    modeIcon.style.color = '#EFB223';
    bodyElem.classList.remove('active')
    
  }
  
}
/*
===========================
Dark Mode Settings
===========================
*/
let removeSkillElem = document.querySelector('.remove');
let skillElem = document.querySelector('.skills');
let informationBtn = document.querySelector('.cv-btn button');
let progressBars = document.querySelectorAll('.lang p');
let overlay = document.createElement('div');
overlay.classList.add('overlay');

informationBtn.addEventListener('click', function(){
  skillElem.classList.add('active');
  document.body.appendChild(overlay);
  progressBars.forEach((bar)=> {
    bar.style.animation = 'progress-anim  1s ease';
    bar.style.animationDelay = `calc(${bar.style.getPropertyValue('--var')} * -1.45s)`;
  })
})

removeSkillElem.addEventListener('click', function(){
  skillElem.classList.remove('active');
  overlay.remove();
})

document.addEventListener('click', function (event) {
  // Check if the click target is outside the skillElem
  if (!skillElem.contains(event.target) && !informationBtn.contains(event.target)) {
    skillElem.classList.remove('active');
     overlay.remove();
  }
});

/*
===========================
Form submission
===========================
*/
const formElem = document.getElementById('form');
const parElem = document.querySelector('.par-message');

formElem.onsubmit = (e)=> {
  e.preventDefault();
  parElem.innerHTML = 'Form Submission Successful';

  setTimeout(()=> {
    parElem.style.display = 'none';
  },2000)
}

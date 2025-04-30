let slideIndex = 0;
let slides = document.querySelectorAll(".slide");
let dots = document.querySelectorAll(".dot");

function showSlide(index) {
  slides.forEach((slide, i) => {
    slide.classList.remove('active');
    dots[i].classList.remove('active');
    if (i === index) {
      slide.classList.add('active');
      dots[i].classList.add('active');
    }
  });
}

// function showSlide(index) {
//   slides.forEach((slide, i) => {
//     if (i === index && !slide.classList.contains('active')) {
//       slide.classList.add('active');
//       dots[i].classList.add('active');
//     } else {
//       slide.classList.remove('active');
//       dots[i].classList.remove('active');
//     }
//   });
// }



function currentSlide(index) {
  slideIndex = index;
  showSlide(slideIndex);
}

function nextSlide() {
  slideIndex++;
  if (slideIndex >= slides.length) {
    slideIndex = 0;
  }
  showSlide(slideIndex);
}

setInterval(nextSlide, 5000); // Auto change every 5 seconds

// Show the first slide when the page loads
document.addEventListener("DOMContentLoaded", function () {
  showSlide(slideIndex);
});

var slides = document.querySelectorAll(".slide");
var btns = document.querySelectorAll("btn");
let currrentSlide = 1;

var manualNav = function (manual) {
    slides.forEach((slide) => {
        slide.classList.remove('active');
    });

    btns.forEach((slide) => {
            btn.classList.remove('active');
    });

    slides[manual].classList.add('active');
    btns[manual].classList.add('active');
}

btns.forEach((btn, 1) => {
    btn.addEventListener('click', () => {
        manualNav(i);
        currentSlide = i;
    })
})

var repeat = function (activeClass) {

    let active = document.getElementsByClassName('active');
    let i = 1;

    var repeater = () => {
        setTimeout(function () {
            [...active].forEach((activeSlide) => {
                activeSlide.classList.remove('active')
            });

            slides[i].classList.add('active');
            btns[i].classList.add('active');
            i++;
        })
    }
}
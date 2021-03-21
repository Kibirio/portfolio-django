

$(function ($) {
    "use strict";
    jQuery(document).ready(function () {

        // Typed js
        $(".typed").typed({
            strings: ["Web Developer.", "Graphic Designer.", "Freelancer."],
            // Optionally use an HTML element to grab strings from (must wrap each string in a <p>)
            stringsElement: null,
            // typing speed
            typeSpeed: 30,
            // time before typing starts
            startDelay: 500,
            // backspacing speed
            backSpeed: 20,
            // time before backspacing
            backDelay: 1200,
            // loop
            loop: true
        });
    });
    $('#testimonial-carousel').owlCarousel({
        autoplay:true,
        dots:false,
        loop:true,
        // margin:10,
        nav:true,
        navText: ['<i class="fas fa-angle-left"></i>', '<i class="fas fa-angle-right"></i>'],
        responsive:{
            0:{
                items:1
            },
            600:{
                items:1
            },
            1000:{
                items:2
            }
        }
    });

    $('#blog-carousel').owlCarousel({
        autoplay:true,
        dots:false,
        loop:true,
        margin:10,
        nav:true,
        // navText: ['<i class="fas fa-angle-left"></i>', '<i class="fas fa-angle-right"></i>'],
        responsive:{
            0:{
                items:1
            },
            600:{
                items:2
            },
            1000:{
                items:3
            }
        }
    });



    // $(window).on('load', function() {
    //     new WOW().init();
    // })


});
// window.sr = ScrollReveal();
//     sr.reveal('.icon-info', {
//     duration: 2000,
//     origin: 'top',
//     distance: '300px'
// });







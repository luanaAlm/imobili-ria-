$(document).ready(function(){
    /* ---Navbar--- */
    $(window).on("scroll", function(){
        if($(this).scrollTop() > 90){
            $(".navbar").addClass("navbar-shrink");
        }
        else{
            $(".navbar").removeClass("navbar-shrink")
        }
    });
    /* ---owl carousel depoiments--- */
    $('.depoiments-carousel').owlCarousel({
        loop:true,
        margin:0,
        autoplay:true,
        responsiveClass:true,
        responsive:{
            0:{
                items:1,
            },
            600:{
                items:2,
            },
            1000:{
                items:3,
            }
        }
    });

    /* ---owl carousel depoiments--- */
    $('.imoveis-carousel').owlCarousel({
        loop:true,
        margin:0,
        autoplay:true,
        responsiveClass:true,
        responsive:{
            0:{
                items:1,
            },
            600:{
                items:2,
            },
            1000:{
                items:3,
            }
        }
    });
    
    /* ---scrolling - scrollit --- */
    $(function(){
        $.scrollIt({
            topOffset: 0
        });
    });
    /* --- navbar - collapse --- */
    $(".nav-link").on("click", function(){
        $(".navbar-collapse").collapse("hide");
    });
    
    /* ---magnific-popup --- */
    $('.parent-container').magnificPopup({
        delegate: 'a', // child items selector, by clicking on it popup will open
        type: 'image',
        gallery:{enabled:true}
        // other options
    });
});
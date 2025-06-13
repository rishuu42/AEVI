(function($) {

  "use strict";

  var searchPopup = function() {
      // open search box
      $('.secondary-nav').on('click', '.search-button', function(e) {
        $('.search-popup').toggleClass('is-visible');
      });

      $('#header-nav').on('click', '.btn-close-search', function(e) {
        $('.search-popup').toggleClass('is-visible');
      });
      
      $(".search-popup-trigger").on("click", function(b) {
          b.preventDefault();
          $(".search-popup").addClass("is-visible"),
          setTimeout(function() {
              $(".search-popup").find("#search-popup").focus()
          }, 350)
      }),
      $(".search-popup").on("click", function(b) {
          ($(b.target).is(".search-popup-close") || $(b.target).is(".search-popup-close svg") || $(b.target).is(".search-popup-close path") || $(b.target).is(".search-popup")) && (b.preventDefault(),
          $(this).removeClass("is-visible"))
      }),
      $(document).keyup(function(b) {
          "27" === b.which && $(".search-popup").removeClass("is-visible")
      })
    }

  // Preloader
  var initPreloader = function() {
    $(document).ready(function($) {
    var Body = $('body');
        Body.addClass('preloader-site');
    });
    $(window).load(function() {
        $('.preloader-wrapper').fadeOut();
        $('body').removeClass('preloader-site');
    });
  }

  // init jarallax parallax
  var initJarallax = function() {
    jarallax(document.querySelectorAll(".jarallax"));

    jarallax(document.querySelectorAll(".jarallax-img"), {
      keepImg: true,
    });
  }

  // Tab Section
  var initTabs = function() {
    const tabs = document.querySelectorAll('[data-tab-target]')
    const tabContents = document.querySelectorAll('[data-tab-content]')

    tabs.forEach(tab => {
      tab.addEventListener('click', () => {
        const target = document.querySelector(tab.dataset.tabTarget)
        tabContents.forEach(tabContent => {
          tabContent.classList.remove('active')
        })
        tabs.forEach(tab => {
          tab.classList.remove('active')
        })
        tab.classList.add('active')
        target.classList.add('active')
      })
    });
  }

  // document ready
  $(document).ready(function() {
    searchPopup();
    initPreloader();
    initTabs();
    initJarallax();

    jQuery(document).ready(function($) {
      jQuery('.stellarnav').stellarNav({
        position: 'right'
      });
    });

    $(".user-items .icon-search").click(function(){
      $(".search-box").toggleClass('active');
      $(".search-box .search-input").focus();
    });
    $(".close-button").click(function(){
      $(".search-box").toggleClass('active');
    });

    var swiper = new Swiper(".main-swiper", {
      speed: 500,
      loop: true,
      navigation: {
        nextEl: ".button-next",
        prevEl: ".button-prev",
      },
      pagination: {
        el: "#billboard .swiper-pagination",
        clickable: true,
      },
    });

    var swiper = new Swiper(".two-column-swiper", {
      speed: 500,
      loop: true,
      navigation: {
        nextEl: ".button-next",
        prevEl: ".button-prev",
      },
    });

    var swiper = new Swiper("#featured-products .product-swiper", {
      pagination: {
        el: "#featured-products .swiper-pagination",
        clickable: true,
      },
      breakpoints: {
        0: {
          slidesPerView: 1,
          spaceBetween: 30,
        },
        768: {
          slidesPerView: 2,
          spaceBetween: 30,
        },
        999: {
          slidesPerView: 3,
          spaceBetween: 30,
        },
        1299: {
          slidesPerView: 4,
          spaceBetween: 30,
        },
      },
    });

    var swiper = new Swiper("#featured-products .product-swiper-two", {
      pagination: {
        el: "#featured-products .swiper-pagination",
        clickable: true,
      },
      breakpoints: {
        0: {
          slidesPerView: 1,
          spaceBetween: 30,
        },
        768: {
          slidesPerView: 2,
          spaceBetween: 30,
        },
        999: {
          slidesPerView: 4,
          spaceBetween: 30,
        },
        1299: {
          slidesPerView: 5,
          spaceBetween: 30,
        },
      },
    });

    var swiper = new Swiper("#flash-sales .product-swiper", {
      pagination: {
        el: "#flash-sales .product-swiper .swiper-pagination",
        clickable: true,
      },
      breakpoints: {
        0: {
          slidesPerView: 1,
          spaceBetween: 30,
        },
        768: {
          slidesPerView: 2,
          spaceBetween: 30,
        },
        999: {
          slidesPerView: 3,
          spaceBetween: 30,
        },
        1299: {
          slidesPerView: 4,
          spaceBetween: 30,
        },
      },
    });

    var swiper = new Swiper(".testimonial-swiper", {
      loop: true,
      navigation: {
        nextEl: ".next-button",
        prevEl: ".prev-button",
      },
    });

    var thumb_slider = new Swiper(".thumb-swiper", {
      slidesPerView: 1,
    });
    var large_slider = new Swiper(".large-swiper", {
      spaceBetween: 10,
      effect: 'fade',
      thumbs: {
        swiper: thumb_slider,
      },
    });

    // Initialize Isotope
    var $grid = $('.entry-container').isotope({
      itemSelector: '.entry-item',
      layoutMode: 'masonry'
    });
    $grid.imagesLoaded().progress(function() {
      $grid.isotope('layout');
    });

    $(".gallery").colorbox({
      rel:'gallery'
    });
    
    $(".youtube").colorbox({
      iframe: true,
      innerWidth: 960,
      innerHeight: 585,
    });

  });

})(jQuery);


//Carousel
  
  window.addEventListener('scroll', function() {
    const logoCarousel = document.getElementById('aevi-logo-carousel');
    const stickyLogo = document.querySelector('.logo-sticky');
    const navBar = document.getElementById('main-nav-bar');
    const scrollTop = window.scrollY;

    if (scrollTop > document.getElementById('main-nav-bar').offsetTop) {
      if (logoCarousel) logoCarousel.style.opacity = '0';
      if (stickyLogo) stickyLogo.style.display = 'block';
      navBar.classList.add('sticky');
    } else {
      if (logoCarousel) logoCarousel.style.opacity = '1';
      if (stickyLogo) stickyLogo.style.display = 'none';
      navBar.classList.remove('sticky');
    }
  });


  document.addEventListener("DOMContentLoaded", function () {
    const primaryBanner = document.querySelector(".primary-banner");
    primaryBanner.addEventListener("mouseenter", () => {
      document.body.classList.add("hovering-primary-banner");
    });
    primaryBanner.addEventListener("mouseleave", () => {
      document.body.classList.remove("hovering-primary-banner");
    });
  });


      const messages = [
        "BEST FACE OIL OF 2024 | NOURISHING FACE OIL",
        "VEGAN & CRUELTY FREE | SUSTAINABLY SOURCED",
        "FREE SHIPPING OVER €50 | WORLDWIDE DELIVERY"
      ];
      let i = 0;

      setInterval(() => {
        const el = document.getElementById("rotating-msg");
        el.style.opacity = 0;
        setTimeout(() => {
          el.textContent = messages[i = (i + 1) % messages.length];
          el.style.opacity = 1;
        }, 500);
      }, 4000);
      const headerWrap = document.getElementById('header-wrap');
      const primaryNav = document.querySelector('.primary-nav');
      const secondaryNav = document.querySelector('.secondary-nav');

      if (primaryNav) {
        primaryNav.addEventListener('mouseenter', () => primaryNav.classList.add('hovered'));
        primaryNav.addEventListener('mouseleave', () => primaryNav.classList.remove('hovered'));
      }

      if (secondaryNav) {
        secondaryNav.addEventListener('mouseenter', () => secondaryNav.classList.add('hovered'));
        secondaryNav.addEventListener('mouseleave', () => secondaryNav.classList.remove('hovered'));
      }

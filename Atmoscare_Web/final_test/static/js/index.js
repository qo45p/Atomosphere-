$(document).ready(function() {
  n = 1
  moving = 0
  $(window).mousewheel(function(event) {
    $("html,body").stop()
    if (moving == 1) {
      event.preventDefault();
    } else {
      if (event.deltaY == -1) {
        if (n < 2) {
          n++;
        }
      } else if (event.deltaY == 1) {
        if (n > 1) {
          n--;
        }
      }
    }
    if ($(document).scrollTop() < $(window).height() - 70 && $(window).width() > 993 && $('#loginmodal').hasClass('open') == false) {
      moving = 1
      if (n == 2) {
        $('html, body').animate({
          scrollTop: $(window).height() - 69
        }, 450, 'easeInOutQuad', function() {
          moving = 0
        });
      } else {
        $('html, body').animate({
          scrollTop: 0
        }, 450, 'easeInOutQuad', function() {
          moving = 0
        });
      }
    }
  })
  $('#pc').height($(window).height() - 70);
  $('.parallax').parallax();
  $('.button-collapse').sideNav({
    menuWidth: 240, // Default is 240
    edge: 'left', // Choose the horizontal origin
    closeOnClick: true // Closes side-nav on <a> clicks, useful for Angular/Meteor
  });
  $('.scrollspy').scrollSpy();
  $('ul.tabs').tabs();
  $('select').material_select();
  $('#getApp').on('click', function(event) {
    event.preventDefault();
    $('html, body').animate({
      scrollTop: $('#download').offset().top - 140
    }, 800);
  });
  $('#mobileGetApp').on('click', function(event) {
    var target = $('#download').offset().top - 70;
    event.preventDefault();
    $('html, body').animate({
      scrollTop: target + 30
    }, 800);
  });
  $('#toVideo').on('click', function(event) {
    event.preventDefault();
    $('html, body').animate({
      scrollTop: $(window).height() - 70
    }, 500);
  });
  if ($(window).width() > 993) {
    $('#main_container').css('top', 21);
  }

});
$(window).load(function() {
  $('#video .card.video.white.hoverable.z-depth-2').css("height", $('.responsive-video').height() - 1);
  $('.dropdown-content.select-dropdown').css({
    'max-height': $(window).height() / 3
  });
});
$('.modal-content').scroll(function() {
  var modal_content = $('.modal-content').scrollTop();
  console.log(modal_content);
  var total = $('#getModalHeight').height() - $('#getContentHeight').height() + 30;
  console.log(total);
  if (modal_content / total <= 1) {
    $('#progressBar').css('width', ((modal_content) / total * 0.8 + 0.2) * 100 + '%');
  }
});
$('#noID').click(function() {
  $('#progressBar').css('display', 'none');
});
$('#withID').click(function() {
  $('#progressBar').css('display', 'block');
});

$('.modal-trigger').on('click', function(event) {
  setTimeout(function() {
    $('.indicator').css({
      'right': $('.tab.col.s3').width(),
      'left': 0
    });
  }, 300);
  $('.modal.modal-fixed-footer').height(500);
});
$('#morebtn').on('click', function(event) {
  event.preventDefault();
  $('html, body').animate({
    scrollTop: $(window).height() - 70
  }, 800);
});
$('#lessbtn').on('click', function(event) {
  event.preventDefault();
  $('html, body').animate({
    scrollTop: 0
  }, 800);
});
$('#logo').on('click', function(event) {
  event.preventDefault();
  $('html, body').animate({
    scrollTop: 0
  }, 800);
});
$(document).scroll(function() {
  var x = $(window).height() - 71
  var y = $(this).scrollTop();
  if (y > x) {
    $('#fixNav').css({
      'position': 'fixed',
      'top': 0,
      'width': '100%',
      'z-index': 99
    });
    $('#main_container').css('top', 99);
    if ($(window).width() > 993) {
      $('.col.hide-on-med-and-down.l3').css({
        'position': 'fixed',
        'top': '160px'
      });
    }
  } else {
    $('#fixNav').css({
      'position': 'initial',
      'top': 0
    });
    $('#main_container').css('top', 21);
    if ($(window).width() > 993) {
      $('.col.hide-on-med-and-down.l3').css({
        'position': 'absolute',
        'top': '70px'
      });
    }
  }
  if ($(window).width() > 993) {
    if (y > x) {
      $('#morebtn').fadeOut("fast", function() {
        $(this).css({
          display: "none"
        });
      });
      $('#logo').fadeIn("fast", function() {
        $(this).css({
          display: "initial"
        });
      });
    } else {
      $('#morebtn').fadeIn("fast", function() {
        $(this).css({
          display: "initial"
        });
      });
      $('#logo').fadeOut("fast", function() {
        $(this).css({
          display: "none"
        });
      });
    }
  } else {
    if (y > x) {
      $('#morebtn').fadeOut("fast", function() {
        $(this).css({
          display: "none"
        });
      });
      $('#lessbtn').fadeIn(50, function() {
        $(this).css({
          display: "initial"
        });
      });
      $('#main_container').fadeIn(50, function() {
        $(this).css({
          top: "95px"
        });
      });
    } else {
      $('#morebtn').fadeIn("fast", function() {
        $(this).css({
          display: "initial"
        });
      });
      $('#lessbtn').fadeOut("fast", function() {
        $(this).css({
          display: "none"
        });
      });
      $('#main_container').fadeIn("fast", function() {
        $(this).css({
          top: "25px"
        });
      });
    }
  }
});
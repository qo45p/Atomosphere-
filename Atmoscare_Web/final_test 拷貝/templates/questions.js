$(document).ready(function() {
  $('.modal-trigger').leanModal();
  $('.button-collapse').sideNav({
      menuWidth: 240, // Default is 240
      edge: 'left', // Choose the horizontal origin
      closeOnClick: true // Closes side-nav on <a> clicks, useful for Angular/Meteor
    }

  );
  setSrc();
  var card_height = $('#weather-row').height();
  var forecast_height = $('#forecast').height();
  var outter_forecast_height = $('#outter-forecast').height();
  var card_width = $('.weather-img').width();
  $('.weather-img').css({
    'margin-top': (card_height - card_width - 65) / 2
  });
  $('#forecast').css({
    'padding-top': (card_height - forecast_height) / 2
  });
  $('#forecast_p').css({
    'padding-top': outter_forecast_height - 25
  });
  $('#pm25-value').css({
    'padding-top': (card_height - 49) / 2,
    'padding-bottom': (card_height - 49) / 2
  });
  $('#pm25-title').css({
    'margin-top': (card_height - 26) / 2
  });
});

function setSrc() {
  if ($(window).width() > 993) {
    $('#systemQuestionImg').attr('src', '{% static "images/question/pcSystemQuestions.png" %}');
  } else if ($(window).width() > 600) {
    $('#systemQuestionImg').attr('src', '{% static "images/question/padSystemQuestions.png" %}');
  } else {
    $('#systemQuestionImg').attr('src', '{% static "images/question/mobileSystemQuestions.png" %}');
  }
}
$("#systemCard").click(function() {
  $('#systemModal').openModal();
});
$("#medicalCard").click(function() {
  $('#medicalModal').openModal();
});
// Hide Header on on scroll down
var didScroll;
var lastScrollTop = 0;
var delta = 5;
var navbarHeight = $('nav').outerHeight();

$(window).scroll(function(event) {
  didScroll = true;
});

setInterval(function() {
  if (didScroll) {
    hasScrolled();
    didScroll = false;
  }
}, 250);

function hasScrolled() {
  var st = $(this).scrollTop();

  // Make sure they scroll more than delta
  if (Math.abs(lastScrollTop - st) <= delta)
    return;

  // If they scrolled down and are past the navbar, add class .nav-up.
  // This is necessary so you never see what is "behind" the navbar.
  if (st > lastScrollTop && st > navbarHeight) {
    // Scroll Down
    $('nav').removeClass('nav-down').addClass('nav-up');
  } else {
    // Scroll Up
    if (st + $(window).height() < $(document).height()) {
      $('nav').removeClass('nav-up').addClass('nav-down');
    }
  }

  lastScrollTop = st;
}
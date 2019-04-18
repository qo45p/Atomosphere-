$(document).ready(function() {
  $('.button-collapse').sideNav({
    menuWidth: 240, // Default is 240
    edge: 'left', // Choose the horizontal origin
    closeOnClick: true // Closes side-nav on <a> clicks, useful for Angular/Meteor
  });
});
$(window).load(function() {
  var card_height = $('#weather-row').height();
  var forecast_height = $('#forecast').height();
  var outter_forecast_height = $('#outter-forecast').height();
  var card_width = $('.weather-img').width();
  $('.weather-img').css({
    'margin-top': (card_height - card_width - 45) / 2
  });
  $('.weather-img').css({
    'padding-left': ($('#forecast').width() / 2) - card_width / 2
  });
  $('#forecast_p').css({
    'padding-left': ($('#forecast').width() / 2) / 2
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
  if ($(window).width() > 1109) {
    $('#forecast_p').css({
      'font-size': '24px'
    });
  } else if ($(window).width() > 1071) {
    $('#forecast_p').css({
      'font-size': '22px'
    });
  } else if ($(window).width() > 753) {
    $('#forecast_p').css({
      'font-size': '20px'
    });
  } else if ($(window).width() > 699) {
    $('#forecast_p').css({
      'font-size': '18px'
    });
  } else if ($(window).width() > 658) {
    $('#forecast_p').css({
      'font-size': '16px'
    });
  } else if ($(window).width() > 601) {
    $('#forecast_p').css({
      'font-size': '14px'
    });
  } else if ($(window).width() > 600) {
    $('#forecast_p').css({
      'font-size': '26px'
    });
  } else if ($(window).width() > 427) {
    $('#forecast_p').css({
      'font-size': '24px'
    });
  } else if ($(window).width() > 406) {
    $('#forecast_p').css({
      'font-size': '22px'
    });
  } else if ($(window).width() > 375) {
    $('#forecast_p').css({
      'font-size': '20px'
    });
  } else if ($(window).width() > 325) {
    $('#forecast_p').css({
      'font-size': '18px'
    });
  } else {
    $('#forecast_p').css({
      'font-size': '16px'
    });
  }
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

var bar = new ProgressBar.Circle(container1, {
  color: '{{OverallColor}}',
  trailColor: '#ff',
  trailWidth: 1,
  duration: 1400,
  easing: 'bounce',
  strokeWidth: 5,
  from: {
    color: '{{OverallColor}}'
  },
  to: {
    color: '{{OverallColor}}'
  },
  // Set default step function for all animate calls
  step: function(state, circle) {
    circle.path.setAttribute('stroke', state.color);
    var value = Math.round(circle.value() * 100);
    circle.setText('{{OverallState}}');
  }
});

bar.animate({
  {
    OverallRisk
  }
});

var bar = new ProgressBar.Line(container2, {
  strokeWidth: 7,
  easing: 'easeInOut',
  duration: 1400,
  color: '{{StrokeColor}}',
  trailColor: '#eee',
  trailWidth: 7,
  svgStyle: {
    width: '100%',
    height: '100%'
  }
});

bar.animate({
  {
    StrokeRisk
  }
});

var bar = new ProgressBar.Line(container3, {
  strokeWidth: 7,
  easing: 'easeInOut',
  duration: 1400,
  color: '{{HeartColor}}',
  trailColor: '#eee',
  trailWidth: 7,
  svgStyle: {
    width: '100%',
    height: '100%'
  }
});

bar.animate({
  {
    userHeartRisk
  }
});

var bar = new ProgressBar.Line(container4, {
  strokeWidth: 7,
  easing: 'easeInOut',
  duration: 1400,
  color: '{{HFColor}}',
  trailColor: '#eee',
  trailWidth: 7,
  svgStyle: {
    width: '100%',
    height: '100%'
  }
});

bar.animate({
  {
    HFRisk
  }
});

var bar = new ProgressBar.Line(container5, {
  strokeWidth: 7,
  easing: 'easeInOut',
  duration: 1400,
  color: '{{AFColor}}',
  trailColor: '#eee',
  trailWidth: 7,
  svgStyle: {
    width: '100%',
    height: '100%'
  }
});

bar.animate({
  {
    AFRisk
  }
});
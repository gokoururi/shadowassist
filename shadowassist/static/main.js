function onLoad() {
    $('.overlay-card').on('click touch', preventCloseOverlay)
    $('.card').on('click touch', openOverlay);
    $('.overlay').on('click touch', closeOverlay);
    $('input[name="spellcasting"]').change(setSuccess);
    $('input[name="resistance"]').change(setResistance);
    $('#potency').on('click touch', createPrep);
    $('a[name=prepActivate]').on('click touch', prepActivate);
    $('a[name=prepStow]').on('click touch', prepStow);
    $('a[name=prepTake]').on('click touch', prepTake);
    $('a[name=prepDelete]').on('click touch', prepDelete);
    $('a.fa-bars').on('click touch', openMenue);
    $('.saMenueOverlay').on('click touch', closeMenue);
    $('.saDmgBtn').on('click touch', controlDmg);
    $('.saStatsBtn').on('click touch', controlStats);
}

function controlStats(event) {
  var stat = event.target.name;
  var char_id = event.target.id;
  if (stat == "essence") {
    var action = "set"
    var newValue = $("input[name=essence]").val();
    var origin = parseFloat($('div[name=essence]').text());
    var displayTarget = $("input[name=essence]");
    var urlTarget = '/character/' + char_id + '/stat/' + stat + '/' + action + '/' + newValue
  } else {
    var text = event.target.text;
    var origin = parseInt($('td[name=' + stat + '].saStatsOrigin').text());
    var value = parseInt($('td[name=' + stat + '].saStatsDisplay').text());
    var displayTarget = 'td[name=' + stat + '].saStatsDisplay'
    if ( text == "+1") {
      var action = "increase";
      var newValue = value + 1;
    } else if ( text == "-1") {
      var action = "decrease";
      var newValue = value - 1;
    }
    var urlTarget = '/character/' + char_id + '/stat/' + stat + '/' + action
  }
  $.getJSON(
    $SCRIPT_ROOT + urlTarget, function(data) {
      $(displayTarget).text(newValue);
      $(displayTarget).addClass("text-success");
      $(displayTarget).addClass("font-weight-bold");
      if (newValue > origin) {
        $(displayTarget).removeClass("text-danger");
        $(displayTarget).addClass("text-success");
        $(displayTarget).addClass("font-weight-bold");
      } else if (newValue < origin) {
        $(displayTarget).addClass("text-danger");
        $(displayTarget).removeClass("text-success");
        $(displayTarget).addClass("font-weight-bold");

      } else if (newValue == origin) {
        $(displayTarget).removeClass("text-danger");
        $(displayTarget).removeClass("text-success");
        $(displayTarget).removeClass("font-weight-bold");
      }
    });
}

function controlDmg(event) {
  var value = event.target.text;
  var type = event.target.name;
  var char_id = event.target.id;
  if (value == "+1") {
    changeDamage(char_id, type, "increase");
  } else if (value == "-1") {
    changeDamage(char_id, type, "decrease");
  }
}

function changeDamage(char_id, type, action) {
  $.getJSON(
    $SCRIPT_ROOT + '/character/' + char_id + '/damage/' + type + '/' + action, function(data) {
      updateDamageBoxes(type, data.damage, data.maxDamage);
    }
  )
}

function updateDamageBoxes(type, damage, maxDamage) {
    for (i = 1; i <= maxDamage;i++) {
        if (i <= damage) {
            $('#' + type + i).css("display", "block");
        } else {
            $('#' + type + i).css("display", "none");
        }
    }
}

function openMenue() {
  $('.saMenue').css("left", "0");
  $('.saMenueOverlay').css("display", "block");
}
function closeMenue() {
  $('.saMenue').css("left", "-500px");
  $('.saMenueOverlay').css("display", "none");
}
function prepTake() {prepChange(2);}
function prepStow() {prepChange(1);}
function prepActivate() {prepChange(0);}

function prepChange(state) {
  var prepId = $('#overPrep.id').text()
  $.getJSON(
    $SCRIPT_ROOT + '/prepChange/state/' + prepId + '/' + state, function(jqXHR) {
      location.reload()
    }
  )
}

function prepDelete() {
  var prepId = $('#overPrep.id').text()
  $.getJSON(
    $SCRIPT_ROOT + '/prepChange/delete/' + prepId, function(jqXHR) {
      location.reload()
    }
  )
}

function createPrep() {
  var spell =$('#spell').text();
  var container =$('#container').text();
  var trigger =$('#trigger').text();
  var force =$('#force').text();
  var success = $('#success').text();
  var resistance = $('#resistance').text();
  if ( success < resistance ) {
    var potency = 0;
  } else {
    var potency = success - resistance;
  }
  window.location.replace($SCRIPT_ROOT + '/createPrep/' + spell + '/' + container + '/' + trigger + '/' + force + '/' + potency)
}

function setSuccess() {
  var success = $('input[name="spellcasting"]:checked').val();
  var resistance = $('#resistance').text();
  if ( success < resistance ) {
    var potency = 0;
  } else {
    var potency = success - resistance;
  }
  $('#success').text(success);
  $('#potency').text(potency);

}

function setResistance() {
  var success = $('#success').text();
  var resistance = $('input[name="resistance"]:checked').val();
  if ( success < resistance ) {
    var potency = 0;
  } else {
    var potency = success - resistance;
  }
  $('#resistance').text(resistance);
  $('#potency').text(potency);
}

function preventCloseOverlay(event) {
  event.stopPropagation();
}

function openOverlay(event) {
  var name = $('#'+event.target.id+'.name').text();
  var force = $('#'+event.target.id+'.force').text();
  var potency = $('#'+event.target.id+'.potency').text();
  var bonus = $('#'+event.target.id+'.bonus').text();
  var container = $('#'+event.target.id+'.cont').text();
  var trigger = $('#'+event.target.id+'.trigger').text();
  var state = $('#'+event.target.id+'.state').text();
  var id = $('#'+event.target.id+'.id').text();
  var badge = $('#'+event.target.id+'.badge').text();
  if (state == 0) {
    $('#overPrep.card').addClass('bg-dark')
    $('#overPrep.card').addClass('text-white')
    $('#overPrep.card').removeClass('bg-secondary')
    $('#overPrep.card').removeClass('card-active')
  } else if (state == 1) {
    $('#overPrep.card').removeClass('bg-dark')
    $('#overPrep.card').addClass('text-white')
    $('#overPrep.card').addClass('bg-secondary')
    $('#overPrep.card').removeClass('card-active')
  } else if (state == 2) {
    $('#overPrep.card').removeClass('bg-dark')
    $('#overPrep.card').removeClass('text-white')
    $('#overPrep.card').removeClass('bg-secondary')
    $('#overPrep.card').addClass('card-active')
  }

  $('#overPrep.name').text(name);
  $('#overPrep.force').text(force);
  $('#overPrep.potency').text(potency);
  $('#overPrep.bonus').text(bonus);
  $('#overPrep.cont').text(container);
  $('#overPrep.trigger').text(trigger);
  $('#overPrep.state').text(state);
  $('#overPrep.id').text(id);
  $('#overPrep.badge').text(badge);
  $('.overlay').css("display", "block");
}

function closeOverlay() {
  $('.overlay').css("display", "none");
}

$(onLoad);

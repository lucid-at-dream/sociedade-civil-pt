function sendShout() {
    $('#shout-btn').attr('disabled', true);

    $.ajax({
      url: '/shout',
      type: 'PUT',
      data: {
        'shout': $('#shout').val()
      },
      complete: function (result) {
        $('#shout-btn').attr('disabled', false);
      },
      success: function (result) {
        $('#shout').val("");
      }
    });
  }

  function getShouts() {

    $.ajax({
      url: '/shout',
      type: 'GET',
      success: function (result) {
        d3.select("#shouts")
          .selectAll('div')
          .data(result)
          .enter()
          .append('div')
          .attr('class', 'shout-row')
          .append('a')
          .text(function (d) { return d; })
          .append('br');
      }
    })
  }

  function listenForShouts(data) {
    if (data == undefined || data.length == 0) {
      return;
    }

    d3.select("#shouts")
      .selectAll('div')
      .data(data)
      .enter()
      .append('a')
      .text(function (d) { return d; })
      .append('br');

    numElements = d3.select("#shouts")
      .selectAll('a')
      .size();

    if (numElements > 1500) {
      d3.select('#shouts a:first-child')
        .remove()
    }

    var scrollDown = ($("#shouts")[0].scrollHeight - $("#shouts")[0].scrollTop) <= 400;
    if (scrollDown) {
      $("#shouts").scrollTop($("#shouts")[0].scrollHeight);
    }
  }

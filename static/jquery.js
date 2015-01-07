$(function () {
    var store_like = function(e) {
      $.getJSON($SCRIPT_ROOT + '/_like', 
        {image_id: e.val() }, 
        function(data) { 
            e.text(data.result); 
        }
      );
      return false;
    };

    //FIXME: how to get the id of the particular link
    $('a#').bind('click', store_like($(this)));

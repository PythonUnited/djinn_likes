// djinn_likes namespace
if (djinn_likes == undefined) {
  var djinn_likes = {};
}

// Our own namespace
djinn_likes['likes'] = {};

djinn_likes.likes.handle_like_action = function(tgt){
    // this will be called as callback from the 'like' button

    $.get('/djinn_likes/likes?' + tgt.data('pu_actiondata'), function(data, status, xhr) {

    if (xhr.status == 202) {
      // nasty
    } else {
      $("#" + tgt.data('pu_clear_id')).replaceWith(data);
    }
  });
};

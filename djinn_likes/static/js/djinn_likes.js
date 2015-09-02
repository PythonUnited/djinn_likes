// djinn_likes namespace
if (djinn_likes == undefined) {
  var djinn_likes = {};
}

// Our own namespace
djinn_likes['likes'] = {};

djinn_likes.likes.handle_like_action = function(tgt){
    // there is no auto-update for this field right now, so remove it...
    $('.update-like-info').remove();
};

/**
 * Bind events for likes. Do this as 'delegate' events on the document.
 */
djinn_likes.likes.bind_events = function() {

  $("body").on("click", "#update-like-action", function(e) {
      return djinn_likes.likes.handle_like_action($(e.target));
    });

};

$(document).ready(function() {
    
    djinn_likes.likes.bind_events();

  });

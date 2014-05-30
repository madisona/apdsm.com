
// Gets 4 digit year
function getYear() {
    return new Date().getFullYear();
}


// makes external links open in new window
(function($) {
    $(document).ready(function() {
        $(".external_link").click(function(event) {
            event.preventDefault();
            event.stopPropagation();
            window.open(this.href, '_blank');
        });
    });
})(jQuery);

// Moves left nav bar over to the right on small screens so main content
// shows first.
(function ($) {
    move60();
    var sidebar_id = "#mobilemove";
    var content_id = "#placeholder";

    //751 instead of 767 to account for 16px in the right vertical scroll bar
    $(window).resize(function() {
        if ($(window).width() < 751) {
            $(sidebar_id).insertAfter(content_id);
        }
        else{
            $(sidebar_id).insertBefore(content_id);
        }
    });

    function move60() {
        if ($(window).width() < 751) {
            $(sidebar_id).insertAfter(content_id);
        };
    };
})(jQuery);

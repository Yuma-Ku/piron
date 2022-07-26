$(function () {

    $("#btn-create-post").click(function () {
        window.location.href = "/create/post";
    });

    $("#btn-create-live").click(function () {
        window.location.href = "/create/live";
    });

});


/*
/create/post
*/

$(function () {

    $("#prev-post").click(function () {
        $(".tab-content .tab-pane").removeClass("active");
        $(".tab-content  .tab-pane:nth-child(1)").addClass("active");
        $(this).removeClass("d-none");
    });

    $("#next-post").click(function () {
        $(".tab-content .tab-pane").removeClass("active");
        $(".tab-content  .tab-pane:nth-child(2)").addClass("active");
        $("#prev-post").removeClass("d-none");
    });

});


/*
/create/live
*/

$(function () {

    $("#prev-live").click(function () {
        $(".tab-content .tab-pane").removeClass("active");
        $(".tab-content  .tab-pane:nth-child(1)").addClass("active");
        $(this).removeClass("d-none");
    });

    $("#next-live").click(function () {
        $(".tab-content .tab-pane").removeClass("active");
        $(".tab-content  .tab-pane:nth-child(2)").addClass("active");
        $("#prev-live").removeClass("d-none");
    });

});



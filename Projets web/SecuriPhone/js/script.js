//partie index.html
$(document).ready(
    function() {
        $("#popover_menu").hide();
        $('#popover_click_menu').click(
            //menu
            function () {
                $("#popover_menu").show();
            }
        );

        $("#close_popover").click(
            function () {
                $("#popover_menu").hide();
            }
        );

        const menu = document.getElementById("liens");
        if (menu.classList == "hidden2")
        {
            menu = () => empty();
        }
    }
);
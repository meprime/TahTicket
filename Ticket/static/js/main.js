/*price range*/

$('#sl2').slider();

var RGBChange = function () {
    $('#RGB').css('background', 'rgb(' + r.getValue() + ',' + g.getValue() + ',' + b.getValue() + ')')
};

/*scroll to top*/

$(document).ready(function () {
    $(function () {
        $.scrollUp({
            scrollName: 'scrollUp', // Element ID
            scrollDistance: 300, // Distance from top/bottom before showing element (px)
            scrollFrom: 'top', // 'top' or 'bottom'
            scrollSpeed: 300, // Speed back to top (ms)
            easingType: 'linear', // Scroll to top easing (see http://easings.net/)
            animation: 'fade', // Fade, slide, none
            animationSpeed: 200, // Animation in speed (ms)
            scrollTrigger: false, // Set a custom triggering element. Can be an HTML string or jQuery object
            //scrollTarget: false, // Set a custom target element for scrolling to the top
            scrollText: '<i class="fa fa-angle-up"></i>', // Text for element, can contain HTML
            scrollTitle: false, // Set a custom <a> title if required.
            scrollImg: false, // Set true to use image
            activeOverlay: false, // Set CSS color to display scrollUp active point, e.g '#00FFFF'
            zIndex: 2147483647 // Z-Index for the overlay
        });
    });


});

function changeGroup(group) {
    document.getElementById('groups').innerHTML = document.getElementById('group_' + group).innerHTML;
    document.getElementById('group').value = group;
}

function getXmlHttpObject() {
    var xmlhttp;
    if (window.XMLHttpRequest)
    {// code for IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp = new XMLHttpRequest();
    }
    else
    {// code for IE6, IE5
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    return xmlhttp;
}

function addToCart(pid,count) {
    xmlhttp = getXmlHttpObject();
    xmlhttp.onreadystatechange = function ()
    {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200)
        {
            alert(xmlhttp.responseText);
        }
    }
    xmlhttp.open("GET", "addToCart.php?pid=" + pid + '&count=' + count, true);
    xmlhttp.send();
}

function addToCartWithOutAlert(pid,count) {
    xmlhttp = getXmlHttpObject();
    xmlhttp.open("GET", "addToCart.php?pid=" + pid + '&count=' + count, true);
    xmlhttp.send();
}

function saveCart(){
    n = document.getElementById('count').value;
    for(i = 1; i <= n; i++){
        pid = document.getElementById('pid' + i).innerHTML;
        pcount = document.getElementById('count' + i).value;
        addToCartWithOutAlert(pid,pcount);
    }
}
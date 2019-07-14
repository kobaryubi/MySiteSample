function getCookie(name){
    var cookieValue = null;
    if (document.cookie && document.cookie !== ''){
        var cookies = document.cookie.split(';');
        for (var i=0; i<cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }

    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    return (/^csrfSafeMethod(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

class PageTransferor {
    constructor() {
    }

    transfer_to(url) {
        location.href = url;
    }
}


class DateGetter {
    constructor() {
        this.now = new Date();
        this.year = this.now.getFullYear();
        this.month = this.now.getMonth() + 1;
        this.day = this.now.getDate();

        this.weeks = new Array(
            "Sunday",
            "Monday",
            "Friday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday"
        );
        this.week = this.weeks[this.now.getDay()];
        this.hour = this.now.getHours();
        this.min = this.now.getMinutes();
        this.sec = this.now.getSeconds();
    }

    set setMonth(value) {
        this.month = value;
    }

    get getMonth() {
        return this.month;
    }

    set setDay(value) {
        this.day = value;
    }

    get getDay() {
        return this.day;
    }

    getDateStr() {
        var day = this.day;
        var month = this.month;

        if (this.month < 10) {
            month = "0" + this.month;
        }
        if (this.day < 10) {
            day = "0" + this.day;
        }
        return this.year + '/' + month + '/' + day;
    }
}


$(function() {
    var $todayMainHeader = $("#js-todayMainHeader");
    var dateGetter = new DateGetter();
//    alert(dateGetter.getDateStr());
//    alert($todayMainHeader.text());
//    $todayMainHeader.text(dateGetter.getDateStr());

    var url = location.href;
    // if here is signin page, hide main header.
    if (url.indexOf("/accounts/login") != -1) {
        var $navMainHeader = $("#js-navMainHeader");
        $navMainHeader.hide();
    }
});
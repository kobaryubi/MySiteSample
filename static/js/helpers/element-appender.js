function appendScript(url) {
    var elem = document.createElement('script');
    elem.src = url;
    document.body.appendChild(elem);
}

function appendCss(url) {
    var elem = document.createElement('link');
    elem.href = url;
    elem.rel = 'stylesheet';
    elem.type = 'text/css';
    document.getElementsByTagName('head')[0].appendChild(elem);
}
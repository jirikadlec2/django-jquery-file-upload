console.log("init.js");
document.addEventListener("DOMContentLoaded", function () {
    console.log("DOMContentLoaded");
    //"use strict";
    var dj;
    if (new Resumable().support) {
        console.log("django resumable starting!");
        dj = new DjangoResumable();
    } else {
        console.log("django resumable has problem");
    }
});

$(document).ready(function (){
    $("#btn-learn-next").click(function(){
        console.log("click!!")
        location.replace(learn["button_href"])
    });
})
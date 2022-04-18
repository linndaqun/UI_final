$(document).ready(function (){
    $("#btn-learn-next").click(function(){
        console.log("click!!")
        location.replace(learn["button_href"])
    });
    for (let cur in learn["slides"]){
        let curr = learn["slides"][cur]
        console.log(curr["title"], curr["description"], curr["img_url"])
        console.log(cur)
        if (cur == 0){
            var newcarousel = $("<div class='carousel-item active'>")
        }
        else {
            var newcarousel = $("<div class='carousel-item'>")
        };
        let newimg = $("<img class='d-block w-100' alt='...'>")
        let newtext = $("<div class='carousel-caption d-none d-md-block'>")
        let newtitle = $("<h5 style='color:blue;'>").append(curr["title"])
        let newdescript = $("<p style='color:blue;'>").append(curr["description"])
        newtext.append(newtitle)
        newtext.append(newdescript)
        newimg.attr("src", curr["img_url"])
        newcarousel.append(newimg)
        newcarousel.append(newtext)
        console.log(newcarousel)
        $("#carousel-learn-inner").append(newcarousel)
    }
})
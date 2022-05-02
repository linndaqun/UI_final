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
        // let newtext = $("<div class='carousel-caption d-none d-md-block'>")
        let newtitle = $("<h5 class='card-subtitle' style='color:white;'>").append(curr["title"])
        let newdescript = $("<p class='tutorial-text' style='color:white;'>").append(curr["description"])
        // newtext.append(newtitle)
        // newtext.append(newdescript)
        newimg.attr("src", curr["img_url"])
        newcarousel.append(newimg)
        let newblock = $("<p id='block-under-image'>")
        newblock.append(newtitle)
        newblock.append(newdescript)
        newcarousel.append(newblock)
        console.log(newcarousel)
        $("#carousel-learn-inner").append(newcarousel)
    }

})
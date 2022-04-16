let selectedCells =[];
function generateGrid() {
    var grid = "<table>";
    for ( row = 0; row < format[0]; row++ ) {
        grid += "<tr>"; 
        for ( col = 0; col < format[1]; col++ ) {      
            grid += "<td class='cell'>";
            let index = row*format[0] + col;
            if (arrangement[index] == 0){
                let candidate = candidates[index];
                grid += "<table>";
                count = 1;
                for ( row1 = 1; row1 <= 3; row1++){
                    grid += "<tr>";
                    for ( col1 = 1; col1 <= 3; col1++ ){
                        grid += "<td class='candidate'>";
                        if (candidate.includes(count)){
                            grid += count.toString();
                        }
                        grid += "</td>";
                        count += 1;
                    }
                    grid += "</tr>";    
                }
                grid += "</table></td>";
            } else {
                grid += arrangement[index].toString();
                grid += "</td>";
            }   
        }
        grid += "</tr>"; 
    }
    grid += "</table>";
    return grid;
}

function submitanswer(){
    let pattern = $("#pattern").val();
    let select = [];

    for (var index in selectedCells) {
        if (selectedCells[index]) {
            select.push(index);
        }
    }

    let data_to_save = {
        "id": id,
        "pattern": pattern,
        "cells": select,
    }

    save(data_to_save);
}

function save(new_data){
    $.ajax({
        type: "POST",
        url: "/quiz/" + id.toString() + "/part1",                
        dataType : "html",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(new_data),
        success: function(result){
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request);
            console.log(status);
            console.log(error);
        }
    });
}

$(document).ready(function(){
    for (i = 0; i < format[0]*format[1]; i++) {
        selectedCells.push(false);
    }

    $( "#tableContainer" ).append( generateGrid() );

    $( ".cell" ).click(function() {
        var index = $( "td" ).index( this );
        console.log(index);

        let bgcolor = $( this ).css( 'background-color');
        if (bgcolor == 'rgb(255, 0, 0)') {
            $( this ).css( 'background-color', 'white' );
            selectedCells[index] = false;
        } else {
            $( this ).css( 'background-color', 'red' );
            selectedCells[index] = true;
        }
    });

    $("#submit").click(function(){
        if(confirm("Are you sure you want to submit your answers?")){
            submitanswer();

            let link = "/answer/" + id.toString() + "/part1";
            window.location.assign(link);
        }
    })
})
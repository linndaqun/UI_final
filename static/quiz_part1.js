let selectedCells =[];
let pattern = '';
function generateGrid() {
    var grid = "<table class='quizTable'>";
    for ( row = 0; row < format[0]; row++ ) {
        grid += "<tr>"; 
        for ( col = 0; col < format[1]; col++ ) {      
            grid += "<td class='cell clickable_item'>";
            let index = row*format[0] + col;
            if (arrangement[index] == 0){
                let candidate = candidates[index];
                grid += "<table class='cell_table'>";
                count = 1;
                for ( row1 = 1; row1 <= 3; row1++){
                    grid += "<tr>";
                    for ( col1 = 1; col1 <= 3; col1++ ){
                        grid += "<td class='candidate'>";
                        if (candidate.includes(count)){
                            grid += count.toString();
                        } else {
                            grid += "<div class='empty_cell'>&nbsp;</div>"
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

async function submitanswer(){

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

    await save(data_to_save);
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

function showHint(){
    $("#hint_text").append(solution.hint);
}

$(document).ready(function(){
    for (i = 0; i < format[0]*format[1]; i++) {
        selectedCells.push(false);
    }
    $("[data-toggle=popover]").popover();
    $( "#tableContainer" ).append( generateGrid() );

    $( ".cell" ).click(function() {
        let myCol = $(this).index();
        let myRow = $(this).closest('tr').index();
        let index = myRow * format[0] + myCol;
        if (selectedCells[index]) {
            $( this ).css( 'background-color', '' );
            selectedCells[index] = false;
        } else {
            $( this ).css( 'background-color', 'lightskyblue' );
            selectedCells[index] = true;
        }
    });

    $("#submit").click(function(){
        if (pattern === '') {
            alert("Please select a pattern!");
            return;
        }

        if(confirm("Are you sure you want to submit your answers?")){
            submitanswer();

            let link = "/answer/" + id.toString() + "/part1";
            window.location.assign(link);
        }
    })

    $("#hint").one("click", function(){
        showHint();
    })

    $("input[type=radio]").change(function(){
        console.log('THis is a change\n');
        if($(this).val() === '1')
        {
            console.log('X-wing!');
            pattern = 'Naked Pair';
        }
        else if($(this).val() === '2')
        {
            pattern = 'Hidden Pair';
        }
        else if($(this).val() === '3')
        {
            pattern = 'X-wing';
        }
    });
})
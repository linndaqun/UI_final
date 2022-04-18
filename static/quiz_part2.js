let selectedCells =[];
function generateGrid() {
    var grid = "<table class='quizTable' id='table'>";
    for ( row = 0; row < format[0]; row++ ) {
        grid += "<tr>";
        for ( col = 0; col < format[1]; col++ ) {
            let index = row*format[0] + col;
            let index_str = index.toString();
            if ( solution1.cells.includes(index_str) ) {
                grid += "<td class='cell red'>";
            } else {
                grid += "<td class='cell'>";
            }
            if (arrangement[index] == 0){
                let candidate = candidates[index];
                grid += "<table class='cell_table'>";
                count = 1;
                for ( row1 = 1; row1 <= 3; row1++){
                    grid += "<tr>";
                    for ( col1 = 1; col1 <= 3; col1++ ){

                        if (candidate.includes(count)){
                            grid += `<td class='candidate color' id="td${row}${col}${row1-1}${col1-1}" onclick='clickEvt(${row}, ${col}, ${row1-1}, ${col1-1})'>`;
                            grid += count.toString();
                        }else {
                            grid += "<td class='candidate'>";
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

function clickEvt (row, col, row1, col1) {

    var cell = $('#td'+row+col+row1+col1)[0];

    if (cell.style.color == '' || cell.style.color == 'grey') {
        cell.style.color = 'white'
    } else {
        cell.style.color = 'grey'
    }
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
        url: "/quiz/" + id.toString() + "/part2",
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
    console.log('1\n')
    for ( row = 0; row < format[0]; row++ ) {
        for ( col = 0; col < format[1]; col++ ) {
            let index = row*format[0] + col;
            if (arrangement[index] == 0){
                let candidate = candidates[index];
                count = 1;
                for ( row1 = 0; row1 < 3; row1++){
                    for ( col1 = 0; col1 < 3; col1++ ){
                        if (candidate.includes(count)){
                            let cell = $('#td'+row+col+row1+col1)[0];
                            cell.style.color = 'grey'
                        }
                        count += 1;
                    }
                }
            }
        }
    }


    $("#submit").click(function(){
        if(confirm("Are you sure you want to submit your answers?")){
            submitanswer();

            let link = "/answer/" + id.toString() + "/part2";
            window.location.assign(link);
        }
    })
})
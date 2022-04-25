function generateSolutionGrid() {
    var grid = "<table class='quizTable' id='table'>";
    for ( row = 0; row < format[0]; row++ ) {
        grid += "<tr>";
        for ( col = 0; col < format[1]; col++ ) {
            let index = row*format[0] + col;
            let index_str = index.toString();
            if ( solution1.cells.includes(index_str) ) {
                grid += "<td class='cell green'>";
            } else {
                grid += "<td class='cell'>";
            }
            if (arrangement[index] == 0){
                let candidate = candidates[index];
                // answer = solution2['cell'];
                // console.log(answer)
                grid += "<table class='cell_table'>";
                count = 1;
                for ( row1 = 1; row1 <= 3; row1++){
                    grid += "<tr>";
                    for ( col1 = 1; col1 <= 3; col1++ ){
                        if (candidate.includes(count)){
                            if(solution2.cells.includes(`${row}${col}${row1-1}${col1-1}`)){
                                if (answer.cells.includes(`${row}${col}${row1-1}${col1-1}`)) {
                                    grid += `<td class='candidate green' >`;
                                } else {
                                    grid += `<td class='candidate red' >`;
                                }
                            } else {
                                grid += `<td class='candidate' id="td${row}${col}${row1-1}${col1-1}" onclick='clickEvt(${row}, ${col}, ${row1-1}, ${col1-1})'>`;
                            }
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

function generateAnswerGrid() {
    var grid = "<table class='quizTable' id='table'>";
    for ( row = 0; row < format[0]; row++ ) {
        grid += "<tr>";
        for ( col = 0; col < format[1]; col++ ) {
            let index = row*format[0] + col;
            let index_str = index.toString();
            if ( solution1.cells.includes(index_str) ) {
                grid += "<td class='cell green'>";
            } else {
                grid += "<td class='cell'>";
            }
            if (arrangement[index] == 0){
                let candidate = candidates[index];
                // answer = solution2['cell'];
                // console.log(answer)
                grid += "<table class='cell_table'>";
                count = 1;
                for ( row1 = 1; row1 <= 3; row1++){
                    grid += "<tr>";
                    for ( col1 = 1; col1 <= 3; col1++ ){
                        if (candidate.includes(count)){
                            if (answer.cells.includes(`${row}${col}${row1-1}${col1-1}`)) {
                                if(solution2.cells.includes(`${row}${col}${row1-1}${col1-1}`)) {
                                    grid += `<td class='candidate green' >`;
                                } else {
                                    grid += `<td class='candidate' >`;
                                }

                            }
                            else {
                                grid += `<td class='candidate' id="td${row}${col}${row1-1}${col1-1}" onclick='clickEvt(${row}, ${col}, ${row1-1}, ${col1-1})'>`;
                            }
                            grid += count.toString();
                        } else {
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

function judgePattern(){
    if (is_correct == 'true'){
        $( "#pattern_feedback").append( "You got this right!" );
        $( "#pattern_feedback").css("color", "green");
    }
    else {
        $( "#pattern_feedback").append( "You didn't choose the correct candidate(s) to eliminate, see the following explanation:" );
        $( "#pattern_feedback").css("color", "red");
    }
}

function review(){
    let pattern = solution1.pattern;
    if (pattern == "Naked Pair") {
        let link = "/learn/1";
        window.location.assign(link);
    } else if (pattern == "Hidden Pair") {
        let link = "/learn/2/1";
        window.location.assign(link);
    } else {
        let link = "/learn/3";
        window.location.assign(link);
    }
}

$(document).ready(function(){
    judgePattern();
    $( "#correctTableContainer" ).append( generateSolutionGrid() );
    $( "#tableContainer" ).append( generateAnswerGrid() );

    if (id == 6) {
        $("#next").html('View Score');
    }
    $("#next").click(function(){
        let link = "";
        if (id < 6){
            let id_int = parseInt(id);
            link = "/quiz/" + (id_int+1).toString() + "/part1";
        }
        else {
            link = "/score";
            $("#next").prop("value", "Result");
        }
        window.location.assign(link);
    });
    $( "#review" ).click(function(){
        review();
    })
})
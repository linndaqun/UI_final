function generateSolutionGrid() {
    var grid = "<table id='table'>";
    for ( row = 0; row < format[0]; row++ ) {
        grid += "<tr>"; 
        for ( col = 0; col < format[1]; col++ ) { 
            let index = row*format[0] + col;
            let index_str = index.toString();
            if ( solution.cells.includes(index_str) ) {
                grid += "<td class='cell green'>";
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
                        grid += "<td class='candidate'>";
                        if (candidate.includes(count)){
                            grid += count.toString();
                        }else {
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
    var grid = "<table id='table'>";
    for ( row = 0; row < format[0]; row++ ) {
        grid += "<tr>"; 
        for ( col = 0; col < format[1]; col++ ) { 
            let index = row*format[0] + col;
            let index_str = index.toString();

            if ( answer.cells.includes(index_str) ) {
                if (solution.cells.includes(index_str)){
                    grid += "<td class='cell green'>";
                } else {
                    grid += "<td class='cell red'>";
                }
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
                        grid += "<td class='candidate'>";
                        if (candidate.includes(count)){
                            grid += count.toString();
                        }else {
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
    if (answer.pattern == solution.pattern){
        $( "#pattern_feedback").append( "You got this right!" );
        $( "#pattern_feedback").css("color", "green");
    }
    else {
        $( "#pattern_feedback").append( "You didn't choose the correct pattern, see the following explanation:" );
        $( "#pattern_feedback").css("color", "red");
    }
}

function judgePattern2(){
    if (is_correct){
        $( "#pattern_feedback2").append( "You got this right!" );
        $( "#pattern_feedback2").css("color", "green");
    }
    else {
        $( "#pattern_feedback2").append( "You didn't choose the correct cell(s), see the following explanation:" );
        $( "#pattern_feedback2").css("color", "red");
    }
}

function review(){
    let pattern = solution.pattern;
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
    judgePattern2();
    $( "#tableContainer" ).append( generateAnswerGrid() );
    $( "#correctTableContainer" ).append( generateSolutionGrid() );
    $("#next").click(function(){
        let link = "/quiz/" + id.toString() + "/part2";
        window.location.assign(link);
    });
    $( "#review" ).click(function(){
        review();
    })
})
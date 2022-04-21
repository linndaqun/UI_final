function generateSolutionGrid() {
    var grid = "<table id='table'>";
    for ( row = 0; row < format[0]; row++ ) {
        grid += "<tr>"; 
        for ( col = 0; col < format[1]; col++ ) { 
            let index = row*format[0] + col;
            let index_str = index.toString();
            if ( solution.cells.includes(index_str) ) {
                if ( answer.cells.includes(index_str) ) {
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

function generateAnswerGrid() {
    var grid = "<table id='table'>";
    for ( row = 0; row < format[0]; row++ ) {
        grid += "<tr>"; 
        for ( col = 0; col < format[1]; col++ ) { 
            let index = row*format[0] + col;
            let index_str = index.toString();
            if ( answer.cells.includes(index_str) ) {
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


$(document).ready(function(){

    $( "#tableContainer" ).append( generateAnswerGrid() );
    $( "#correctTableContainer" ).append( generateSolutionGrid() );
    $("#next").click(function(){
        let link = "/quiz/" + id.toString() + "/part2";
        window.location.assign(link);
    });
})
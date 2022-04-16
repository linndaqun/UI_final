function generateGrid() {
    var grid = "<table>";
    for ( row = 0; row < format[0]; row++ ) {
        grid += "<tr>"; 
        for ( col = 0; col < format[1]; col++ ) {      
            grid += "<td class='cell'>"
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

$(document).ready(function(){
    $( "#tableContainer" ).append( generateGrid() );

    $( ".cell" ).click(function() {
        var index = $( "td" ).index( this );
        var row = Math.floor( ( index ) / 5) + 1;
        var col = ( index % 5 ) + 1;

        let bgcolor = $( this ).css( 'background-color');
        if (bgcolor == 'rgb(255, 0, 0)') {
            $( this ).css( 'background-color', 'white' );
        } else {
            $( this ).css( 'background-color', 'red' );
        }
    });

    $("#submit").click(function(){
        if(confirm("Are you sure you want to submit your answers?")){
            let link = "/answer/" + id.toString() + "/part1";
            console.log(link);
            window.location.assign(link);
        }
    })
})
window.onload = function() {
    function print(message){
        console.log(message)
    }

    function reset_python_board(){
        $.ajax({
            type : 'GET',
            url: 'reset',
            success : function(data) {
                console.log(data);
            }
        });
    }

    reset_python_board()



    var board = document.getElementById('tictactoe');
    for(var i = 0; i < 9; i++){
        var div = document.createElement('div');
        div.className = 'block block' + i;
        div.id = i
        div.style.backgroundColor = 'white'
        board.appendChild(div)
    }
    // Declare variables
    var turn = 1,
        blocks = document.getElementsByClassName('block'),
        WINNING_MOVES = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]
        ],
        gameRunning = true,
        playerOneColor = '#2196F3',
        playerTwoColor = '#F44336',
        reset = document.getElementById('reset'),
        gameOver = document.getElementById('gameOverText'),
        resetButton = document.getElementById('resetButton');
        checkBlock = 0;

    $('#train').click(function(){
        $.ajax({
            type : 'GET',
            url: 'train/' + $('#train_amount').val(),
            success : function(data) {
                console.log(data);
            }
        });
        function check() {
            $.ajax({
                type : 'GET',
                dataType : 'json',
                url: 'json/test.json',
                success : function(data) {
                    if(data["trained"] == 'done'){
                        alert(data["time"])
                        clearInterval(id)
                        if (data["last_move"]){
                            var bigNumber = data.last_move[0] + data.last_move[1] * 3
                            var block = document.getElementsByClassName('block' + bigNumber)
                            setBlock(turn, block[0], 'check')
                        }
                        return
                    }
                },
                timeout: 10
            });
        }
        var id = setInterval(check, 1000);
    })

    $('#begin').click(function(){
        $('#begin').text() == 'SPELER' ? $('#begin').text('AI') : $('#begin').text('SPELER')
        reset_board()
        $.ajax({
            type : 'GET',
            url: 'swap',
            success : function(data) {
                console.log('test')
                console.log(data);
                reset_python_board()
                if (data["last_move"]){
                    var bigNumber = data.last_move[0] + data.last_move[1] * 3
                    var block = document.getElementsByClassName('block' + bigNumber)
                    setBlock(turn, block[0], 'begin')
                }
            },
            error: function(error){
                console.log(error)
            }
        });
    })

    function display_qvalues(data){
        for (var i = 0, x = blocks.length; i < x; i++) {
            var block = blocks[i]
            if(block.style.backgroundColor != 'white'){
                block.innerHTML = ''
            }
            else {
                block.innerHTML = data.shift()
            }
        }
    }

    // Check if user clicks on block
    for (var i = 0, x = blocks.length; i < x; i++) {
        blocks[i].onclick = function() {
            if (gameRunning) {
                if(this.style.backgroundColor != 'white'){
                    return
                }
                setBlock(turn, this, 'click')
                if(checkForVictory(turn)){
                    return;
                }
                x = (this.id % 3)
                y = (Math.floor(this.id / 3))
                $.ajax({
                    type : 'GET',
                    url: 'move/' + x + '/' + y + '/' + turn, // Not sure why this is * -1
                    success : function(data) {
                        console.log(data);
                        $.ajax({
                            type : 'GET',
                            dataType : 'json',
                            url: 'json/test.json',
                            success : function(data) {
                                console.log(data)
                                console.log(data.qvalues);
                                display_qvalues(data.qvalues);
                                console.log(data.last_move);
                                var bigNumber = data.last_move[0] + data.last_move[1] * 3;
                                console.log(bigNumber);
                                var block = document.getElementsByClassName('block' + bigNumber);
                                if(checkForVictory(turn)) {
                                    return;
                                }
                                setBlock(turn, block[0], 'ajax');
                                if(checkForVictory(turn)) {
                                    return;
                                }
                            }
                        });
                    }
                });
            }
        };
    }

    // Give block a color

    function setBlock(player, block, whom) {
        //alert('setblock called by ' + whom);
        if (player === 1 && block.style.backgroundColor != playerTwoColor) {
            block.style.backgroundColor = playerOneColor;
            turn = -1;
            block.taken = -1;
            block.style.fontSize = '40'
        }
        else if (player === -1 && block.style.backgroundColor != playerOneColor) {
            block.style.backgroundColor = playerTwoColor;
            turn = 1;
            block.taken = 1;
            block.style.fontSize = '40'
        }
        else {
            console.log('NO')
            return false;
        }

        //checkForVictory(player)

        checkBlock++;
        checkTie();
        return false
    }

    // Check with all the posible WINNING_MOVES if there's a winner

    function checkForVictory(playerToCheck) {
        for (var i = WINNING_MOVES.length - 1; i >= 0; i--) {
            if (blocks[WINNING_MOVES[i][0]].taken == playerToCheck &&
                blocks[WINNING_MOVES[i][1]].taken == playerToCheck &&
                    blocks[WINNING_MOVES[i][2]].taken == playerToCheck) {
                        var green = "#4CAF50";

                        blocks[WINNING_MOVES[i][0]].style.backgroundColor = green;
                        blocks[WINNING_MOVES[i][1]].style.backgroundColor = green;
                        blocks[WINNING_MOVES[i][2]].style.backgroundColor = green;

                        //reset.style.backgroundColor = 'rgba(100, 100, 100, 0.7)';
                        gameOver.innerHTML =  'De ' + (playerToCheck == -1 ? 'mens ' : 'computer ') + 'heeft gewonnen';
                        resetButton.style.display = 'block';

                        gameRunning = false;
                        checkBlock = 0;

                        return true
                        break
                    }
        }
        return false;
    }

    // Check if it's a tie

    function checkTie() {
        if (checkBlock === 9) {
            gameRunning = false;
            reset.style.backgroundColor = 'rgba(100, 100, 100, 0.7)';
            gameOver.innerHTML = 'Gelijkspel';
            resetButton.style.display = 'block';
        }
    }

    // Reset the game when clicked on the reset button

    function reset_board(){
        for (var i = 0, x = blocks.length; i < x; i++) {
            blocks[i].style.backgroundColor = 'white';
            blocks[i].taken = null;
            blocks[i].innerHTML = '';
            blocks[i].style.fontSize = '20';
        }

        reset.style.backgroundColor = 'rgba(100, 100, 100, 0.0)';
        gameOver.innerHTML = '';
        resetButton.style.display = 'none';
        turn = 1;
        gameRunning = true;
        checkBlock = 0;

        reset_python_board()

        $.ajax({
            type : 'GET',
            url: 'start',
            success : function(data) {
                console.log(data);
            }
        });

        // THis causes problems but we'll need this if we want the computer to start
        //$.ajax({
            //type : 'GET',
            //dataType : 'json',
            //url: 'json/test.json',
            //success : function(data) {
                //console.log(data)
                //if (data["last_move"]){
                    //var bigNumber = data.last_move[0] + data.last_move[1] * 3
                    //var block = document.getElementsByClassName('block' + bigNumber)
                    //setBlock(turn, block[0], 'reset')
                //}
            //}
        //});
    }

    resetButton.onclick = function(){ reset_board() }
};

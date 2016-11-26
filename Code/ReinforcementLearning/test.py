#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

PORT_NUMBER = 8080

#This class will handles any incoming request from
#the browser
class myHandler(BaseHTTPRequestHandler):

    #Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        from time import clock
        from QLearningPlayer import QLearningPlayer
        from Player import Player
        from TicTacToe import TicTacToe
        from ConnectFour import ConnectFour

        test_games_results = {'Player1wins': 0, 'Player2wins': 0, 'Ties': 0}

        def train(games):
                # Set timer
                startTime = clock()

                # Train computer
                for i in range(1, games + 1):
                        if i % 1000 == 0: print(i)
                        game = TicTacToe(p1, p2)
                        game.play_game()

                deltaTime = clock() - startTime
                m, s = divmod(deltaTime, 60)
                self.wfile.write("It took " + str(int(m)) + " minutes and " + str(s) + " seconds to play " + str(games) + " games")
                self.wfile.write("<br>")

# Assign the players
        p1 = QLearningPlayer()
        p2 = QLearningPlayer()

# Do your own stuff
        train(int(1e3))

# Let the computer play againt a real player
# p1 = Player()
        p1.epsilon = 0
        p2.epsilon = 1

        def test_games(games):
            for i in range(games):
                game = TicTacToe(p1, p2)
                game.play_game()
                for thing in test_games_results:
                    test_games_results[thing] += game.score[thing]
            self.wfile.write('The results of ' + str(games) + ' games played was ' + str(test_games_results))
            self.wfile.flush()
            # self.wfile.close()
            self.wfile.write('test')

        test_games(int(1e3))
        return

try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print('Started httpserver on port ' , PORT_NUMBER)

    #Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print('^C received, shutting down the web server')
    server.socket.close()

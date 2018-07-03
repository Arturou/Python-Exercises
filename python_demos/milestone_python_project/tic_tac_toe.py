def create_board():
	"""
	Creates an empty board.
	Returns:
	    An array of 9 empty slots.
	"""
	return [" "]*9

def display_board(board):
	"""
	Prints to console the Tic-Tac-Toe Board
	Args:
		board: 1-D array representation of the tic-tac-toe board
	"""
	print("\n"*1000)
	top_row="|".join(board[6:])
	middel_row="|".join(board[3:6])
	bottom_row="|".join(board[:3])
	print("{}\n{}\n{}\n{}\n{}".format(top_row, "-"*5,middel_row, "-"*5,bottom_row))
	
def check_win(current_player, board):
	"""
	Verifies if current player has won.
	Args:
		current_player: String representation of current player [X or O]
		board: 1-D array representation of the tic-tac-toe board
	Returns:
	    A boolean value, True if current player has won False otherwise
	"""
	board = list(map(lambda cell: cell==current_player,board))
	win_options = list()
	#rows
	win_options.append(board[6:])
	win_options.append(board[3:6])
	win_options.append(board[:3])
	#columns			row	columns		row	column	 row column
	win_options.append([board[6:][0], board[3:6][0], board[:3][0]])
	win_options.append([board[6:][1], board[3:6][1], board[:3][1]])
	win_options.append([board[6:][2], board[3:6][2], board[:3][2]])
	#diagonals			row	columns		row	column	 row column
	win_options.append([board[6:][0], board[3:6][1], board[:3][2]])
	win_options.append([board[6:][2], board[3:6][1], board[:3][0]])
	#check if any win option is true
	win_options = list(map(lambda item: all(item), win_options))
	return len(list(filter((lambda item: item), win_options))) > 0

def check_tie(players, board):
	"""
	Verifies if both players are in a tie.
	Args:
		players: 1-D array of string representation of players [X and O]
		board: 1-D array representation of the tic-tac-toe board
	Returns:
	   A boolean, True if all values in board are true, False otherwise
	"""
	board = list(map(lambda cell: cell==players[0] or cell==players[1],board))
	return all(board)

def make_move(player, board):
	"""
	Places player's symbol on the board.
	Args:
		player: Current player's symbol. [X or O]
		board: 1-D array representation of the tic-tac-toe board
	Returns:
	    An updated 1-D array representation of the tic-tac-toe board
	"""
	print("\nPlayer {} turn!".format(player))
	move = input("\nPlease enter a cell number to make a move: ")
	if not move.isdigit():
		return make_move(player, board)
	else:
		move = int(move)-1
		if move > len(board) or move < 0:
			print("\nInvalid move!")
			return make_move(player, board)
		elif board[move] != " ":
			print("\nCell is already marked!")
			return make_move(player, board)
		else:
			board[move] = player
			return board
	
def game_loop(players, board):
	"""
	The main loop of the game (recursive function).
	It displays the board, lets the user make a move on the board
	and verifies if the game is a tie or win for the current player.
	Args:
		players: 1-D array of string representation of players [X and O]
		board: 1-D array representation of the tic-tac-toe board
	"""
	display_board(board)
	board = make_move(players[0], board)
	display_board(board)
	if check_tie(players, board):
		print("\nIt's a TIE!")
	elif check_win(players[0], board):
		print("\nPlayer {} has won!".format(players[0]))
	else:
		players = list(reversed(players))
		game_loop(players, board)
		
def start_game():
	"""
	Welcome menu for the Tic-Tac-Toe Game, it's also in charge of starting the game loop.
	"""
	print("Welcome to the super awesome TIC-TAC-TOE GAME!\n")
	print("Currently this is a human vs human version.\nNo Human vs CP option implemented yet.")
	option = input("Select symbol for player one: 1.-X 2.-O: ")
	if not option.isdigit():
		start_game()
	else:
		option=int(option)
		if option > 2 or option < 1:
			start_game()
		else:
			players=["X","O"]
			players = players if option == 1 else list(reversed(players))
			game_loop(players, create_board())

start_game()
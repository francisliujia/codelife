import random

def draw_board(board):
	print(board[7] + '|' + board[8] + '|' + board[9])
	print('-+-+-')
	print(board[4] + '|' + board[5] + '|' + board[6])
	print('-+-+-')
	print(board[1] + '|' + board[2] + '|' + board[3])

def input_player_letter():
	letter = ''
	while not (letter == 'X' or letter == 'O'):
		print('Do you want to be X or O ?')
		letter = input().upper()

	if letter == 'X':
		return ['X', 'O']
	else:
		return ['O', 'X']

def who_goes_first():
	if random.randint(0,1) == 0:
		return 'computer'
	else:
		return 'player'

def make_move(board, letter, move):
	board[move] = letter

def is_winner(board, letter):
	return (
		(board[4]==letter and board[5]== letter and board[6]==letter) or 
		(board[1]==letter and board[2]== letter and board[3]==letter) or 
		(board[7]==letter and board[4]== letter and board[1]==letter) or 
		(board[8]==letter and board[5]== letter and board[2]==letter) or 
		(board[9]==letter and board[6]== letter and board[3]==letter) or 
		(board[7]==letter and board[5]== letter and board[3]==letter) or 
		(board[9]==letter and board[5]== letter and board[1]==letter))


def get_board_copy(board):
	board_copy = []
	for i in board:
		board_copy.append(i)
	return board_copy

def is_space_free(board, move):
	return board[move] == ' '

def get_player_move(board):
	move = ' '
	while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
		print('What is your next move? (1-9)')
		move = input()
	return int(move)

def choose_random_move_from_list(board, moveList):
	possibleMoves = []
	for i in moveList:
		if is_space_free(board, i):
			possibleMoves.append(i)

		if len(possibleMoves) != 0:
			return random.choice(possibleMoves)
		else:
			return None

def get_computer_move(board, computerLetter):
	if computerLetter == 'X':
		playLetter = 'O'
	else:
		playLetter = 'X'

	# check if we can win in the next move
	for i in range(1, 10):
		board_copy = get_board_copy(board)
		if is_space_free(board_copy, i):
			make_move(board_copy, computerLetter, i)
			if is_winner(board_copy, computerLetter):
				return i

	#  check if the player can win in the next  move and block them
	for i in range(1, 10):
		board_copy = get_board_copy(board)
		if is_space_free(board_copy, i):
			make_move(board_copy, playLetter, i)
			if is_winner(board_copy, playLetter):
				return i

	# try to take one of the corners, if they are free 
	move = choose_random_move_from_list(board, [1,3,7,9])
	if move != None:
		return move

	# try to take the center, if it is free.
	if is_space_free(board, 5):
		return 5

	# move on one of the sides
	return choose_random_move_from_list(board, [2,4,6,8])

def is_board_full(board):
	for i in range(1, 10):
		if is_space_free(board, i):
			return False
	return True


print('\n\t\t\tTIC TAC TOE\n')

while True:
	the_board = [' '] * 10
	playLetter, computerLetter = input_player_letter()
	turn = who_goes_first()
	print(f'The {turn} will go first.')
	game_is_playing= True

	while game_is_playing:
		if turn == 'player':
			draw_board(the_board)
			move = get_player_move(the_board)
			make_move(the_board, playLetter, move)

			if is_winner(the_board, playLetter):
				draw_board(the_board)
				print('Hooray! You have won the game!')
				game_is_playing = False

			else:
				if is_board_full(the_board):
					draw_board(the_board)
					print('The game is a tie!')
					break
				else:
					turn = 'computer'

		else:
			move = get_computer_move(the_board, computerLetter)
			make_move(the_board, computerLetter, move)

			if is_winner(the_board, computerLetter):
				draw_board(the_board)
				print('The computer have beaten you! You lose!')
				game_is_playing = False
			else:
				if is_board_full(the_board):
					draw_board(the_board)
					print('The game is a tie!')
					break
				else:
					turn = 'player'

	print('Do you want to play again? (yes/no)')
	if not input().lower().startswith('y'):
		break























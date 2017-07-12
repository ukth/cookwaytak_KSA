import copy,os,time
def AI(Board):
	if iswinner(Board) or boardfull(Board):
		return Board
	#print 'ai in'
	if whoseturn(Board)=='O':
		minS=2
		for i in cases(Board):
			# print i
			# print score(i, alpha, beta)
			# print
			if score(i, -2, 2)<minS:
				minS=score(i, -2, 2)
				ans=i
		return ans

	maxS=-2
	for i in cases(Board):
		# print i
		# print score(i, alpha, beta)
		# print
		if score(i, -2, 2)>maxS:
			maxS=score(i, -2, 2)
			ans=i
	return ans

# def scorelist(L):
# 	#print 'scorelist'
# 	ans=[]
# 	for i in range(len(L)):
# 		ans.append(score(L[i]))
# 	return ans


def score(Board, alpha, beta):
	#time.sleep(1)
	#print '########'
	player=whoseturn(Board)
	if player=='O':
		if iswinner(Board):#O win
			return 1
		if boardfull(Board):
			return 0
		for i in cases(Board):
			result=score(i,alpha,beta)
			if result<beta:
				beta=result
			if beta<=alpha:
				return beta
		return beta
	elif player=='X':
		if iswinner(Board):#O win
			return -1
		if boardfull(Board):
			return 0

		for i in cases(Board):
			result=score(i,alpha,beta)
			if result>alpha:
				alpha =result
			if beta<=alpha:
				return alpha
		return alpha
def cases(Board):
	ans=[]
	player=whoseturn(Board)
	for i in range(Board.size):
		for j in range(Board.size):
			if Board.board[i][j]==' ':
				#print i,j
				k=copey(Board)
				#print k
				k.board[i][j]=player
				#print k
				ans.append(k)
	#print 'qqqqqqqqqqqqqqqqqq'
	#for i in ans:
		#print i
	#print 'wwwwwwwwwwwwwww'
	return ans

class Board():
	def __init__(self,size):
		self.size=size
		self.board = [[' ']*self.size for j in range(self.size)]

	def __str__(self):
		ans=''
		for i in range(self.size):
			ans+=str(self.board[i])+'\n'
		return ans

# difficulty = raw_input('Enter your difficulty level (easy,medium,hard)')

def copey(B):
	ans=Board(B.size)
	ans.board=copy.deepcopy(B.board)
	return ans

def iswinner(tictactoe):
	#print tictactoe
	# for n in ['O','X']:
	# 	for i in range(tictactoe.size):
	# 		if tictactoe.board[i]==[n]*tictactoe.size:
	# 			return True
	# 		column=True
	# 		for j in range(tictactoe):
	# 			if tictactoe.board[j][i]!=n:
	# 				column=False
	# 				break
	# 		if column:return True
	# 	diag1=True
	# 	diag2=True
	# 	for i in range(tictactoe.size):
	# 		if tictactoe.board[i][i]!=n: 
	# 			diag1=False
	# 		if tictactoe.board[i][tictactoe.size-i]!=n:
	# 			diag2=False
	# 	if diag1 or diag2:
	# 		return True

	# return False
	for i in range(tictactoe.size):
		if tictactoe.board[i]==['O']*tictactoe.size or tictactoe.board[i]==['X']*tictactoe.size:
			return True
	for i in range(tictactoe.size):
		n=tictactoe.board[0][i]
		column=True
		for j in range(tictactoe.size):
			if tictactoe.board[j][i]==' ' or tictactoe.board[j][i]!=n:
				column=False
				break
		if column:
			return True
	diag1, diag2=True, True
	a,b=tictactoe.board[0][0],tictactoe.board[0][tictactoe.size-1]
	for i in range(tictactoe.size):
		if tictactoe.board[i][i]==' ' or tictactoe.board[i][i]!=a: 
			diag1=False
			break
	for i in range(tictactoe.size):
		if tictactoe.board[i][tictactoe.size-i-1]==' ' or tictactoe.board[i][tictactoe.size-i-1]!=b:
			diag2=False
			break
	if diag1 or diag2:
		return True
	return False

def boardfull(tictactoe):
	for n in tictactoe.board:
		if ' ' in n:
			return False
	return True

def whoseturn(tictactoe):
	numx = 0
	numo = 0
	for n in tictactoe.board:
		numx += n.count('X')
		numo += n.count('O')
	if numx == numo:
		return 'X'
	return 'O'

def drawboard(tictactoe):
	for i in range(tictactoe.size-1):
		ans1,ans2='',''
		for j in range(tictactoe.size-1):
			a = ' ' + tictactoe.board[i][j] + ' ' + '|'
			ans1+=a
			b = '-' * 3 + '+'
			ans2+=b
		j=tictactoe.size-1
		a = ' ' + tictactoe.board[i][j] + ' '
		ans1+=a
		print ans1
		b = '-' * 3
		ans2+=b
		print ans2
	i=tictactoe.size-1
	ans1=''
	for j in range(tictactoe.size-1):
		a = ' ' + tictactoe.board[i][j] + ' ' + '|'
		ans1+=a
	j=tictactoe.size-1
	a = ' ' + tictactoe.board[i][j] + ' '
	ans1+=a
	print ans1

	# print ' ' + tictactoe.board[0][0] + ' ' + '|' + ' ' + tictactoe.board[0][1] + ' ' + '|' + ' ' + tictactoe.board[0][2] + ' '
	# print '-' * 3 + '+' + '-' * 3 + '+' + '-' * 3
	# print ' ' + tictactoe.board[1][0] + ' ' + '|' + ' ' + tictactoe.board[1][1] + ' ' + '|' + ' ' + tictactoe.board[1][2] + ' '
	# print '-' * 3 + '+' + '-' * 3 + '+' + '-' * 3
	# print ' ' + tictactoe.board[2][0] + ' ' + '|' + ' ' + tictactoe.board[2][1] + ' ' + '|' + ' ' + tictactoe.board[2][2] + ' '

def move(player,tictactoe):
	#print 'move in'
	players = ['X','O']
##	ai = players.remove(player,tictactoe)
	localletter = whoseturn(tictactoe)
##	if localletter != player:
##		initializeai(ai)
##	else:
	try:
		playerspace=raw_input('Enter the row and the column you want to put your letter into, ex.00\n')
		if playerspace == 'exit' or playerspace == 'quit':
			os._exit(1)
		row,column=int(playerspace[0]),int(playerspace[1])
		if tictactoe.board[row][column] == ' ':
			tictactoe.board[row][column] = localletter
			if iswinner(tictactoe):
				return tictactoe
			#print 'AI in'
			tictactoe=AI(tictactoe)
		else:
			print "That move is invalid"
		return tictactoe
		#print 'aaaa'
	#drawboard(tictactoe)
	#print 'aaa'

	#move(player,tictactoe)
	except:
	 	print "That move is invalid"
	 	return tictactoe

##def initializeai(letter):
##	localboard = copy.deepcopy(tictactoe.board)
##	moves = {}
##	inc = 0
##	for n in localboard:
##		for b in n:
##			localn = localboard.index(n)
##			if b == ' ':
##				moves[inc] = (localn.index(' '),localboard.index(n))
##				b,localn[] = letter
##
def game():
	size = input('input size\n')
	tictactoe = Board(size)
	player = raw_input('Enter your letter (X or O): ')
	if player=='O':
		tictactoe = AI(tictactoe)
	while not(iswinner(tictactoe) or boardfull(tictactoe)):
		drawboard(tictactoe)
		tictactoe = move(player,tictactoe)
	if iswinner(tictactoe):
		localletter = whoseturn(tictactoe)
		drawboard(tictactoe)
		players = ['X','O']
		players.remove(localletter)
		print 'Congratulations ' + players[0] + ', you win!'
		return None
	if boardfull(tictactoe):
		localletter = whoseturn(tictactoe)
		drawboard(tictactoe)
		print 'It\'s a draw!'
		return None
game()
# T=Board(3)
# T.board=[['X','O',' '],
# 		['X',' ','O'],
# 		['X','O',' ']]
# print iswinner(T)
# T.board=[['X','O',' '],
# 		[' ','X','O'],
# 		[' ','O','X']]
# print iswinner(T)
# T.board=[[' ','O','X'],
# 		[' ','X','O'],
# 		['X','O',' ']]
# print iswinner(T)
# T.board=[['X','O',' '],
# 		[' ','X','O'],
# 		['X','O',' ']]
# print iswinner(T)
# T.board=[['O','O',' '],
# 		['X','X','X'],
# 		[' ','O',' ']]
# print iswinner(T)
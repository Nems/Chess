#lookup table of each piece to speed up the check of a valid move

rock   = {(-7, 0): True, (-6, 0): True, (-5, 0): True, (-4, 0): True,\
		  (-3, 0): True, (-2, 0): True, (-1, 0): True, (1, 0): True,\
		  (2, 0): True, (3, 0): True, (4, 0): True, (5, 0): True,\
		  (6, 0): True, (7, 0): True, (0, -7): True, (0, -6): True,\
		  (0, -5): True, (0, -4): True, (0, -3): True, (0, -2): True,\
		  (0, -1): True, (0, 1): True, (0, 2): True, (0, 3): True,\
		  (0, 4): True, (0, 5): True, (0, 6): True, (0, 7): True}
		  
knight = {(-1, -2): True, (1, 2): True, (-2, -1): True, (2, 1): True,\
		  (-1, 2): True, (1, -2): True, (-2, 1): True, (2, -1): True}
		  
bishop = {(-7, -7): True, (-6, -6): True, (-5, -5): True,\
		  (-4, -4): True, (-3, -3): True, (-2, -2): True,\
		  (-1, -1): True, (1, 1): True, (2, 2): True, (3, 3): True,\
		  (4, 4): True, (5, 5): True, (6, 6): True, (7, 7): True,\
		  (-7, 7): True, (-6, 6): True, (-5, 5): True, (-4, 4): True,\
		  (-3, 3): True, (-2, 2): True, (-1, 1): True, (1, -1): True,\
		  (2, -2): True, (3, -3): True, (4, -4): True, (5, -5): True,\
		  (6, -6): True, (7, -7): True}
		  
queen = {(-7, 0): True, (-6, 0): True, (-5, 0): True, (-4, 0): True,\
		  (-3, 0): True, (-2, 0): True, (-1, 0): True, (1, 0): True,\
		  (2, 0): True, (3, 0): True, (4, 0): True, (5, 0): True,\
		  (6, 0): True, (7, 0): True, (0, -7): True, (0, -6): True,\
		  (0, -5): True, (0, -4): True, (0, -3): True, (0, -2): True,\
		  (0, -1): True, (0, 1): True, (0, 2): True, (0, 3): True,\
		  (0, 4): True, (0, 5): True, (0, 6): True, (0, 7): True,\
		  (-7, -7): True, (-6, -6): True, (-5, -5): True,\
		  (-4, -4): True, (-3, -3): True, (-2, -2): True,\
		  (-1, -1): True, (1, 1): True, (2, 2): True, (3, 3): True,\
		  (4, 4): True, (5, 5): True, (6, 6): True, (7, 7): True,\
		  (-7, 7): True, (-6, 6): True, (-5, 5): True, (-4, 4): True,\
		  (-3, 3): True, (-2, 2): True, (-1, 1): True, (1, -1): True,\
		  (2, -2): True, (3, -3): True, (4, -4): True, (5, -5): True,\
		  (6, -6): True, (7, -7): True}

king = {(-1, 0): True, (1, 0): True, (0, -1): True, (0, 1): True,\
		(-1, -1): True,	(1, 1): True, (-1, 1): True, (1, -1): True}

pawn = {(0, -1): True, (0, 1): True, (-1, -1): True,\
		(1, 1): True, (-1, 1): True, (1, -1): True}

#end lookup

class ChessBoard:
	
	rules_table = { 'r': rock, 'n': knight, 'b': bishop, 'q': queen, 'k': king, 'p': pawn }
	
	def __init__(self):
		self._board = [['br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br'],\
					   ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],\
					   ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],\
					   ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],\
					   ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],\
					   ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],\
					   ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],\
					   ['wr', 'wn', 'wb', 'wq', 'wk', 'wb', 'wn', 'wr']]
					   
	def move(self, sx, sy, dx, dy):
		
		rx = dx - sx
		ry = dy - sy
		piece = self._board[sy][sx]
		board = self._board
		
		if piece == '  ' or piece[0] != self._color:
			return False
			
		else:
			#pawn special check......				
					
			if piece[1] == 'p':
				if piece[0] == 'b':
					if abs(rx) == abs(ry) and ry == 1 and board[dy][dx][0] == 'w':
						board[dy][dx] = board[sy][sx] if dy % 7 else 'bq'
						board[sy][sx] = '  '
						return True
					if sy < 2 and ry == 2:
						ry = 1
					if ry != 1 or rx != 0 or board[dy][dx][0] != ' ':
						return False
				elif piece[0] == 'w':
					if abs(rx) == abs(ry) and ry == -1 and board[dy][dx][0] == 'b':
						print dx, dy, board[sy][sx]
						board[dy][dx] = board[sy][sx] if dy % 7 else 'wq'
						board[sy][sx] = '  '
						return True
					if sy > 5 and ry == -2:
						ry = -1
					if ry != -1 or rx != 0 or board[dy][dx][0] != ' ':
						return False
			
			#end pawn.....
			
			if self.follow_rules(piece[1], rx, ry):
				crx = (cmp(rx, 0))
				cry = (cmp(ry, 0))
				
				if piece[1] != 'n':
					while rx != 0 or ry != 0:
						if board[sy+ry][sx+rx] != '  ' and board[sy+ry][sx+rx][0] == piece[0] and board[sy+ry][sx+rx] != piece:
							return False
						rx -= crx
						ry -= cry
				elif board[dy][dx][0] == piece[0]:
					return False
					
				if dy in (0, 7) and board[sy][sx][1] == 'p':
					board[sy][sx] = board[sy][sx][0] + 'q'
					
				board[dy][dx] = board[sy][sx]
				board[sy][sx] = '  '
				return True
				
			else:
				return False
		
	def follow_rules(self, piece, rx, ry):
			
		try:
			return self.rules_table[piece][(rx,ry)]
		except KeyError:
			return False
			
	def set_allowed_color(self, color):
		self._color = color
	
	#def victory_check(self):
		
		
	#def __repr__(self):
		#return "\n-------------------------------------\n".join([" | ".join(x) for x in self._board])
		
	
	def getBoard(self):
		return self._board
		
	def getPiece(self, x, y):
		return self._board[y][x]
		
	def __str__(self):
		return "\n-------------------------------------\n".join([" | ".join(x) for x in self._board])

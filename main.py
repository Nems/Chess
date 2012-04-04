from chess import ChessBoard
import pygame

def load_images():
	piecestr = 'prnbqk'
	pieces = pygame.image.load("imgs/chess-pieces.png").convert_alpha()
	chess = dict([('b'+ piecestr[x], pieces.subsurface((x*32, 0 , 32, 32))) for x in range(6)])
	chess.update(dict([('w'+ piecestr[x], pieces.subsurface((x*32, 32 , 32, 32))) for x in range(6)]))
	board = pygame.image.load("imgs/chess-board.png").convert_alpha()
	return board, chess


def pygame_main():

	pygame.init()
	
	pygame_mainloop()


def pygame_mainloop():
	
	#pygame board test
	
	cb = ChessBoard()
	color = ('w', 'b')
	player = 0
	cb.set_allowed_color(color[player])
	
	screen = pygame.display.set_mode((640, 480))
	board, chess = load_images()
	
	selected=pygame.Surface((32,24),pygame.SWSURFACE|pygame.SRCALPHA,32)
	#selected.set_alpha(60)
	selected.fill((255,255,0))
	
	selection = False
	sx, sy = None, None
	
	offset = 22
	
	print 'player\'s', player, 'turn'
	
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					return
			elif event.type == pygame.MOUSEBUTTONUP:
				x, y = event.pos
				x -= offset
				y -= offset
				if 0 <= x <= 255 and 0 <= y <= 191:
					x /= 32
					y /= 24
					if selection:
						selection = False
						if cb.move(int(sx), int(sy), int(x), int(y)):
							player = (player + 1) % 2
							cb.set_allowed_color(color[player])
							print 'player\'s', player, 'turn'
						sx, sy = None, None
					else:
						sx, sy = x, y
						if cb.getPiece(x, y)[0] == color[player]:
							selection = True
						else:
							sx, sy = None, None
							
				
		screen.fill((109,165, 165))
		screen.blit(board, (offset, offset))
		if sx != None and sy != None:
			screen.blit(selected, (sx*32+offset+2, sy*24+offset+2))
		for y, col in enumerate(cb.getBoard()):
			for x, piece in enumerate(col):
				if piece[0] != ' ':
					screen.blit(chess[piece], (x*32+offset, y*24+offset-12))
		pygame.display.update()
		pygame.time.delay(40)
	

def main():
	cb = ChessBoard()
	color = ('w', 'b')
	player = 0
	cb.set_allowed_color(color[player])
	while(1):
		print '-------------------------------------\n', str(cb), '\n-------------------------------------\n'
		inp = raw_input("Player%s's move: " % (player,))
		try:
			sx, sy, dx, dy = inp.split(' ')
		except:
			if inp == 'exit':
				break
		if not cb.move(int(sx), int(sy), int(dx), int(dy)):
			print 'Invalid move'
			continue
		player = (player + 1) % 2
		cb.set_allowed_color(color[player])

if __name__ == "__main__":
	pygame_main()

import curses
import time
from curses import textpad

def main(stdscr,box):
	curses.curs_set(0)
	

	grid(stdscr) #making 3X3 box
	#display(stdscr,box)
	playgame(stdscr,'X',box) #allowing multi-player inputs 
	
	stdscr.getch()

def playgame(stdscr,s,box) :
	curses.mousemask(1)
	key = stdscr.getch()

	if key==27 : #number for ESC key
		stdscr.addstr(4,3,"Bye !")
		stdscr.refresh()
		time.sleep(1)
		exit(0)

	if key == curses.KEY_MOUSE : #if mouse has been clicked, then
		_, x, y, _, _ = curses.getmouse()
		
		if x not in [1,4,7] : #if the player clicks in the borders, re-play
			playgame(stdscr,s,box)
		
		else:
			stdscr.addstr(y,x,s)
			i = varied_x(x)
			box[y][i] = s
			stdscr.refresh()	
			#display(stdscr,box)
			cases(box,stdscr)
		

		if s=='X' :
			s = 'O'
		else:
			s = 'X'
		

		
		
	
		playgame(stdscr,s,box)

def display(stdscr,box) :
	for i in range(3):
		for j in range(3) :
			stdscr.addstr(i+5,j,box[i][j])
			stdscr.refresh()
def check(s,stdscr,coordinates) :
	if s=='XXX' or s=='OOO' :
		time.sleep(1)
		for pair in coordinates :
				stdscr.addstr(pair[0],pair[1],s[0],curses.A_BLINK)
				stdscr.refresh()

def cases(box, stdscr ) :
	s = ''
	co = []
	matches = {0:1,1:4,2:7}

	# checking the rows ,if the cond. satisfies
	for i in range(3) :
		for j in range(3) :
			s = s+box[i][j]
			co.append((i,matches[j]))
		check(s,stdscr,co)
		s=''
		co = []
	
	# checking the cols, if the cond. satisfies
	for i in range(3) :
		for j in range(3) :
			s = s+box[j][i]
			co.append((j,matches[i]))
		check(s,stdscr,co)
		s = ''
		co = []
	
	# checking left diagonal
	for i in range(3) :
		s = s+box[i][i]
		co.append((i,matches[i]))
	check(s,stdscr,co)

	s = ''
	co = []
	
	# checking right diagonal
	for i in range(3) :
		s = s+box[i][2-i]
		co.append((i,matches[2-i]))
	check(s,stdscr,co)

def varied_x(x) :
	if x==1 :
		return 0
	elif x==4 :
		return 1
	elif x==7 :
		return 2

def grid(stdscr) :
	i = 0
	
	while i<3 :
		j = 0
		while j<9:
			stdscr.addstr(i,j,'[ ]')
			j+=3
		i+=1

	stdscr.refresh()
box = [['#']*3 for _ in range(3)]
curses.wrapper(main,box)
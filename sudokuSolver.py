#!/bin/python3

grid = [[0,0,0,0,3,0,0,0,0],
		[1,0,2,0,0,0,4,0,7],
		[0,3,0,0,0,0,9,0,0],
		[0,0,0,4,2,0,0,6,0],
		[0,0,0,0,0,0,0,9,1],
		[0,0,7,0,1,0,0,4,0],
		[0,4,0,0,7,0,0,0,0],
		[0,2,0,0,0,9,0,5,8],
		[8,0,0,0,0,6,0,0,0]]

def print_grid():
	for y in range(9):
		print(grid[y])

def safe(x, y, n):
	for i in range(9):
		if grid[y][i] == n or grid[i][x] == n:
			return False
	x = x // 3
	y = y // 3
	for i in range(3):
		for j in range(3):
			if grid[i + 3 * y][j + 3 * x] == n:
				return False
	return True

def solve(x, y):
	global grid

	if x >= 9 and y >= 8:
		print_grid()
		exit()
	elif x >= 9:
		y += 1
		x = 0
	if grid[y][x] == 0:
		for n in range(1, 10):
			if safe(x, y, n):
				grid[y][x] = n
				if not solve(x + 1, y):
					grid[y][x] = 0
		return False
	else:
		solve(x + 1, y)

solve(0, 0)

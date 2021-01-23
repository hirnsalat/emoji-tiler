class Grid:
    def __init__(self, rows, cols, cellsize, gapsize):
        self.rows = rows
        self.cols = cols
        self.cellh = cellsize
        self.cellw = cellsize
        self.gapx = gapsize
        self.gapy = gapsize
        self.width = (cellsize+gapsize)*cols
        self.height = (cellsize+gapsize)*rows

    def __iter__(self):
        for y in range(int(self.gapy/2), self.height, self.cellh+self.gapy):
            for x in range(int(self.gapx/2), self.width, self.cellw+self.gapx):
                yield x,y

if __name__=="__main__":
    g = Grid(5,4,72,16)
    for x,y in g:
        print(f"x={x}, y={y}")
    print(f"w={g.width}, h={g.height}")

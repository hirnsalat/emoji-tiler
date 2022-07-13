import pathlib
import random
from grid import Grid
import config

def appendpart(x, y, part):
    part = part.replace("%translatex%", str(x))
    part = part.replace("%translatey%", str(y))
    return part

def fetchparts(indir):
    return [x.read_text() for x in indir.iterdir()]

def generate(grid, parts):
    res = f"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n<svg id="emoji" viewBox="0 0 {grid.width} {grid.height}" xmlns="http://www.w3.org/2000/svg" fill="{config.color}">\n"""
    for x,y in grid:
        res += appendpart(x, y, random.choice(parts))
    res += "</svg>\n"
    return res

if __name__ == "__main__":
    grid = Grid(config.rows,config.cols,config.size,config.gap)

    parts = fetchparts(pathlib.Path("imported"))
    
    for i in range(100):
        with open(f"test/tile{i:03}.svg", "w") as outfile:
            outfile.write(generate(grid, parts))

import cherrypy
import tiler
import config
from pathlib import Path
from grid import Grid


class HelloWorld(object):
    def __init__(self):
        self.parts = tiler.fetchparts(Path("imported"))
        self.grid = Grid(config.rows, config.cols, config.size, config.gap)

    @cherrypy.expose
    def index(self):
        return tiler.generate(self.grid, self.parts)

    def _cp_dispatch(self, vpath):
        print("party")
        return self.index



if __name__ == '__main__':
    cherrypy.quickstart(HelloWorld())

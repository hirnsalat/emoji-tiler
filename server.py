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
        cherrypy.response.headers['Content-Type'] = 'image/svg+xml'
        cherrypy.response.headers['Content-Encoding'] = 'utf-8'
        cherrypy.response.headers['Vary'] = 'Accept-Encoding'
        return tiler.generate(self.grid, self.parts).encode()

    def _cp_dispatch(self, vpath):
        #print("party")
        return self.index



if __name__ == '__main__':
    cherrypy.config.update({'server.socket_port': 8080, 'server.socket_host':'0.0.0.0'})
    cherrypy.quickstart(HelloWorld())

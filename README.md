# emoji-tiler

A simple tool to generate randomized backgrounds from emoji.

How to use:

- change settings in `config.py`
- download black & white emoji from [OpenMoji](https://openmoji.org/) and put them in `to-import/`
- run `svgimporter.py`
- `tiler.py` generates a hundred backgrounds to `test/`
- `server.py` starts a webserver that responds with a new background to every request (requires [cherrypy](https://cherrypy.dev/))


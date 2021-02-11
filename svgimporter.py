import pathlib
import config
import re

strokepattern = re.compile('stroke-width="[0-9.]+"')

def importall(indir, outdir):
    for filepath in indir.iterdir():
        openandimport(indir, outdir, filepath.name)

def openandimport(indir, outdir, basename):
    with indir.joinpath(basename).open("r") as infile, outdir.joinpath(basename).open("w") as outfile:
        fileimport(infile, outfile)

def restroke(line, new):
    return strokepattern.sub(f"stroke-width=\"{new}\"", line)

def recolor(line, color):
    return line.replace("#000000", color).replace("#000", color)

def modify(line):
    line = recolor(line, config.color)
    if(config.do_stroke):
        line = restroke(line, config.stroke)
    return line

def fileimport(infile, outfile):
    lines = infile.readlines()[1:-1]
    lines[0] = lines[0].replace('id="line"', 'transform="translate(%translatex% %translatey%)"')
    outfile.writelines([modify(line) for line in lines])


if __name__ == "__main__":
    indir = pathlib.Path("to-import")
    outdir = pathlib.Path("imported")
    importall(indir, outdir)


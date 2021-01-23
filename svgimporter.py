import pathlib
import config

def importall(indir, outdir):
    for filepath in indir.iterdir():
        openandimport(indir, outdir, filepath.name)

def openandimport(indir, outdir, basename):
    with indir.joinpath(basename).open("r") as infile, outdir.joinpath(basename).open("w") as outfile:
        fileimport(infile, outfile)

def recolor(line, color):
    return line.replace("#000000", color).replace("#000", color)

def fileimport(infile, outfile):
    lines = infile.readlines()[1:-1]
    lines[0] = lines[0].replace('id="line"', 'transform="translate(%translatex% %translatey%)"')
    outfile.writelines([recolor(line, config.color) for line in lines])


if __name__ == "__main__":
    indir = pathlib.Path("to-import")
    outdir = pathlib.Path("imported")
    importall(indir, outdir)


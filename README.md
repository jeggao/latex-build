# $\LaTeX$ Build
__A simple python script and folder structure for standard `latexmk` compilation.__

Create copies of `project-name` for each $\LaTeX$ project. Initialize git repos if needed.

```
usage: ./build.py [-h] [-l] [-d] [-s] [-v]

options:
  -h, --help         show this help message and exit
  -l, --live         specify build type
  -d, --draft        not include images
  -s, --spell-check  enable aspell
  -v, --verbose      make verbose
```

## Prerequisites
- [$\TeX$ Live](https://tug.org/texlive/)
  - `latexmk` (by-default included in $\TeX$ Live)
- `aspell`

> As of now, this script only formally supports linux. It is directly usable of Windows with an installation of $\TeX$ Live, but nothing is tested. Raise an issue if further support is desired.

# $\LaTeX$ Build
__A simple python script and folder structure for standard `latexmk` compilation.__

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
- `texlive`
  - `latexmk` (by-default included in `texlive`)
- `aspell`

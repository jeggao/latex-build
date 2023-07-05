# $\LaTeX$ Build
__A simple python script and folder structure for standard `latexmk` compilation.__

Create copies of `project-name` for each $\LaTeX`project. Initialize git repos if needed.

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

> As of now, this script only supports linux. Raise an issue if further support is desired.

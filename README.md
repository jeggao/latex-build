# $\LaTeX$ Build
__A simple python script and folder structure for standard `latexmk` compilation. Also used for integrating basic scripting (e.g. R plots) in documents.__

Create copies of `project_name` for each $\LaTeX$ project. Initialize git repos for each if needed.

```
usage: ./build [-h] [-l] [-d] [-s] [-v]

options:
  -h, --help         show this help message and exit
  -l, --live         specify build type
  -d, --draft        not include images
  -s, --spell-check  enable aspell
  -v, --verbose      make verbose
```

## Prerequisites
- Python 3
- [TeX Live](https://tug.org/texlive/)
  - `latexmk` (by-default included in $\TeX$ Live)
- `aspell`

## Usage
- With this latex-build, each $\LaTeX$ project is a folder. To make a new one, make a copy of `project_name` abd rename it.
- Initialize a git repository in the folder.
- Use `build.toml` to configure the project
- Use `./build` (or `python ./build` on Windows) to build the project. Information about `./build` can be found with `./build -h`.

> As of now, this script only formally supports Linux. It is directly usable on Windows with an installation of $\TeX$ Live, but nothing is tested. Raise an issue if further support is desired.

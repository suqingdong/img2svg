# Convert an image to an SVG format with interactive elements

### Installation
```bash
python3 -m pip install img2svg
```

### Usage
```bash
img2svg --help

img2svg input.png

img2svg input.png -c conf.txt

img2svg input.png -c conf.txt -o output.svg --fill-color '#FF00FF' --fill-opacity 0.5
```

### Config Format
> separate with `<Tab>`
```
x   y   rx  ry  title   link
```
`config.txt` example:
```
0   0   140 720 Eudicots    https://www.baidu.com/s?wd=Eudicots
141 0   510 720 Monocots    https://www.baidu.com/s?wd=Monocots
511 0   720 720 Lycophytest https://www.baidu.com/s?wd=Lycophytest
721 0   890 720 Liverworts  https://www.baidu.com/s?wd=Liverworts
891 0   1359    720   Mosses   https://www.baidu.com/s?wd=Mosses
```

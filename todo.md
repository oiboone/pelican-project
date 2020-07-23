# themes to try

brownstone
built-texts
cebong - nice background color, very plain
dev-random
dev-random2
flex - claims to be simple and easy to follow
cid - uses javascript rot13 to obfuscate email address, nice font and color
dev-random3

elegant - lots of features, ongoing developemnt, info on use
astrochelys - nice layout, but nees work for fonts and colors

# Plugins

1. It appears that yaml headers are allowed without a plugin, but title must be first line in header. Ok, I don't see what's going on here.

2. It appears that this pandoc reader works : https://github.com/liob/pandoc_reader#configuration but still haven't figured out TOC

3. Use katex or mathjax parameter for pandoc, not render_math plugin

4. pandoc filters should work as command line parameters for pandoc reader

5. modified yaml-metadata plugin to work with pandoc reader. Figure out how to do this right.

# Open questions

having a single page of references for multiple md files
cross references between md pages that work in markdown and html
diagrams in html
knitr style code?
best layout for online book?
using same markdown for print or online book
coding templates/css for clarity and compactifying for speed
How to control order of articles in lists
How to connect numbering from one file to another
Look at other pandoc options like --section-div and --email-obfuscate --id-prefix
MathJax fallback for Katex <https://github.com/rbnvrw/katex-auto-render>


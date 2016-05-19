# Running
1. Get sgflib from here, http://gotools.sourceforge.net/sgflib/ , and untar
1. Download sgf to current directory
1. Run crazystone, analyze-game, print game analysis.  When printing select a pdf option (I installed pdf creator), copy and paste results to a file.  I called mine simply analysis
1. ./crazystone-analysis sgf-file analysis-file > sgf-with-analysis-file

# Example
./crazystone-analysis.py examples/64nhk1-18.sgf examples/64nhk1-18.analysis > examples/64nhk1-18-analysis.sgf

# Apologies
This is a quick hack put together so I could analyze my games
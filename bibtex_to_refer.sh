#!/bin/bash
# PURPOSE Reformat a BibTex.bib to the preprocessor refer bib database to be used with groff
# ./biber_to_refer.sh input_filename.bib output_filename.bib

# replaces the three letter month name with itself but quoted
# example: jan, -> "jan",
sed -i 's/\([jfmasond][aepueco][nbrylgptvc]\),/\"\1\",/g' $1

# replaces \url with url
sed -i 's/\\url/url/g' $1

# replaces -- with - for the page number
sed -i 's/--/-/g' $1

# call the python script
python3 bibtex_to_refer.py $1 > $2

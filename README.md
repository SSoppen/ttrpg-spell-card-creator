# ttrpg-spell-card-creator
PDF based generator of 5e spell-reference cards for print using JSON or CSV files

Requires wkhtmltopdf to be installed, which can be acquired at https://wkhtmltopdf.org/. Remember to set the install location in the config variable if needed
Each row in the CSV file turns into a single card, the order for each component is found in "generate-cards.py", alternatively see example image

Default delimiter is "|"

To run, fill in CSV file and run "generate-cards.py". Cards will be put in a folder named "generated cards"

When running, if an image with a given title already exists in the folder it will be overriden with the newly generated one
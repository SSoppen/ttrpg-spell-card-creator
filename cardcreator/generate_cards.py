import csv
from pathlib import Path

import imgkit
import jinja2

# Define order and names of csv values to be zipped into named parameters later
csv_order = ['title', 'name', 'level', 'range', 'casting_cost', 'description']
# Path to wkhtmltoimage exe
config = imgkit.config(wkhtmltoimage='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltoimage.exe')

if __name__ == "__main__":
    # Setup template
    templateLoader = jinja2.FileSystemLoader(searchpath="./static/templates")
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template("card-generator.html")

    # Generate output folder if it does not exist
    Path("generated_cards").mkdir(parents=True, exist_ok=True)

    # Open CSV file and iterate over defined cards
    with open('cardtext.csv', newline='') as csvfile:
        card_texts = csv.reader(csvfile, delimiter='|')
        for row in card_texts:
            parameters_dict = dict(zip(csv_order, row))
            rendered_card = template.render(**parameters_dict)
            imgkit.from_string(rendered_card,
                               f'generated_cards/{parameters_dict["title"]}.jpg',
                               config=config
                               )

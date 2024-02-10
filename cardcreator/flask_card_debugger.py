from flask import (
    Flask,
    render_template
)

from generate_cards import csv_order

app = Flask(__name__, template_folder='./static/templates')


@app.route("/")
def card_debugger():
    self_named_dict = dict(zip(csv_order, csv_order))
    return render_template('card-generator.html', **self_named_dict)

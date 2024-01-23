from flask import (
    render_template,
)
from . import app


@app.route('/a')
def hello():
    return render_template('card-generator.html', foo='bar')

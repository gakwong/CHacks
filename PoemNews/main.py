from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from werkzeug import secure_filename
#import PoemNews.webscrape_script.py as wbs

#app = Flask(__name__)
bp = Blueprint('main', __name__)

@bp.route("/")
def main():
    #a = get database info
    #dict = wbs.main()
    #print(dict)
    return render_template('index.html')

'''
if __name__ == '__main__':
    app.run(debug=True)

@bp.route("")
def index():
'''

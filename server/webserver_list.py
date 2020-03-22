from flask import Flask
from flask import render_template
import os

app = Flask(__name__)

@app.route('/')
def photos():
    # photos_names = os.listdir('static/Images')
    # photos_names = ['Images/' + file for file in photos_names]
    # photos_names.sort()

    #create and sort photo list
    os.chdir('/')
    photos_list = os.listdir('Users/whatzat/photobooth/server/static/Images')
    photos_list.sort()

    #function to convert list to nested list
    def Convert_nested(list):
        nested_list = [[list[j], list[j + 1]] for j in range(0, len(list), 2)]
        return nested_list

    #create photos nested list
    photos_list_nested = Convert_nested(photos_list)

    return render_template('main_list.html',photos_list_nested = photos_list_nested)

@app.route('/diy')
def diy():
    return render_template ('diy.html')

if __name__ == "__main__":
    app.run(debug=True, port=80, host='0.0.0.0')

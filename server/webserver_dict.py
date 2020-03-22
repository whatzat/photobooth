from flask import Flask
from flask import render_template
import os

app = Flask(__name__)

@app.route('/')
def photos():

    os.chdir('/')
    photos_list = os.listdir('/Users/whatzat/photobooth/server/static/Images')
    photos_list = ['Images/' + s for s in photos_list]
    photos_list.sort()
    # for x in photos_list:
    #     print(x)
    print(len(photos_list))

    #function to convert list to dictionary
    def Convert(list):
        dict = {list[i]: list[i + 1] for i in range(0, len(list), 2)}
        return dict


    #create photos dictionary
    photos_dict = Convert(photos_list)

    return render_template('main_dict.html', photos_dict = photos_dict)

@app.route('/diy')
def diy():
    return render_template ('diy.html')

if __name__ == "__main__":
    app.run(debug=flase, port=80, host='0.0.0.0')

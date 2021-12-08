from instapy import InstaPy
from instapy.util import smart_run

insta_username = 'lumpyproduction@gmail.com'
insta_password = 'lumpybeats1996'

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
#session = InstaPy(username=insta_username,
#                password=insta_password,headless_browser=True)
from selenium import webdriver
from instapy_chromedriver import binary_path # this will get you the path variable


@app.route('/123')
def index():

        """ Activity flow """
        # settings
        driver = webdriver.Chrome(executable_path=binary_path)
        driver.get("http://www.python.org")

        return 'Done'

from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>
    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)



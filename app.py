from instapy import InstaPy
from instapy.util import smart_run

from flask import Flask


app = Flask(__name__)
# login credentials
insta_username = 'lumpyproduction@gmail.com'
insta_password = 'lumpybeats1996'

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
#session = InstaPy(username=insta_username,
#                password=insta_password,headless_browser=True)
from selenium import webdriver
from instapy_chromedriver import binary_path # this will get you the path variable

@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

@app.route('/123')
def index():

        """ Activity flow """
        # settings
        driver = webdriver.Chrome(executable_path=binary_path)
        driver.get("http://www.python.org")

        return 'Done'

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)



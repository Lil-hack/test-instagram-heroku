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

driver = webdriver.Chrome(executable_path=binary_path)
driver.get("http://www.python.org")

@app.route('/')
def index():
    with smart_run(session):
        """ Activity flow """
        # settings
        session.set_relationship_bounds(
            enabled=True,
            delimit_by_numbers=True,
            max_followers=4590,
            min_followers=45,
            min_following=77)

        # actions
        session.like_by_tags(["natgeo"], amount=10)

    return 'Done'

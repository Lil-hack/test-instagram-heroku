import os
from instapy import InstaPy

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.

    InstaPy(username="<your_username>", password="<your_password>").login()
    while True:
        pass

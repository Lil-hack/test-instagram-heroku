import os
from instapy import InstaPy

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.

    InstaPy(username="lumpyproduction@gmail.com", password="lumpybeats1996").login()
    while True:
        pass

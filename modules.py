# module basically contains a set of functions to include in our application
# there are core modules as well as can be installed with pip.

# import datetime

# today = datetime.date.today()

# we can import just date object instead of whole datetime
import time
from datetime import date
# from time import time # and then use time() instead of time.time()
today = date.today()
print(today)    # yyyy-mm-dd format

timestamp = time.time()
print(timestamp)

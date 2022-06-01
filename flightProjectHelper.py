from datetime import date, timedelta, datetime
import random

# Takes a DATETIME object and returns it in YYYY-mm-dd
# ----------------------------------------------------------------------------------------------------------------------------------------------------
def date_time_to_str(date):
    return date.strftime("%Y") + "-" + date.strftime("%m") + "-" + date.strftime("%d")
# ----------------------------------------------------------------------------------------------------------------------------------------------------

# Takes a String date and returns it as a DATETIME OBJECT
# ----------------------------------------------------------------------------------------------------------------------------------------------------
def str_to_date_time(date):
    return datetime.strptime(date, "%Y-%m-%d")
# ----------------------------------------------------------------------------------------------------------------------------------------------------


# This is a generator used for iteration over spans of time ( ie "for day in daterange(start_date, end_date): ")
# ----------------------------------------------------------------------------------------------------------------------------------------------------
def daterange(start_date, end_date):
        for n in range(int((end_date - start_date).days)):
            yield start_date + timedelta(n)
# ----------------------------------------------------------------------------------------------------------------------------------------------------


# Self Explanatory
# ----------------------------------------------------------------------------------------------------------------------------------------------------
def random_date_generator():
    x = random.randint(1, 365)
    return date.today() + timedelta(days= x)
# ----------------------------------------------------------------------------------------------------------------------------------------------------
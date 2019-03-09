from datetime import date
from datetime import datetime

my_date = date.today()

my_time = datetime.min.time()

print(datetime.combine(my_date,my_time))



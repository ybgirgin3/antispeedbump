import schedule
import time
import os
from automatic_post_sender import job



schedule.every(10).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)

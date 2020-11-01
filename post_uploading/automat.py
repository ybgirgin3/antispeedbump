import schedule as sh
import time
from datetime import datetime
from automatic_post_sender import job

sh.every(3).hours.do(job)

while True:
    print(datetime.now().strftime('%H:%M:%S'))
    sh.run_pending()
    time.sleep(1)



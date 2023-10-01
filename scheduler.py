import subprocess
from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def job():
    command = "python3 -m spacy download en"
    subprocess.call(command, shell=True)
    print("done")

sched.start()

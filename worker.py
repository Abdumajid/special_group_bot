from apscheduler.schedulers.blocking import BlockingScheduler
import urllib2
sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=10)
def timed_job():
    response = urllib2.urlopen("http://special-group.herokuapp.com")

sched.start()

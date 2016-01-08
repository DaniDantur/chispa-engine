from apscheduler.scheduler import Scheduler
import datetime as dt

sched = Scheduler()
sched.start()

def timeout(job_fn, *fn_args, **delta_args):
    time = dt.datetime.now() + dt.timedelta(**delta_args)
    return sched.add_date_job(job_fn, time, fn_args)

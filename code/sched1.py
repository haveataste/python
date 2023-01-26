import sched

sched.scheduler()#创建一个调度任务
scheduler.enter(delay,priority,action,argument=())
scheduler.run()
scheduler.cancel(event)

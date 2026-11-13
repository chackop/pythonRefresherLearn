import sched
import time


def schedule_alarm(event_time, function, *args):
    schedvar = sched.scheduler(time.time, time.sleep)
    schedvar.enterabs(event_time, 1, function, argument=args)
    print(
        f"Alarm scheduled for {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(event_time))}"
    )
    schedvar.run()


schedule_alarm(time.time() + 10, print, "Alarm triggered!")

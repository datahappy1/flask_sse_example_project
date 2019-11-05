import time
import boto3
import random
import time

class EMR:
    """

    """
    def __init__(self, job_id):
        self.job_id = job_id

    def list_steps_for_job(self):
        pass

    def trigger_step(self):
        pass

def fetch_step_states(job_id):
    j1= [{'step1': 'running', 'step2': 'pending', 'step3': 'finished'}]
    j2= [{'step1': 'pending', 'step2': 'failed', 'step3': 'finished'}]

    if random.randint(0, 2) == 1:
        time.sleep(1)
        return j1
    else:
        time.sleep(2)
        return j2

    # def get_message(id):
    #     "this could be any function that blocks until data is ready"
    #
    #     time.sleep(float(id))
    #
    #     s = time.ctime(time.time())
    #     return s

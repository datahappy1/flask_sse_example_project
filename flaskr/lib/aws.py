import boto3
import random
import time
from flaskr.config.settings import EMR_JOB_STATUSES_FINISHED_FAILED, \
    EMR_JOB_STATUSES_FINISHED_SUCCEEDED, EMR_JOB_STATUSES_NON_FINISHED, EMR_JOB_ID
from flask import session

class EMR:
    """

    """
    def __init__(self, job_id):
        self.job_id = job_id

    def list_steps_for_job(self):
        pass

    def trigger_step(self):
        pass

def fetch_step_state(step_id):
    if step_id not in EMR_JOB_STATUSES_FINISHED_SUCCEEDED or step_id not in EMR_JOB_STATUSES_FINISHED_FAILED:
        step_id_status = ''
    return step_id_status

def fetch_step_states(job_id):
    j1= [{'step1': 'running'}, {'step2': 'pending'}, {'step3': 'finished'}]
    j2= [{'step1': 'pending'}, {'step2': 'failed'}, {'step3': 'finished'}]

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

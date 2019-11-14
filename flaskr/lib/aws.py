import boto3
import random
import time
import json
from flaskr.config.settings import EMR_JOB_STATUSES_FINISHED_FAILED, \
    EMR_JOB_STATUSES_FINISHED_SUCCEEDED, EMR_JOB_STATUSES_NON_FINISHED, EMR_JOB_ID
from flask import jsonify

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
    j1= [{'step_name': 'step1', 'step_state': 'running'}, {'step_name': 'step2', 'step_state': 'pending'}, {'step_name': 'step3', 'step_state': 'finished'}]
    j2= [{'step_name': 'step1', 'step_state': 'pending'}, {'step_name': 'step2', 'step_state': 'failed'}, {'step_name': 'step3', 'step_state': 'finished'}]

    if random.randint(0, 2) == 1:
        time.sleep(1)
        return json.dumps(j1)
    else:
        time.sleep(2)
        return json.dumps(j2)

    # def get_message(id):
    #     "this could be any function that blocks until data is ready"
    #
    #     time.sleep(float(id))
    #
    #     s = time.ctime(time.time())
    #     return s

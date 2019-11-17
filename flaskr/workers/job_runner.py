import random
import time
import json

def fetch_job_states():
    """
    dummy function returning random dictionaries
    with job names and job states for the purpose of
    simulating the actual long running tasks
    :return:
    """
    j1 = [{'job_name': 'job1', 'job_state': 'running'}, {'job_name': 'job2', 'job_state': 'pending'}, {'job_name': 'job3', 'job_state': 'finished'}]
    j2 = [{'job_name': 'job1', 'job_state': 'pending'}, {'job_name': 'job2', 'job_state': 'failed'}, {'job_name': 'job3', 'job_state': 'finished'}]

    if random.randint(0, 2) == 1:
        time.sleep(1)
        return json.dumps(j1)
    else:
        time.sleep(2)
        return json.dumps(j2)

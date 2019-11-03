import time
import boto3

class EMR:
    """

    """
    def __init__(self, job_id):
        self.job_id = job_id

    def list_steps_for_job(self):
        pass

    def trigger_step(self):
        pass

    def fetch_step_state(self, step_id):
        pass

    def get_message(id):
        "this could be any function that blocks until data is ready"

        time.sleep(float(id))

        s = time.ctime(time.time())
        return s

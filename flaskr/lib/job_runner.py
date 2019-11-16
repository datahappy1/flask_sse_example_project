import random
import time
import json

def fetch_step_states():
    j1= [{'step_name': 'step1', 'step_state': 'running'}, {'step_name': 'step2', 'step_state': 'pending'}, {'step_name': 'step3', 'step_state': 'finished'}]
    j2= [{'step_name': 'step1', 'step_state': 'pending'}, {'step_name': 'step2', 'step_state': 'failed'}, {'step_name': 'step3', 'step_state': 'finished'}]

    if random.randint(0, 2) == 1:
        time.sleep(1)
        return json.dumps(j1)
    else:
        time.sleep(2)
        return json.dumps(j2)

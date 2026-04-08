from env.models import Action
from env.tasks import get_tasks
from env.graders import grade

class EmailEnv:

    def __init__(self, task="easy"):
        self.task_data = get_tasks()
        self.task_name = task
        self.emails = self.task_data[task]
        self.done = False
        self.actions = []

    def reset(self):
     self.done = False
     self.actions = []
     return {
        "observation": {
            "emails": [
                {
                    "id": e.id,
                    "subject": e.subject,
                    "body": e.body
                }
                for e in self.emails
            ],
            "message": "Start triaging emails"
        }
    }

    def step(self, action):
        if isinstance(action, dict):
            action = Action(**action)

        self.actions.append(action)

        reward = 0.1

        if len(self.actions) > len(self.emails):
            reward = -0.1

        if len(self.actions) == len(self.emails):
            self.done = True
            reward = grade(self.task_name, self.actions)

        return (
    {
        "observation": {
            "emails": [
                {
                    "id": e.id,
                    "subject": e.subject,
                    "body": e.body
                }
                for e in self.emails
            ],
            "message": "Continue"
        }
    },
    reward,
    self.done,
    {}
)

    def state(self):
        return {
            "task": self.task_name,
            "actions_taken": len(self.actions)
        }

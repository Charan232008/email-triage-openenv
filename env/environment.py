from env.models import Observation, Action
from env.tasks import get_tasks
from env.graders import grade

class EmailEnv:

    def __init__(self, task="easy"):
        self.tasks = get_tasks()
        self.task_name = task
        self.emails = self.tasks[task]
        self.done = False
        self.actions = []

    def reset(self):
        self.done = False
        self.actions = []
        return Observation(emails=self.emails, message="Start triaging emails")

    def step(self, action: Action):
        self.actions.append(action)

        # small reward for progress
        reward = 0.1

        # penalty if too many actions
        if len(self.actions) > len(self.emails):
            reward = -0.1

        # final scoring
        if len(self.actions) == len(self.emails):
            self.done = True
            reward = grade(self.task_name, self.actions)

        return (
            Observation(emails=self.emails, message="Continue"),
            reward,
            self.done,
            {}
        )

    def state(self):
        return {
            "task": self.task_name,
            "actions_taken": len(self.actions)
        }
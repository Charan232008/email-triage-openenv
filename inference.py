import os
from openai import OpenAI
from env.environment import EmailEnv
from env.models import Action

# environment variables
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
HF_TOKEN = os.getenv("HF_TOKEN")  # NO DEFAULT

# OpenAI client
client = OpenAI(api_key="HF_TOKEN", base_url=API_BASE_URL)


def get_label_from_model(email):
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "Classify email as important, spam, or ignore."},
                {"role": "user", "content": f"Subject: {email['subject']}\nBody: {email['body']}"}
            ],
            max_tokens=5
        )

        output = response.choices[0].message.content.lower()

        if "spam" in output:
            return "spam"
        elif "ignore" in output:
            return "ignore"
        else:
            return "important"

    except Exception:
        subject = email["subject"].lower()

        if "free" in subject or "lottery" in subject:
            return "spam"
        elif "newsletter" in subject:
            return "ignore"
        else:
            return "important"


def run(task):
    print(f"[START] Running task: {task}")

    env = EmailEnv(task=task)
    obs = env.reset()

    done = False
    step_count = 0

    while not done:
        email = obs["emails"][len(env.actions)]

        label = get_label_from_model(email)

        action = Action(email_id=email["id"], label=label)

        obs, reward, done, _ = env.step(action)

        step_count += 1
        print(f"[STEP] {step_count} | email_id={email['id']} | action={label} | reward={reward}")

    print(f"[END] Task={task} Final Score={reward}\n")


if __name__ == "__main__":
    run("easy")
    run("medium")
    run("hard")

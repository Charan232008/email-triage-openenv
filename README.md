# 📧 Email Triage OpenEnv

## 🔍 Overview
This project implements a real-world email classification environment using the OpenEnv framework.

Agents must classify emails into:
- important
- spam
- ignore

---

## 🎯 Tasks

### 🟢 Easy
- Simple spam vs important classification

### 🟡 Medium
- Mixed email types with ambiguity

### 🔴 Hard
- Complex classification including ignore category

---

## ⚙️ Observation Space
- List of emails (id, subject, body)
- Instruction message

---

## 🎮 Action Space
Each action contains:
- email_id
- label (important / spam / ignore)

---

## 🏆 Reward Function
- +0.1 for each step (progress reward)
- Final reward based on accuracy (0 to 1)

---

## 🧪 Baseline Performance

| Task   | Score |
|--------|------|
| Easy   | 1.0  |
| Medium | 0.66 |
| Hard   | 1.0  |

---

## 🚀 Run Locally

```bash
pip install -r requirements.txt
python inference.py


---

## 💡 Motivation
In daily life, especially in professional environments, people spend a lot of time sorting through emails to identify what actually matters. Some emails require immediate attention, while others are irrelevant or spam.

I wanted to simulate this real-world scenario in a structured environment where an agent can learn how to prioritize and classify emails effectively. The goal was to keep the environment simple but realistic enough to reflect how humans make decisions while managing inboxes.

This project focuses on building a practical task rather than a theoretical one, making it useful for evaluating decision-making capabilities of AI systems.
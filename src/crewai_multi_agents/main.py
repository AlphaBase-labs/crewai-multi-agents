#!/usr/bin/env python
import sys
import warnings

from crewai_multi_agents.crew import AiAgents

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Systems management 101: An ultimate guide by Bryce Emley discusses the essential role of systems management in maintaining IT systems across organizations. It highlights tasks such as security, asset inventory, user management, backup and recovery, data analytics, automation, capacity forecasting, cloud management, help desk support, interoperability, education, and compliance. The purpose is to ensure networks and IT infrastructures run smoothly, from single IT personnel in basic settings to dedicated teams managing complex systems. Challenges include a learning curve, added complexity, costs, implementation issues, and strain on IT teams. Best practices involve consulting IT teams on requirements and budgets, utilizing established frameworks like FCAPS and COBIT, aligning goals with strategic vision, and setting attainable objectives. When choosing software, factors like budget, timelines, existing resources, interoperability potential, and organizational size are crucial. The right tools can enhance efficiency and reduce costs.'
    }
    
    try:
        AiAgents().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        AiAgents().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        AiAgents().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        AiAgents().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

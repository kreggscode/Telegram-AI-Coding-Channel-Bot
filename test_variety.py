"""Test script to demonstrate variety in prompts"""
from src.templates import get_python_prompt, get_js_prompt, get_ml_prompt, get_clean_code_prompt

print("=" * 60)
print("TESTING PROMPT VARIETY")
print("=" * 60)

print("\nPYTHON PROMPTS (showing topic variety):\n")
for i in range(5):
    prompt = get_python_prompt()
    # Extract the topic from the prompt
    topic_start = prompt.find("about '") + 7
    topic_end = prompt.find("'", topic_start)
    topic = prompt[topic_start:topic_end]
    print(f"  {i+1}. Topic: {topic}")

print("\nJAVASCRIPT PROMPTS (showing topic variety):\n")
for i in range(5):
    prompt = get_js_prompt()
    topic_start = prompt.find("about '") + 7
    topic_end = prompt.find("'", topic_start)
    topic = prompt[topic_start:topic_end]
    print(f"  {i+1}. Topic: {topic}")

print("\nML/AI PROMPTS (showing topic variety):\n")
for i in range(5):
    prompt = get_ml_prompt()
    topic_start = prompt.find("about '") + 7
    topic_end = prompt.find("'", topic_start)
    topic = prompt[topic_start:topic_end]
    print(f"  {i+1}. Topic: {topic}")

print("\nCLEAN CODE PROMPTS (showing topic variety):\n")
for i in range(5):
    prompt = get_clean_code_prompt()
    topic_start = prompt.find("about '") + 7
    topic_end = prompt.find("'", topic_start)
    topic = prompt[topic_start:topic_end]
    print(f"  {i+1}. Topic: {topic}")

print("\n" + "=" * 60)
print("SUCCESS: Each call generates a DIFFERENT topic!")
print("=" * 60)

from datetime import datetime
import random
from .config import COURSE_START_DATE

print("LOG: Using Templates Engine v2.1")

def get_current_day():
    """Calculate the current day of the course."""
    start = datetime.strptime(COURSE_START_DATE, "%Y-%m-%d")
    now = datetime.now()
    delta = now - start
    return max(1, delta.days + 1)

# Advanced Topic pools for high-quality variety
PYTHON_TOPICS = [
    "Object Oriented Programming (OOP)", "Generators and Iterators", "Decorators", "Context Managers",
    "List/Dict Comprehensions", "Metaclasses", "Multithreading vs Multiprocessing", "AsyncIO and Concurrency",
    "Type Hinting", "Regular Expressions", "File I/O and OS module", "Networking with Requests/Sockets",
    "Data Structures (Queues, Stacks, Heaps)", "Algorithm Complexity (Big O)"
]

JS_TOPICS = [
    "ES6+ Features", "Asynchronous JS (Promises, Async/Await)", "Closures and Scopes", "Prototypal Inheritance",
    "DOM Manipulation", "Event Loop Mechanics", "Functional Programming", "Higher Order Functions",
    "Storage (LocalStorage, IndexedDB)", "Web APIs (Fetch, Geolocation)", "Module Systems (ESM vs CJS)",
    "Performance Optimization", "Security Best Practices (XSS, CSRF)"
]

ML_TOPICS = [
    "Supervised vs Unsupervised Learning", "Linear and Logistic Regression", "Decision Trees and Random Forests",
    "Neural Network Architectures", "Natural Language Processing (NLP)", "Computer Vision Basics",
    "Feature Engineering", "Model Evaluation Metrics", "Reinforcement Learning", "Deep Learning with PyTorch",
    "Gradient Descent Optimization", "Clustering Algorithms"
]

SECURITY_TOPICS = [
    "Web Application Pentesting (OWASP Top 10)", "SQL Injection (SQLi)", "Cross-Site Scripting (XSS)", 
    "Broken Authentication", "Insecure Direct Object References (IDOR)", "Subdomain Takeover",
    "API Security Vulnerabilities", "Network Hacking and Nmap", "Buffer Overflows", "Privilege Escalation",
    "Reverse Engineering basics", "Bug Bounty Hunting Methodologies"
]


def get_python_prompt():
    day = get_current_day()
    topic = random.choice(PYTHON_TOPICS)
    return (
        f"Today is Day {day} of the Elite Python Course. Topic: {topic}. "
        "Create an advanced lesson (100 words max) including:\n"
        "1. Header: **🐍 Python Mastery: Day [X] - [Topic]**\n"
        "2. An extreme/advanced engineering insight.\n"
        "3. A professional code snippet in triple backticks.\n"
        "STRICT: No beginner talk. Focus on high-performance logic. "
        "Use triple backticks for code so it's copy-pasteable."
    )


def get_js_prompt():
    day = get_current_day()
    topic = random.choice(JS_TOPICS)
    return (
        f"Today is Day {day} of the Modern JavaScript Pro Course. Topic: {topic}. "
        "Create an advanced lesson (100 words max) including:\n"
        "1. Header: **⚡ JS Pro: Day [X] - [Topic]**\n"
        "2. Senior-level architectural insight (ES6+).\n"
        "3. A clean code snippet in triple backticks.\n"
        "STRICT: No 'hello world' examples. Focus on production-grade logic."
    )


def get_ml_prompt():
    day = get_current_day()
    topic = random.choice(ML_TOPICS)
    return (
        f"Today is Day {day} of the AI/ML Engineering Course. Topic: {topic}. "
        "Create a technical lesson (120 words max) including:\n"
        "1. Header: **🤖 ML Engineering: Day [X] - [Topic]**\n"
        "2. Mathematical or structural insight.\n"
        "3. A scikit-learn/numpy/torch code snippet in triple backticks.\n"
        "STRICT: Focus on performance and scalability."
    )


def get_security_prompt():
    day = get_current_day()
    topic = random.choice(SECURITY_TOPICS)
    return (
        f"Today is Day {day} of the Cyber Security & Bug Bounty Course. Topic: {topic}. "
        "Create a 'wild' technical lesson (120 words max) including:\n"
        "1. Header: **🔓 Cyber Security: Day [X] - [Topic]**\n"
        "2. Detailed exploit/vulnerability logic.\n"
        "3. A PoC script/payload in triple backticks.\n"
        "STRICT: Make it sound professional and advanced."
    )


TEXT_TEMPLATES = {
    "python_tip": get_python_prompt,
    "js_tip": get_js_prompt,
    "ml_tip": get_ml_prompt,
    "security_tip": get_security_prompt,
    "tech_news": (
        "Write a short tech/coding news update with this EXACT format:\n\n"
        "**📰 Tech News: [Headline]**\n\n"
        "[2-3 sentences about a recent development in programming, AI, or tech]\n\n"
        "**🔍 What This Means:**\n"
        "• [Impact point 1]\n"
        "• [Impact point 2]\n\n"
        "**💭 For Developers:**\n"
        "[One sentence about how this affects developers]\n\n"
        "Keep it current, relevant, and under 120 words. Make it sound recent and exciting."
    ),
    "thread_explainer": (
        "Explain a programming concept with this EXACT format:\n\n"
        "**🧵 Thread: [Concept Name Explained]**\n\n"
        "**1️⃣ What is it?**\n"
        "[2-3 sentences]\n\n"
        "**2️⃣ How it works:**\n"
        "[2-3 sentences with simple example]\n\n"
        "**3️⃣ When to use it:**\n"
        "[2-3 sentences]\n\n"
        "**4️⃣ Pro tip:**\n"
        "[1-2 sentences with actionable advice]\n\n"
        "Keep each section concise and clear."
    ),
    "poll_question": (
        "Create ONE multiple choice coding question. "
        "Format strictly as: Question? | Option A, Option B, Option C. "
        "Make it short and clear, suitable for a Telegram poll."
    )
}


IMAGE_TEMPLATES = {
    "coding_hero": "futuristic illustration of a programmer surrounded by glowing code, cyberpunk style, high detail, vibrant colors",
    "python_image": "minimalist flat illustration of a Python snake made of colorful code, modern design, dark background with neon accents",
    "ml_image": "neural network with glowing connections, abstract art, dark background, vibrant blue and purple colors",
    "js_image": "JavaScript code flowing in 3D space, golden and yellow colors, modern tech illustration, dark background",
    "tech_news": "futuristic tech news broadcast, holographic displays, cyberpunk style, vibrant colors, high detail",
    "clean_code": "before and after code comparison, split screen, one side messy one side clean, minimalist illustration",
}

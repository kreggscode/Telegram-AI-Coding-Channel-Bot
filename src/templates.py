from datetime import datetime
from .config import COURSE_START_DATE

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
        f"You are teaching a Python course. Today is **Day {day}**. "
        f"Topic: {topic}. "
        "Create a lesson that includes:\n"
        "1. A clear header: **🐍 Python Mastery: Day [X] - [Topic Name]**\n"
        "2. A detailed yet concise explanation of the concept.\n"
        "3. A high-quality, professional code snippet using triple backticks and the 'python' language tag so it's easy to copy-paste.\n"
        "4. 2-3 bullet points on practical use cases.\n\n"
        "STRICT RULE: The code must be in this format for Telegram copy-paste to work:\n"
        "```python\n[CODE HERE]\n```\n"
        f"Make this unique for {topic}."
    )


def get_js_prompt():
    day = get_current_day()
    topic = random.choice(JS_TOPICS)
    return (
        f"You are teaching a JavaScript course. Today is **Day {day}**. "
        f"Topic: {topic}. "
        "Create a lesson that includes:\n"
        "1. A clear header: **⚡ JavaScript Pro Course: Day [X] - [Topic Name]**\n"
        "2. A detailed yet concise explanation using modern ES6+ standards.\n"
        "3. A high-quality code snippet using triple backticks and 'javascript' for copy-paste compatibility.\n"
        "4. A 'Pro Tip' highlight.\n\n"
        "STRICT RULE: The code must be in this format:\n"
        "```javascript\n[CODE HERE]\n```\n"
        f"Make this unique for {topic}."
    )


def get_ml_prompt():
    day = get_current_day()
    topic = random.choice(ML_TOPICS)
    return (
        f"You are teaching Machine Learning. Today is **Day {day}**. "
        f"Topic: {topic}. "
        "Create a lesson that includes:\n"
        "1. A clear header: **🤖 AI/ML Engineering: Day [X] - [Topic Name]**\n"
        "2. A clear explanation of the mathematical or logical concept.\n"
        "3. A working code example using numpy, pandas, or scikit-learn in triple backticks ('python' tag).\n"
        "4. A 'Real-world Application' point.\n\n"
        "STRICT RULE: Use triple backticks for the code snippet so it's copy-pasteable."
    )


def get_security_prompt():
    day = get_current_day()
    topic = random.choice(SECURITY_TOPICS)
    return (
        f"You are teaching Cybersecurity and Bug Bounty Hunting. Today is **Day {day}**. "
        f"Topic: {topic}. "
        "Create a highly detailed technical lesson that includes:\n"
        "1. A clear header: **🔓 Cyber Security & Bug Bounty: Day [X] - [Topic Name]**\n"
        "2. Detailed information on the vulnerability or technique.\n"
        "3. A code snippet (PoC), payload, or script (e.g., Python, Bash) in triple backticks.\n"
        "4. 2-3 Remediation steps to fix the bug.\n\n"
        "STRICT RULE: Ensure all code/payloads are in triple backticks for easy copy-pasting."
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

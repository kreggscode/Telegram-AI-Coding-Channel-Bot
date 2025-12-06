import random

# Topic pools for variety
PYTHON_TOPICS = [
    "list comprehensions", "decorators", "generators", "context managers", 
    "lambda functions", "f-strings", "dataclasses", "async/await", 
    "type hints", "walrus operator", "match statements", "itertools",
    "collections module", "pathlib", "enumerate tricks", "zip function"
]

JS_TOPICS = [
    "destructuring", "spread operator", "async/await", "promises", 
    "arrow functions", "template literals", "optional chaining", 
    "nullish coalescing", "array methods", "modules", "fetch API",
    "map/filter/reduce", "closures", "event delegation", "proxy objects"
]

ML_TOPICS = [
    "linear regression", "decision trees", "neural networks", "k-means clustering",
    "random forests", "gradient descent", "feature scaling", "cross-validation",
    "confusion matrix", "overfitting prevention", "data preprocessing", "model evaluation"
]

CLEAN_CODE_TOPICS = [
    "meaningful variable names", "single responsibility", "DRY principle",
    "function length", "error handling", "code comments", "magic numbers",
    "nested conditionals", "early returns", "code duplication"
]


def get_python_prompt():
    topic = random.choice(PYTHON_TOPICS)
    return (
        f"Write a Python programming tip about '{topic}' with this EXACT format:\n\n"
        "**🐍 Python Tip: [Catchy Title]**\n\n"
        "[Brief 2-3 sentence explanation]\n\n"
        "**💡 Example:**\n"
        "```python\n"
        "[working code example - make it practical and different from common examples]\n"
        "```\n\n"
        "**✨ Why This Matters:**\n"
        "• [Benefit 1]\n"
        "• [Benefit 2]\n\n"
        f"Keep total under 150 words. Use actual code that works. Focus on {topic}. "
        "Make this example unique and creative, not the typical tutorial example."
    )


def get_js_prompt():
    topic = random.choice(JS_TOPICS)
    return (
        f"Write a JavaScript tip about '{topic}' with this EXACT format:\n\n"
        "**⚡ JavaScript Pro Tip: [Catchy Title]**\n\n"
        "[Brief 2-3 sentence explanation about modern ES6+ feature]\n\n"
        "**💡 Code Example:**\n"
        "```javascript\n"
        "[working code example - make it practical and modern]\n"
        "```\n\n"
        "**🎯 Key Benefits:**\n"
        "• [Benefit 1]\n"
        "• [Benefit 2]\n\n"
        f"Keep total under 150 words. Focus on {topic}. "
        "Make it practical, modern, and show a real-world use case."
    )


def get_ml_prompt():
    topic = random.choice(ML_TOPICS)
    return (
        f"Write a machine learning tip about '{topic}' with this EXACT format:\n\n"
        "**🤖 ML/AI Tip: [Catchy Title]**\n\n"
        "[Brief 2-3 sentence explanation for beginners]\n\n"
        "**💡 Code Example:**\n"
        "```python\n"
        "[simple working code example using scikit-learn, numpy, or pandas]\n"
        "```\n\n"
        "**📊 Pro Tips:**\n"
        "• [Practical tip 1]\n"
        "• [Practical tip 2]\n\n"
        f"Keep total under 180 words. Focus on {topic}. "
        "Include actual working code with a unique example."
    )


def get_clean_code_prompt():
    topic = random.choice(CLEAN_CODE_TOPICS)
    return (
        f"Write a clean code principle about '{topic}' with this EXACT format:\n\n"
        "**✨ Clean Code Principle: [Principle Name]**\n\n"
        "[Brief explanation in 2-3 sentences]\n\n"
        "**❌ Bad Example:**\n"
        "```python\n"
        "[bad code example showing the problem]\n"
        "```\n\n"
        "**✅ Good Example:**\n"
        "```python\n"
        "[improved code example showing the solution]\n"
        "```\n\n"
        "**🎯 Remember:** [One key takeaway]\n\n"
        f"Keep total under 150 words. Focus on {topic}. "
        "Use realistic code examples, not foo/bar placeholders."
    )


TEXT_TEMPLATES = {
    "python_tip": get_python_prompt,
    "js_tip": get_js_prompt,
    "ml_tip": get_ml_prompt,
    "clean_code": get_clean_code_prompt,
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

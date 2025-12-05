TEXT_TEMPLATES = {
    "python_tip": (
        "Write a Python programming tip with this EXACT format:\n\n"
        "**🐍 Python Tip: [Catchy Title]**\n\n"
        "[Brief 2-3 sentence explanation]\n\n"
        "**💡 Example:**\n"
        "```python\n"
        "[working code example]\n"
        "```\n\n"
        "**✨ Why This Matters:**\n"
        "• [Benefit 1]\n"
        "• [Benefit 2]\n\n"
        "Keep total under 150 words. Use actual code that works."
    ),
    "js_tip": (
        "Write a JavaScript tip with this EXACT format:\n\n"
        "**⚡ JavaScript Pro Tip: [Catchy Title]**\n\n"
        "[Brief 2-3 sentence explanation about modern ES6+ feature]\n\n"
        "**💡 Code Example:**\n"
        "```javascript\n"
        "[working code example]\n"
        "```\n\n"
        "**🎯 Key Benefits:**\n"
        "• [Benefit 1]\n"
        "• [Benefit 2]\n\n"
        "Keep total under 150 words. Make it practical and modern."
    ),
    "ml_tip": (
        "Write a machine learning tip with this EXACT format:\n\n"
        "**🤖 ML/AI Tip: [Catchy Title]**\n\n"
        "[Brief 2-3 sentence explanation for beginners]\n\n"
        "**💡 Code Example:**\n"
        "```python\n"
        "[simple working code example using scikit-learn or similar]\n"
        "```\n\n"
        "**📊 Pro Tips:**\n"
        "• [Practical tip 1]\n"
        "• [Practical tip 2]\n\n"
        "Keep total under 180 words. Include actual code."
    ),
    "clean_code": (
        "Write a clean code principle with this EXACT format:\n\n"
        "**✨ Clean Code Principle: [Principle Name]**\n\n"
        "[Brief explanation in 2-3 sentences]\n\n"
        "**❌ Bad Example:**\n"
        "```python\n"
        "[bad code example]\n"
        "```\n\n"
        "**✅ Good Example:**\n"
        "```python\n"
        "[improved code example]\n"
        "```\n\n"
        "**🎯 Remember:** [One key takeaway]\n\n"
        "Keep total under 150 words."
    ),
    "tech_news": (
        "Write a short tech/coding news update with this EXACT format:\n\n"
        "**📰 Tech News: [Headline]**\n\n"
        "[2-3 sentences about a recent development in programming, AI, or tech]\n\n"
        "**🔍 What This Means:**\n"
        "• [Impact point 1]\n"
        "• [Impact point 2]\n\n"
        "**💭 For Developers:**\n"
        "[One sentence about how this affects developers]\n\n"
        "Keep it current, relevant, and under 120 words. Make it sound recent."
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
    ),
    "motivational_tip": (
        "Write an inspiring developer career tip with this EXACT format:\\n\\n"
        "**💪 Developer Motivation: [Catchy Title]**\\n\\n"
        "[2-3 sentences of encouraging advice for developers]\\n\\n"
        "**🎯 Action Steps:**\\n"
        "• [Actionable step 1]\\n"
        "• [Actionable step 2]\\n\\n"
        "**💡 Remember:**\\n"
        "[One powerful closing thought]\\n\\n"
        "Keep it positive, practical, and under 120 words. Focus on career growth, learning, or work-life balance."
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

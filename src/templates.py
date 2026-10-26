from datetime import datetime
import random
from .config import COURSE_START_DATE

print("LOG: Using Templates Engine v2.3 (LeetCode POTD, Executive PDFs & SEO)")


def get_current_day():
    """Calculate the current day of the course."""
    try:
        start = datetime.strptime(COURSE_START_DATE, "%Y-%m-%d")
        now = datetime.now()
        delta = now - start
        return max(1, delta.days + 1)
    except Exception:
        return 1


# Advanced Topic pools for high-quality variety
PYTHON_TOPICS = [
    "Object Oriented Programming (OOP & Dunder Methods)",
    "Generators, Yield and Memory-Efficient Iterators",
    "Advanced Decorators and Function Wrappers",
    "Context Managers and the 'with' Statement",
    "List, Set & Dict Comprehensions with Walrus Operator",
    "Metaclasses and Class Creation Hooks",
    "Multithreading vs Multiprocessing & the GIL",
    "AsyncIO, Coroutines and Event Loops",
    "Type Hinting, Generics and Pydantic Models",
    "Advanced Regular Expressions and Pattern Matching",
    "High-Performance File I/O and Streaming",
    "Networking with Async Sockets and HTTPX",
    "Data Structures: Queues, Heaps (heapq) & Deques",
    "Algorithm Complexity & Memory Profiling (tracemalloc)",
    "Design Patterns: Factory, Singleton & Observer in Python",
    "Functional Programming: functools (lru_cache, partial)"
]

LEETCODE_TOPICS = [
    "Two Sum & HashMap Lookup (O(N) Optimal Strategy)",
    "Best Time to Buy and Sell Stock (Kadane's & Single Pass)",
    "LRU Cache Architecture (Doubly Linked List + HashMap)",
    "Trapping Rain Water (Two-Pointer vs Monotonic Stack)",
    "Longest Substring Without Repeating Characters (Sliding Window)",
    "Reverse Linked List (Iterative Pointer Manipulation vs Recursion)",
    "Merge Intervals & Overlapping Range Optimization",
    "Binary Tree Level Order Traversal (BFS & Queue Optimization)",
    "Word Break & Dynamic Programming Tabulation",
    "Coin Change Problem (Unbounded Knapsack DP)",
    "Course Schedule & Topological Sort (Kahn's Algorithm)",
    "Kth Largest Element in an Array (Min-Heap vs QuickSelect)",
    "Median of Two Sorted Arrays (Binary Search on Partition)",
    "Number of Islands & Connected Components (DFS Grid Traversal)",
    "Valid Parentheses & Monotonic Stack Evaluation",
    "Search in Rotated Sorted Array (Modified Binary Search)"
]

JS_TOPICS = [
    "ES6+ Modern Syntax and Destructuring Patterns",
    "Asynchronous JS: Deep Dive into Promises & Async/Await",
    "Closures, Lexical Scope and Execution Context",
    "The JavaScript Event Loop, Microtasks & Macrotasks",
    "Functional Programming, Immutability & Currying",
    "Prototypal Inheritance and Class Mechanics",
    "Web APIs: Fetch API, AbortController & Streams",
    "Module Systems: ESM vs CommonJS & Tree Shaking",
    "TypeScript Essentials: Generics, Utility Types & Inference",
    "Performance Optimization: Debouncing, Throttling & Memoization",
    "Web Security: Preventing XSS, CSRF & Injection",
    "State Management Principles & Immutability Patterns"
]

ML_TOPICS = [
    "Supervised vs Unsupervised Learning Paradigms",
    "Linear and Logistic Regression from Intuition to Code",
    "Decision Trees, Random Forests and Ensemble Methods",
    "Neural Network Architectures & Backpropagation",
    "Natural Language Processing (NLP) & Tokenization",
    "Computer Vision Fundamentals & Convolutional Operations",
    "Feature Engineering, Encoding & Scaling Strategies",
    "Model Evaluation Metrics: ROC-AUC, F1-Score & Precision-Recall",
    "Deep Learning Workflows with PyTorch Tensors",
    "Gradient Descent Optimization: Adam, RMSprop & Learning Rate Schedules",
    "Clustering Algorithms: K-Means, DBSCAN & Silhouette Analysis",
    "Vector Embeddings and Semantic Search Architecture"
]

SECURITY_TOPICS = [
    "OWASP Top 10 Vulnerabilities & Enterprise Defense",
    "SQL Injection (SQLi) Exploitation & Prepared Statements",
    "Cross-Site Scripting (XSS): Stored, Reflected & DOM-based",
    "Broken Authentication & Secure JWT Implementation",
    "Insecure Direct Object References (IDOR) & Access Control",
    "API Security: Rate Limiting, CORS & Token Validation",
    "Network Reconnaissance & Port Scanning Architecture",
    "Privilege Escalation Mechanics & Remediation",
    "Reverse Engineering Fundamentals & Static Analysis",
    "Cryptographic Hashing, Salt & Secure Password Storage",
    "Bug Bounty Hunting Methodologies & Recon Workflows",
    "Defense in Depth & Cloud Security Hardening"
]

INTERVIEW_TOPICS = [
    "Data Structures: Arrays, HashMaps & Two-Pointer Patterns",
    "System Design: Designing a High-Throughput URL Shortener",
    "Concurrency, Race Conditions & Mutex Locks",
    "Database Indexing: B-Trees, Query Optimization & EXPLAIN",
    "Distributed Systems: CAP Theorem, Partitioning & Consensus",
    "Caching Strategies: Cache-Aside, Write-Through & Eviction (LRU)",
    "Load Balancing Algorithms & Reverse Proxies (Nginx)",
    "Message Queues & Event-Driven Architecture (Kafka / RabbitMQ)",
    "Dynamic Programming: Memoization vs Tabulation Strategies",
    "Graph Algorithms: Breadth-First Search (BFS) vs DFS & Dijkstra",
    "Object-Oriented Design: SOLID Principles with Practical Examples",
    "Microservices Architecture: Service Mesh, Gateways & Circuit Breakers"
]


def get_python_prompt():
    day = get_current_day()
    topic = random.choice(PYTHON_TOPICS)
    return (
        f"Today is Day {day} of the Elite Python Course. Topic: {topic}.\n\n"
        "Create a premium, master-level coding lesson in Markdown with this EXACT structure:\n\n"
        f"**🐍 Python Mastery: Day {day} - {topic}**\n\n"
        "💡 **Architectural Insight:**\n"
        "Explain senior-level intuition (2-3 concise paragraphs): how it works under the hood, memory/runtime implications, and why it matters in high-performance production systems.\n\n"
        "💻 **Production Code Snippet:**\n"
        "Provide a realistic, production-ready code snippet. CRITICAL REQUIREMENTS:\n"
        "- The code MUST be 100% complete, runnable, and bug-free.\n"
        "- NEVER use placeholders or ellipses like '# ... rest of code'. Write working logic.\n"
        "- Include helpful comments explaining key lines.\n"
        "- Wrap the code in triple backticks with the language tag (```python\\n...\\n```) so Telegram renders the interactive Copy Code button.\n\n"
        "⚡ **Key Takeaways:**\n"
        "• Pro-Tip: [Senior best practice]\n"
        "• Pitfall: [Common mistake/anti-pattern to avoid]\n\n"
        "[QUIZ]\n"
        "Question: [A clear knowledge-check multiple choice question]\n"
        "Options: [Option A] | [Option B] | [Option C] | [Option D]\n"
        "Correct: [Index 0-3]\n"
        "Explanation: [Concise 1-2 sentence explanation of the correct answer]\n"
        "[/QUIZ]\n\n"
        "STRICT OPTION FORMAT: Each option MUST be inside brackets separated by pipe: [Option 1] | [Option 2] | [Option 3] | [Option 4]."
    )


def get_leetcode_prompt():
    day = get_current_day()
    topic = random.choice(LEETCODE_TOPICS)
    return (
        f"Today is Day {day} of the FAANG LeetCode Problem of the Day. Problem Focus: {topic}.\n\n"
        "Create an elite, interview-ready LeetCode deep-dive in Markdown with this EXACT structure:\n\n"
        f"**🧩 LeetCode POTD: Day {day} - {topic}**\n\n"
        "💡 **Problem & Algorithmic Strategy:**\n"
        "Explain the core algorithmic pattern (2-3 concise paragraphs): why brute force fails, how senior engineers identify the optimal approach (e.g. Two-Pointer, Sliding Window, Monotonic Stack, or DP), and key constraints.\n\n"
        "💻 **Optimal Solution (Python):**\n"
        "Provide the complete, 100% runnable, optimal solution. CRITICAL REQUIREMENTS:\n"
        "- The code MUST be 100% complete, runnable, and bug-free.\n"
        "- NEVER use placeholders or ellipses like '# ...'. Write genuine working logic.\n"
        "- Specify Time Complexity (e.g. O(N)) and Space Complexity (e.g. O(1)) in comments.\n"
        "- Wrap the code in triple backticks with the language tag (```python\\n...\\n```) so Telegram renders the Copy Code button.\n\n"
        "⚡ **FAANG Interview Tips:**\n"
        "• Reusable Pattern: [How to apply this pattern to similar LeetCode problems]\n"
        "• Edge Case: [Critical edge case interviewers test for]\n\n"
        "[QUIZ]\n"
        "Question: [A question testing algorithmic complexity or edge case for this problem]\n"
        "Options: [Option A] | [Option B] | [Option C] | [Option D]\n"
        "Correct: [Index 0-3]\n"
        "Explanation: [Concise 1-2 sentence explanation of why this is correct]\n"
        "[/QUIZ]\n\n"
        "STRICT OPTION FORMAT: Each option MUST be inside brackets separated by pipe: [Option 1] | [Option 2] | [Option 3] | [Option 4]."
    )


def get_js_prompt():
    day = get_current_day()
    topic = random.choice(JS_TOPICS)
    return (
        f"Today is Day {day} of the Modern JavaScript Pro Course. Topic: {topic}.\n\n"
        "Create a premium, senior-level coding lesson in Markdown with this EXACT structure:\n\n"
        f"**⚡ JS Pro: Day {day} - {topic}**\n\n"
        "💡 **Architectural Insight:**\n"
        "Explain senior-level intuition (2-3 concise paragraphs): event loop behavior, browser/Node engine mechanics, and modern ES6+/TypeScript best practices.\n\n"
        "💻 **Production Code Snippet:**\n"
        "Provide a realistic, production-ready code snippet. CRITICAL REQUIREMENTS:\n"
        "- The code MUST be 100% complete, runnable, and bug-free.\n"
        "- NEVER use placeholders or ellipses like '// ... rest of code'. Write working logic.\n"
        "- Include helpful comments explaining key lines.\n"
        "- Wrap the code in triple backticks with the language tag (```javascript\\n...\\n```) so Telegram renders the interactive Copy Code button.\n\n"
        "⚡ **Key Takeaways:**\n"
        "• Pro-Tip: [Senior best practice]\n"
        "• Pitfall: [Common mistake/anti-pattern to avoid]\n\n"
        "[QUIZ]\n"
        "Question: [A clear knowledge-check multiple choice question]\n"
        "Options: [Option A] | [Option B] | [Option C] | [Option D]\n"
        "Correct: [Index 0-3]\n"
        "Explanation: [Concise 1-2 sentence explanation of the correct answer]\n"
        "[/QUIZ]\n\n"
        "STRICT OPTION FORMAT: Each option MUST be inside brackets separated by pipe: [Option 1] | [Option 2] | [Option 3] | [Option 4]."
    )


def get_ml_prompt():
    day = get_current_day()
    topic = random.choice(ML_TOPICS)
    return (
        f"Today is Day {day} of the AI/ML Engineering Course. Topic: {topic}.\n\n"
        "Create a premium, engineering-focused ML lesson in Markdown with this EXACT structure:\n\n"
        f"**🤖 ML Engineering: Day {day} - {topic}**\n\n"
        "💡 **Mathematical & Architectural Insight:**\n"
        "Explain senior-level intuition (2-3 concise paragraphs): core math/structural logic, data scaling challenges, and production deployment considerations.\n\n"
        "💻 **Production Code Snippet:**\n"
        "Provide a realistic, production-ready scikit-learn, numpy, or PyTorch snippet. CRITICAL REQUIREMENTS:\n"
        "- The code MUST be 100% complete, runnable, and bug-free.\n"
        "- NEVER use placeholders or ellipses like '# ... rest of code'. Write working logic.\n"
        "- Include helpful comments explaining key lines.\n"
        "- Wrap the code in triple backticks with the language tag (```python\\n...\\n```) so Telegram renders the interactive Copy Code button.\n\n"
        "⚡ **Key Takeaways:**\n"
        "• Pro-Tip: [Senior best practice]\n"
        "• Pitfall: [Common mistake/anti-pattern to avoid]\n\n"
        "[QUIZ]\n"
        "Question: [A clear knowledge-check multiple choice question]\n"
        "Options: [Option A] | [Option B] | [Option C] | [Option D]\n"
        "Correct: [Index 0-3]\n"
        "Explanation: [Concise 1-2 sentence explanation of the correct answer]\n"
        "[/QUIZ]\n\n"
        "STRICT OPTION FORMAT: Each option MUST be inside brackets separated by pipe: [Option 1] | [Option 2] | [Option 3] | [Option 4]."
    )


def get_security_prompt():
    day = get_current_day()
    topic = random.choice(SECURITY_TOPICS)
    return (
        f"Today is Day {day} of the Cyber Security & Bug Bounty Course. Topic: {topic}.\n\n"
        "Create an elite, technical cyber security lesson in Markdown with this EXACT structure:\n\n"
        f"**🔓 Cyber Security: Day {day} - {topic}**\n\n"
        "💡 **Vulnerability & Threat Analysis:**\n"
        "Explain senior-level exploit logic (2-3 concise paragraphs): root cause vulnerability, real-world attack vectors, and secure defensive engineering.\n\n"
        "💻 **Security Audit / Remediation Script:**\n"
        "Provide a realistic Python security audit script, payload demo, or defensive mitigation snippet. CRITICAL REQUIREMENTS:\n"
        "- The code MUST be 100% complete, runnable, and bug-free.\n"
        "- NEVER use placeholders or ellipses like '# ...'. Write working logic.\n"
        "- Include helpful comments explaining key lines.\n"
        "- Wrap the code in triple backticks with the language tag (```python\\n...\\n```) so Telegram renders the interactive Copy Code button.\n\n"
        "⚡ **Key Takeaways:**\n"
        "• Offensive Recon: [How attackers identify this flaw]\n"
        "• Defensive Hardening: [How architects patch it securely]\n\n"
        "[QUIZ]\n"
        "Question: [A clear knowledge-check multiple choice question]\n"
        "Options: [Option A] | [Option B] | [Option C] | [Option D]\n"
        "Correct: [Index 0-3]\n"
        "Explanation: [Concise 1-2 sentence explanation of the correct answer]\n"
        "[/QUIZ]\n\n"
        "STRICT OPTION FORMAT: Each option MUST be inside brackets separated by pipe: [Option 1] | [Option 2] | [Option 3] | [Option 4]."
    )


def get_interview_prompt():
    day = get_current_day()
    topic = random.choice(INTERVIEW_TOPICS)
    return (
        f"Today is Day {day} of the FAANG Interview Prep Series. Topic: {topic}.\n\n"
        "Create a top-tier technical interview guide in Markdown with this EXACT structure:\n\n"
        f"**💼 Interview Prep: Day {day} - {topic}**\n\n"
        "💡 **The Problem / Architecture Question:**\n"
        "Present a realistic technical question asked at FAANG/Tier-1 companies, followed by the senior engineering approach to solve it with optimal time/space complexity.\n\n"
        "💻 **Optimal Production Solution:**\n"
        "Provide the complete, optimal Python or algorithm solution snippet. CRITICAL REQUIREMENTS:\n"
        "- The code MUST be 100% complete, runnable, and bug-free.\n"
        "- NEVER use placeholders or ellipses like '# ...'. Write working logic.\n"
        "- Include Big-O Time & Space complexity in comments.\n"
        "- Wrap the code in triple backticks with the language tag (```python\\n...\\n```) so Telegram renders the interactive Copy Code button.\n\n"
        "⚡ **Interview Success Key:**\n"
        "• Trade-off: [Key trade-off to mention to the interviewer]\n"
        "• Follow-up: [Typical follow-up question interviewers ask]\n\n"
        "[QUIZ]\n"
        "Question: [A quick conceptual knowledge check related to this interview problem]\n"
        "Options: [Option A] | [Option B] | [Option C] | [Option D]\n"
        "Correct: [Index 0-3]\n"
        "Explanation: [Concise 1-2 sentence explanation of why this answer is correct]\n"
        "[/QUIZ]\n\n"
        "STRICT OPTION FORMAT: Each option MUST be inside brackets separated by pipe: [Option 1] | [Option 2] | [Option 3] | [Option 4]."
    )


TEXT_TEMPLATES = {
    "python_tip": get_python_prompt,
    "leetcode_tip": get_leetcode_prompt,
    "js_tip": get_js_prompt,
    "ml_tip": get_ml_prompt,
    "security_tip": get_security_prompt,
    "interview_tip": get_interview_prompt,
    "tech_news": (
        "Write a short tech/coding news update with this EXACT format:\n\n"
        "**📰 Tech News: [Headline]**\n\n"
        "[2-3 sentences about a recent development in programming, AI, or software engineering]\n\n"
        "**🔍 What This Means:**\n"
        "• [Key architectural impact point 1]\n"
        "• [Key architectural impact point 2]\n\n"
        "**💭 For Developers:**\n"
        "[One actionable sentence about how developers should prepare or leverage this]\n\n"
        "Keep it current, relevant, and under 150 words. Make it sound exciting and insightful."
    ),
    "thread_explainer": (
        "Explain a core computer science or programming concept with this EXACT format:\n\n"
        "**🧵 Deep Dive: [Concept Name Explained]**\n\n"
        "**1️⃣ Core Intuition:**\n"
        "[2-3 sentences explaining the fundamental concept simply]\n\n"
        "**2️⃣ How It Works Under The Hood:**\n"
        "[2-3 sentences with a concise code snippet or example]\n\n"
        "**3️⃣ Real-World Production Use Case:**\n"
        "[2-3 sentences explaining where high-scale companies use this]\n\n"
        "**4️⃣ Senior Engineer Pro Tip:**\n"
        "[1-2 sentences with actionable architectural advice]\n\n"
        "Keep each section clear, structured, and visually engaging."
    ),
    "poll_question": (
        "Create ONE multiple choice coding question testing software engineering knowledge. "
        "Format strictly as: Question? | Option A, Option B, Option C, Option D. "
        "Make it sharp, challenging, and suitable for a Telegram poll."
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

# SEO-Optimized Targeted Hashtags for Maximum Discoverability in Telegram Search & Google SERP
HASHTAGS = {
    "python": "\n\n━━━━━━━━━━━━━━━━━━━━\n🏷️ #Python #LearnPython #PythonProgramming #SoftwareEngineering #CodeSnippet #Developer #CodingTips #PythonProjects",
    "leetcode": "\n\n━━━━━━━━━━━━━━━━━━━━\n🏷️ #LeetCode #DSA #CodingInterview #FAANG #Algorithms #DataStructures #Python #ProblemOfTheDay #TechInterview #SoftwareEngineer",
    "javascript": "\n\n━━━━━━━━━━━━━━━━━━━━\n🏷️ #JavaScript #TypeScript #WebDevelopment #Frontend #NodeJS #ReactJS #SoftwareEngineering #CodingCommunity",
    "ml": "\n\n━━━━━━━━━━━━━━━━━━━━\n🏷️ #MachineLearning #ArtificialIntelligence #DataScience #DeepLearning #PythonML #PyTorch #AIEngineering #BigData",
    "security": "\n\n━━━━━━━━━━━━━━━━━━━━\n🏷️ #CyberSecurity #EthicalHacking #BugBounty #InfoSec #PenetrationTesting #NetworkSecurity #AppSec #Coding",
    "interview": "\n\n━━━━━━━━━━━━━━━━━━━━\n🏷️ #CodingInterview #FAANG #LeetCode #SystemDesign #SoftwareEngineer #DataStructures #Algorithms #TechCareers",
    "tech_bundle": "\n\n━━━━━━━━━━━━━━━━━━━━\n🏷️ #SoftwareEngineering #Python #JavaScript #MachineLearning #CyberSecurity #CodingCheatSheet #TechMastery",
    "magazine": "\n\n━━━━━━━━━━━━━━━━━━━━\n🏷️ #TechMagazine #SoftwareArchitecture #CodeEngineering #ProgrammingDaily #ComputerScience #TechJournal",
    "tech_news": "\n\n━━━━━━━━━━━━━━━━━━━━\n🏷️ #TechNews #ProgrammingNews #SoftwareEngineering #AIUpdates #DeveloperLife #TechTrends",
    "thread": "\n\n━━━━━━━━━━━━━━━━━━━━\n🏷️ #TechDeepDive #CodingThread #ComputerScience #SoftwareArchitecture #LearnToCode #DeveloperTips",
    "poll": "\n\n━━━━━━━━━━━━━━━━━━━━\n🏷️ #CodingQuiz #ProgrammingChallenge #DeveloperTrivia #SoftwareEngineer #TechPoll"
}

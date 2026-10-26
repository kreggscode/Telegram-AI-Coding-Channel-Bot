from datetime import datetime
import random
from .config import COURSE_START_DATE

print("LOG: Using Templates Engine v2.4 (Elite 2026 AI Engineering, LeetCode & Targeted SEO)")


def get_current_day():
    """Calculate the current day of the course."""
    try:
        start = datetime.strptime(COURSE_START_DATE, "%Y-%m-%d")
        now = datetime.now()
        delta = now - start
        return max(1, delta.days + 1)
    except Exception:
        return 1


# Elite 2026 Generative AI & Machine Learning Topics
AI_TOPICS = [
    "Retrieval-Augmented Generation (RAG) Architecture & Vector Chunking",
    "Building Autonomous AI Agents with Tool Calling & Function Execution",
    "Vector Databases: Embeddings, Cosine Similarity & HNSW Indexing",
    "Fine-Tuning LLMs with LoRA, QLoRA & HuggingFace PEFT",
    "Prompt Engineering & Structured Outputs with Pydantic & Instructor",
    "PyTorch Fundamentals: Autograd, Tensors & Custom Neural Layers",
    "Transformers Architecture: Self-Attention Mechanics & Multi-Head Attention",
    "Optimizing LLM Inference: KV-Caching, Quantization & vLLM Streaming",
    "Evaluating LLM Outputs: The RAG Triad, Faithfulness & Groundedness",
    "Multimodal AI Systems: Vision-Language Models & Embeddings",
    "Semantic Search Pipelines: Hybrid Dense & Sparse Retrieval (BM25 + Cohere)",
    "Deploying AI Microservices with FastAPI, Docker & Asynchronous WebSockets"
]

# Senior Python & Backend Systems Topics
PYTHON_TOPICS = [
    "AsyncIO Event Loops, Coroutines & Concurrency Best Practices",
    "Memory Profiling & High-Throughput Streaming (tracemalloc & generators)",
    "Metaprogramming & Advanced Decorator Architectures with functools.wraps",
    "Pydantic V2 & High-Performance Microservice Schema Validation",
    "Context Managers & Resource Management (contextlib under the hood)",
    "Multithreading vs Multiprocessing & Python 3.13 Free-Threaded GIL",
    "Type Hinting, Generics, Protocol & Static Analysis with Mypy",
    "High-Performance Caching Patterns with Redis & functools.lru_cache",
    "Design Patterns: Dependency Injection, Factory & Observer in Python",
    "Building Resilient REST APIs with FastAPI, Background Tasks & Rate Limiting",
    "Data Structures in Python: Heaps (heapq), Deques & Priority Queues",
    "Database Query Optimization with SQLAlchemy 2.0 & Connection Pooling"
]

# FAANG LeetCode Problem of the Day
LEETCODE_TOPICS = [
    "Two Sum & HashMap Lookup (O(N) Single-Pass Pattern)",
    "Best Time to Buy and Sell Stock (Kadane's Algorithm & Greedy)",
    "LRU Cache Architecture (Doubly Linked List + HashMap in O(1))",
    "Trapping Rain Water (Two-Pointer vs Monotonic Stack in O(N))",
    "Longest Substring Without Repeating Characters (Sliding Window Pattern)",
    "Reverse Linked List (Iterative Pointer Manipulation vs Recursion)",
    "Merge Intervals & Overlapping Range Optimization (Sorting + Greedy)",
    "Binary Tree Level Order Traversal (BFS & Queue Memory Optimization)",
    "Word Break & Dynamic Programming Tabulation (Bottom-Up DP)",
    "Coin Change Problem (Unbounded Knapsack & State Transitions)",
    "Course Schedule & Topological Sort (Kahn's Algorithm & Cycle Detection)",
    "Kth Largest Element in an Array (Min-Heap vs QuickSelect in O(N))",
    "Median of Two Sorted Arrays (Binary Search on Partition in O(log(min(m,n))))",
    "Number of Islands & Connected Components (DFS Grid Traversal & Flood Fill)",
    "Valid Parentheses & Monotonic Stack Evaluation",
    "Search in Rotated Sorted Array (Modified Binary Search in O(log N))"
]

# Modern Fullstack & Web Architecture Topics
FULLSTACK_TOPICS = [
    "TypeScript Advanced Types: Generics, Mapped Types & Conditional Types",
    "The JavaScript Event Loop: Microtasks, Macrotasks & Promise Execution Order",
    "Next.js App Router Architecture: Server Components vs Client Components",
    "Web Security: Defending against XSS, CSRF, CORS & Prototype Pollution",
    "Performance Optimization: Debouncing, Throttling & Web Workers",
    "State Management Architecture: Zustand, Redux Toolkit & Immutability",
    "WebSockets & Real-Time Communication with Node.js & Redis Pub/Sub",
    "API Security: JWT Authentication, Refresh Tokens & Secure Cookie Storage"
]

# Cyber Security & Defensive Engineering Topics
SECURITY_TOPICS = [
    "OWASP Top 10 Vulnerabilities: Root Cause & Enterprise Remediation",
    "SQL Injection (SQLi) Exploitation Mechanics & Parameterized Defense",
    "Cross-Site Scripting (XSS): Stored, Reflected & DOM-based Mitigation",
    "Broken Authentication & Secure JWT Implementation Vulnerabilities",
    "Insecure Direct Object References (IDOR) & Role-Based Access Control (RBAC)",
    "API Security: Rate Limiting, DDoS Mitigation & Token Bucket Algorithm",
    "Network Reconnaissance & Port Scanning Architecture with Nmap & Scapy",
    "Privilege Escalation Mechanics & Linux Security Hardening",
    "Cryptographic Hashing, Salt & Secure Password Storage (Argon2 / bcrypt)",
    "Bug Bounty Hunting Methodologies: Subdomain Enumeration & Recon Pipelines"
]


def get_ai_prompt():
    day = get_current_day()
    topic = random.choice(AI_TOPICS)
    return (
        f"Today is Day {day} of the Elite AI & Machine Learning Engineering Series. Topic: {topic}.\n\n"
        "Create an elite, cutting-edge AI engineering masterclass formatted in Markdown:\n\n"
        f"**🤖 AI Engineering: Day {day} - {topic}**\n\n"
        "💡 **Architectural & Mathematical Intuition:**\n"
        "Explain senior-level intuition (1-2 dense paragraphs): why this matters in modern Generative AI / LLM systems, core mechanisms, and production scaling challenges (latency, memory, token cost).\n\n"
        "💻 **Production-Grade Implementation (Python):**\n"
        "Provide a realistic, production-ready Python snippet (PyTorch, LangChain, Transformers, or Vector DB). CRITICAL REQUIREMENTS:\n"
        "- The code MUST be 100% complete, runnable, and bug-free.\n"
        "- NEVER use placeholders or ellipses like '# ...'. Write working logic.\n"
        "- Keep the code snippet focused and under 25 lines.\n"
        "- Wrap the code in triple backticks with the language tag (```python\\n...\\n```) so Telegram renders the Copy Code button.\n\n"
        "⚡ **Senior AI Engineer Pro-Tips:**\n"
        "• Production Best Practice: [Senior architectural rule]\n"
        "• Common Pitfall: [Real-world issue like hallucination, latency bottleneck, or OOM]\n\n"
        "[QUIZ]\n"
        "Question: [A clear knowledge-check multiple choice question on this AI concept]\n"
        "Options: [Option A] | [Option B] | [Option C] | [Option D]\n"
        "Correct: [Index 0-3]\n"
        "Explanation: [Concise 1-2 sentence explanation of why this answer is correct]\n"
        "[/QUIZ]\n\n"
        "STRICT LENGTH & FORMAT RULES:\n"
        "- Total response MUST be UNDER 2,200 characters to fit in ONE single Telegram message.\n"
        "- Each quiz option MUST be inside brackets separated by pipe: [Option 1] | [Option 2] | [Option 3] | [Option 4]."
    )


def get_python_prompt():
    day = get_current_day()
    topic = random.choice(PYTHON_TOPICS)
    return (
        f"Today is Day {day} of the Elite Python Backend Architecture Series. Topic: {topic}.\n\n"
        "Create a senior-level Python engineering lesson formatted in Markdown:\n\n"
        f"**🐍 Python Mastery: Day {day} - {topic}**\n\n"
        "💡 **Architectural Intuition & Deep Dive:**\n"
        "Explain senior-level intuition (1-2 dense paragraphs): internal runtime behavior, memory/performance implications, and why senior backend architects use this pattern.\n\n"
        "💻 **Production Code Snippet:**\n"
        "Provide a realistic, production-ready Python snippet. CRITICAL REQUIREMENTS:\n"
        "- The code MUST be 100% complete, runnable, and bug-free.\n"
        "- NEVER use placeholders or ellipses like '# ...'. Write genuine working logic.\n"
        "- Keep the code snippet focused and under 25 lines.\n"
        "- Wrap the code in triple backticks with the language tag (```python\\n...\\n```) so Telegram renders the interactive Copy Code button.\n\n"
        "⚡ **Key Architectural Takeaways:**\n"
        "• Pro-Tip: [Senior best practice for high scale]\n"
        "• Anti-Pattern: [Common bug or memory leak to avoid]\n\n"
        "[QUIZ]\n"
        "Question: [A clear knowledge-check multiple choice question]\n"
        "Options: [Option A] | [Option B] | [Option C] | [Option D]\n"
        "Correct: [Index 0-3]\n"
        "Explanation: [Concise 1-2 sentence explanation of the correct answer]\n"
        "[/QUIZ]\n\n"
        "STRICT LENGTH & FORMAT RULES:\n"
        "- Total response MUST be UNDER 2,200 characters to fit in ONE single Telegram message.\n"
        "- Each quiz option MUST be inside brackets separated by pipe: [Option 1] | [Option 2] | [Option 3] | [Option 4]."
    )


def get_leetcode_prompt():
    day = get_current_day()
    topic = random.choice(LEETCODE_TOPICS)
    return (
        f"Today is Day {day} of the FAANG LeetCode Problem of the Day. Problem Focus: {topic}.\n\n"
        "Create an elite, interview-ready LeetCode challenge formatted in Markdown:\n\n"
        f"**🧩 LeetCode POTD: Day {day} - {topic}**\n\n"
        "💡 **Problem & Algorithmic Strategy:**\n"
        "Explain the core algorithmic pattern (1-2 dense paragraphs): why brute force fails, how senior engineers identify the optimal approach (e.g. Two-Pointer, Sliding Window, Monotonic Stack, or DP), and key constraints.\n\n"
        "💻 **Optimal Solution (Python):**\n"
        "Provide the complete, 100% runnable, optimal solution. CRITICAL REQUIREMENTS:\n"
        "- The code MUST be 100% complete, runnable, and bug-free.\n"
        "- NEVER use placeholders or ellipses like '# ...'. Write genuine working logic.\n"
        "- Specify Time Complexity (e.g. O(N)) and Space Complexity (e.g. O(1)) in comments.\n"
        "- Keep the code snippet under 25 lines.\n"
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
        "STRICT LENGTH & FORMAT RULES:\n"
        "- Total response MUST be UNDER 2,200 characters to fit in ONE single Telegram message.\n"
        "- Each quiz option MUST be inside brackets separated by pipe: [Option 1] | [Option 2] | [Option 3] | [Option 4]."
    )


def get_fullstack_prompt():
    day = get_current_day()
    topic = random.choice(FULLSTACK_TOPICS)
    return (
        f"Today is Day {day} of the Modern Fullstack & TypeScript Series. Topic: {topic}.\n\n"
        "Create a modern engineering lesson formatted in Markdown:\n\n"
        f"**⚡ Fullstack Pro: Day {day} - {topic}**\n\n"
        "💡 **Architectural Insight:**\n"
        "Explain senior-level intuition (1-2 dense paragraphs): runtime mechanics, browser/Node engine behavior, and modern production best practices.\n\n"
        "💻 **Production Code Snippet:**\n"
        "Provide a clean, production-grade TypeScript/JavaScript snippet. CRITICAL REQUIREMENTS:\n"
        "- The code MUST be 100% complete, runnable, and bug-free.\n"
        "- NEVER use placeholders or ellipses like '// ...'. Write working logic.\n"
        "- Keep the code snippet focused and under 25 lines.\n"
        "- Wrap the code in triple backticks with the language tag (```typescript\\n...\\n```) so Telegram renders the Copy Code button.\n\n"
        "⚡ **Key Takeaways:**\n"
        "• Pro-Tip: [Senior best practice]\n"
        "• Pitfall: [Common mistake/anti-pattern to avoid]\n\n"
        "[QUIZ]\n"
        "Question: [A clear knowledge-check multiple choice question]\n"
        "Options: [Option A] | [Option B] | [Option C] | [Option D]\n"
        "Correct: [Index 0-3]\n"
        "Explanation: [Concise 1-2 sentence explanation of the correct answer]\n"
        "[/QUIZ]\n\n"
        "STRICT LENGTH & FORMAT RULES:\n"
        "- Total response MUST be UNDER 2,200 characters to fit in ONE single Telegram message.\n"
        "- Each quiz option MUST be inside brackets separated by pipe: [Option 1] | [Option 2] | [Option 3] | [Option 4]."
    )


def get_security_prompt():
    day = get_current_day()
    topic = random.choice(SECURITY_TOPICS)
    return (
        f"Today is Day {day} of the Cyber Security & Bug Bounty Course. Topic: {topic}.\n\n"
        "Create an elite, technical cyber security lesson in Markdown:\n\n"
        f"**🔓 Cyber Security: Day {day} - {topic}**\n\n"
        "💡 **Vulnerability & Threat Analysis:**\n"
        "Explain senior-level exploit logic (1-2 dense paragraphs): root cause vulnerability, real-world attack vectors, and secure defensive engineering.\n\n"
        "💻 **Security Audit / Remediation Script:**\n"
        "Provide a realistic Python security audit script, payload demo, or defensive mitigation snippet. CRITICAL REQUIREMENTS:\n"
        "- The code MUST be 100% complete, runnable, and bug-free.\n"
        "- Keep the code snippet focused and under 25 lines.\n"
        "- Wrap the code in triple backticks with the language tag (```python\\n...\\n```) so Telegram renders the Copy Code button.\n\n"
        "⚡ **Key Takeaways:**\n"
        "• Offensive Recon: [How attackers identify this flaw]\n"
        "• Defensive Hardening: [How architects patch it securely]\n\n"
        "[QUIZ]\n"
        "Question: [A clear knowledge-check multiple choice question]\n"
        "Options: [Option A] | [Option B] | [Option C] | [Option D]\n"
        "Correct: [Index 0-3]\n"
        "Explanation: [Concise 1-2 sentence explanation of the correct answer]\n"
        "[/QUIZ]\n\n"
        "STRICT LENGTH & FORMAT RULES:\n"
        "- Total response MUST be UNDER 2,200 characters to fit in ONE single Telegram message.\n"
        "- Each quiz option MUST be inside brackets separated by pipe: [Option 1] | [Option 2] | [Option 3] | [Option 4]."
    )


TEXT_TEMPLATES = {
    "ai_tip": get_ai_prompt,
    "python_tip": get_python_prompt,
    "leetcode_tip": get_leetcode_prompt,
    "fullstack_tip": get_fullstack_prompt,
    "security_tip": get_security_prompt,
    # Backward compatibility aliases
    "ml_tip": get_ai_prompt,
    "js_tip": get_fullstack_prompt,
    "interview_tip": get_leetcode_prompt,
    "tech_news": (
        "Write a short tech/coding news update with this EXACT format:\n\n"
        "**📰 Tech News: [Headline]**\n\n"
        "[2-3 sentences about a recent development in AI, LLMs, or Software Engineering]\n\n"
        "**🔍 What This Means:**\n"
        "• [Key architectural impact point 1]\n"
        "• [Key architectural impact point 2]\n\n"
        "**💭 For Developers:**\n"
        "[One actionable sentence about how developers should prepare or leverage this]\n\n"
        "Keep it current, relevant, and under 150 words. Make it sound exciting and insightful."
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

# High-Intent SEO Hashtags & Search Topics Bar for Maximum Telegram Global Search Ranking
HASHTAGS = {
    "ai": "\n\n━━━━━━━━━━━━━━━━━━━━\n🔍 Topics: Generative AI • LLM Engineering • PyTorch • RAG Systems\n🏷️ #ArtificialIntelligence #GenerativeAI #MachineLearning #DeepLearning #LLM #PyTorch #AIEngineering #DataScience #PythonAI",
    "ml": "\n\n━━━━━━━━━━━━━━━━━━━━\n🔍 Topics: Generative AI • LLM Engineering • PyTorch • RAG Systems\n🏷️ #ArtificialIntelligence #GenerativeAI #MachineLearning #DeepLearning #LLM #PyTorch #AIEngineering #DataScience #PythonAI",
    "python": "\n\n━━━━━━━━━━━━━━━━━━━━\n🔍 Topics: Python Backend • Microservices • Concurrency • Clean Code\n🏷️ #Python #LearnPython #PythonProgramming #SoftwareEngineering #Backend #FastAPI #CleanCode #CodeSnippet #Developer",
    "leetcode": "\n\n━━━━━━━━━━━━━━━━━━━━\n🔍 Topics: LeetCode POTD • Data Structures • Algorithms • FAANG\n🏷️ #LeetCode #DSA #CodingInterview #FAANG #Algorithms #DataStructures #Python #ProblemOfTheDay #SoftwareEngineer #TechCareers",
    "fullstack": "\n\n━━━━━━━━━━━━━━━━━━━━\n🔍 Topics: Modern TypeScript • Next.js • Fullstack Architecture • Node.js\n🏷️ #TypeScript #JavaScript #WebDev #Fullstack #NextJS #Frontend #NodeJS #SoftwareEngineering #WebDevelopment",
    "javascript": "\n\n━━━━━━━━━━━━━━━━━━━━\n🔍 Topics: Modern TypeScript • Next.js • Fullstack Architecture • Node.js\n🏷️ #TypeScript #JavaScript #WebDev #Fullstack #NextJS #Frontend #NodeJS #SoftwareEngineering #WebDevelopment",
    "security": "\n\n━━━━━━━━━━━━━━━━━━━━\n🔍 Topics: Cyber Security • Bug Bounty • OWASP • AppSec Hardening\n🏷️ #CyberSecurity #EthicalHacking #BugBounty #InfoSec #PenetrationTesting #NetworkSecurity #AppSec #SecurityEngineering",
    "interview": "\n\n━━━━━━━━━━━━━━━━━━━━\n🔍 Topics: System Design • FAANG Interview • Scalability • Microservices\n🏷️ #SystemDesign #SoftwareArchitecture #CodingInterview #DistributedSystems #FAANG #TechCareers #SoftwareEngineer",
    "tech_bundle": "\n\n━━━━━━━━━━━━━━━━━━━━\n🔍 Topics: AI • Python • LeetCode • Fullstack • Security\n🏷️ #SoftwareEngineering #Python #GenerativeAI #LeetCode #CyberSecurity #TechMastery #Programming",
    "magazine": "\n\n━━━━━━━━━━━━━━━━━━━━\n🔍 Topics: Weekly Journal • Software Architecture • AI & Cloud\n🏷️ #TechMagazine #SoftwareArchitecture #AIEngineering #CodeEngineering #ProgrammingDaily #ComputerScience"
}

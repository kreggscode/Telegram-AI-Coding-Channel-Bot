import os
import random
from datetime import datetime
from fpdf import FPDF
from . import pollinations_client as ai
from .config import POLLINATIONS_API_KEY

class CodingMagazine(FPDF):
    def __init__(self):
        super().__init__(format="A5", unit="mm")
        self.set_margins(15, 20, 15)
        self.set_auto_page_break(True, margin=20)

    def header(self):
        if self.page_no() > 1:
            self.set_font("helvetica", "I", 8)
            self.set_text_color(150)
            self.cell(0, 10, f"KREGGSCODE DAILY JOURNAL - {datetime.now().strftime('%B %d, %Y')}", align="R")
            self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 8)
        self.set_text_color(150)
        self.cell(0, 10, f"Page {self.page_no()} | KREGGSCODE ELITE", align="C")

    def clean_text(self, text):
        """Ultra-clean text for PDF: removes markdown and special chars"""
        replacements = [("*", ""), ("#", ""), ("`", ""), ("__", ""), ("- ", "o "), (">", ""), ("_", "")]
        for old, new in replacements:
            text = text.replace(old, new)
        while "\n\n\n" in text:
            text = text.replace("\n\n\n", "\n\n")
        return text.encode('latin-1', 'ignore').decode('latin-1').strip()

    def set_body_font(self):
        self.set_font("helvetica", "", 11.5)
        self.set_text_color(30)

    def draw_code_box(self, code_text):
        """Renders code in a persistent dark box across page breaks"""
        self.set_font("courier", "B", 8)
        lines = code_text.strip().split('\n')
        lh = 4.5
        
        # Dark background for the whole block area
        self.set_fill_color(20, 22, 30)
        self.set_text_color(140, 210, 255)
        
        for line in lines:
            if self.get_y() + 10 > 200:
                self.add_page()
                
            safe_line = " " + line.encode('latin-1', 'ignore').decode('latin-1')
            if len(safe_line) > 60: # Rough limit for A5 width at size 8
                safe_line = safe_line[:57] + "..."
            
            # Use X=15 to ensure we stay within margins
            self.set_x(15)
            # Use cell with ln=1 and fill=True for stability
            self.cell(118, lh, safe_line, ln=1, fill=True)
        
        self.set_text_color(0)
        self.set_body_font()
        self.ln(5)

def create_magazine():
    print("LOG: Starting Robust Mega-Generation...")
    date_str = datetime.now().strftime("%Y-%m-%d")
    full_date = datetime.now().strftime("%B %d, %Y")
    
    pdf = CodingMagazine()
    
    # --- PAGE 1: COVER ---
    print("LOG: Designing Elite Cover...")
    pdf.add_page()
    pdf.set_y(20)
    pdf.set_font("helvetica", "B", 46)
    pdf.set_text_color(20, 40, 100)
    pdf.set_x(0)
    pdf.cell(148, 20, "KREGGSCODE", align="C")
    
    pdf.set_draw_color(0, 120, 255)
    pdf.set_line_width(1.5)
    pdf.line(30, 40, 118, 40)
    
    pdf.set_y(45)
    pdf.set_font("helvetica", "B", 22)
    pdf.set_text_color(80)
    pdf.set_x(0)
    pdf.cell(148, 10, "THE ELITE TECHNICAL DAILY", align="C")

    user_image = "photo_6176981275043284142_w (1) - Copy-photoaidcom-cropped.jpg"
    if os.path.exists(user_image):
        pdf.image(user_image, x=24, y=65, w=100)
    
    pdf.set_y(180)
    pdf.set_font("helvetica", "B", 16)
    pdf.set_text_color(40)
    pdf.set_x(0)
    pdf.cell(148, 10, full_date, align="C")
    pdf.ln(8)
    pdf.set_font("helvetica", "I", 12)
    pdf.set_text_color(100)
    pdf.set_x(0)
    pdf.cell(148, 10, "Python Engineering | Distributed AI | Scalable Systems", align="C")

    # --- PAGE 2: EDITOR'S PROLOGUE ---
    print("LOG: Drafting Editor's Prologue...")
    pdf.add_page()
    pdf.set_font("helvetica", "B", 26)
    pdf.set_text_color(0, 100, 200)
    pdf.cell(0, 20, "The Director's Desk")
    pdf.ln(18)
    
    intro_p = "Write a sophisticated introduction for KREGGSCODE. Topic: The evolution of code architecture in AI-first engineering. 350 words. PLAIN TEXT. NO ASTERISKS."
    intro_txt = ai.generate_text(intro_p)
    pdf.set_body_font()
    pdf.set_x(15)
    pdf.multi_cell(118, 8, pdf.clean_text(intro_txt))

    # --- DYNAMIC CONTENT POOL ---
    topic_pool = {
        "Python Masterclass": [
            "Memory Management Internals & GC", "Meta-Programming Hooks", "High-Performance Concurrency", 
            "The Art of C-Extensions", "Bytecode Architecture", "AsyncIO Event Loop Mechanics", 
            "Metaclasses and Type Creation", "The GIL and Multicore Python", "The Descriptor Protocol Architecture",
            "Garbage Collection & Cycle Detection", "Memory Slots and __slots__ Internals"
        ],
        "Neural Infrastructure": [
            "Vision & Flash Attention", "Model Quantization & LoRA", "Distributed GPU Training", 
            "State-Space Model Internals", "RLHF Training Loops", "Transformer Scalability",
            "Knowledge Distillation", "CUDA Kernel Optimization", "MoE Architecture", "PEFT Architecture"
        ],
        "System Architecture": [
            "Zero-Trust Microservices", "LSM Engine Engineering", "Consensus Protocol Design", 
            "Kernel-Level Observability", "Vector Database Internals", "Distributed Consensus (Paxos/Raft)",
            "Scalable Cache Invalidation", "Service Mesh Performance", "Atomic Design Systems"
        ],
        "Advanced Engineering": [
            "Atomic Design Patterns", "Scaling Billions of Requests", "Clean Code in AI Era", 
            "Post-Quantum Cryptography", "High-Speed Networking", "Clean Code 2.0",
            "Low-latency Socket Programming", "eBPF Observability Patterns", "Kubernetes Operator Patterns"
        ]
    }

    # Select 4 topics per sector for a balanced ~50 page magazine (fast & deep)
    selected_sectors = []
    for sector, all_topics in topic_pool.items():
        daily_topics = random.sample(all_topics, 3) # 3 topics per sector = 12 total deep dives
        selected_sectors.append((sector, daily_topics))

    for sector_title, topics in selected_sectors:
        print(f"LOG: Processing Sector: {sector_title}...")
        for topic in topics:
            print(f"LOG: Generating Deep Dive for {topic}...")
            pdf.add_page()
            pdf.set_font("helvetica", "B", 22)
            pdf.set_text_color(0, 80, 180)
            pdf.cell(0, 15, f"{sector_title}")
            pdf.ln(10)
            pdf.set_font("helvetica", "B", 18)
            pdf.set_text_color(60)
            pdf.cell(0, 10, f"Topic: {topic}")
            pdf.ln(15)
            
            # Step 1: Technical Core (Small chunk)
            c1 = f"Technical Core of {topic}: Explain how it works at a low level. 300 words. PLAIN TEXT. NO SYMBOLS."
            t1 = ai.generate_text(c1)
            pdf.set_body_font()
            pdf.set_x(15)
            pdf.multi_cell(118, 7.5, pdf.clean_text(t1))
            pdf.ln(5)
            
            # Step 2: Implementation (Small chunk)
            c2 = f"Practical Implementation for {topic}. Provide high-quality logic or code. Wrap code in [CODE] tags. 300 words. PLAIN TEXT."
            t2 = ai.generate_text(c2)
            pdf.set_x(15)
            if "[CODE]" in t2:
                parts = t2.split("[CODE]")
                pdf.multi_cell(118, 7.5, pdf.clean_text(parts[0]))
                code_parts = parts[1].split("[/CODE]")
                pdf.draw_code_box(code_parts[0])
                if len(code_parts) > 1:
                    pdf.set_x(15)
                    pdf.multi_cell(118, 7.5, pdf.clean_text(code_parts[1]))
            else:
                pdf.multi_cell(118, 7.5, pdf.clean_text(t2))
            
            # Step 3: Production Bottlenecks (Small chunk)
            c3 = f"Explain production scaling bottlenecks and optimization strategies for {topic}. 300 words. PLAIN TEXT."
            t3 = ai.generate_text(c3)
            pdf.set_x(15)
            pdf.multi_cell(118, 7.5, pdf.clean_text(t3))

    # --- COGNITIVE LAB (QUIZZES) ---
    print("LOG: Forging Interactivity Labs...")
    for i in range(4): # 4 pages of quizzes
        pdf.add_page()
        pdf.set_font("helvetica", "B", 24)
        pdf.set_text_color(200, 0, 0)
        pdf.cell(0, 20, f"The Cognitive Lab: Set {i+1}")
        pdf.ln(15)
        
        q_p = "Create 4 elite technical MCQ questions (A-D) about the architectural topics discussed. Include detailed answers. 400 words. PLAIN TEXT. NO ASTERISKS."
        q_txt = ai.generate_text(q_p)
        pdf.set_body_font()
        pdf.set_x(15)
        pdf.multi_cell(118, 8, pdf.clean_text(q_txt))

    # --- FINAL: SOCIAL ACCESS ---
    print("LOG: Finalizing Access Channels...")
    print("LOG: Finalizing Access Channels...")
    pdf.add_page()
    pdf.set_fill_color(240, 245, 255)
    pdf.rect(0, 0, 148, 210, "F")
    
    pdf.set_y(60)
    pdf.set_font("helvetica", "B", 42)
    pdf.set_text_color(20, 40, 100)
    pdf.cell(0, 20, "KREGGSCODE", align="C")
    pdf.ln(45)
    
    socials = [
        ("INSTAGRAM", "@kreggscode", "https://instagram.com/kreggscode"),
        ("YOUTUBE", "/kreggscode", "https://youtube.com/@kreggscode"),
        ("TELEGRAM", "t.me/kreggscode", "https://t.me/kreggscode")
    ]
    
    for platform, handle, link in socials:
        pdf.set_font("helvetica", "B", 12)
        pdf.set_text_color(0, 100, 220)
        pdf.cell(0, 8, platform, align="C")
        pdf.ln(10)
        pdf.set_font("helvetica", "B", 20)
        pdf.set_text_color(40)
        pdf.cell(0, 12, handle, align="C", link=link)
        pdf.ln(25)

    out_file = f"KREGGSCODE_Premium_{date_str}.pdf"
    pdf.output(out_file)
    print(f"LOG: Successfully saved to {out_file}")
    return out_file

def download_image(url, filename):
    import requests
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
            return True
    except Exception as e:
        print(f"Error downloading image: {e}")
    return False

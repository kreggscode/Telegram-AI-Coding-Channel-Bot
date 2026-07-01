"""
Magazine Generator - Creates a branded daily magazine PDF
Uses magazine_cover.jpg as the cover image so each magazine
is visually identifiable by its unique cover. Each PDF has a unique name.
"""
import os
import random
from datetime import datetime
from fpdf import FPDF
from . import pollinations_client as ai
from .config import POLLINATIONS_API_KEY

COVER_IMAGE = "magazine_cover.jpg"


class CodingMagazine(FPDF):
    def __init__(self):
        super().__init__(format="A5", unit="mm")
        self.set_margins(15, 20, 15)
        self.set_auto_page_break(True, margin=20)

    def header(self):
        if self.page_no() > 1:
            self.set_fill_color(20, 40, 100)
            self.rect(0, 0, 148, 10, "F")
            self.set_x(0)
            self.set_y(2)
            self.set_font("helvetica", "B", 7)
            self.set_text_color(200, 220, 255)
            self.cell(148, 6, f"KREGGSCODE DAILY JOURNAL - {datetime.now().strftime('%B %d, %Y')}", align="C")
            self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 8)
        self.set_text_color(150)
        self.cell(0, 10, f"Page {self.page_no()} | KREGGSCODE ELITE", align="C")

    def clean_text(self, text):
        """Ultra-clean text for PDF: removes markdown and special chars"""
        for old, new in [("*", ""), ("#", ""), ("`", ""), ("__", ""), ("- ", "o "), (">", ""), ("_", "")]:
            text = text.replace(old, new)
        while "\n\n\n" in text:
            text = text.replace("\n\n\n", "\n\n")
        return text.encode("latin-1", "ignore").decode("latin-1").strip()

    def set_body_font(self):
        self.set_font("helvetica", "", 11.5)
        self.set_text_color(30)

    def draw_code_box(self, code_text):
        """Renders code in a persistent dark box across page breaks"""
        self.set_font("courier", "B", 8)
        lines = code_text.strip().split("\n")
        lh = 4.5
        self.set_fill_color(20, 22, 30)
        self.set_text_color(140, 210, 255)
        for line in lines:
            if self.get_y() + 10 > 200:
                self.add_page()
            safe_line = " " + line.encode("latin-1", "ignore").decode("latin-1")
            if len(safe_line) > 60:
                safe_line = safe_line[:57] + "..."
            self.set_x(15)
            self.cell(118, lh, safe_line, ln=1, fill=True)
        self.set_text_color(0)
        self.set_body_font()
        self.ln(5)

    def add_cover(self, full_date: str):
        """Cover page with logo image, title below it, only date shown.
        All elements are centered to the A5 page (148mm wide)."""
        self.add_page()
        # Dark top band (full width, starts at x=0)
        self.set_fill_color(5, 15, 50)
        self.rect(0, 0, 148, 32, "F")
        self.set_xy(0, 6)
        self.set_font("helvetica", "B", 32)
        self.set_text_color(255, 255, 255)
        self.cell(148, 12, "KREGGSCODE", align="C")
        self.set_xy(0, 20)
        self.set_font("helvetica", "", 9)
        self.set_text_color(180, 200, 255)
        self.cell(148, 5, "THE ELITE TECHNICAL DAILY", align="C")

        # Cover image (centered: x = (148-100)/2 = 24)
        if os.path.exists(COVER_IMAGE):
            try:
                self.image(COVER_IMAGE, x=24, y=36, w=100)
                content_start = 148
            except Exception as e:
                print(f"WARNING: Cover image failed: {e}")
                content_start = 55
        else:
            content_start = 55

        # Title below the image
        self.set_x(0)
        self.set_y(content_start)
        self.set_draw_color(255, 215, 0)
        self.set_line_width(0.8)
        self.line(24, self.get_y(), 124, self.get_y())
        self.ln(7)

        self.set_x(0)
        self.set_font("helvetica", "B", 18)
        self.set_text_color(15, 35, 90)
        self.cell(148, 10, "DAILY TECHNICAL MAGAZINE", align="C")
        self.ln(14)

        # Date only
        self.set_x(0)
        self.set_font("helvetica", "I", 11)
        self.set_text_color(80)
        self.cell(148, 7, full_date, align="C")
        self.ln(12)

        # Divider
        self.set_draw_color(0, 120, 255)
        self.set_line_width(0.4)
        self.line(34, self.get_y(), 114, self.get_y())
        self.ln(8)

        # Social
        self.set_x(0)
        self.set_font("helvetica", "I", 7)
        self.set_text_color(130)
        self.cell(148, 5, "Telegram: @kreggscode  |  YouTube: /kreggscode", align="C")


def create_magazine():
    print("LOG: Starting Robust Mega-Generation...")
    date_str = datetime.now().strftime("%Y-%m-%d")
    full_date = datetime.now().strftime("%B %d, %Y")

    pdf = CodingMagazine()

    # --- PAGE 1: COVER (with magazine_cover.jpg branding) ---
    print("LOG: Designing Elite Cover...")
    pdf.add_cover(full_date)

    # --- SECTORS: AI-Generated Content ---
    print("LOG: Forging Elite Content Sectors...")
    sectors = [
        ("PYTHON", "Generators and Iterators", "Mastering Lazy Evaluation"),
        ("ML ENGINEERING", "Gradient Descent and Backpropagation", "Optimization Deep Dive"),
        ("SYSTEM DESIGN", "Microservices Architecture", "Scaling Distributed Systems"),
        ("CYBER SECURITY", "Zero-Day Vulnerability Analysis", "Advanced Pentesting"),
    ]

    for sector_title, topic, subtitle in sectors:
        print(f"LOG: Generating Content for {sector_title} - {topic}...")
        pdf.add_page()
        pdf.set_x(0)
        pdf.set_font("helvetica", "B", 22)
        pdf.set_text_color(0, 80, 180)
        pdf.cell(148, 15, f"{sector_title}", align="C")
        pdf.ln(12)
        pdf.set_x(0)
        pdf.set_font("helvetica", "B", 16)
        pdf.set_text_color(60)
        pdf.cell(148, 10, f"Topic: {topic}", align="C")
        pdf.ln(15)

        c = f"Write about {topic} in three parts: (1) Technical Core - how it works at low level (2) Implementation with code snippet (wrap code in [CODE] tags) (3) Production scaling bottlenecks. 400 words total. PLAIN TEXT."
        t = ai.generate_text(c)
        if "AI generation failed" in t:
            t = f"Technical deep-dive on {topic} is being prepared. Check @kreggscode for updates."

        pdf.set_body_font()
        pdf.set_x(15)
        if "[CODE]" in t:
            parts = t.split("[CODE]")
            pdf.multi_cell(118, 7.5, pdf.clean_text(parts[0]))
            code_parts = parts[1].split("[/CODE]")
            pdf.draw_code_box(code_parts[0])
            if len(code_parts) > 1:
                pdf.set_x(15)
                pdf.multi_cell(118, 7.5, pdf.clean_text(code_parts[1]))
        else:
            pdf.set_x(15)
            pdf.multi_cell(118, 7.5, pdf.clean_text(t))

    # --- COGNITIVE LAB (QUIZZES) ---
    print("LOG: Forging Interactivity Labs...")
    pdf.add_page()
    pdf.set_x(0)
    pdf.set_font("helvetica", "B", 24)
    pdf.set_text_color(200, 0, 0)
    pdf.cell(148, 20, "The Cognitive Lab", align="C")
    pdf.ln(15)

    q_p = "Create 4 elite technical MCQ questions (A-D) about software architecture, Python, and ML. Include detailed answers. 400 words. PLAIN TEXT. NO ASTERISKS."
    q_txt = ai.generate_text(q_p)
    if "AI generation failed" in q_txt:
        q_txt = "Quizzes for this edition are being calibrated. Check @kreggscode for our weekend challenge!"

    pdf.set_body_font()
    pdf.set_x(15)
    pdf.multi_cell(118, 8, pdf.clean_text(q_txt))

    # --- FINAL: SOCIAL ACCESS ---
    print("LOG: Finalizing Access Channels...")
    pdf.add_page()
    pdf.set_fill_color(240, 245, 255)
    pdf.rect(0, 0, 148, 210, "F")
    pdf.set_x(0)
    pdf.set_y(60)
    pdf.set_font("helvetica", "B", 42)
    pdf.set_text_color(20, 40, 100)
    pdf.cell(148, 20, "KREGGSCODE", align="C")

    # Re-show the cover image on the last page
    if os.path.exists(COVER_IMAGE):
        try:
            pdf.image(COVER_IMAGE, x=44, y=85, w=60)
        except Exception:
            pass

    pdf.ln(55)
    socials = [
        ("INSTAGRAM", "@kreggscode", "https://instagram.com/kreggscode"),
        ("YOUTUBE", "/kreggscode", "https://youtube.com/@kreggscode"),
        ("TELEGRAM", "t.me/kreggscode", "https://t.me/kreggscode"),
    ]
    for platform, handle, link in socials:
        pdf.set_x(0)
        pdf.set_font("helvetica", "B", 12)
        pdf.set_text_color(0, 100, 220)
        pdf.cell(148, 8, platform, align="C")
        pdf.ln(10)
        pdf.set_x(0)
        pdf.set_font("helvetica", "B", 20)
        pdf.set_text_color(40)
        pdf.cell(148, 12, handle, align="C", link=link)
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
            with open(filename, "wb") as f:
                f.write(response.content)
            return True
    except Exception as e:
        print(f"Error downloading image: {e}")
    return False
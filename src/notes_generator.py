"""
Modern Executive Notes Generator.
Produces publication-grade, Silicon-Valley-style technical cheat sheets
with clean header banners, terminal-style dark code containers,
structured takeaway cards, and zero overflow bugs.
"""

import os
import re
from datetime import datetime
from fpdf import FPDF
from fpdf.enums import XPos, YPos

COVER_IMAGE = "magazine_cover.jpg"


class ModernNotesPDF(FPDF):
    def __init__(self, post_type: str, day: int):
        super().__init__(format="A4", unit="mm")
        self.set_margins(15, 15, 15)
        self.set_auto_page_break(True, margin=18)
        self.post_type = post_type
        self.day = day
        self.full_date = datetime.now().strftime("%B %d, %Y")

        self.type_labels = {
            "ai": "GENERATIVE AI & LLM SYSTEMS",
            "python": "PYTHON MASTERY",
            "leetcode": "LEETCODE PROBLEM OF THE DAY",
            "fullstack": "MODERN FULLSTACK & TS PRO",
            "javascript": "JAVASCRIPT & TS PRO",
            "ml": "AI / ML ENGINEERING",
            "security": "CYBER SECURITY & BUG BOUNTY",
            "interview": "FAANG INTERVIEW PREP",
            "magazine": "TECHNICAL JOURNAL",
        }
        self.track_colors = {
            "ai": (106, 27, 154),        # AI Purple / Violet
            "python": (15, 76, 129),     # Deep Python Blue
            "leetcode": (220, 110, 40),   # LeetCode Orange
            "fullstack": (195, 140, 20), # JS Warm Gold
            "javascript": (195, 140, 20), # JS Warm Gold
            "ml": (114, 9, 183),         # AI Purple
            "security": (180, 35, 40),    # Cyber Red
            "interview": (35, 95, 130),   # Slate Blue
        }

    def clean_text_for_pdf(self, text: str) -> str:
        """Convert Unicode symbols, smart quotes, and dashes to clean Latin-1 characters."""
        replacements = [
            ("“", '"'), ("”", '"'), ("‘", "'"), ("’", "'"),
            ("—", "-"), ("–", "-"), ("•", "*"), ("→", "->"),
            ("💡", "[CONCEPT] "), ("💻", "[CODE] "), ("⚡", "[PRO-TIP] "),
            ("🐍", ""), ("🤖", ""), ("🔓", ""), ("💼", ""), ("🧩", ""),
            ("**", ""), ("__", ""), ("#", "")
        ]
        for old, new in replacements:
            text = text.replace(old, new)
        return text.encode("latin-1", "replace").decode("latin-1")

    def header(self):
        # Top Modern Banner
        primary_color = self.track_colors.get(self.post_type, (15, 30, 80))
        self.set_fill_color(*primary_color)
        self.rect(0, 0, 210, 24, "F")

        # Accent Stripe
        self.set_fill_color(0, 180, 216)
        self.rect(0, 24, 210, 1.5, "F")

        # Header Title
        self.set_xy(15, 4)
        self.set_font("helvetica", "B", 13)
        self.set_text_color(255, 255, 255)
        label = self.type_labels.get(self.post_type, "KREGGSCODE ELITE")
        self.cell(120, 8, f"KREGGSCODE  |  {label}")

        # Subtitle / Day
        self.set_xy(15, 13)
        self.set_font("helvetica", "", 8)
        self.set_text_color(200, 225, 255)
        self.cell(120, 5, f"DAY {self.day}  *  OFFICIAL TECHNICAL REFERENCE  *  {self.full_date.upper()}")

        # Right-side Community Tag
        self.set_xy(135, 6)
        self.set_font("helvetica", "B", 9.5)
        self.set_text_color(255, 215, 0)  # Gold
        self.cell(60, 6, "TELEGRAM: @kreggscode", align="R")

        self.set_xy(135, 13)
        self.set_font("helvetica", "I", 7.5)
        self.set_text_color(220, 230, 255)
        self.cell(60, 5, "github.com/kreggscode", align="R")

        self.set_y(32)

    def footer(self):
        self.set_y(-14)
        self.set_draw_color(200, 210, 225)
        self.set_line_width(0.3)
        self.line(15, self.get_y(), 195, self.get_y())

        self.set_y(-12)
        self.set_font("helvetica", "I", 7.5)
        self.set_text_color(120, 130, 145)
        self.cell(90, 6, "KREGGSCODE Elite Architecture  |  Free Educational Reference", align="L")
        self.cell(90, 6, f"Page {self.page_no()}  |  Join: t.me/kreggscode", align="R")

    def draw_code_box(self, code_text: str, language: str = "python"):
        """Render code in a dark terminal-style container box."""
        lines = code_text.strip().split("\n")

        # Terminal header bar
        self.set_fill_color(30, 32, 44)
        self.rect(15, self.get_y(), 180, 7, "F")
        self.set_xy(18, self.get_y() + 1)
        self.set_font("courier", "B", 7.5)
        self.set_text_color(160, 170, 190)
        self.cell(174, 5, f"[terminal: {language}]", align="L")
        self.ln(6)

        # Code block body
        line_height = 4.6
        self.set_fill_color(22, 24, 34)
        self.set_font("courier", "", 8.5)
        self.set_text_color(166, 227, 161)  # Terminal Green/Cyan

        for line in lines:
            if self.get_y() + line_height > 275:
                self.add_page()
            safe_line = "  " + self.clean_text_for_pdf(line)
            if len(safe_line) > 85:
                safe_line = safe_line[:82] + "..."
            self.set_x(15)
            self.cell(180, line_height, safe_line, fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        self.ln(4)

    def add_section_header(self, title: str):
        self.ln(2)
        self.set_fill_color(235, 243, 250)
        self.rect(15, self.get_y(), 180, 7, "F")

        # Left accent pill
        primary_color = self.track_colors.get(self.post_type, (15, 76, 129))
        self.set_fill_color(*primary_color)
        self.rect(15, self.get_y(), 2.5, 7, "F")

        self.set_xy(19, self.get_y() + 1)
        self.set_font("helvetica", "B", 9.5)
        self.set_text_color(*primary_color)
        self.cell(170, 5, self.clean_text_for_pdf(title).upper(), align="L")
        self.ln(7)

    def render_cheat_sheet(self, title: str, content: str):
        self.add_page()

        # Document Main Title
        self.set_font("helvetica", "B", 15)
        self.set_text_color(20, 30, 55)
        self.multi_cell(180, 7.5, self.clean_text_for_pdf(title))
        self.ln(3)

        # Extract code block
        code_match = re.search(r"```([a-zA-Z0-9_\-+]*)\n?(.*?)```", content, re.DOTALL)
        code_lang = "python"
        code_content = ""
        pre_code_text = content
        post_code_text = ""

        if code_match:
            code_lang = code_match.group(1) or "python"
            code_content = code_match.group(2).strip()
            pre_code_text = content[:code_match.start()].strip()
            post_code_text = content[code_match.end():].strip()

        # 1. Render Pre-code Concept / Architecture
        if pre_code_text:
            self.add_section_header("1. Core Concept & Architectural Deep Dive")
            self.set_font("helvetica", "", 9.5)
            self.set_text_color(45, 55, 72)
            cleaned_pre = self.clean_text_for_pdf(pre_code_text)
            for p in cleaned_pre.split("\n\n"):
                p = p.strip()
                if p:
                    self.multi_cell(180, 5.2, p)
                    self.ln(2)

        # 2. Render Code Block
        if code_content:
            self.add_section_header("2. Production-Grade Implementation")
            self.draw_code_box(code_content, language=code_lang)

        # 3. Render Post-code Takeaways
        if post_code_text:
            self.add_section_header("3. Key Takeaways & Production Rules")
            self.set_font("helvetica", "", 9.5)
            self.set_text_color(45, 55, 72)
            cleaned_post = self.clean_text_for_pdf(post_code_text)
            for p in cleaned_post.split("\n"):
                p = p.strip()
                if p:
                    self.multi_cell(180, 5, p)
                    self.ln(1)


def generate_notes(post_type: str, day: int, content: str) -> str:
    """
    Generate an executive branded PDF cheat sheet.
    Returns the file path.
    """
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"KREGGSCODE_{post_type.upper()}_Day{day}_{date_str}.pdf"

    pdf = ModernNotesPDF(post_type, day)
    title = f"{pdf.type_labels.get(post_type, 'Technical Cheat Sheet')} - Day {day}"
    pdf.render_cheat_sheet(title, content)
    pdf.output(filename)
    print(f"LOG: Modern Executive Notes PDF saved: {filename}")
    return filename

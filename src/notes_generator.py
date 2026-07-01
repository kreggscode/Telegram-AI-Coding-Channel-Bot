"""
Notes Generator - Creates a branded PDF notes page for each daily post
Uses magazine_cover.jpg as the cover branding image so every PDF
is visually identifiable by its cover. Each PDF has a unique filename.
"""
import os
from datetime import datetime
from fpdf import FPDF

COVER_IMAGE = "magazine_cover.jpg"


class NotesPDF(FPDF):
    def __init__(self, post_type: str, day: int):
        super().__init__(format="A4", unit="mm")
        self.set_margins(20, 20, 20)
        self.set_auto_page_break(True, margin=25)
        self.post_type = post_type
        self.day = day
        self.full_date = datetime.now().strftime("%B %d, %Y")

        self.type_labels = {
            "python": "PYTHON MASTERY",
            "javascript": "JAVASCRIPT PRO",
            "ml": "ML ENGINEERING",
            "security": "CYBER SECURITY",
            "interview": "INTERVIEW PREP",
            "magazine": "DAILY MAGAZINE",
        }
        self.titles = {
            "python": "Python Mastery - Advanced Concepts",
            "javascript": "JavaScript Pro - Modern JS Patterns",
            "ml": "ML Engineering - AI & Machine Learning",
            "security": "Cyber Security - Bug Bounty & Pentesting",
            "interview": "Interview Prep - Technical Questions",
            "magazine": "Daily Technical Magazine",
        }

    def header(self):
        if self.page_no() > 1:
            self.set_fill_color(20, 40, 100)
            self.rect(0, 0, 210, 12, "F")
            self.set_x(0)
            self.set_y(2)
            self.set_font("helvetica", "B", 8)
            self.set_text_color(200, 220, 255)
            self.cell(105, 8, "KREGGSCODE ELITE NOTES", align="L")
            self.set_font("helvetica", "I", 7)
            self.cell(105, 8, self.full_date, align="R")
            self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 8)
        self.set_text_color(130)
        self.cell(0, 10, f"Page {self.page_no()} | KREGGSCODE ELITE | {self.full_date}", align="C")

    def clean_text(self, text):
        """Clean markdown for PDF display"""
        for old, new in [("**", ""), ("*", ""), ("#", ""), ("`", ""), ("__", ""), ("_", ""), (">", "")]:
            text = text.replace(old, new)
        while "\n\n\n" in text:
            text = text.replace("\n\n\n", "\n\n")
        return text.encode("latin-1", "ignore").decode("latin-1").strip()

    def add_cover(self):
        """Branded cover: title below the logo image, only date shown.
        All elements perfectly centered on the A4 page (210mm wide)."""
        self.add_page()

        # --- TOP BAND (full page width) ---
        self.set_fill_color(5, 15, 50)
        self.rect(0, 0, 210, 38, "F")
        self.set_xy(0, 8)
        self.set_font("helvetica", "B", 26)
        self.set_text_color(255, 255, 255)
        self.cell(210, 10, "KREGGSCODE", align="C")
        self.set_xy(0, 22)
        self.set_font("helvetica", "", 9)
        self.set_text_color(180, 200, 255)
        self.cell(210, 5, "ELITE TECHNICAL DAILY", align="C")

        # --- COVER IMAGE (centered: x = (210-100)/2 = 55) ---
        label = self.type_labels.get(self.post_type, self.post_type.upper())
        img_y = 42

        if os.path.exists(COVER_IMAGE):
            try:
                self.image(COVER_IMAGE, x=55, y=img_y, w=100)
                content_start = img_y + 108
            except Exception as e:
                print(f"WARNING: Cover image failed: {e}")
                content_start = img_y + 5
        else:
            content_start = img_y + 5

        # --- TITLE BELOW THE LOGO IMAGE ---
        self.set_x(0)
        self.set_y(content_start)
        self.set_draw_color(255, 215, 0)
        self.set_line_width(0.8)
        self.line(55, self.get_y(), 155, self.get_y())
        self.ln(7)

        self.set_x(0)
        self.set_font("helvetica", "B", 22)
        self.set_text_color(15, 35, 90)
        self.cell(210, 11, label, align="C")
        self.ln(14)

        # --- DATE ONLY ---
        self.set_x(0)
        self.set_font("helvetica", "I", 11)
        self.set_text_color(80)
        self.cell(210, 6, self.full_date, align="C")
        self.ln(14)

        # --- DIVIDER ---
        self.set_draw_color(0, 120, 255)
        self.set_line_width(0.4)
        self.line(65, self.get_y(), 145, self.get_y())
        self.ln(8)

        # --- SOCIAL FOOTER ---
        self.set_x(0)
        self.set_font("helvetica", "", 8)
        self.set_text_color(130)
        self.cell(210, 5, "Built for the KREGGSCODE Community", align="C")
        self.ln(4)
        self.set_x(0)
        self.cell(210, 5, "Telegram: @kreggscode  |  YouTube: /kreggscode", align="C")

    def add_content(self, title: str, content: str):
        """Add content page with proper formatting"""
        self.add_page()
        self.set_font("helvetica", "B", 18)
        self.set_text_color(20, 40, 100)
        self.multi_cell(0, 10, title)
        self.ln(3)
        self.set_draw_color(0, 120, 255)
        self.set_line_width(0.6)
        self.line(20, self.get_y(), 190, self.get_y())
        self.ln(8)

        cleaned = self.clean_text(content)
        self.set_font("helvetica", "", 11)
        self.set_text_color(30)
        for line in cleaned.split("\n"):
            if self.get_y() > 255:
                self.add_page()
            self.multi_cell(0, 6.5, line)
            self.ln(1)

        self.ln(6)
        self.set_draw_color(0, 120, 255)
        self.set_line_width(0.3)
        self.line(20, self.get_y(), 190, self.get_y())
        self.ln(4)
        self.set_font("helvetica", "I", 8)
        self.set_text_color(150)
        self.cell(0, 8, "--- KREGGSCODE ELITE : MASTERY THROUGH PRACTICE ---", align="C")


def generate_notes(post_type: str, day: int, content: str) -> str:
    """
    Generate a branded PDF notes file with magazine_cover.jpg on the cover.
    Returns the file path (unique per post_type/day/date).
    """
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"KREGGSCODE_{post_type}_Day{day}_{date_str}.pdf"

    pdf = NotesPDF(post_type, day)
    title = pdf.titles.get(post_type, "Technical Notes")
    pdf.add_cover()
    pdf.add_content(title, content)
    pdf.output(filename)
    print(f"LOG: Notes PDF saved: {filename}")
    return filename

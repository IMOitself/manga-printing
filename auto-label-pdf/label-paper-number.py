import glob
import sys
import io
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

try:
    pdfmetrics.registerFont(TTFont('CustomFont', 'font.ttf'))
    FONT_NAME = 'CustomFont' # Use the name you just registered
except:
    print("⚠️ Warning: Arial Bold font not found. Falling back to Helvetica-Bold.")
    FONT_NAME = 'Helvetica-Bold'

# --- CONFIGURATION ---
FONT_SIZE = 12
WHITE = Color(1, 1, 1)
BLACK = Color(0, 0, 0)

def label_pages():
    """Finds a single PDF and overlays styled, generated labels on each page."""
    pdf_files = glob.glob('*.pdf')
    if len(pdf_files) != 1:
        print(f"❌ Error: Expected 1 PDF, found {len(pdf_files)}. Place one PDF in the folder.")
        sys.exit()

    input_pdf_path = pdf_files[0]
    output_pdf_path = f"labeled_{input_pdf_path}"
    print(f"📄 Processing '{input_pdf_path}'...")

    try:
        reader = PdfReader(input_pdf_path)
        writer = PdfWriter()

        for i, page in enumerate(reader.pages):
            text = f"PAPER {(i // 2) + 1} - {'BACK' if i % 2 else 'FRONT'}"

            packet = io.BytesIO()
            width, height = page.mediabox.upper_right
            can = canvas.Canvas(packet, pagesize=(width, height))

            # --- DRAW CENTER LINE ---
            text_width = can.stringWidth(text, FONT_NAME, FONT_SIZE)
            line_x = float(width) / 2
            y_center = float(height) / 2
            gap_size = (text_width / 2) + 10

            can.setStrokeColor(BLACK)
            can.setLineWidth(0.5)
            can.line(line_x, 0, line_x, y_center - gap_size)
            can.line(line_x, y_center + gap_size, line_x, float(height))

            can.saveState()

            # 1. Calculate the center position for the text
            x_center = (float(width) / 2) + (FONT_SIZE / 4)
            y_center = (float(height) / 2)

            # 2. Move the canvas origin to this position and rotate
            can.translate(x_center, y_center)
            can.rotate(90)

            # 3. Set colors and draw the text centered on the NEW origin (0,0)
            can.setFillColor(BLACK)
            # can.setStrokeColor(WHITE)
            
            # The text object is needed for the fill-and-stroke effect
            text_object = can.beginText()
            text_object.setFont(FONT_NAME, FONT_SIZE)
            text_object.setTextRenderMode(2) # Mode 2: Fill and Stroke

            # Center the text horizontally by offsetting its start position
            text_width = can.stringWidth(text, FONT_NAME, FONT_SIZE)
            text_object.setTextOrigin(-text_width / 2, 0)
            
            text_object.textLine(text)
            can.drawText(text_object)

            can.restoreState()
            can.save()
            packet.seek(0)
            
            overlay = PdfReader(packet).pages[0]
            page.merge_page(overlay)
            writer.add_page(page)

        with open(output_pdf_path, "wb") as f:
            writer.write(f)

        print(f"✅ Success! Output saved as '{output_pdf_path}'.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    label_pages()
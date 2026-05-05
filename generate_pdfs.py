#!/usr/bin/env python3
"""
My Spanish Visa - Lead Magnet PDF Checklists Generator
Generates three professional branded PDFs using reportlab
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, Image, KeepTogether, Preformatted
)
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from datetime import datetime
import os

# ===== BRAND COLORS =====
NAVY = colors.HexColor("#0c1930")
RED = colors.HexColor("#be0011")
RED_DEEP = colors.HexColor("#8c000d")
YELLOW = colors.HexColor("#facf39")
CREAM = colors.HexColor("#f8f7f4")
WHITE = colors.HexColor("#ffffff")
BLACK = colors.HexColor("#1a1a1a")
MUTED_GREY = colors.HexColor("#5a6478")

# ===== PAGE DIMENSIONS =====
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 0.8 * cm
CONTENT_WIDTH = PAGE_WIDTH - (2 * MARGIN)

# ===== STYLES =====
def get_custom_styles():
    styles = getSampleStyleSheet()

    # Title style for cover
    styles.add(ParagraphStyle(
        name='CoverTitle',
        parent=styles['Normal'],
        fontSize=42,
        textColor=NAVY,
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
        leading=50
    ))

    # Subtitle style
    styles.add(ParagraphStyle(
        name='CoverSubtitle',
        parent=styles['Normal'],
        fontSize=18,
        textColor=RED,
        spaceAfter=24,
        alignment=TA_CENTER,
        fontName='Helvetica',
        leading=24
    ))

    # Section heading with red underline effect
    styles.add(ParagraphStyle(
        name='SectionHeading',
        parent=styles['Normal'],
        fontSize=16,
        textColor=NAVY,
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold',
        alignment=TA_LEFT
    ))

    # Subsection heading
    styles.add(ParagraphStyle(
        name='SubsectionHeading',
        parent=styles['Normal'],
        fontSize=13,
        textColor=NAVY,
        spaceAfter=8,
        spaceBefore=6,
        fontName='Helvetica-Bold',
        alignment=TA_LEFT
    ))

    # Checklist item
    styles.add(ParagraphStyle(
        name='ChecklistItem',
        parent=styles['Normal'],
        fontSize=10,
        textColor=BLACK,
        spaceAfter=6,
        fontName='Helvetica',
        leftIndent=18,
        leading=14
    ))

    # Notes/tips text
    styles.add(ParagraphStyle(
        name='NoteText',
        parent=styles['Normal'],
        fontSize=9,
        textColor=MUTED_GREY,
        spaceAfter=6,
        fontName='Helvetica',
        leading=12
    ))

    # Body text - use different name to avoid conflict
    styles.add(ParagraphStyle(
        name='CustomBodyText',
        parent=styles['Normal'],
        fontSize=10,
        textColor=BLACK,
        spaceAfter=8,
        fontName='Helvetica',
        alignment=TA_JUSTIFY,
        leading=14
    ))

    return styles


def create_header_section(story, styles):
    """Create navy header bar with branding"""
    # Create a table with navy background for header effect
    header_data = [['My Spanish Visa']]
    header_table = Table(header_data, colWidths=[CONTENT_WIDTH])
    header_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), NAVY),
        ('TEXTCOLOR', (0, 0), (-1, -1), WHITE),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 14),
        ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('LINEBELOW', (0, 0), (-1, -1), 3, RED),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 0.3 * cm))


def create_cover_page(story, styles, title, subtitle):
    """Create a professional cover page"""
    story.append(Spacer(1, 2 * cm))

    # Main title
    story.append(Paragraph(title, styles['CoverTitle']))
    story.append(Spacer(1, 0.3 * cm))

    # Subtitle
    story.append(Paragraph(subtitle, styles['CoverSubtitle']))
    story.append(Spacer(1, 1.5 * cm))

    # Branding text
    branding = f'<font color="#0c1930"><b>Download provided by</b></font><br/><font color="#be0011">My Spanish Visa</font><br/><font color="#5a6478">www.myspanishvisa.com</font>'
    story.append(Paragraph(branding, styles['CustomBodyText']))
    story.append(Spacer(1, 1 * cm))

    # Year indicator
    story.append(Paragraph(f'<font color="#5a6478">© 2026 My Spanish Visa</font>', styles['NoteText']))

    story.append(PageBreak())


def create_red_underline():
    """Create a red line for section headers"""
    return Table([['_' * 80]], colWidths=[CONTENT_WIDTH])


def create_checklist_section(story, styles, section_title, items, subsection_note=None):
    """Create a checklist section with checkbox items"""
    # Section heading with red underline
    story.append(Paragraph(section_title, styles['SectionHeading']))

    # Red line under section heading
    line_table = Table([['']],colWidths=[CONTENT_WIDTH * 0.3])
    line_table.setStyle(TableStyle([
        ('LINEBELOW', (0, 0), (-1, -1), 2, RED),
    ]))
    story.append(line_table)
    story.append(Spacer(1, 0.2 * cm))

    if subsection_note:
        story.append(Paragraph(subsection_note, styles['NoteText']))
        story.append(Spacer(1, 0.3 * cm))

    # Create checkbox table
    data = []
    for item in items:
        data.append(['☐', item])

    checklist_table = Table(data, colWidths=[0.5*cm, CONTENT_WIDTH - 0.7*cm])
    checklist_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (0, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (0, -1), 11),
        ('FONTSIZE', (1, 0), (1, -1), 10),
        ('TEXTCOLOR', (0, 0), (-1, -1), BLACK),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (1, 0), (1, -1), 8),
    ]))
    story.append(checklist_table)
    story.append(Spacer(1, 0.4 * cm))


def create_notes_section(story, styles, title, notes_list):
    """Create a notes/tips section"""
    story.append(Paragraph(title, styles['SectionHeading']))

    # Red line
    line_table = Table([['']],colWidths=[CONTENT_WIDTH * 0.15])
    line_table.setStyle(TableStyle([
        ('LINEBELOW', (0, 0), (-1, -1), 2, RED),
    ]))
    story.append(line_table)
    story.append(Spacer(1, 0.2 * cm))

    for note in notes_list:
        story.append(Paragraph(f'<b>•</b> {note}', styles['NoteText']))

    story.append(Spacer(1, 0.3 * cm))


def create_cta_section(story, styles, cta_text, cta_link):
    """Create call-to-action section"""
    story.append(Spacer(1, 0.5 * cm))

    cta_html = f'<font color="#be0011"><b>Need help?</b></font> <font color="#1a1a1a">{cta_text}</font>'
    story.append(Paragraph(cta_html, styles['CustomBodyText']))


def add_footer(canvas_obj, doc, page_num):
    """Add footer to each page"""
    canvas_obj.saveState()
    canvas_obj.setFont('Helvetica', 8)
    canvas_obj.setFillColor(MUTED_GREY)

    # Footer text
    footer_text = "www.myspanishvisa.com | © 2026 My Spanish Visa"
    canvas_obj.drawString(MARGIN, 0.5 * cm, footer_text)

    # Page number
    page_text = f"Page {page_num}"
    canvas_obj.drawRightString(PAGE_WIDTH - MARGIN, 0.5 * cm, page_text)

    canvas_obj.restoreState()


def generate_nlv_checklist():
    """Generate NLV Document Checklist PDF"""
    filename = '/sessions/optimistic-youthful-johnson/mnt/My Spanish Visa/nlv-document-checklist.pdf'

    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=MARGIN,
        leftMargin=MARGIN,
        topMargin=MARGIN,
        bottomMargin=1.2 * cm,
        onFirstPage=lambda c, d: add_footer(c, d, 1),
        onLaterPages=lambda c, d: add_footer(c, d, d.page)
    )

    story = []
    styles = get_custom_styles()

    # COVER PAGE
    create_header_section(story, styles)
    create_cover_page(story, styles,
        "Non-Lucrative Visa Document Checklist 2026",
        "Your complete checklist for applying for Spain's Non-Lucrative Visa"
    )

    # PAGE 2: Before You Start
    create_header_section(story, styles)
    create_checklist_section(story, styles, "Before You Start", [
        "Valid passport (minimum 1 year validity)",
        "Two recent passport photos (white background, 3x4cm)",
        "Completed visa application form (national visa form)",
        "Proof of accommodation in Spain (rental contract, property deed, or hotel booking)",
        "Private health insurance policy (full coverage, no copay, valid in Spain)",
        "Criminal record certificate (apostilled and translated)",
        "Medical certificate (issued within 3 months)",
        "Proof of financial means (bank statements showing €28,800+ for single applicant)",
        "Proof of address in home country",
    ])
    story.append(Spacer(1, 0.3 * cm))

    story.append(PageBreak())

    # PAGE 3: Financial Documents
    create_header_section(story, styles)
    create_checklist_section(story, styles, "Financial Documents - Detailed", [
        "Bank statements (last 6-12 months)",
        "Pension statements (if applicable)",
        "Investment portfolio statements",
        "Rental income proof",
        "Letter from bank confirming account balance",
    ], "All documents must be translated to Spanish and apostilled")

    story.append(Spacer(1, 0.3 * cm))

    story.append(Paragraph("<b><font color='#0c1930'>Key Financial Notes:</font></b>", styles['SubsectionHeading']))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph(
        "<b>IPREM Calculation:</b> Minimum €28,800/year for single applicant (12 × IPREM of €2,400)",
        styles['NoteText']
    ))
    story.append(Paragraph(
        "<b>Couples:</b> Add €7,200 per additional family member (0.25 × IPREM per person)",
        styles['NoteText']
    ))
    story.append(Paragraph(
        "<b>Currency:</b> Amounts may change annually with IPREM updates",
        styles['NoteText']
    ))

    story.append(PageBreak())

    # PAGE 4: After Approval
    create_header_section(story, styles)
    create_checklist_section(story, styles, "After Approval", [
        "Collect visa from consulate",
        "Enter Spain within 90 days of visa approval",
        "Apply for TIE card (Tarjeta de Identidad de Extranjero) within 30 days of arrival",
        "Register on padrón (empadronamiento) with local town hall",
        "Open Spanish bank account",
        "Get NIE number (Número de Identidad de Extranjero)",
        "Register with local health centre for access to public healthcare",
    ])

    create_cta_section(story, styles,
        "Visit <b>myspanishvisa.com/eligibility-check</b> for personalised guidance",
        "eligibility-check"
    )

    story.append(PageBreak())

    # PAGE 5: Tips & Reminders
    create_header_section(story, styles)
    create_notes_section(story, styles, "Important Reminders & Tips", [
        "Start the application 3-4 months before your planned move",
        "Keep all documents in both original and certified copies",
        "All non-English documents must be officially translated and apostilled",
        "Health insurance must offer full coverage with no copayment requirements",
        "Proof of funds must show consistent balance for 3-6 months prior",
        "The €28,800 requirement is yearly passive income, not a one-time amount",
        "Consider hiring a gestoria (tax/legal adviser) to support your application",
        "Register on the padrón before applying for the TIE card",
    ])

    story.append(Spacer(1, 0.5 * cm))
    story.append(Paragraph(
        "<font color='#be0011'><b>Questions about the Non-Lucrative Visa?</b></font><br/>Visit my Spanish Visa for detailed guides, FAQs, and expert support.",
        styles['CustomBodyText']
    ))

    # Build PDF
    doc.build(story)
    print(f"✓ Created: {filename}")


def generate_dnv_checklist():
    """Generate Digital Nomad Visa Document Checklist PDF"""
    filename = '/sessions/optimistic-youthful-johnson/mnt/My Spanish Visa/dnv-document-checklist.pdf'

    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=MARGIN,
        leftMargin=MARGIN,
        topMargin=MARGIN,
        bottomMargin=1.2 * cm,
        onFirstPage=lambda c, d: add_footer(c, d, 1),
        onLaterPages=lambda c, d: add_footer(c, d, d.page)
    )

    story = []
    styles = get_custom_styles()

    # COVER PAGE
    create_header_section(story, styles)
    create_cover_page(story, styles,
        "Digital Nomad Visa Document Checklist 2026",
        "Your complete checklist for Spain's Digital Nomad Visa application"
    )

    # PAGE 2: Employment Documents
    create_header_section(story, styles)
    create_checklist_section(story, styles, "Employment Documents", [
        "Valid passport (minimum 1 year validity)",
        "Employment contract or proof of freelance activity (minimum 1 year with current employer/clients)",
        "Proof employer is based outside Spain",
        "Letter from employer authorising remote work from Spain",
        "Proof of income (minimum €33,150/year gross — 200% of SMI)",
        "Last 3-6 months payslips or invoice records",
        "Company registration documents (for self-employed)",
        "Tax returns from home country (last year)",
    ])

    story.append(PageBreak())

    # PAGE 3: Personal Documents
    create_header_section(story, styles)
    create_checklist_section(story, styles, "Personal & Administrative Documents", [
        "Criminal record certificate (apostilled and translated)",
        "Medical certificate (issued within 3 months, health screening)",
        "Private health insurance (full coverage, no copay, valid in Spain)",
        "Proof of accommodation in Spain (rental contract or property deed)",
        "Two recent passport photos (white background, 3x4cm)",
        "Completed visa application form",
        "Proof you haven't been a Spanish resident in the last 5 years",
    ], "All foreign documents must be translated to Spanish and apostilled")

    story.append(Spacer(1, 0.3 * cm))
    story.append(Paragraph(
        "<b><font color='#0c1930'>Income Requirements:</font></b> The Digital Nomad Visa requires €33,150/year minimum income (200% of SMI). This must be verifiable through payslips, contracts, or tax returns.",
        styles['NoteText']
    ))

    story.append(PageBreak())

    # PAGE 4: After Approval & Beckham Law
    create_header_section(story, styles)
    create_checklist_section(story, styles, "After Approval", [
        "Enter Spain within 90 days of visa approval",
        "Apply for TIE card (within 30 days of arrival)",
        "Register on padrón (empadronamiento)",
        "Apply for Beckham Law within 6 months (if eligible for tax benefits)",
        "Register with Social Security as an employee or self-employed (autónomo)",
        "Open Spanish bank account",
        "Get digital certificate for tax/business purposes",
    ])

    story.append(Spacer(1, 0.3 * cm))
    story.append(Paragraph(
        "<b><font color='#be0011'>Beckham Law Bonus:</font></b> Foreign workers may qualify for special tax treatment (non-resident status) for 4 years. Apply within 6 months of arrival through a gestoría.",
        styles['NoteText']
    ))

    story.append(PageBreak())

    # PAGE 5: Tips & CTA
    create_header_section(story, styles)
    create_notes_section(story, styles, "Pro Tips for Digital Nomads", [
        "Ensure your employment contract explicitly permits remote work from Spain",
        "Non-EU citizens must apply from outside Spain; EU citizens can apply at immigration office",
        "Keep detailed records of hours worked and client communications as proof of activity",
        "The visa is valid for 2 years and renewable",
        "Consider joining Spain's freelancer union (colegio profesional) for additional benefits",
        "Start the Beckham Law application process 5 months after arrival",
        "Digital tools and SaaS subscriptions often count as legitimate business expenses",
        "Register as autónomo if you're self-employed to access Spanish social benefits",
    ])

    story.append(Spacer(1, 0.5 * cm))

    create_cta_section(story, styles,
        "Learn more at <b>myspanishvisa.com</b> for visa guides and application support",
        "dnv-guide"
    )

    # Build PDF
    doc.build(story)
    print(f"✓ Created: {filename}")


def generate_moving_checklist():
    """Generate Moving to Spain Checklist PDF"""
    filename = '/sessions/optimistic-youthful-johnson/mnt/My Spanish Visa/moving-to-spain-checklist.pdf'

    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=MARGIN,
        leftMargin=MARGIN,
        topMargin=MARGIN,
        bottomMargin=1.2 * cm,
        onFirstPage=lambda c, d: add_footer(c, d, 1),
        onLaterPages=lambda c, d: add_footer(c, d, d.page)
    )

    story = []
    styles = get_custom_styles()

    # COVER PAGE
    create_header_section(story, styles)
    create_cover_page(story, styles,
        "Moving to Spain Checklist 2026",
        "Your step-by-step guide to relocating to Spain"
    )

    # PAGE 2: 3-6 Months Before
    create_header_section(story, styles)
    create_checklist_section(story, styles, "3-6 Months Before Moving", [
        "Research visa options (NLV, Digital Nomad, Student, EU registration)",
        "Start visa application process with required documentation",
        "Arrange private health insurance valid in Spain",
        "Research areas and neighbourhoods to live in Spain",
        "Start learning basic Spanish or take an online course",
        "Notify employer/clients of relocation plans",
        "Research schools (if moving with children)",
        "Get criminal record check from your home country",
        "Arrange medical certificate from your GP or physician",
        "Consult with tax advisor about Spanish tax residency",
    ])

    story.append(PageBreak())

    # PAGE 3: 1-3 Months Before
    create_header_section(story, styles)
    create_checklist_section(story, styles, "1-3 Months Before Moving", [
        "Secure accommodation in Spain (rental or purchase)",
        "Arrange shipping or moving company for household goods",
        "Notify bank of international move and arrange transfers",
        "Set up international money transfer account (Wise, OFX, etc.)",
        "Cancel or redirect utilities, subscriptions, and services",
        "Arrange mail forwarding service",
        "Book flights to Spain",
        "Organise pet transport (if applicable, check import requirements)",
        "Get international driving permit (if needed for your home country)",
        "Translate and apostille key documents (birth certificate, diplomas, etc.)",
    ])

    story.append(PageBreak())

    # PAGE 4: First 30 Days in Spain
    create_header_section(story, styles)
    create_checklist_section(story, styles, "First 30 Days in Spain", [
        "Register on padrón (empadronamiento) at your local town hall",
        "Apply for TIE card (Tarjeta de Identidad de Extranjero) — deadline is critical",
        "Open Spanish bank account (required for most services)",
        "Get NIE number (Número de Identidad de Extranjero)",
        "Register with local health centre (centro de salud) for NHS access",
        "Set up utilities (electricity, water, internet, gas)",
        "Get Spanish SIM card or arrange mobile plan",
        "Register children at school (if applicable)",
        "Exchange driving licence (if you plan to drive)",
        "Arrange auto insurance if bringing a vehicle",
    ])

    story.append(PageBreak())

    # PAGE 5: First 3-6 Months & Ongoing
    create_header_section(story, styles)
    create_checklist_section(story, styles, "First 3-6 Months & Ongoing", [
        "File for Beckham Law (if eligible, within 6 months)",
        "Register as autónomo (self-employed) if needed",
        "Understand Spanish tax obligations and file first tax return",
        "Build emergency contacts list (doctor, dentist, police, embassy)",
        "Join local expat communities and networking groups",
        "Set calendar reminder for visa renewal (60 days before expiry)",
        "Arrange Spanish driving licence (if converting from abroad)",
        "Open investment or savings accounts for financial planning",
    ])

    story.append(Spacer(1, 0.4 * cm))
    create_notes_section(story, styles, "Moving Day Tips", [
        "Document your home contents with photos/video for insurance",
        "Keep important documents in a separate carry-on bag",
        "Request certified copies of all documents from your home country",
        "Check Spanish customs regulations before shipping items",
        "Schedule padrón registration immediately upon arrival",
        "The TIE card application has a strict 30-day deadline — don't miss it!",
        "Open a bank account within the first week of arrival",
    ])

    story.append(Spacer(1, 0.5 * cm))
    create_cta_section(story, styles,
        "Get expert support and detailed guides at <b>myspanishvisa.com</b>",
        "relocation-guide"
    )

    # Build PDF
    doc.build(story)
    print(f"✓ Created: {filename}")


def main():
    """Generate all three PDFs"""
    print("\n" + "="*60)
    print("My Spanish Visa - PDF Checklist Generator")
    print("="*60 + "\n")

    try:
        generate_nlv_checklist()
        generate_dnv_checklist()
        generate_moving_checklist()

        print("\n" + "="*60)
        print("✓ All PDFs generated successfully!")
        print("="*60 + "\n")

        # List generated files
        output_dir = '/sessions/optimistic-youthful-johnson/mnt/My Spanish Visa/'
        pdfs = [f for f in os.listdir(output_dir) if f.endswith('.pdf')]
        print(f"Generated PDFs in {output_dir}:")
        for pdf in sorted(pdfs):
            filepath = os.path.join(output_dir, pdf)
            filesize = os.path.getsize(filepath) / 1024  # KB
            print(f"  • {pdf} ({filesize:.1f} KB)")

    except Exception as e:
        print(f"\n✗ Error generating PDFs: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()

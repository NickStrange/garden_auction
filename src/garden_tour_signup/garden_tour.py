from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table
from src.garden_tour_signup.description import set_description
from src.garden_tour_signup.table import set_table
from src.garden_tour_signup.title import set_title


def front_page(pdf,team_name):
    width, height = A4
    tborder = 0.01 * height
    bborder = 0.01 * height
    height = (height - tborder - bborder) * 1
    heightlist = [
                  tborder,
                  0.10*height,   # title
                  0.15*height,   # description
                  0.75*height,   # table
                  bborder,       # footer
                  ]
    main_table = Table([
        [''],
        [set_title(width, heightlist[1], team_name)],
        [set_description(width, heightlist[2])],
        [set_table(width, heightlist[3])],
        [''],
    ], colWidths=width,
       rowHeights=heightlist)

    main_table.setStyle([
        # ('GRID', (0, 0), (-1, -1), 1, 'red'),
        ('LEFTPADDING', (0, 0), (0, -1), 0),
        # description
        # Table
        ('ALIGN', (0, 3), (0, 3), 'CENTRE'),
        ('VALIGN', (0, 3), (0, 3), 'MIDDLE'),
        # buy_now
        # footer
    ])

    main_table.wrapOn(pdf, 0, 0)
    main_table.drawOn(pdf, 0, 0)


if __name__ == '__main__':
    canvas = canvas.Canvas(f"../../data/garden_tour.pdf", pagesize=A4)
    for name in ['DOCENTS TEAM',
                 'HOMEOWNERS GIFTS TEAM',
                 'MARKETING TEAM',
                 'SPONSORSHIP TEAM',
                 'INSURANCE + PERMITS TEAM',
                 'HOMEOWNERS PARTY TEAM',
                 '']:
        front_page(canvas, name)
        canvas.showPage()
    canvas.save()

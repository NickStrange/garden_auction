
from reportlab.platypus import Table


def set_title(width: int, height: int, team_name):
    width_list = [0.17*width, 0.66*width, 0.17*width]
    tborder = 0.01*height
    bborder = 0.01*height
    height = height - tborder - bborder
    title_table = Table([
        ['', '', ''],
        ['', 'GARDEN TOUR MAY 30-31st 2026', ''],
        ['', team_name, ''],
    ], colWidths=width_list,
       rowHeights=[tborder, height, bborder])

    title_table.setStyle([
        # ('GRID', (0, 0), (-1, -1), 1, 'red'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        # Left flower
        ('ALIGN', (0, 0), (0, 0), 'RIGHT'),
        # title
        ('ALIGN', (1, 0), (1, -1), 'CENTRE'),
        ('VALIGN', (1, 0), (1, -1), 'MIDDLE'),
        ('TEXTCOLOR', (1, 1), (1, 2), 'green'),
        ('FONTSIZE', (1, 1), (1, 2), 30),
        ('FONTNAME', (1, 1), (1, 2), 'Helvetica-Bold'),
    ])

    return title_table

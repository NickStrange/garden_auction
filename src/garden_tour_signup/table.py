from reportlab.lib import colors
from reportlab.platypus import Table


def set_table(width: int, height: int):
    width_list = [width*0.075, width * 0.4, width*0.5]
    color = colors.toColor('rgba(0, 115, 153, 0.9)')
    matrix = [['', 'Name', 'email']]
    linecount = 16
    for i in range(1, linecount):
        matrix += ([['', '', '']])
    res = Table(matrix, colWidths = width_list, rowHeights = height/(linecount + 1))
    res.setStyle([
        # ('GRID', (0, 0), (-1, -1), 1, 'blue'),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, 'grey'),
        ('BACKGROUND', (0, 0), (-1, 0), color),
        ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (1, 0), (-1, -1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1),  [colors.white, colors.lightgrey]),
    ])

    return res


from reportlab.platypus import Table, Image


def set_title(width:int, height:int):
    widthList = [0.17*width, 0.66*width, 0.17*width]
    tborder = 0.01*height
    bborder = 0.01*height
    height = height - tborder - bborder
    titleTable = Table([
        ['', '', ''],
        ['', '2024 Cary Newcomers',''],
        ['', '', ''],
    ], colWidths=widthList,
       rowHeights=[tborder, height, bborder])

    titleTable.setStyle([
  #      ('GRID', (0, 0), (-1, -1), 1, 'red'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        # Left flower
        ('ALIGN', (0, 0), (0, 0), 'RIGHT'),
        #title
        ('ALIGN', (1,0), (1,-1), 'CENTRE'),
        ('VALIGN', (1,0), (1,-1), 'MIDDLE'),
        ('TEXTCOLOR', (1,1), (1, 1), 'green'),
         ('FONTSIZE', (1, 1), (1, 1), 30),
        ('FONTNAME', (1, 1), (1, 1), 'Helvetica-Bold'),
    ])

    return titleTable

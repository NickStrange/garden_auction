
from reportlab.platypus import Table, Image


def set_title(width:int, height:int):
    widthList = [0.17*width, 0.66*width, 0.17*width]
    image_pathl = '../data/garden_club_logo.jpeg'
    imgl = Image(image_pathl, 0.9*widthList[0], height=height, kind='proportional')
    image_pathr = '../data/garden_club_logo.jpeg'
    imgr = Image(image_pathr, 0.9*widthList[2], height=height, kind='proportional')

    titleTable = Table([
        [imgl, '2024 Cary Garden Club Auction','']
    ], colWidths=widthList,
       rowHeights=height)

    titleTable.setStyle([
  #      ('GRID', (0, 0), (-1, -1), 1, 'red'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        # Left flower
        ('ALIGN', (0, 0), (0, 0), 'RIGHT'),
        #title
        ('ALIGN', (1,0), (1,0), 'CENTRE'),
        ('VALIGN', (1,0), (1,0), 'MIDDLE'),
     #   ('FONTSIZE', (1,0), (1, 0), 24),
        ('TEXTCOLOR', (1,0), (1, 0), 'green'),
        ('BOTTOMPADDING', (1, 0), (1, 0), 25),
        ('FONTSIZE', (1, 0), (1, 0), 25),
        ('FONTNAME', (1, 0), (1, 0), 'Helvetica-Bold'),

        #right flower
        ('ALIGN', (2, 0), (2, 0), 'RIGHT'),
    ])

    return titleTable

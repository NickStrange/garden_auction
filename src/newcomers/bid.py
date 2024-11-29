from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Table, Image, Paragraph


def set_bid_info(width:int, height:int, minimum_bid: float, increment: float):
    heightList = [0.5*height,0.5*height]

    bidTable = Table([
        [f'MINIMUM BID ${minimum_bid}'],
        [f'MINIMUM BID INCREMENT: ${increment}'],
    ], colWidths=width,
       rowHeights=heightList)

    bidTable.setStyle([
   #     ('GRID', (0, 0), (-1, -1), 1, 'blue'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        # # minimum bid
        ('ALIGN', (0, 0), (0, 0), 'CENTRE'),
        ('VALIGN', (0, 0), (0, 0), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (0, 0), 10),
     #   ('BOTTOMPADDING', (0, 0), (0, 0), 5),
        ('FONTSIZE', (0, 0), (0, 0), 10),
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),
        # # # minimum bid
        ('ALIGN', (0,1), (0,1), 'CENTRE'),
        ('VALIGN', (0,1), (0,1), 'MIDDLE'),
        ('FONTSIZE', (0, 1), (0, 1), 10),
        ('FONTNAME', (0, 1), (0, 1), 'Helvetica-Bold'),
    ])

    return bidTable
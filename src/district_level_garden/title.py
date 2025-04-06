
from reportlab.platypus import Table, Image


def set_title(width: int, height: int):
    width_list = [0.17*width, 0.66*width, 0.17*width]
    image_pathl = '../../data/silent.jpg'
    image = Image(image_pathl, 0.9*width_list[0], height=height, kind='proportional')

    title_table = Table([
        [image, 'Silent Auction', image]
    ], colWidths=width_list,
       rowHeights=height)

    title_table.setStyle([
     #   ('GRID', (0, 0), (-1, -1), 1, 'red'),
        # Left flower
        ('ALIGN', (0, 0), (0, 0), 'RIGHT'),
        # title
        ('ALIGN', (1, 0), (1, 0), 'CENTRE'),
        ('VALIGN', (1, 0), (1, 0), 'MIDDLE'),
        ('TEXTCOLOR', (1, 0), (1, 0), 'green'),
        ('BOTTOMPADDING', (1, 0), (1, 0), 25),
        ('FONTSIZE', (1, 0), (1, 0), 25),
        ('FONTNAME', (1, 0), (1, 0), 'Helvetica-Bold'),

        # right flower
        ('ALIGN', (2, 0), (2, 0), 'RIGHT'),
    ])

    return title_table

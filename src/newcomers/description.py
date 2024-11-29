from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Table, Paragraph


def setdesc(width, height):
    colwidth = [0.05*width, 0.90*width, 0.0*width]
    para2_style = ParagraphStyle('para2d')
    para2_style.fontSize = 15
    para2_style.spaceAfter = 5
    para2_style.textColor = colors.HexColor('#003363')
    para2 = Paragraph(f' Donated by: ')
    desc_table = Table([
        ['', '', ''],
        ['', para2, '']
    ], colWidths=colwidth,
       rowHeights=[height*13/16, height*3/16])
    # description section
    desc_table.setStyle([
        # ('GRID', (0, 0), (-1, -1), 1, 'blue'),
        ('GRID', (1, 0), (1, 1), 1, 'black'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTRE'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold')])

    return desc_table


def set_description(width: int, height: int):
    height_list: list[float] = [height*0.05, height*0.75, height*0.15, height*0.05]
    description_table = Table([
        [''],
        [setdesc(width, height_list[1])],
        [f'RETAIL VALUE: '],
        [''],
    ], colWidths=width,
       rowHeights=height_list)


    description_table.setStyle([
        # ('GRID', (0, 0), (-1, -1), 1, 'green'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        # # top section
        ('ALIGN', (0, 0), (0, 0), 'CENTRE'),
        ('VALIGN', (0, 0), (0, 0), 'MIDDLE'),
        ('FONTSIZE', (0, 0), (0, 0), 20),
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),

        # retail price section
        ('ALIGN', (0, 2), (0, -1), 'CENTRE'),
        ('VALIGN', (0, 2), (0, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 2), (0, -1), 0),
        ('FONTSIZE', (0, 2), (0, -1), 20),
        ('FONTNAME', (0, 2), (0, -1), 'Helvetica-Bold'),
    ])

    return description_table

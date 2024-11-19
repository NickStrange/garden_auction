from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, Image, Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors


def orangeLabel(width, height, line1, line2, line3):
    tmargin=5
    lmargin=10
    widths=[lmargin, width-2*lmargin, lmargin]
    heights = [height*0.1, height*0.1, height*0.1]
    image_pathr = '../data/roser.jpg'
    img = Image(image_pathr, heights[1], height=height, kind='proportional')

    frontTable = Table(
        [['', line1, ''],
         ['', line2, ''],
         ['', line3, '']],
       colWidths=widths,
       rowHeights=heights)

    frontTable.setStyle([
        #    ('GRID', (0, 0), (-1, -1), 1, 'blue'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTRE'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTSIZE', (0, 0), (-1, 1), 30),
        ('FONTSIZE', (0, 1), (-1, -1), 20),
    ])
    return frontTable


def drinks_front_page(line1, line2, line3):
    width, height = A4
    linecount=1
    heights = [height*0.25, height*0.75]
    lwidth=width
    lheight=height

    mainTable = Table(
        [[orangeLabel(lwidth, heights[1], line1, line2, line3)],
         ['']]
    , colWidths=lwidth,
       rowHeights=heights)

    mainTable.setStyle([
     #   ('GRID', (0, 0), (-1, -1), 1, 'red'),
    ])
    mainTable.wrapOn(pdf,0,0)
    mainTable.drawOn(pdf, 0, 0)




if __name__ == '__main__':
    pdf = canvas.Canvas("../data/drinks.pdf", pagesize=A4)

    drinks_front_page(line1="Drink A L'Orange",
                      line2="Prosecco and Orange",
                      line3='Garnish Tangerine, Strawberry and Grape')
    pdf.showPage()
   # pdf.save()

    drinks_front_page(line1="OOH La La Passionate Parisienne",
                      line2="Prosecco with Passion Fruit Juice",
                      line3='Garnish Peach, Golden Berries and Basil')
    pdf.showPage()

    drinks_front_page(line1="Le Berry Beret",
                      line2="Prosecco and Berry Blend",
                      line3='Garnish Berries and Mint')
    pdf.showPage()
    pdf.save()

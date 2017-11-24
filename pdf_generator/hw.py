from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, mm
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import *
from reportlab.lib import colors

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('hei', 'hei.ttf'))
from reportlab.lib import fonts
fonts.addMapping('hei', 0, 0, 'hei')
fonts.addMapping('hei', 0, 1, 'hei')
import copy



def hello():
    c = canvas.Canvas("../hellozhizying.pdf")
    c.drawString(10, 800, "hellozhiying")
    c.drawString(10, 700, "hellopython")
    c.drawString(10, 600, "你好")
    c.drawString(10, 500, "nihao")
    c.showPage()
    c.save()
# hello()


def pdf_generator(pdf_url, pdf_data):

    pdf_data = {
        'order_id': '2017111618133515',
        'create_time': '',
        'expire_time': '',
        'user': 'fetest',
        'tel_num': '17712345678',
        'order_detail': [
            {'app': '电影数据',
             'main_dime': '每日，星期，省份',
             'child_dime': '上午场，下午场'},
            {'app': '大盘数据',
             'main_dime': '大区',
             'child_dime': '黄金场，午夜场'},
            {'app': '城市数据',
             'main_dime': '城市',
             'child_dime': '3D'}
        ],
        'subtotal': '20000',
        'years': '2',
        'totalprice': '40000',
        'discounts': '3000',
        'payment': '37000'
    }

    c = canvas.Canvas(pdf_url)


def pdf_test01():
    c = canvas.Canvas('form.pdf', pagesize=A4)
    c.setLineWidth(.3)
    c.setFont('hei', 8)

    c.drawString(50,765,'北京源石智影科技有限公司')
    c.drawString(450,765,'合同编号:')

    c.line(50,761,570,761)
    c.setFont('hei', 16)
    c.drawString(200, 665, '电影office Pro 产品订购单')

    c.save()


def pdf_table():
    # 创建元素列表
    elements = []
    styles = getSampleStyleSheet()
    normalstyle = copy.deepcopy(styles['Normal'])
    normalstyle.fontName = 'hei'
    normalstyle.fontSize = 12
    doc = SimpleDocTemplate('pdf_table.pdf')
    # elements.append(Paragraph("订单信息", normalstyle))
    data = [
        ['order_id', '2017111618133515'],
        ['创建时间', '2017-11-17'],
        ['expire_time', '2017-11-18'],
        ['user_id', 'fetest', 'tel_num', '17712345678']
    ]
    ts = [
        ('ALIGN', (1, 1), (-1, -1), 'CENTER'),
    ]
    table = Table(data, style=ts)
    elements.append(table)
    doc.build(elements)

if __name__ == "__main__":
    pdf_test01()
    # pdf_table()

    pdf_data = {
        'order_id': '2017111618133515',
        'create_time': '2017-11-17 18:30',
        'expire_time': '2017-11-18 18:30',
        'user': 'fetest',
        'tel_num': '17712345678',
        'order_detail': [
            {'app': '电影数据',
             'main_dime': '每日，星期，省份, 影院, 院线, 城市, 演员, 导演',
             'child_dime': '上午场，下午场'},
            {'app': '大盘数据',
             'main_dime': '大区',
             'child_dime': '黄金场，午夜场'},
            {'app': '城市数据',
             'main_dime': '城市',
             'child_dime': '3D'}
        ],
        'subtotal': '20000',
        'years': '2',
        'totalprice': '40000',
        'discounts': '3000',
        'payment': '37000'
    }

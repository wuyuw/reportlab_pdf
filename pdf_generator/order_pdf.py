from reportlab.pdfgen import canvas
from reportlab.lib.units import mm, inch
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('hei', 'hei.ttf'))
from reportlab.lib import fonts
fonts.addMapping('hei', 0, 0, 'hei')

# 左边距
LEFT = 60
# 行高
LINE_HEIGHT = 24
# 起始高度
START_HIGH = 810


def pdf_test01():
    c = canvas.Canvas('form.pdf', pagesize=A4)
    c.setLineWidth(.3)
    c.setFont('hei', 11)
    # 页眉文字
    c_high = START_HIGH
    c.drawImage('logo.jpg', LEFT, c_high, width=40, height=11)
    c.drawString(LEFT+42, c_high+1, '北京源石智影科技有限公司')
    c.drawString(LEFT+300, c_high+1, '合同编号: 2017112409392300014578')
    # 页眉下划线
    c_high -= 3.5
    c.line(LEFT, c_high, LEFT+500, c_high)
    # 标题
    c_high -= 50
    c.setFont('hei', 16)
    c.drawString(LEFT+150, c_high, '电影office Pro 产品订购单')
    c_high -= 10
    # 基本信息
    c.setFont('hei', 12)
    text_list = ['订单号：2017112409392300014578',
                 '创建时间： 2017-11-24 09：54',
                 '过期时间： 2017-11-25 09：54',
                 '用户： 测试企业',
                 '手机号： 18912345678'
                 ]
    for text in text_list:
        c_high -= 20
        c.drawString(LEFT, c_high, text)
    # 明细标题
    c.setFont('hei', 14)
    c_high -= 30
    c.drawString(LEFT+200, c_high, "订购明细清单")
    # 基本会员费
    c.setFont('hei', 12)
    c_high -= 30
    c.line(LEFT, c_high, LEFT+500, c_high)
    c.line(LEFT, c_high, LEFT, c_high-LINE_HEIGHT)
    c.line(LEFT+500, c_high, LEFT+500, c_high-LINE_HEIGHT)
    c.line(LEFT, c_high-LINE_HEIGHT, LEFT+500, c_high-LINE_HEIGHT)
    c.drawString(LEFT+20, c_high-16, "基本会员费")
    c.drawString(LEFT+400, c_high-16, "28000.00/年")
    c_high -= LINE_HEIGHT
    # 订单明细
    for i in range(6):
        if c_high < 100:
            c.showPage()
            c.setFont('hei', 11)
            # 页眉文字
            c_high = START_HIGH
            c.drawImage('logo.jpg', LEFT, c_high, width=40, height=11)
            c.drawString(LEFT + 42, c_high + 1, '北京源石智影科技有限公司')
            c.drawString(LEFT + 300, c_high + 1, '合同编号: 2017112409392300014578')
            # 页眉下划线
            c_high -= 3.5
            c.line(LEFT, c_high, LEFT + 500, c_high)
            # 页脚
            c.drawImage('office_pro_white.jpg', 230, 20, width=115, height=26)
            c_high = 700
            c.line(LEFT, c_high, LEFT+500, c_high)

        app = "电影数据"
        main_dimension = "每天，星期，省份，城市，演员，导演，电影，影院，院线，复盘，大盘，区县，价格，网票，时段，编剧，每天，星期，省份，城市，演员"
        child_dimension = "上午场，上午场2D,上午场3"
        c_high = draw_app(c, LEFT, LINE_HEIGHT, c_high, main_dimension, child_dimension, app)

    # 合计
    c.drawString(LEFT+300, c_high-16, "合计")
    c.drawString(LEFT+400, c_high-16, "15000000"+".00/年")
    c_high -= LINE_HEIGHT
    c.line(LEFT, c_high+LINE_HEIGHT, LEFT, c_high)
    c.line(LEFT+340, c_high+LINE_HEIGHT, LEFT+340, c_high)
    c.line(LEFT+500, c_high+LINE_HEIGHT, LEFT+500, c_high)
    c.line(LEFT, c_high, LEFT+500, c_high)
    # 声明
    c.setFont('hei', 10)
    c.drawString(LEFT, c_high-10, "*本订购单是《智影科技智慧云数据产品使用合同》的合法附件*")
    # 签名
    c_high -= 2*LINE_HEIGHT
    c.setFont('hei', 12)
    c.drawString(LEFT, c_high, "甲 方 (签章）：")
    c.drawString(LEFT+250, c_high, "乙 方 (签章）：")
    c_high -= LINE_HEIGHT
    c.drawString(LEFT, c_high, "代表人签字：")
    c.drawString(LEFT+250, c_high, "代表人签字：")
    c_high -= 2*LINE_HEIGHT
    c.drawString(LEFT+350, c_high, "签约日期：2017年   月   日")
    # 页脚
    c.drawImage('office_pro_white.jpg', 230, 20, width=115, height=26)

    c.showPage()
    c.save()


def draw_app(c, LEFT, LINE_HEIGHT, c_high, main_dimension, child_dimension, app):
    c.drawString(LEFT+20, c_high-16, "所选购APP")
    c.drawString(LEFT+150, c_high-16, app)
    c_high -= LINE_HEIGHT
    c.line(LEFT, c_high+LINE_HEIGHT, LEFT, c_high)
    c.line(LEFT+140, c_high+LINE_HEIGHT, LEFT+140, c_high)
    c.line(LEFT+500, c_high+LINE_HEIGHT, LEFT+500, c_high)
    c.line(LEFT, c_high, LEFT+500, c_high)

    main_title = "数据大类"
    child_title = "数据报表"
    c_high = draw_dimen(c, LEFT, LINE_HEIGHT, c_high, title=main_title, text=main_dimension)
    c_high = draw_dimen(c, LEFT, LINE_HEIGHT, c_high, title=child_title, text=child_dimension)
    return c_high


def draw_dimen(c, LEFT, LINE_HEIGHT, c_high, title, text):
    c.drawString(LEFT+20, c_high-16, title)
    l_high = c_high
    c_high = draw_multi_row(c, LEFT, LINE_HEIGHT, c_high, text=text)
    c.line(LEFT, l_high, LEFT, c_high)
    c.line(LEFT+140, l_high, LEFT+140, c_high)
    c.line(LEFT+500, l_high, LEFT+500, c_high)
    c.line(LEFT, c_high, LEFT+500, c_high)
    return c_high


def draw_multi_row(c, LEFT, LINE_HEIGHT, c_high, text):
    if len(text) <= 26:
        c.drawString(LEFT+150, c_high-16, text)
        c_high -= LINE_HEIGHT
        return c_high
    else:
        c.drawString(LEFT+150, c_high-16, text[:27])
        c_high -= LINE_HEIGHT
        text = text[27:]
        return draw_multi_row(c, LEFT, LINE_HEIGHT, c_high, text)

if __name__ == '__main__':
    pdf_test01()

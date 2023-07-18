from pyecharts.charts import Bar, Pie, WordCloud, EffectScatter, Page
from pyecharts import options as opts
from pyecharts.globals import ThemeType
# 评论数最多的前十名电影
def evalNumPeoTop10(x_data, y_data) -> Bar():
    # 画条形图
    bar = Bar(
        init_opts=opts.InitOpts(theme=ThemeType.WHITE, width="450px", height="350px", chart_id='bar_cmt1'))  # 初始化条形图
    bar.add_xaxis(x_data)  # 增加x轴数据
    bar.add_yaxis("评论数量", y_data)  # 增加y轴数据
    bar.reversal_axis()  # 设置水平方向
    bar.set_series_opts(label_opts=opts.LabelOpts(position="right"))  # Label出现位置
    bar.set_global_opts(
        legend_opts=opts.LegendOpts(pos_left='right'),
        title_opts=opts.TitleOpts(title="评论数TOP10-条形图", pos_left='center'),  # 标题
        toolbox_opts=opts.ToolboxOpts(is_show=False, ),  # 不显示工具箱
        xaxis_opts=opts.AxisOpts(name="评论",  # x轴名称
                                 axislabel_opts=opts.LabelOpts(font_size=8, rotate=0),
                                 splitline_opts=opts.SplitLineOpts(is_show=False)
                                 ),
        yaxis_opts=opts.AxisOpts(name="电影",  # y轴名称
                                 axislabel_opts=opts.LabelOpts(font_size=7, rotate=45),  # y轴名称
                                 )
    )
    bar.render("评论数TOP10_条形图.html")  # 生成html文件
    print('生成完毕:评论数TOP10_条形图.html')
    return bar
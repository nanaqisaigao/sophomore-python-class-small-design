from pyecharts.charts import Bar, Pie, WordCloud, EffectScatter, Page
from pyecharts import options as opts
from pyecharts.globals import ThemeType
import pandas as pd
def eval_num(cmt_count_list) -> Bar():  # v_cmt_list是评价分数列表
    # 设置分段
    bins = [0, 100000, 200000, 300000, 500000, 1000000, 3000000]  # 设置评价数量区间
    # 设置标签
    labels = ['0-10w', '10w-20w', '20w-30w', '30w-50w', '50w-100w', '100w-300w']  # 这里labels和Categories 一样
    # 从mysql中获取评价数量
    # 按分段离散化数据
    segments = pd.cut(cmt_count_list, bins, labels=labels)  # 按分段切割数据
    counts = pd.value_counts(segments, sort=False).values.tolist()  # 统计个数
    bar = Bar(
        init_opts=opts.InitOpts(theme=ThemeType.WHITE, width="550px", height="350px", chart_id='bar_cmt2'))  # 初始化条形图
    bar.add_xaxis(labels, )  # 增加x轴数据
    bar.add_yaxis("评价数", counts)  # 增加y轴数据
    bar.set_global_opts(
        legend_opts=opts.LegendOpts(pos_left='right'),
        title_opts=opts.TitleOpts(title="评价数量区间分布-柱形图", pos_left='center'),  # 标题
        toolbox_opts=opts.ToolboxOpts(is_show=False, ),  # 不显示工具箱
        xaxis_opts=opts.AxisOpts(name="评论数",  # x轴名称
                                 axislabel_opts=opts.LabelOpts(font_size=8)),  # 字体大小
        yaxis_opts=opts.AxisOpts(name="电影数量",
                                 axislabel_opts={"rotate": 0},
                                 splitline_opts=opts.SplitLineOpts(is_show=True,
                                                                   linestyle_opts=opts.LineStyleOpts(type_='solid')),
                                 ),  # y轴名称
    )
    # 标记最大值
    bar.set_series_opts(
        markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max", name="最大值"), ],
                                          symbol_size=35)  # 标记符号大小
    )
    bar.render("评价数分布-柱形图.html")  # 生成html文件
    print('生成完毕:评价数分布-柱形图.html')
    return bar
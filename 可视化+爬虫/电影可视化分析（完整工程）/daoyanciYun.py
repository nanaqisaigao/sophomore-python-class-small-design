from collections import Counter
from pyecharts.charts import Bar, Pie, WordCloud, EffectScatter, Page
from pyecharts import options as opts
from pyecharts.globals import ThemeType
def daoyanciYun(data) -> WordCloud():
    words_counter = Counter(data)
    # print('words_counter',words_counter)
    # 将Counter类型转换为列表
    words_list = words_counter.most_common(10)  # 导演次数最多的10人
    print('wordlist', words_list)
    wc = WordCloud(init_opts=opts.InitOpts(width="450px", height="350px", theme=ThemeType.WHITE, chart_id='wc1'))
    wc.add(series_name="导演名称",
           data_pair=words_list,
           word_size_range=[12, 18],
           width='500px',  # 宽度
           height='400px',  # 高度
           word_gap=3  # 单词间隔
           )  # 增加数据
    wc.set_global_opts(
        title_opts=opts.TitleOpts(pos_left='center',
                                  title="导演姓名分析-词云图",
                                  title_textstyle_opts=opts.TextStyleOpts(font_size=20)  # 设置标题
                                  ),
        tooltip_opts=opts.TooltipOpts(is_show=True),  # 不显示工具箱
    )
    wc.set_series_opts(label_opts=opts.LabelOpts(is_show=True))
    wc.render('导演姓名_词云图.html')  # 生成html文件
    print('生成完毕:导演姓名_词云图.html')
    return wc
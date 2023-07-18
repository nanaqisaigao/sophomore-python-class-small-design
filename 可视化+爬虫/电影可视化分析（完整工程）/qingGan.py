from pyecharts.charts import Bar, Pie, WordCloud, EffectScatter, Page
import pandas as pd
from snownlp import SnowNLP
from pyecharts import options as opts
from pyecharts.globals import ThemeType
def qinggan(v_cmt_list) -> Pie():
    df = pd.DataFrame()  # 初始化一个DataFrame对象
    score_list = []  # 情感评分值
    tag_list = []  # 打标分类结果
    pos_count = 0  # 计数器-积极
    mid_count = 0  # 计数器-中性
    neg_count = 0  # 计数器-消极
    for comment in v_cmt_list:
        tag = ''
        sentiments_score = SnowNLP(comment).sentiments
        if sentiments_score < 0.4:  # 情感分小于0.4判定为消极
            tag = '消极'
            neg_count += 1
        elif 0.4 <= sentiments_score <= 0.6:  # 情感分在[0.4,0.6]直接判定为中性
            tag = '中性'
            mid_count += 1
        else:  # 情感分大于0.6判定为积极
            tag = '积极'
            pos_count += 1
        score_list.append(sentiments_score)  # 得分值
        tag_list.append(tag)  # 判定结果
    df['情感得分'] = score_list
    df['分析结果'] = tag_list
    df.to_excel('情感判定结果.xlsx', index=None)  # 把情感分析结果保存到excel文件
    # 画饼图
    pie = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.WHITE, width="450px", height="350px", chart_id='pie1'))
            .add(series_name="评价情感分布",  # 系列名称
                 data_pair=[['积极', pos_count],  # 添加数据
                            ['中性', mid_count],
                            ['消极', neg_count]],
                 rosetype="radius",  # 是否展示成南丁格尔图
                 radius=["30%", "55%"],  # 扇区圆心角展现数据的百分比，半径展现数据的大小
                 )  # 加入数据
            .set_global_opts(  # 全局设置项
            title_opts=opts.TitleOpts(title="短评情感分布-饼图", pos_left='center'),  # 标题
            legend_opts=opts.LegendOpts(pos_left='right', orient='vertical')  # 图例设置项,靠右,竖向排列
        )
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}")))  # 样式设置项
    pie.render('情感分布_饼图.html')  # 生成html文件
    print('生成完毕:情感分布_饼图.html')
    return pie

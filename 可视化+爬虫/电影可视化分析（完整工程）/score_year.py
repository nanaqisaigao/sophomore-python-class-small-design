from pyecharts.charts import Bar, Pie, WordCloud, EffectScatter, Page
from pyecharts import options as opts
from pyecharts.globals import ThemeType
# 评分-年份关系图
def score_year(x_data, y_data) -> EffectScatter():
    sc = (
        EffectScatter(
            init_opts=opts.InitOpts(width="450px", height="350px", theme=ThemeType.WHITE, chart_id='scatter1'))
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(
            series_name="评分",
            y_axis=y_data,
            symbol_size=10,
            label_opts=opts.LabelOpts(is_show=False),
        )
            .set_series_opts()
            .set_global_opts(
            # 忽略部分代码
        )
    )
    sc.render('评分年份分布-散点图.html')
    print('生成完毕:散点图.html')
    return sc
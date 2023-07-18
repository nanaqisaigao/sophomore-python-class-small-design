from pyecharts.charts import Liquid
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Line
from pyecharts.charts import Page


def backgroud() -> Line:
    line1 = (
        Line(init_opts=opts.InitOpts(
            width="1200px",  # 宽度
            height="700px",  # 高度
            bg_color={
                "type": "pattern",
                "image": JsCode(
                    "img"),  # 实例化一个 Image 的对象赋值给 img 变量，然后给它的 src 属性赋值为图片的 URL 链接
                "repeat": "repeat",
            }))  # 设置背景图片
        .add_xaxis([None])  # 插入空数据
        .add_yaxis("", [None])  # 插入空数据
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="智慧城市数据可视化分析监控大屏",
                pos_left='center',
                pos_top='10%',
                title_textstyle_opts=opts.TextStyleOpts(font_size=45,
                                                        font_family='cursive',
                                                        color='white',
                                                        align='left'),
            ),
            yaxis_opts=opts.AxisOpts(is_show=False),  # 不显示y轴
            xaxis_opts=opts.AxisOpts(is_show=False))  # 不显示x轴
    )

    # 设置背景图片 添加一个自定义的 javascript 函数
    line1.add_js_funcs(
        """        
          var img = new Image(); img.src ='./pic/wuhan.webp';
        """
    )
    line1.render("背景.html")
    print("背景")
    return line1


def jiaotong() -> Bar:
    x_data = [str(i) + 'w\月' for i in range(1, 13)]
    y1_data = [193, 242, 206, 198, 335, 298, 38, 93, 88, 285, 297, 302]
    y2_data = [96, 41, 28, 95, 36, 94, 29, 61, 42, 85, 99, 31]
    bar1 = (
        Bar(init_opts=opts.InitOpts(
            theme=ThemeType.LIGHT,
            width="750px",
            height="350px",
            chart_id='bar_county'))
        .add_xaxis(x_data).add_yaxis("高峰期", y1_data, gap="0%")
        .add_yaxis("非高峰期", y2_data, gap="0%").set_global_opts(
            title_opts=opts.TitleOpts(
                title="近年城建重点项目统计",
                pos_left='center',
                title_textstyle_opts=opts.TextStyleOpts(color="#fff"),
            ),
            legend_opts=opts.LegendOpts(pos_right='10%',
                                        orient='vertical'),
            tooltip_opts=opts.TooltipOpts(trigger="axis",
                                          axis_pointer_type="cross",
                                          is_show=True),  # 提示框配置
            xaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(color="#fff"), ),
            yaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(color="#fff"), ),
        ))
    print("交通统计")
    bar1.render("交通统计.html")
    return bar1


def tushuguan() -> Liquid:
    data_list = [[23, 0.6328]]
    l1 = Liquid(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, width="250px", height="250px", chart_id="v_chart_id"))
    l1.add("完成率", [data_list[0][1]], center=["30%", "50%"],
           label_opts=opts.LabelOpts(font_size=20, position='inside'))
    l1.set_global_opts(title_opts=opts.TitleOpts(title="图书馆建设率",
                                                 pos_left='15%',
                                                 pos_top='15%',
                                                 title_textstyle_opts=opts.TextStyleOpts(color="#fff"),
                                                 ))
    l1.render("图书馆.html")
    return l1


def airQuality() -> Line:
    x_data = [str(i) + '月' for i in range(1, 13)]
    y_data = [36.8, 35.2, 36.0, 31.9, 29.5, 14.9, 33.5, 20.8, 37.1, 42.6, 44.9, 53.3]
    area_color_js = (  # 设置美观背景色
        "new echarts.graphic.LinearGradient(0, 0, 0, 1, "
        "[{offset: 0, color: '#eb64fb'}, {offset: 1, color: '#3fbbff0d'}], false)")

    line2 = (
        Line(init_opts=opts.InitOpts(
            theme=ThemeType.LIGHT,
            width="450px",
            height="300px",
            chart_id='line_aqi')).add_xaxis(xaxis_data=x_data).add_yaxis(
            series_name="增长率",
            y_axis=y_data,
            is_smooth=True,  # 是否平滑
            is_symbol_show=True,
            symbol="circle",
            symbol_size=6,
            linestyle_opts=opts.LineStyleOpts(color="#fff"),
            label_opts=opts.LabelOpts(is_show=True,
                                      position="top",
                                      color="white"),
            itemstyle_opts=opts.ItemStyleOpts(color="red",
                                              border_color="#fff",
                                              border_width=3),
            tooltip_opts=opts.TooltipOpts(is_show=False),
            areastyle_opts=opts.AreaStyleOpts(color=JsCode(area_color_js),
                                              opacity=1),
        )
    )
    line2.render("城市空气质量.html")
    print("空气质量")
    return line2


def rencai() -> Bar:
    x_data = ['博士人才', '硕士人才', '本科人才', '专科人才', '专科以下']
    y_data = [0.4, 5.8, 26.4, 29.8, 37.6]
    # 画柱形图
    bar2 = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT,
                                       width="450px",
                                       height="350px",
                                       chart_id='bar_talent'))  # 初始化条形图
    bar2.add_xaxis(x_data)  # 增加x轴数据
    bar2.add_yaxis("占比", y_data)  # 增加y轴数据
    bar2.set_series_opts(label_opts=opts.LabelOpts(position="right"))  # Label出现位置
    bar2.render("城市人才占比.html")
    print("人才")
    return bar2


def replace():
    Page.save_resize_html(
        source="大屏_临时.html",  # 源html文件
        cfg_file="chart_config.json",  # 配置文件
        dest="最终大屏.html"  # 目标html文件
    )


from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


# 定义路由及视图函数
@app.route('/')  # 装饰器
def f_index():
    return render_template('最终大屏.html')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    page = Page(
        page_title="智慧城市数据可视化分析监控大屏",  # 页面标题
        layout=Page.DraggablePageLayout,  # 采用拖拽方式
    )
    page.add(backgroud(),  # 背景
             jiaotong(),  # 交通
             tushuguan(),  # 图书馆
             airQuality(),  # 空气质量
             rencai()  # 人才占比
             )
    # 执行完毕后,打开临时html并拖拽,拖拽完点击Save Config，把chart_config.json放到本目录下
    page.render('大屏_临时.html')
    print('生成完毕:大屏_临时.html')
    replace()
    app.run(host='0.0.0.0', port=7888, debug=True),

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import pymysql
import pandas as pd
from itertools import chain
from pyecharts.charts import Bar, Pie, WordCloud, EffectScatter, Page
import operator
import qingGan
import daoyanciYun
import eval_num
import evalNumPeoTop10
import score_year
import scoretop10
import bigTitle
def database_connect_figure():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='Wust#cs2023', database='bigscreen')
    cur = conn.cursor()  # 获取游标
    data1 = cur.execute("SELECT 评分人数 FROM t_film")  # 执行SQL查询，获取所有的评分人数
    # 评价分数柱状图
    evalNumlist = list(chain.from_iterable(cur.fetchall()))  # 获取单条数据
    # eval_num(evalNumlist)

    # 简评情感分析
    data2 = cur.execute("SELECT 简评 FROM t_film")  # 执行SQL查询，
    comments = list(chain.from_iterable(cur.fetchall()))  # 获取单条数据
    # qinggan(comments)

    # 导演词云 词云图 table的输入需要双列表
    data3 = cur.execute("SELECT 导演 FROM t_film")  # 执行SQL查询，
    daoyans = list(chain.from_iterable(cur.fetchall()))
    # 是否要考虑将一电影中多个导演分开
    # daoyanciYun(daoyans)

    # 评分前十 所有信息 table必须是二位数组
    data4 = cur.execute(
        "SELECT 电影名称,电影评分,评分人数,上映年份,简评 FROM t_film ORDER BY 电影评分 DESC Limit 10")  # 执行SQL查询，评分数最高前10条完整数据
    # (cur.fetchall()是双元组，chain.from_iterable(cur.fetchall() 作用是将双元组中内元组的括号去掉，元组之间改成;list(cur.fetchall())列表，列表中每个元素是元组
    # 转换成外列表，内元组的形式
    list1 = list(cur.fetchall())
    # print(list1)
    # 转换成双列表
    score10 = [list(it) for it in list1]
    # scoretop10(score10)

    # 评论人数数前10
    data5 = cur.execute("SELECT 电影名称,评分人数 FROM t_film ORDER BY 评分人数 DESC Limit 10")  # 执行SQL查询，前10条评论数最高
    df = pd.DataFrame(list(cur.fetchall()))
    x_data = df[0].tolist()
    y_data = df[1].tolist()
    # evalNumPeoTop10(x_data,y_data)

    # 评分-年份关系图
    data6 = cur.execute("SELECT 上映年份,电影评分 FROM t_film")  #
    # scoreyearlist = list(chain.from_iterable(cur.fetchall()))
    df = pd.DataFrame(list(cur.fetchall()))
    years = df[0].tolist()
    # 将year中特殊的字段（含有中国大陆）的转换成年份，同时将字符串转换成数字
    for year in years:
        if (operator.contains(year, "(")):
            year2 = year.split("(")[0]  # 将(分割1次s
            years[years.index(year)] = year2
    scores = df[1].tolist()

    #绘制整个页面
    page = Page(
            page_title="基于Python的电影数据分析大屏",
            layout=Page.DraggablePageLayout,  # 拖拽方式
        )
    page.add(
            eval_num.eval_num(evalNumlist),
            qingGan.qinggan(comments),
            daoyanciYun.daoyanciYun(daoyans),
            scoretop10.scoretop10(score10),
            evalNumPeoTop10.evalNumPeoTop10(x_data, y_data),
            score_year.score_year(years, scores),
            bigTitle.bigTitle()
        )
    #page.render('大屏_临时.html')  # 执行完毕后,打开临时html并排版,排版完点击Save Config，把json文件放到本目录下
    print('生成完毕:大屏_临时.html')
    Page.save_resize_html(
        source="大屏_临时.html",
        cfg_file="chart_config.json",
        dest="大屏_最终.html",
    )
    print("大屏_最终.html")
    cur.close()
    conn.close()  # 关闭数据库连接
from pyecharts.components import Table
from pyecharts import options as opts
from pyecharts.options import ComponentTitleOpts
# 评分最高的前10电影
def scoretop10(data_list) -> Table():
    table=Table()
    headers = ['电影名称', '评分', '评论数', '上映年', '一句话短评']
    table.add(headers,data_list)
    table.render('电影排名TOP10_数据表格.html')
    print('生成完毕:电影排名TOP10_数据表格.html')
    return table
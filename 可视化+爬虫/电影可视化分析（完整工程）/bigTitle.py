from pyecharts.components import Table
def bigTitle() -> Table():
    # 大标题
    table = Table()
    table.add(headers='基于Python的电影数据分析大屏', rows=[], attributes={
        "align": "center",
        "border": False,
        "padding": "2px",
        "style": "background:{}; width:800px; height:50px; font-size:25px; color:#C0C0C0;"
    })
    table.render('大标题.html')
    print('生成完毕:大标题.html')
    return table

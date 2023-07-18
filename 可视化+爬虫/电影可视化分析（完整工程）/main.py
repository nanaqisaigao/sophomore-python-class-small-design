# 导入模块
import requests  # 发送请求
from bs4 import BeautifulSoup  # 解析网页
import pandas as pd  # 存取csv

import databaseConnect
import databaseCreat

from itertools import chain
from openpyxl.workbook import Workbook
# 申明全局变量 用以存储电影信息
movie_name = []  # 电影名称
movie_url = []  # 电影链接
movie_star = []  # 电影评分
movie_star_people = []  # 评分人数
movie_director = []  # 导演
movie_actor = []  # 主演
movie_year = []  # 上映年份
movie_country = []  # 国家
movie_type = []  # 类型
movie_short_comment = []  # 一句话短评


def get_movies(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/83.0.4103.116 '
                      'Safari/537.36'
    }
    # 向网页发送请求：
    res = requests.get(url, headers=headers)
    # 利用BeautifulSoup库解析响应页面：
    soup = BeautifulSoup(res.text, 'html.parser')  # soup = BeautifulSoup(res, 'lxml')
    # 用BeautifulSoup的select函数，（css解析的方法）编写代码逻辑，部分核心代码：
    for movie in soup.select('.item'):
        # 显示当前电影编号
        num = movie.find('em').get_text()
        print(num)
        # print(movie.select('.hd a')) 表示当前页面中所有item的'.hd a'都爬出来。 这里只需要获取当前item第一个a，用find比较好，但find层级太复杂
        name = movie.select('.hd>a>span')[0].get_text().replace('\n', '').strip()  # 电影名称 只显示第一个span中的title
        print('[电影名称]', name)
        movie_name.append(name)
        url = movie.select('.hd a')[0].attrs['href']  # 电影链接尽管只有一个a，但是[0]必须要加.用[0]之后可用attrs
        print('[电影链接]', url)
        movie_url.append(url)
        star = movie.select('.rating_num')[0].get_text()  # 电影评分景
        print('[电影评分]', star)
        movie_star.append(star)
        star_people = movie.select('.star span')[3].get_text()  # 评分人数
        star_people = star_people.strip().replace('人评价', '')  # strip()去掉两端的空格
        print('[评分人数]', star_people)
        movie_star_people.append(star_people)
        direct = movie.select('.bd p')[0].get_text().strip().split('\n')[0].replace("导演:", '').strip()
        # print(direct)
        director = direct.split("\xa0\xa0")[0].strip()
        # directors=re.sub('[a-zA-Z]', '', director) #只显示中文名
        print('[导演]', director)
        movie_director.append(director)
        # html中导演名字太长，无法出现主演的情况
        if director != direct:
            actor = direct.split("\xa0\xa0")[1].strip()  # strip()可将第三个&nbsp()去掉，但是&nb...却无法去掉
            print('[主演]', actor)
            movie_actor.append(actor)
        else:
            actor = '无'
            print('[主演]', actor)
            movie_actor.append(actor)
            # print(movie.select('.bd p')[0].get_text().strip().split('\n'))
        # 大闹天宫，特殊处理
        movie_infos = movie.select('.bd p')[0].get_text().strip()
        if name == '大闹天宫':
            # print(name+"text")
            year0 = movie_infos.split('\n')[1].split('/')[0].strip()
            year1 = movie_infos.split('\n')[1].split('/')[1].strip()
            year2 = movie_infos.split('\n')[1].split('/')[2].strip()
            year = year0 + '/' + year1 + '/' + year2
            movie_year.append(year)
            country = movie_infos.split('\n')[1].split('/')[3].strip()
            movie_country.append(country)
            type = movie_infos.split('\n')[1].split('/')[4].strip()
            movie_type.append(type)
        else:
            # print(name)
            year = movie_infos.split('\n')[1].split("/")[0].strip()
            print('[上映年份]', year.strip())
            movie_year.append(year.strip())
            country = movie_infos.split('\n')[1].split("/")[1].strip()
            print('[国家]', country.strip())
            movie_country.append(country.strip())
            type = movie_infos.split('\n')[1].split('/')[2].strip()
            print('[类型]', type.strip())
            movie_type.append(type.strip())
            # info = tag.find(attrs={"class": "inq"})
            #         if (info):  # 避免没有影评时调用 get_text() 报错
            #             content = info.get_text()
            #             print('[影评]', content)
            #             infofile.write("[影评]" + content + "\r\n")
            # 寄生虫电影没有影评 129
        quote = movie.select('.inq')
        if quote:
            short_comment = quote[0].get_text()
        else:
            short_comment = '无'
        print('[简评]', short_comment)
        movie_short_comment.append(short_comment)


def save_to_csv(csv_name):
    """
    数据保存到csv
    dataframe = pd.DataFrame({'a_name':a,'b_name':b})
    dataframe.to_csv("test.csv",index=False,sep=',') ,index表示是否显示行名，default=True
    data = pd.read_csv('test.csv')
    """
    df = pd.DataFrame()  # 初始化一个DataFrame对象
    df['电影名称'] = movie_name
    df['电影链接'] = movie_url
    df['电影评分'] = movie_star
    df['评分人数'] = movie_star_people
    df['导演'] = movie_director
    df['主演'] = movie_actor
    df['上映年份'] = movie_year
    df['国家'] = movie_country
    df['类型'] = movie_type
    df['简评'] = movie_short_comment
    df.to_csv(csv_name, encoding='utf_8_sig')  # 将数据保存到csv文件


# 部署到flask
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', )


# 定义路由及视图函数
@app.route('/')  # 装饰器
def f_index():
    return render_template('最终大屏.html')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    csv_name = 'movie250.csv'  # csv文件名
    i = 0
    # while i < 10:
    #     # 延迟一段时间后爬虫，避免ip被封
    #     time.sleep(random.randint(3, 5))
    #     print('页码：', i + 1)
    #     num = i * 25  # 每次显示 25 部，URL 序号按 25 增加
    #     urls = 'https://movie.douban.com/top250?start=' + str(num) + '&filter='
    #     get_movies(urls)
    #     save_to_csv(csv_name)
    #     i = i + 1
# 建立数据库连接
databaseCreat.database_creat()  # 创建表，从csv读取数据写入到MySQL
databaseConnect.database_connect_figure()  # 连接数据，读取数据并作图
app.run(host='0.0.0.0', port=7888, debug=True)

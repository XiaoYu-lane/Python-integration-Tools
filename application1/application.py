"""
后台主程序
"""
# 导入
from flask import Flask, render_template
import webview as web

# 实例化flask对象
app = Flask(__name__,
            template_folder='front_page',
            static_folder='front_page/static')


# 启动信息处理
def on_closed():
    print('窗口关闭')


def on_closing():
    print('窗口正在关闭')


def on_shown():
    print('窗口正在展示')


def on_loaded():
    print('dom读取完成')

# 定义路由渲染模板
# 首页


@app.route('/')
def index():
    return render_template('/index.html')


# 网络爬虫
@app.route('/web_spider')
def web_spider():
    return render_template('/webSpider.html')


# 设置
@app.route('/setting')
def setting():
    return render_template('/setting.html')


# 接口
class Api:
    def select_dir(self):   # 选择爬虫爬取的保存目录
        result = master_window.create_file_dialog(web.FOLDER_DIALOG)
        print(result)
        return result[0] if result else ''

    def quit(self):     # 退出
        master_window.destroy()

    def new_win(self, name, url):  # 创建新窗口
        child_window = web.create_window(name, url=url,
                                         width=300,
                                         height=400,
                                         resizable=False,
                                         text_select=False)
        # web.start(child_window)


if __name__ == '__main__':
    # 实例化api
    api = Api()
    # 中文提示
    chinese = {
        'global.quitConfirmation': u'确定退出？',
    }
    # 创建程序窗口
    master_window = web.create_window('集成爬虫',
                                      url=app,
                                      width=600,
                                      height=400,
                                      resizable=False,
                                      text_select=False,
                                      confirm_close=True,
                                      js_api=api)

    # 添加窗口事件
    master_window.events.closed += on_closed
    master_window.events.closing += on_closing
    master_window.events.shown += on_shown
    master_window.events.loaded += on_loaded

    web.start(localization=chinese, debug=True)

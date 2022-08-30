"""
路由和入口
"""
# 导入
import threading

import webview as web
from flask import Flask, render_template
from werkzeug.middleware.dispatcher import DispatcherMiddleware

# 静态文件夹
template_folder = '../../frontend'
static_folder = '../../frontend/static'
# 创建路由以及初始化
app_index = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
app_setting = Flask(__name__, template_folder=template_folder, static_folder=static_folder)


# 调试信息处理


def on_closed():
    print('窗口关闭')


def on_closing():
    print('窗口正在关闭')


def on_shown():
    print('窗口正在展示')


def on_loaded():
    print('dom读取完成')

# 添加路由

# 首页


@app_index.route('/')
def index():
    return render_template('/index.html')

# 网络爬虫


# @app.route('/web_spider')
# def web_spider():
#     return render_template('/webSpider.html')


@app_setting.route('/')
def setting():
    return render_template('/setting.html')


# 主页接口
class Api:
    """
    定义传入的window窗口
    """

    def __init__(self) -> None:
        self._window = None

    def set_window(self, window):
        self._window = window

    def select_save_dir(self):   # 选择保存目录文件夹
        pass

    def quit(self):     # 退出当前窗口
        self._window.destroy()

    def minimize(self):     # 最小化窗口
        self._window.minimize()

    def get_url(self, window):
        print(window.get_current_url())

    def create_win(self, url):
        child_window = web.create_window('设置',
                                         url=app_setting,
                                         width=200,
                                         height=300,
                                         resizable=False,
                                         text_select=False,
                                         frameless=True)

        # c_win = threading.Thread(target=child_window)
        # c_win.start()
        web.start(child_window, self.get_url(child_window))


if __name__ == '__main__':
    # 实例化Api类
    api = Api()
    # 中文提示
    chinese = {
        'global.quitConfirmation': u'确定退出？',
    }
    # 创建程序窗口
    master_window = web.create_window('集成爬虫',
                                      url=app_index,
                                      width=600,
                                      height=400,
                                      resizable=False,
                                      text_select=False,
                                      confirm_close=True,
                                      js_api=api,
                                      frameless=True
                                      )

    # 添加窗口事件
    master_window.events.closed += on_closed
    master_window.events.closing += on_closing
    master_window.events.shown += on_shown
    master_window.events.loaded += on_loaded

    # 将上面创建的window对象再通过函数传给实例化后的api对象
    api.set_window(master_window)

    web.start(localization=chinese, debug=True)

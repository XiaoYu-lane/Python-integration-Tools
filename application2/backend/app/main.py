"""
路由和入口
"""
# 导入
import webview as web
from flask import Flask, render_template

# 创建路由以及初始化
app = Flask(__name__, template_folder='../../frontend', static_folder='../../frontend/src')


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


@app.route('/')
@app.route('/index')
def index():
    return render_template('/index.html')


if __name__ == '__main__':
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
                                      confirm_close=True
                                      )

    # 添加窗口事件
    master_window.events.closed += on_closed
    master_window.events.closing += on_closing
    master_window.events.shown += on_shown
    master_window.events.loaded += on_loaded

    web.start(localization=chinese, http_server=True, debug=True)

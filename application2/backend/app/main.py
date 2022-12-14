"""
路由和入口
"""
# 导入
import os.path
from flask import Flask, render_template, request, jsonify
from setting import *
import json
from link import *

# 静态文件夹
template_folder = '../../frontend'
static_folder = '../../frontend/static'
config = '../../frontend/config'

# 创建路由以及初始化
app_index = Flask(__name__, template_folder=template_folder,
                  static_folder=static_folder)
app_setting = Flask(__name__, template_folder=template_folder,
                    static_folder=static_folder)
app_help = Flask(__name__, template_folder=template_folder,
                 static_folder=static_folder)
app_edit = Flask(__name__, template_folder=template_folder,
                 static_folder=static_folder)

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


@app_index.route('/', methods=['GET', 'POST'])   # 首页
def index():
    if request.method == 'POST':
        if os.path.exists(config):
            with open('{}/config.json'.format(config), 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data
        else:
            data = {
                'status': 366,
                'message': 'Please select a file path'
            }
            return jsonify(data)
    elif request.method == 'GET':
        if os.path.exists(config):
            os.remove('{}/config.json'.format(config))
            os.rmdir(config)
            return render_template('/index.html')
        else:
            return render_template('/index.html')


@app_index.route('/web_spider')  # 网络爬虫
def web_spider():
    return render_template('/webSpider.html')


@app_setting.route('/')     # 设置窗口
def setting():
    return render_template('/setting.html')


@app_setting.route('/save_folder', methods=['POST'])     # 传入保存文件的路径
def load_folder():
    if request.method == 'POST':
        if request.form['save_folder'] != '':
            if not os.path.exists(config):  # 创建json文件存放保存文件路径
                os.mkdir(config)
                with open('{}/config.json'.format(config), 'w', encoding='utf-8') as f:
                    json_data = {
                        'save_folder': request.form['save_folder'], 'status': 201}
                    json.dump(json_data, f)
                    result = {
                        'save_folder': request.form['save_folder'],
                        'status': 201,
                        'message': 'select success'
                    }
                    return jsonify(result)
            else:
                with open('{}/config.json'.format(config), 'w', encoding='utf-8') as f:
                    json_data = {
                        'save_folder': request.form['save_folder'], 'status': 201}
                    json.dump(json_data, f)
                    result = {
                        'save_folder': request.form['save_folder'],
                        'status': 201,
                        'message': 'select success'
                    }
                    return jsonify(result)

        else:
            result = {
                'status': 400,
                'message': 'unknown error'
            }
            return jsonify(result)


# 主页接口
class Api(SettingApi, Link):
    """
    定义传入的window窗口
    """

    def __init__(self) -> None:
        self._window = None
        self.child_window = None

    def set_window(self, window):
        self._window = window

    def quit(self):     # 退出当前窗口
        self._window.destroy()

    def minimize(self):     # 最小化窗口
        self._window.minimize()

    def create_win(self, app, other_api):  # 创建新窗口
        self.child_window = web.create_window('设置',
                                              url=app,
                                              width=400,
                                              height=500,
                                              resizable=False,
                                              text_select=False,
                                              js_api=other_api)

        other_api.select_window(self.child_window)

        web.start(self.child_window, other_api.get_url())

    def url_option(self, url):  # 判断新建窗口的内容
        # 通过传进来的url判断新建窗口返回的内容
        if url != '':
            if url == 'setting':
                app = app_setting   # 路由
                js = SettingApi()       # 接口
                self.create_win(app, js)
            elif url == 'help':
                app = app_help
                js = setting()
                print(app)
                self.create_win(app, js)
            elif url == 'edit':
                app = app_edit
                js = setting()
                print(app)
                self.create_win(app, js)
        else:
            exit(0)

    def help(self):
        webbrowser.open(
            'https://github.com/XiaoYu-lane/Python-integration-Tools')


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
                                      height=600,
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
    api.select_window(master_window)

    web.start(localization=chinese, debug=True)

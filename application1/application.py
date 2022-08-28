"""
后台主程序
"""
# 导入
from flask import Flask, render_template
import webview as web


# 启动信息处理
def on_closed():
    print('窗口关闭')


def on_closing():
    print('窗口正在关闭')


def on_shown():
    print('窗口正在展示')


def on_loaded():
    print('dom读取完成')

# 用flask做路由




# 接口
class Api:
    def select_dir(self):   # 选择保存文件的目录
        result = window.create_file_dialog(web.FOLDER_DIALOG)
        print(result)
        return result[0]


if __name__ == '__main__':
    # 中文提示
    chinese = {
        'global.quitConfirmation': u'确定退出？',
    }
    # 创建程序窗口
    window = web.create_window('集成爬虫',
                               url='front_page',
                               width=900,
                               height=620,
                               resizable=False,
                               text_select=False,
                               confirm_close=True)

    # 添加窗口事件
    window.events.closed += on_closed
    window.events.closing += on_closing
    window.events.shown += on_shown
    window.events.loaded += on_loaded

    web.start(localization=chinese, http_server=True, debug=True)

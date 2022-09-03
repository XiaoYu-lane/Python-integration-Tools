"""
设置窗口处理逻辑
"""
import webview as web


class SettingApi:

    def select_window(self, window):
        self.window = window

    # 选择文件夹路径
    def select_dir(self):
        result = self.window.create_file_dialog(web.FOLDER_DIALOG)
        return result[0] if result else ''

    def get_url(self):
        current_url = self.window.get_current_url()
        return current_url

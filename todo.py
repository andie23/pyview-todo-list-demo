import webview
from tkinter import filedialog

class Api:
    def saveToFile(self, content):
        try:
            f = filedialog.asksaveasfile(mode="w", defaultextension="txt")
            f.write(content)
            f.close()
        except Exception as error:
            return {
                "ok": False,
                "error": error
            }
        return {
            "ok": True
        }

if __name__ == '__main__':
    api = Api()
    webview.create_window('Todo App', 'index.html', js_api=api)
    webview.start()

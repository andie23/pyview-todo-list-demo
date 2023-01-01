import webview

class Api:
    def saveToFile(self, file_name, content):
        try:
            f = open(f'{file_name}.txt', "a")
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

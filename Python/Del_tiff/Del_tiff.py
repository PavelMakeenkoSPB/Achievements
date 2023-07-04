# Требуется удалить все файлы .tiff  из папки при условии наличия .jpg файлов с теми же именами
import os
import tkinter as tk
import tkinter.filedialog as fd

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        btn_dir = tk.Button(self, text="Выбрать папку где лежат ненужные .tiff",
                             command=self.choose_directory)
        btn_exit = tk.Button(self, text='Пойду проч', command=self.destroy)

        btn_dir.pack(padx=60, pady=10)
        btn_exit.pack(padx=60, pady=10)

    def choose_directory(self):
        dir_name = fd.askdirectory(title="Укажите путь к папке", initialdir="/")
        filesIntoDirectory = os.listdir(dir_name)
        for item in filesIntoDirectory:
            if item.endswith(".tiff"):
                os.remove(os.path.join(dir_name, item))

if __name__ == "__main__":
    app = App()
    app.mainloop()    
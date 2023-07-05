import os
import tkinter as tk
import tkinter.filedialog as fd
import filecmp
import collections
import tkinter.messagebox as mb

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        btn_warn = tk.Button(self, text="Что делает эта программа?",
                             command=self.show_warning)

        btn_dir = tk.Button(self, text="Выбрать папку, где лежат ненужные .tiff",
                             command=self.choose_directory)
        btn_exit = tk.Button(self, text='Поскачу радостно дальше по дороге жизни!', command=self.destroy)

        opts = {'padx': 100, 'pady': 10, 'expand': True, 'fill': tk.BOTH}
        btn_warn.pack(**opts)


        btn_dir.pack(padx=60, pady=10)
        btn_exit.pack(padx=60, pady=10)

    def show_warning(self):
        msg = "Эта программа удаляет из выбранной папки файлы .tiff ТОЛЬКО если существуют файлы с точно таким же именем, но другим расширением, например .jpg"
        mb.showwarning("Инструкция", msg)

    def choose_directory(self):
        dir_name = fd.askdirectory(title="Укажите путь к папке", initialdir="/")
        allFiles = os.listdir(dir_name)


        notDots_list = []
        temp_list = []
        TiffDelList = []
        
        for i in range(len(allFiles)):
            cuttingAfterDots = (allFiles[i].split('.')).pop(0)
            notDots_list.append(cuttingAfterDots)
        
        countering = collections.Counter(notDots_list)
        
        temp_list.extend(z for z in countering if countering[z] > 1)
        
        for el in range(len(temp_list)):
            tiffing = temp_list[el] + '.tiff'
            TiffDelList.append(tiffing)
        
        
        for item in TiffDelList:
            if item.endswith(".tiff"):
                os.remove(os.path.join(dir_name, item))
                
        mb.showinfo('Это Победа', 'Файлы .tiff, имевшие тёзок, покинули этот мир')
                
if __name__ == "__main__":
    app = App()
    app.mainloop()  

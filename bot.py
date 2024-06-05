
import tkinter as tk
from tkinter import ttk

# Список заголовков и содержаний текста
content = {
    "сураи фотиҳа": "АЪУЗУБИЛЛАҲИМИНАШ-ШАЙТ АНИР-РАҲИМ Бисмиллаҳир-Раҳманир-Раҳим 1 .Алҳамду лиллаҳи раббил баламин 2.Ар-раҳманир-раҳим 3. МаликиявМИДДИН 4. Иййаканаъбуду ва иййака настаъин5 .Иҳдинас-сиротал мустақ им 6 . Сиротал-лазина анъамта ъалайҳим ғайрил мағзуби ъалайҳим Валаззоллин7.",
    "сураи Ёсин": "Бисмиллаҳир-Раҳманир-Раҳим Йа син 1.Вал қур-анил ҳаким 2. Иннака ламинал мурсалин 3. Ъала сироти(н)м мустақим 4. Танзилал ъазизир-раҳим 5. Литунзира қавма(н)м ма унизира абауҳум фаҳум ғофилун 6. Лақад ҳаққал қавлу ъала аксариҳим фаҳум ла юьминун 7. Инна ҷаъална фи аънақиҳим ағлалан фаҳия илал азқони фаҳум-муқмаҳун 8. Ва ҷаъална ми(н)м байни айдиҳим садда(н)в ва мин халфиҳим саддан фа ағшайнаҳум фаҳум лаюбсирун 9. Вз саваун ъалайҳим а-анзартаҳум ам ламт унзирҳум ла юьминун 10. Иннама тунзиру, манит- табаъаз-зикра ва хашияр раҳмана бил ғайб. Фабашширҳу бимағфирати(н)в ва аҷрин карим 11. Инна наҳну нуҳйил",
    "сураи мулк(таборак)": "Благословен Тот, в Чьей Длани - власть, ибо Он над всякой вещью мощен.",
    "сураи набаь": "О чем они спрашивают друг друга? О великом Вести,",
    "сураи сураи ториқ": "Клянусь небом и Ночным [светилом]!",
    "сураи иншироҳ": "",
    "Сураи тин": "Клянусь смоковницей и маслиной!",
    "Сураи Алақ": "",
    "Сураи қадр": "",
    "Сураи Баййинаҳ": "",
    "Сураи Залзала": "",
    "Сураи одиёт": "",
    "Сураи Қориъаҳ" : "",
    "Сураи такосур": "",
    "Сураи Аср": "",
    "Сураи Ҳумазаҳ": "",
    "Сураи Фил": "",
    "Сураи Қурайш": "",
    "Сураи моъун": "",
    "Сураи Кавсар": "",
    
    

}

# Функция для открытия нового окна
def open_new_window(title):
    new_window = tk.Toplevel(root)
    new_window.title(title)
    new_window.geometry("600x400")
    new_window.configure(bg="#B0E0E6")

    # Стили для нового окна
    new_window.option_add("*Font", "helvetica 14")
    new_window.option_add("*Background", "#B0E0E6")
    new_window.option_add("*Foreground", "#333333")

    # Создание фрейма с полосой прокрутки
    content_frame = tk.Frame(new_window)
    content_frame.pack(fill=tk.BOTH, expand=True)

    # Создание полосы прокрутки
    scrollbar = ttk.Scrollbar(content_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Создание текстового поля с прокруткой
    label = tk.Text(content_frame, yscrollcommand=scrollbar.set, bg="#B0E0E6", fg="#333333", wrap=tk.WORD,
                    font="helvetica 14")
    label.insert(tk.END, content[title])
    label.config(state=tk.DISABLED)
    label.pack(fill=tk.BOTH, expand=True)

    scrollbar.config(command=label.yview)

    back_button = tk.Button(new_window, text="Назад", command=new_window.destroy, bg="#007bff", fg="#ffffff",
                            activebackground="#0056b3", activeforeground="#ffffff", padx=10, pady=5, borderwidth=0)
    back_button.pack(side=tk.BOTTOM, pady=10)

# Функция для переключения режима
def toggle_mode():
    if root.cget("background") == "#B0E0E6":
        root.configure(bg="#333333", fg="#B0E0E6")
        for widget in root.winfo_children():
            widget.configure(bg="#333333", fg="#B0E0E6")
    else:
        root.configure(bg="#B0E0E6", fg="#333333")
        for widget in root.winfo_children():
            widget.configure(bg="#B0E0E6", fg="#333333")

# Создание главного окна
root = tk.Tk()
root.title("КИТОБИ СУРАҲО")
root.geometry("400x400")
root.configure(bg="#B0E0E6")

# Стили для главного окна
root.option_add("*Font", "helvetica 14")
root.option_add("*Background", "#B0E0E6")
root.option_add("*Foreground", "#333333")

# Создание меню
menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar)



menubar.add_cascade(label="Меню", menu=file_menu)
file_menu.add_command(label="Каталог суpаҳо", command=lambda: open_new_window("Каталог суpаҳо"))
file_menu.add_command(label="Темный / Светлый", command=toggle_mode)
file_menu.add_command(label="Выход", command=root.quit)

# Создание списка заголовков
content_list = tk.Frame(root)
content_list.pack(fill=tk.BOTH, expand=True)

# Создание полосы прокрутки для главного окна
scrollbar = ttk.Scrollbar(content_list)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Создание списка кнопок с прокруткой
buttons_list = tk.Listbox(content_list, yscrollcommand=scrollbar.set, bg="#B0E0E6", fg="#333333", font="helvetica 14")
buttons_list.pack(fill=tk.BOTH, expand=True)

for header in content.keys():
    buttons_list.insert(tk.END, header)
    buttons_list.bind("<<ListboxSelect>>", lambda event: open_new_window(buttons_list.get(buttons_list.curselection())))

scrollbar.config(command=buttons_list.yview)

root.mainloop()
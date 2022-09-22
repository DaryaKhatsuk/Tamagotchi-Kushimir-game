import json
import random
import tkinter
from tkinter import messagebox, RIGHT, Y, BOTH


class Cat:
    def __init__(self, name):
        self.name = name
        self.age = 0.3
        self.hunger = 50
        self.thirst = 50
        self.cheerfulness = 50
        self.joy = 50
        self.live = 9
        self.MainWindow = tkinter.Tk()
        self.info_frame = tkinter.Frame(bg="blue")
        self.text = tkinter.Text(master=self.info_frame, font=("Comic Sans MS", 11))

    def lives(self):
        if self.ends_of_life():
            self.live -= 1
            self.hunger = 50
            self.thirst = 50
            self.cheerfulness = 50
            self.joy = 50
            self.text.insert(tkinter.END, f"""Вы огорчили {self.name}а и потеряли одну жизнь. 
Осталось жизней: {self.live}.\n""")
            self.info()
        if self.live == 0:
            messagebox.showinfo("Конец игры", f"Вы разочаровали {self.name}а, он решил больше не возвращаться к вам!")
            self.MainWindow.destroy()

    def ends_of_life(self):
        if self.age > 12:
            self.text.insert(tkinter.END, f"{self.name} погиб от старости.\n")
            return True
        if self.hunger > 100:
            self.text.insert(tkinter.END, "Гибель в стиле Диониса.\n")
            return True
        elif self.hunger <= 0:
            self.text.insert(tkinter.END, f"{self.name} погиб от голода.\n")
            return True
        if self.thirst <= 0:
            self.text.insert(tkinter.END, f"{self.name} погиб от жажды.\n")
            return True
        if self.joy <= 0:
            self.text.insert(tkinter.END, f"{self.name} погиб от Вашего безразличия.\n")
            return True
        return False

    def info(self):
        self.text.insert(tkinter.END, f"""\nВозраст: {self.age} года
Сытость: {self.hunger}%
Водный баланс: {self.thirst}%
Бодрость: {self.cheerfulness}%
Счастье: {self.joy}%\n""")

    def cheer(self):
        if self.cheerfulness <= 20:
            self.text.insert(tkinter.END, f"""{self.name} устал, приставай к кому нибудь другому!
{self.name} свернулся калачиком и заснул.""")
            self.age += 0.04
            self.hunger -= random.randint(5, 8)
            self.thirst -= random.randint(5, 8)
            self.cheerfulness += random.randint(10, 20)
            self.joy -= 2
            self.info()
            self.lives()

    def feed(self):
        if self.cheerfulness <= 20:
            self.cheer()
        else:
            self.text.insert(tkinter.END, f"Вы покормили {self.name}а.")
            self.age += 0.05
            self.hunger += random.randint(10, 12)
            self.thirst -= random.randint(5, 8)
            self.cheerfulness -= random.randint(3, 7)
            self.joy += 3
            self.info()
            self.lives()

    def pour(self):
        if self.cheerfulness <= 20:
            self.cheer()
        elif self.thirst >= 101:
            self.text.insert(tkinter.END, f"{self.name} не хочет больше пить, Вы просто льете воду в миску.\n")
        elif self.thirst >= 150:
            self.text.insert(tkinter.END, "Вода уже льется через край. Пожалуйста, остановитесь!\n")
        else:
            self.text.insert(tkinter.END, f"{self.name} наслаждается свежей водой.")
            self.age += 0.01
            self.hunger -= random.randint(7, 10)
            self.thirst += random.randint(7, 10)
            self.cheerfulness -= random.randint(3, 7)
            self.joy -= 3
            self.info()
            self.lives()

    def play(self):
        if self.cheerfulness <= 20:
            self.cheer()
        elif self.joy >= 100:
            self.text.insert(tkinter.END, f"{self.name} не в настроении для игр.\n")
        else:
            self.text.insert(tkinter.END, f"Вы поиграли с {self.name}ом.")
            self.age += 0.08
            self.hunger -= random.randint(5, 8)
            self.thirst -= random.randint(5, 8)
            self.cheerfulness -= random.randint(10, 14)
            self.joy += random.randint(15, 25)
            self.info()
            self.lives()

    def pet(self):
        if self.cheerfulness <= 20:
            self.cheer()
        elif self.joy >= 100:
            self.text.insert(tkinter.END, f"{self.name} не хочет что бы его сейчас гладили.\n")
        else:
            self.text.insert(tkinter.END, f"Вы погладили {self.name}а.")
            self.age += 0.015
            self.hunger -= random.randint(5, 8)
            self.thirst -= random.randint(5, 8)
            self.cheerfulness -= random.randint(6, 10)
            self.joy += random.randint(20, 40)
            self.info()
            self.lives()

    def leave(self):
        if self.cheerfulness <= 20:
            self.cheer()
        elif self.cheerfulness >= 99:
            self.text.insert(tkinter.END, f"{self.name} хорошо поиграл пока Вас не было.")
            self.age += 0.09
            self.hunger -= random.randint(5, 8)
            self.thirst -= random.randint(5, 8)
            self.cheerfulness -= random.randint(6, 10)
            self.joy += random.randint(17, 28)
            self.info()
            self.lives()
        else:
            self.text.insert(tkinter.END, f"{self.name} хорошо отдохнул пока Вас не было.")
            self.age += 0.09
            self.hunger -= random.randint(5, 8)
            self.thirst -= random.randint(5, 8)
            self.cheerfulness += random.randint(20, 30)
            self.joy -= random.randint(6, 10)
            self.info()
            self.lives()


class Interact(Cat):
    def __init__(self, name):
        super().__init__(name)

    def save(self):
        with open('TamagotchiSave.json', 'w') as file:
            TamagotchiSave = {"self.age": self.age, "self.hunger": self.hunger, "self.thirst": self.thirst,
                              "self.cheerfulness": self.cheerfulness, "self.joy": self.joy, "self.live": self.live}
            json.dump(TamagotchiSave, file)

    def load(self):
        with open('TamagotchiSave.json', 'r') as file:
            data = json.load(file)
            self.age = data["self.age"]
            self.hunger = data["self.hunger"]
            self.thirst = data["self.thirst"]
            self.cheerfulness = data["self.cheerfulness"]
            self.joy = data["self.joy"]
            self.live = data["self.live"]
        self.text.insert(tkinter.END, f"Жизней: {self.live}")
        self.info()

    def tk_init(self):
        MainFrame = tkinter.Frame()
        self.MainWindow.geometry("400x700")
        self.MainWindow.title("Tamagotchi Kushimir-game")
        mainmenu = tkinter.Menu(self.MainWindow)
        self.MainWindow.config(menu=mainmenu)
        mainmenu.add_command(label='Сохранение', command=self.save)
        mainmenu.add_command(label='Загрузка', command=self.load)
        hello = tkinter.Label(self.MainWindow, text=f"Добро пожаловать в {self.name}-game! \n"
                              "Играя не забывайте, на все воля случая!", font=("Comic Sans MS", 11))
        hello.pack()
        button1 = tkinter.Button(master=MainFrame, text="Покормить кота", command=self.feed,
                                 font=("Comic Sans MS", 11))
        button1.pack(padx=6, pady=3, fill=BOTH)
        button2 = tkinter.Button(master=MainFrame, text="Налить коту воды", command=self.pour,
                                 font=("Comic Sans MS", 11))
        button2.pack(padx=6, pady=3, fill=BOTH)
        button3 = tkinter.Button(master=MainFrame, text="Поиграть с котом", command=self.play,
                                 font=("Comic Sans MS", 11))
        button3.pack(padx=6, pady=3, fill=BOTH)
        button4 = tkinter.Button(master=MainFrame, text="Погладить кота", command=self.pet,
                                 font=("Comic Sans MS", 11))
        button4.pack(padx=6, pady=3, fill=BOTH)
        button5 = tkinter.Button(master=MainFrame, text="Пойти на работу", command=self.leave,
                                 font=("Comic Sans MS", 11))
        button5.pack(padx=6, pady=3, fill=BOTH)
        button6 = tkinter.Button(master=MainFrame, text="Выйти из игры", command=exit,
                                 font=("Comic Sans MS", 11))
        button6.pack(padx=6, pady=3, fill=BOTH)
        MainFrame.pack(fill=BOTH)
        scroll = tkinter.Scrollbar(self.MainWindow)
        scroll.pack(side=RIGHT, fill=Y)
        scroll.config(command=self.text.yview)
        self.text.config(yscrollcommand=scroll.set)
        self.text.pack(fill=BOTH)
        self.info_frame.pack(fill=BOTH)
        self.MainWindow.mainloop()


inter = Interact("Кусимир")
inter.tk_init()

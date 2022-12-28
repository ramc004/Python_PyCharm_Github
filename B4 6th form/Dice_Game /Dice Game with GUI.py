from tkinter import *
from tkinter import messagebox
from random import *

firstPlayerName = StringVar
secondPlayerName = StringVar
playerNames = []
score1 = IntVar
score2 = IntVar
main_score = 5
p1 = IntVar
p2 = IntVar
headCounter = 0
tailCounter = 0


def dis_Appear_Main_Window(master):
    master.quit()
    master.withdraw()


def the_Dice(flag, master):
    par = randint(1, 6)
    global p1, p2
    if par == 1:
        p1 = 1
        p2 = 1
    elif par == 2:
        p1 = 2
        p2 = 2
    elif par == 3:
        p1 = 3
        p2 = 3
    elif par == 4:
        p1 = 4
        p2 = 4
    elif par == 5:
        p1 = 5
        p2 = 5
    elif par == 6:
        p1 = 6
        p2 = 6
    master.quit()
    master.withdraw()


def player_1(main_score, head_Player, ftypeuno):
    global p1, p2
    p1 = 0
    p2 = 0
    root = Tk()
    root.title(head_Player + " Dice")
    root.geometry("450x350")
    txt = "Winning Score: " + str(main_score)
    main_Score_Label = Label(root, text=txt)
    main_Score_Label.place(relx=0.7, rely=0.1)
    main_Score_Label.config(bg="black", fg="white", font=ftypeuno)

    player_Label = Label(root, text="Turn-> " + head_Player)
    player_Label.place(rely=0.4, anchor="center")
    player_Label.config(bg="yellow", fg="blue", font=ftypeuno)

    the_Button = Button(root, text="Throw the Dice", width=25, command=lambda: the_Dice(1, root))
    the_Button.place(relx=0.5, rely=0.5, anchor="center")
    the_Button.config(font=ftypeuno, bg="#17c1c1", fg="black")

    root.resizable(False, False)
    root.mainloop()


def player2(main_score, tail_Player, ftypeuno):
    global p1, p2
    p1 = 0
    p2 = 0
    root = Tk()
    root.title(tail_Player + " Dice")
    root.geometry("450x350")

    txt = "Winning Score: " + str(main_score)
    main_Score_Label = Label(root, text=txt)
    main_Score_Label.place(relx=0.7, rely=0.1)
    main_Score_Label.config(bg="black", fg="white", font=ftypeuno)

    player_Label = Label(root, text="Turn-> " + tail_Player)
    player_Label.place(relx=0.5, rely=0.4, anchor="center")
    player_Label.config(bg="yellow", fg="blue", font=ftypeuno)

    the_Button = Button(root, text="Throw the Dice", width=25, command=lambda: the_Dice(2, root))
    the_Button.place(relx=0.5, rely=0.5, anchor="center")
    the_Button.config(font=ftypeuno, bg="#17c1c1", fg="black")

    root.resizable(False, False)
    root.mainloop()


class Image_Tk(object):
    @classmethod
    def Photo_Image(cls, img):
        pass


def photo(args):
    pass


def thrown_Dice(p, player_Name, score, ftypeuno, main_score):
    root = Toplevel()
    title = player_Name + " Dice"
    root.title(title)
    root.geometry("450x350")

    txt = "Winning Score: " + str(main_score)
    main_Score_Label = Label(root, text=txt)
    main_Score_Label.place(relx=0.7, rely=0.1)
    main_Score_Label.config(bg="black", fg="white", font=ftypeuno)

    image_Name = "dice_" + str(p) + ".jpg"
    img = Image.open(image_Name)
    img = img.resize((90, 90), Image.ANTIALIAS)
    Image_Tk.Photo_Image(img)

    im_label = Label(root, image=photo)
    im_label.place(relx=0.5, rely=0.5, anchor="center")

    name_Label = Label(root, text=player_Name, width=20)
    name_Label.place(relx=0.5, rely=0.7, anchor="center")
    name_Label.config(bg="#e78c10", fg="black", font=ftypeuno)

    info_Label = Label(root, text="Score: " + str(score), width=20)
    info_Label.place(relx=0.5, rely=0.8, anchor="center")
    info_Label.config(bg="black", fg="white", font=ftypeuno)

    root.resizable(False, False)
    root.wait_window()


def head_To_head_Table(winner, head_player, tail_player, ftypeuno):
    global head_Counter, tail_Counter
    root = Tk()
    root.title("Head to Head")
    root.geometry("450x350")

    if (winner is head_player):
        head_Counter += 1
    else:
        tail_Counter += 1

    head_player_Label = Label(root, text=head_player)
    head_player_Label.place(relx=0.3, rely=0.4, anchor="center")
    head_player_Label.config(bg="blue", fg="white", font=ftypeuno)

    head_player_Counter_Label = Label(root, text=str(headCounter), width=10)
    head_player_Counter_Label.place(relx=0.3, rely=0.5, anchor="center")
    head_player_Counter_Label.config(bg="#00c6f2", fg="black", font=ftypeuno)

    tail_player_Label = Label(root, text=tail_player)
    tail_player_Label.place(relx=0.6, rely=0.4, anchor="center")
    tail_player_Label.config(bg="blue", fg="white", font=ftypeuno)

    tail_player_Counter_Label = Label(root, text=str(tailCounter), width=10)
    tail_player_Counter_Label.place(relx=0.6, rely=0.5, anchor="center")
    tail_player_Counter_Label.config(bg="#00c6f2", fg="black", font=ftypeuno)

    root.resizable(False, False)
    root.wait_window()


def dice_Game_Code(head_player, tail_player, ftypeuno):
    pass


class ImageTk(object):
    def Photo_Image(cls, img):
        pass


def head_Table(player_Name, head_player, tail_player, ftypeuno):
    pass


def head_Player(args):
    pass


def tail_Player(args):
    pass


def the_Winner(player_Name, head_player, tail_player, ftypeuno):
    root = Toplevel()
    root.title("Winner")
    root.geometry("450x350")

    global playerNames

    img = Image.open("emo.jpg")
    img = img.resize((150, 100), Image.ANTIALIAS)
    photo = ImageTk.Photo_Image(img)

    photo_Label = Label(root, image=photo)
    photo_Label.place(relx=0.5, rely=0.2, anchor="center")

    msg = "Congratulations !!!"
    msg_Label = Label(root, text=msg)
    msg_Label.place(relx=0.5, rely=0.4, anchor="center")
    msg_Label.config(fg="blue", font=ftypeuno)

    winner_Label = Label(root, text=player_Name, width=25)
    winner_Label.place(relx=0.5, rely=0.5, anchor="center")
    winner_Label.config(bg="black", fg="white", font=ftypeuno)

    f_Label = Label(root, text="Winner of this game")
    f_Label.place(relx=0.5, rely=0.6, anchor="center")
    f_Label.config(bg="#48b7ea", fg="#000000", font=ftypeuno)

    play_Again_Button = Button(root, text="Play Again", width=20,
                               command=lambda: {root.destroy(), head_To_head_Table(
                                   head_Table(player_Name, head_player, tail_player, ftypeuno),
                                   dice_Game_Code(head_player, tail_player, ftypeuno))})
    play_Again_Button.place(relx=0.5, rely=0.9, anchor="center")
    play_Again_Button.config(bg="blue", fg="white", font=ftypeuno)

    root.resizable(False, False)
    root.mainloop()
    global main_score, score2, score1, p1, p2
    p1 = 0
    p2 = 0
    main_score += 5
    score1 = 0
    score2 = 0

    while (score1 <= main_score or score2 <= main_score):
        player_1(main_score, head_Player, ftypeuno)

        score1 += p1

        if (score1 > main_score):
            score1 -= p1
        if (score1 == main_score):
            thrown_Dice(p1, head_Player, score1, ftypeuno, main_score)
            the_Winner(head_Player, head_Player, tail_Player, ftypeuno)
            break
        else:

            thrown_Dice(p1, head_Player, score1, ftypeuno, main_score)
        player2(main_score, tail_Player, ftypeuno)

        score2 += p2

        if (score2 > main_score):
            score2 -= p2
        if (score2 == main_score):
            thrown_Dice(p2, tail_Player, score2, ftypeuno, main_score)
            the_Winner(tail_Player, head_Player, tail_Player, ftypeuno)
            break
        else:
            thrown_Dice(p2, tail_Player, score2, ftypeuno, main_score)
    return 0


def toss_Button_Action(event, ftypeuno, pName, par, player_Names=None, message_box=None):
    event.withdraw()
    event.destroy()

    global playerNames
    title = "Toss Decided"
    head_Player = ""
    tail_Player = ""

    if par == 1:
        if pName == player_Names[0]:
            head_Player = player_Names[0]
            tail_Player = player_Names[1]
            message_box.showinfo(title, player_Names[1] + " will play for Tail")
        else:
            tail_Player = player_Names[0]
            head_Player = player_Names[1]
            message_box.showinfo(title, player_Names[0] + " will play for Tail")
    else:
        if pName == player_Names[0]:
            tail_Player = player_Names[0]
            head_Player = player_Names[1]
            message_box.showinfo(title, player_Names[1] + " will play for Head")
        else:
            tail_Player = player_Names[1]
            head_Player = player_Names[0]
            message_box.showinfo(title, player_Names[0] + " will play for Head")

    dice_Game_Code(head_Player, tail_Player, ftypeuno)


def tossWindow(ftypeuno):
    master = Tk()
    master.title("Toss")
    master.geometry("450x350")

    global playerNames

    player_id = randint(1, 2)

    if player_id is 1:
        pName = playerNames[0]
    else:
        pName = playerNames[1]

    msg = "Welcome to Toss Round !!\n"

    tossLabel_1 = Label(master, text=msg, width=20)
    tossLabel_1.place(relx=0.5, rely=0.1, anchor="center")
    tossLabel_1.config(bg="black", fg="white", font=ftypeuno)

    tossLabel_2 = Label(master, text=pName, width=20, height=2)
    tossLabel_2.place(relx=0.5, rely=0.2, anchor="center")
    tossLabel_2.config(bg="#0e73a2", fg="white", font=ftypeuno)

    tossLabel_3 = Label(master, text="\nwill turn the Choice", width=20)
    tossLabel_3.place(relx=0.5, rely=0.3, anchor="center")
    tossLabel_3.config(bg="black", fg="white", font=ftypeuno)

    headimg = Image.open("head.jpg")
    tailimg = Image.open("tail.jpg")

    headimg = headimg.resize((90, 90), Image.ANTIALIAS)

    tailimg = tailimg.resize((90, 90), Image.ANTIALIAS)

    headPhoto = ImageTk.PhotoImage(headimg, master=master)
    tailPhoto = ImageTk.PhotoImage(tailimg, master=master)

    headButton = Button(master, image=headPhoto, command=lambda: toss_Button_Action(master, ftypeuno, pName, 1))
    headButton.place(relx=0.35, rely=0.6, anchor="center")

    taileButton = Button(master, image=tailPhoto, command=lambda: toss_Button_Action(master, ftypeuno, pName, 2))
    taileButton.place(relx=0.65, rely=0.6, anchor="center")

    headLabel = Label(master, text="Head", font=ftypeuno)
    headLabel.place(relx=0.35, rely=0.8, anchor="center")

    tailLabel = Label(master, text="Tail", font=ftypeuno)
    tailLabel.place(relx=0.65, rely=0.8, anchor="center")

    master.resizable(False, False)
    master.mainloop()


def playerTwo(master, ftypeuno):
    global secondPlayerName, playerNames

    dis_Appear_Main_Window(master)

    player2 = Tk()
    player2.title("Second Player")
    player2.geometry("450x350")

    nameLabel = Label(player2, text="Enter Player 2 name", font=ftypeuno, bg="yellow")
    nameLabel.place(relx=0.5, rely=0.3, anchor="center")

    secondPlayerName = Entry(player2, font=ftypeuno, fg="blue")
    secondPlayerName.place(relx=0.5, rely=0.4, anchor="center")

    nameButton = Button(player2, text="get Registered", font=ftypeuno,
                        command=lambda: greetingsToPlayer(player2, secondPlayerName.get(), secondPlayerName, ftypeuno,
                                                          2, 2))
    nameButton.place(relx=0.5, rely=0.5, anchor="center")
    nameButton.config(bg="#0e73a2", fg="white")

    player2.resizable(False, False)
    player2.mainloop()


def greetingsToPlayer(master, theName, event, ftypeuno, flag, id):
    event.delete(0, END)

    global playerNames

    playerName = theName
    playerNumber = str(flag)

    pNameLen = len(playerName)

    if (pNameLen > 1 and (
            (playerName[0] >= 'a' and playerName[0] <= 'z') or (playerName[0] >= 'A' and playerName[0] <= 'Z'))):
        if (len(playerNames) >= 1 and playerNames[0] == playerName):
            messagebox.showerror("Name Error", "Player name should be different")
            if (id == 1):
                playerOne(master, ftypeuno)
            else:
                playerTwo(master, ftypeuno)
        else:
            playerNames.append(playerName)

            greetings_Message = "Welcome!!\n" + playerName + "\nYou will play as player " + playerNumber + " on this " \
                                                                                                           "Dice game\nGood luck!!!"

            dis_Appear_Main_Window(master)

            messagebox.showinfo("Greetings", greetings_Message)

            if (flag == 1):
                playerTwo(master, ftypeuno)
            if (flag == 2):
                tossWindow(ftypeuno)
    else:
        messagebox.showerror("Name Error", "Player should be a valid name")
        if (id == 1):
            playerOne(master, ftypeuno)
        else:
            playerTwo(master, ftypeuno)


def playerOne(master, ftypeuno):
    dis_Appear_Main_Window(master)

    global firstPlayerName, playerNames

    player1 = Tk()
    player1.title("First Player")
    player1.geometry("450x350")

    nameLabel = Label(player1, text="Enter Player 1 name", font=ftypeuno, bg="yellow")
    nameLabel.place(relx=0.5, rely=0.3, anchor="center")

    firstPlayerName = Entry(player1, font=ftypeuno, fg="blue")
    firstPlayerName.place(relx=0.5, rely=0.4, anchor="center")

    nameButton = Button(player1, text="get Registered", font=ftypeuno,
                        command=lambda: greetingsToPlayer(player1, firstPlayerName.get(), firstPlayerName, ftypeuno, 1,
                                                          1))
    nameButton.place(relx=0.5, rely=0.5, anchor="center")
    nameButton.config(bg="#0e73a2", fg="white")

    player1.resizable(False, False)
    player1.mainloop()


def main():
    main_Window = Tk()
    main_Window.title("Dice Game")
    main_Window.geometry("450x350")

    ftypeun = "arial 10 bold underline"
    ftypeuno = "arial 10 bold"

    welcome_Message_Label = Label(main_Window, text="Welcome to my Dice Game", font=ftypeuno, bg="yellow", fg="blue")
    welcome_Message_Label.place(relx=0.5, rely=0.3, anchor="center")

    start_Button = Button(main_Window, text="Let's start the game", font=ftypeuno, width=20, height=2, fg="green"
                          , command=lambda: playerOne(main_Window, ftypeuno))
    start_Button.place(relx=0.5, rely=0.5, anchor="center")
    start_Button.config(bg="#0e73a2", fg="white")

    main_Window.resizable(False, False)
    main_Window.mainloop()


main()

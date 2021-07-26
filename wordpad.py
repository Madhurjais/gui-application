from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tmsg
from PIL import Image, ImageTk
import pyttsx3
import speech_recognition as sr
from tkinter import font, colorchooser,filedialog
import os



root = Tk()
root.geometry("1200x800")
root.title("Madpad")
# root.wm_iconbitmap("lulogo.png")


# main menu 
# end main menu
file_icon = PhotoImage(file = "icon/new.png")
open_icon = PhotoImage(file = "icon/open.png")
save_icon = PhotoImage(file = "icon/save.png")
saveas_icon = PhotoImage(file = "icon/save_as.png")
exit_icon = PhotoImage(file = "icon/exit.png")

copy_icon = PhotoImage(file = "icon/copy.png")
cut_icon = PhotoImage(file = "icon/cut.png")
paste_icon = PhotoImage(file = "icon/paste.png")
clear_icon = PhotoImage(file = "icon/clear_all.png")
find_icon = PhotoImage(file = "icon/find.png")

toolbar_icon = PhotoImage(file = "icon/tool_bar.png")
statusbar_icon = PhotoImage(file = "icon/status_bar.png")

lightdef_icon = PhotoImage(file = "icon/light_default.png")
lightplus_icon = PhotoImage(file = "icon/light_plus.png")
dark_icon = PhotoImage(file = "icon/dark.png")
red_icon = PhotoImage(file = "icon/red.png")
monokai_icon = PhotoImage(file = "icon/monokai.png")
nightblue_icon = PhotoImage(file = "icon/night_blue.png")

mainmenu = Menu(root)



# ************file***********
file = Menu(mainmenu, tearoff = 0)
edit = Menu(mainmenu, tearoff = 0)
view  = Menu(mainmenu, tearoff = 0)
color = Menu(mainmenu, tearoff = 0)

# **************color theme ***********
themechoice = StringVar()
color_icon = [lightdef_icon,lightplus_icon,dark_icon,red_icon,monokai_icon,nightblue_icon]
color_dict = {
    "light_def":("#000000,#ffffff"),
    "light-plus":("#474747","#e0e0e0"),
    "Dark":("#c4c4c4","#2d2d2d"),
    "Red":("#2d2d2d","#ffe8e8"),
    "monokai":("#d3b774","#474747"),
    "Night Blue":("#ededed","#6b9dc2")
}


mainmenu.add_cascade(label = "file",menu = file)
mainmenu.add_cascade(label = "edit",menu = edit)
mainmenu.add_cascade(label = "view",menu = view)
mainmenu.add_cascade(label = "color",menu = color)


# tool bar
toolbar = Label(root)
toolbar.pack(fill = X, side = TOP)
font_list = font.families()
font_family = StringVar()
font_box = ttk.Combobox(toolbar,width = 30,textvariable = font_family,state = 'readonly')
font_box['values'] = font_list
font_box.current(font_list.index('Arial'))
font_box.grid(row = 0, column = 0,padx = 10)

fontsize_var = IntVar()
font_value = tuple(range(10,80,2))
font_size = ttk.Combobox(toolbar,width = 15,textvariable = fontsize_var,state = 'readonly')
font_size['values'] = font_value 
font_size.current(2)
font_size.grid(row = 0, column = 1, padx = 10)

# ****bold Button*****
bold_icon = PhotoImage(file = 'icon/bold.png')
boldbtn = Button(toolbar,height = 20,image = bold_icon)
boldbtn.grid(row =0 ,column = 2,ipadx = 3) 

# *****italic button ******
italic_icon = PhotoImage(file = "icon/italic.png")
italicbtn = Button(toolbar,image = italic_icon,height =20,padx = 20)
italicbtn.grid(row = 0, column = 3,padx =5)
# *****underline*******
underline_icon = PhotoImage(file = "icon/underline1.png")
underline_btn = Button(toolbar,image = underline_icon)
underline_btn.grid(row =0 , column = 4,padx = 5)
# *****font color btn******
fontclr_icon = PhotoImage(file ="icon/fontclr1.png")
fontclr_btn = Button(toolbar,image =fontclr_icon)
fontclr_btn.grid(row = 0, column =5,padx =5)

# *****left alignment *******
alignleft_icon = PhotoImage(file = "icon/leftalign1.png")
left_btn = Button(toolbar , image = alignleft_icon, height = 20, width = 20)
left_btn.grid(row =0 ,column = 6, padx = 5)

right_icon = PhotoImage(file = "icon/rightalign1.png")
right_btn = Button(toolbar, image = right_icon)
right_btn.grid(row = 0, column = 7, padx = 5)

center_icon = PhotoImage(file = "icon/center.png")
center_btn = Button(toolbar, image = center_icon)
center_btn.grid(row = 0, column = 8, padx = 5)

overstrike_icon = PhotoImage(file = "icon/strike.png")
strike_btn = Button(toolbar,image = overstrike_icon)
strike_btn.grid(row = 0, column = 9, padx = 5)

reading_icon = PhotoImage(file = 'icon/speech.png')
reading_btn = Button(toolbar ,image = reading_icon)
reading_btn.grid(row = 0, column = 10, padx = 5)

voice_icon = PhotoImage(file = "icon/voice.png")
voice_btn = Button(toolbar, image = voice_icon)
voice_btn.grid(row = 0, column = 11, padx = 5)
# end tool bar


# text editor 

text_editor = Text(root)
text_editor.config(wrap = "word",relief =FLAT)
text_editor.focus_set()

Scrollbar = Scrollbar(root)
Scrollbar.pack(fill = Y,side = RIGHT)
text_editor.pack(fill = BOTH,expand = True)

Scrollbar.config(command =text_editor.yview)
text_editor.config(yscrollcommand = Scrollbar.set)

# ***font family and font size 
current_font_family = "Arial"
current_font_size = 12

def change_font(root):
    global current_font_family
    
    current_font_family = font_family.get()
    text_editor.configure(font = (current_font_family,current_font_size))

font_box.bind("<<ComboboxSelected>>",change_font)

def change_size(root):
    global current_font_size
    current_font_size = fontsize_var.get()
    text_editor.configure(font =(current_font_family,current_font_size))
font_size.bind("<<ComboboxSelected>>",change_size)
# ***button functionality*****
def boldb():
    bold_btn = font.Font(font = text_editor['font']).actual()  
    if bold_btn['weight'] == "normal" :
        text_editor.configure(font = (current_font_family,current_font_size,"bold"))
    if bold_btn['weight'] == "bold" :
        text_editor.configure(font = (current_font_family,current_font_size,"normal"))
boldbtn.configure(command = boldb)
  

def change_italic():
        italic_btn = font.Font(font = text_editor['font']).actual()
        if italic_btn['slant'] == "roman" :
            text_editor.configure(font = (current_font_family,current_font_size,"italic"))
        if italic_btn['slant'] == "italic" :
            text_editor.configure(font = (current_font_family,current_font_size,"roman"))
italicbtn.configure(command = change_italic)  

def underline():
    italic_btn = font.Font(font = text_editor['font']).actual()
    if italic_btn['underline'] == 0 :
        text_editor.configure(font = (current_font_family,current_font_size,'underline'))
    if italic_btn['underline'] == 1 :
        text_editor.configure(font = (current_font_family,current_font_size,'normal'))
underline_btn.configure(command = underline) 

def overstrike():
    over_btn = font.Font(font = text_editor['font']).actual()
    if over_btn['overstrike'] == 0 :
        text_editor.configure(font = (current_font_family,current_font_size,'overstrike'))
    if over_btn['overstrike'] == 1 :
        text_editor.configure(font = (current_font_family,current_font_size,'normal'))
strike_btn.configure(command = overstrike) 

def change_color():
    color_var = colorchooser.askcolor()
    text_editor.configure(fg = color_var[1])
fontclr_btn.configure(command = change_color)

def change_left():
    text = text_editor.get(1.0,END)
    text_editor.tag_config(LEFT,justify = LEFT)
    text_editor.delete(1.0,END)
    text_editor.insert(INSERT,text,LEFT)
left_btn.configure(command = change_left)
def change_right():
    text = text_editor.get(1.0,END)
    text_editor.tag_config(RIGHT,justify = RIGHT)
    text_editor.delete(1.0,END)
    text_editor.insert(INSERT,text,RIGHT)
right_btn.configure(command = change_right)
def change_center():
    text = text_editor.get(1.0,END)
    text_editor.tag_config(CENTER,justify = CENTER)
    text_editor.delete(1.0,END)
    text_editor.insert(INSERT,text,CENTER)
center_btn.configure(command = change_center)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak():
    audio = text_editor.get(1.0,END)
    engine.say(audio)
    engine.runAndWait()
reading_btn.configure(command = speak)

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # listen = "listening..."
        # text_editor.tag_config(listen)
        # text_editor.pack()
        r.pause_threshold = 1
        audio = r.listen(source)
        query = r.recognize_google(audio,language = "eng-in")
        # text_editor.insert(INSERT,query)
        # text_editor.pack()
    return text_editor.config(text= str(query))



    # try:
    #     recognize = "recognising.."
    #     text_editor.insert(INSERT,recognize)
    #     query = str(r.recognize_google(audio,language = "eng-in"))
    #     text_editor.insert(INSERT,query)
    #     text_editor.pack()

    # except :
    #     # print(e)
    #     # print("say again please...")
    #     repeat = "please say again.."
    #     text_editor.insert(INSERT,repeat)
        
    #     return "none"
    # return text_editor.insert(INSERT,query)
        
    
voice_btn.configure(command = takecommand)
text_editor.configure(font = ("Arial,12"))
# end of text editor
# status bar 
statusbar = Label(root,text = "status bar")
statusbar.pack(side = BOTTOM, fill = X)

text_changed = False
def status(event = None):
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0,"end-1c").split())
        character = len(text_editor.get(1.0,"end-1c"))
        statusbar.config(text =f"characters :{character},Words : {words}")
    text_editor.edit_modified(False)
text_editor.bind("<<Modified>>",status)

# end of status bar 
# main menu functionality

# *****new******
url = ''
def newfile(event = None):
    global url
    url = ''
    text_editor.delete(1.0,END)
file.add_command(label = "new",image = file_icon,compound = LEFT, accelerator ="Cntr + N",command = newfile)

def openfile(event = None):
    global url
    url = filedialog.askopenfilename(initialdir =os.getcwd(),title = "file name",filetype = (('text file','*.txt'),('text file','*.pdf'),('all file',"*.*")))
    try:
        with open(url,"r") as fr:
            text_editor.delete(1.0,END)
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return
    except:
        return
    root.title(os.path.basename(url))

def savefile(event = None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0,END))
            with open(url, "a",encoding="utf-8") as fw:
                
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode = W,defaultextension = ".txt", filetype = (('text file','*.txt'),('text file','*.pdf'),('All file',"*.*")))
            content2 = text_editor.get(1.0,END)
            url.write(content2)
            url.close()
    except:
        return
    root.title(os.path.basename(url))

def saveasfile(event = None):
    global url
    try:
        content = text_editor.get(1.0,END)
        url = filedialog.asksaveasfile(mode = W,defaultextension = ".txt", filetype = (('text file','*.txt'),('text file','*.pdf'),('All file',"*.*")))
        url.write(content)
        url.close()
    except:
        return

def exitfunc():
    global url, text_changed
    try:
        if text_changed:
            mbox = tmsg.askyesnocancel('Warning','do you what to save the file')
            if mbox is True:
                if url:
                    content = str(text_editor.get(1.0,END))
                    with open(url, 'a', encoding="utf-8") as fw:
                        fw.write(content)
                        root.destroy()
                else:
                    content2 = str(text_editor.get(1.0,END))
                    url = filedialog.asksaveasfile(mode = W,defaultextension = ".txt", filetype = (('text file','*.txt'),('text file','*.pdf'),('All file',"*.*")))
                    url.write(content2)
                    url.close()
                    root.destroy()
            elif mbox is False:
                root.destroy()
        else:
            root.destroy()
    except:
        return
# find functionality
def find_func(event = None):
    def findfunc():
        word = find_input.get()
        text_editor.tag_remove('match','1.0',END)
        matches = 0
        if word:
            start_pos ='1.0'
            while True:
                start_pos = text_editor.search(word,start_pos,stopindex = END)
                if not start_pos :
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground = 'red',background = 'yellow')
    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, END)
        new_content =  content.replace(word, replace_text) 
        text_editor.delete(1.0,END)
        text_editor.insert(1.0,new_content)
    find = Toplevel()
    find.geometry("450x250+500+200")
    find.title("find")
    find.resizable(0,0)

    find_frame = LabelFrame(find,text = "find/replace")
    find_frame.pack(pady = 20)

    text_find = Label(find_frame,text = "find ")
    text_replace = ttk.Label(find_frame, text = "replace :")
    
    find_input = Entry(find_frame,width = 20)
    replace_input = Entry(find_frame, width = 20)
    find_btn = Button(find_frame,text ="find",width = 8,command = findfunc)
    replace_btn = Button(find_frame, text = "replace",width =8,command = replace)

    text_find.grid(row = 0, column =0 ,padx = 4, pady = 4)
    text_replace.grid(row = 1, column =0 ,padx = 4, pady = 4)
    find_input.grid(row = 0, column = 1, padx = 4, pady = 4)
    replace_input.grid(row = 1, column = 1, padx = 4, pady = 4)
    
    find_btn.grid(row = 2, column = 1, padx = 3, pady = 8)
    replace_btn.grid(row = 2, column = 2, padx = 2, pady = 8)
    find.mainloop()


edit.add_command(label = "find",image = find_icon, compound = LEFT, accelerator = "Cntr + F",command = find_func)

file.add_command(label = "open",image = open_icon ,compound = LEFT,accelerator = "Cntr + O",command = openfile)
file.add_command(label = "save",image = save_icon ,compound = LEFT,accelerator = "Cntr + S",command = savefile)
file.add_command(label = "save as",image = saveas_icon,compound = LEFT,accelerator = "Cntr + alt-s",command = saveasfile)
file.add_command(label = "exit",image = exit_icon,compound = LEFT, accelerator = "Cntr + X",command = exitfunc)
# *************edit************
edit.add_command(label = "copy",image = copy_icon, compound = LEFT, accelerator = "Cntr + C",command = lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label = "cut",image = cut_icon, compound = LEFT, accelerator = "Cntr + X",command = lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label = "paste",image = paste_icon, compound = LEFT, accelerator = "Cntr + V",command = lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label = "clear all",image = clear_icon, compound = LEFT, accelerator = "Cntr + T",command = lambda:text_editor.delete(1.0,END))






# **********view***********
show_toolbar = BooleanVar()
show_toolbar.set(True)
show_statusbar = BooleanVar()
show_statusbar.set(True)
def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        toolbar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        statusbar.pack_forget()
        toolbar.pack(side = TOP, fill = X)
        text_editor.pack(fill = BOTH,expand = True)
        statusbar.pack(side = BOTTOM)
        show_toolbar = True
def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        statusbar.pack_forget()
        show_statusbar = False
    else:
        statusbar.pack(side = BOTTOM, fill = X)
        show_statusbar = True
view.add_checkbutton(label = "tool bar",onvalue = True,offvalue = 0,variable = show_toolbar, image = toolbar_icon, compound = LEFT,command = hide_toolbar)
view.add_checkbutton(label = "status bar",onvalue = 1, offvalue =False,variable = show_statusbar,  image = statusbar_icon, compound = LEFT,command = hide_statusbar)

def change_theme():
    choose_theme = themechoice.get()
    color_tuple = color_dict.get(choose_theme)
    fg_color, bg_color = color_tuple[0],color_tuple[1]
    text_editor.config(background = bg_color,foreground = fg_color)
temp = 0
for i in color_dict:
    color.add_radiobutton(label = i,image = color_icon[temp], variable = themechoice,compound = LEFT,command =change_theme)
    temp += 1

root.config(menu = mainmenu)
# end main menu functionality
root.bind("<Control-n>",newfile)
root.bind("<Control-o>",openfile)
root.bind("<Control-s>",savefile)
root.bind("<Control-v>",saveasfile)
root.bind("<Control-q>",exitfunc)
root.bind("<Control-f>",find_func)


root.mainloop()
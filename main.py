import tkinter as tk
import os
import shutil
import os.path
from tkinter.filedialog import askdirectory, askopenfile, askopenfilename
import voice_assistant



# Information to ask when installing app for first time 
# - C://Desktop Assistant/music_folder_location.txt
# C://Desktop Assistant/app_exe_locations.txt
if os.path.isdir(r'C://Desktop Assistant'):
    shutil.rmtree(r'C://Desktop Assistant', ignore_errors=True)

if not os.path.isdir(r'C://Desktop Assistant'):
    os.mkdir(r"C://Desktop Assistant")

    # Muisc part
    window=tk.Tk()
    window.title('Music folder location info')

    window.rowconfigure(list(range(3)),minsize=40,weight=1)
    window.columnconfigure(list(range(1)),minsize=100,weight=1)
    def open_folder():
        folder_name=askdirectory()
        lbl_flr_name['text']=f"You selected {folder_name}"
        with open(r'C://Desktop Assistant/music_folder_location.txt','w') as f:
            f.write(folder_name)

    lbl_info=tk.Label(master=window,text='Please select folder location of music files.')
    btn_open=tk.Button(master=window,text='Open',command=open_folder)
    lbl_flr_name=tk.Label(master=window,text='Selected folder will be displayed here.')

    lbl_info.grid(row=0,column=0,padx=5,pady=5)
    btn_open.grid(row=1,column=0,padx=5,pady=5)
    lbl_flr_name.grid(row=2,column=0,padx=5,pady=5)

    height=300
    width=400
    window.geometry(f'{width}x{height}')
    window.mainloop()

    # Applications part
    window=tk.Tk()
    window.title('App exes location info')

    window.rowconfigure(list(range(3)),minsize=40,weight=1)
    window.columnconfigure(list(range(1)),minsize=100,weight=1)
    def open_file():
        file_name=askopenfilename()
        if not lbl_file_names['text']:
            lbl_file_names['text']=file_name
        else:
            lbl_file_names['text']+=f"\n{file_name}"
        
        lbl_file_names['text']=f"You selected {file_name}"
        mode = 'r+' if os.path.exists(r'C://Desktop Assistant/app_exe_locations.txt') else 'w'
        with open(r'C://Desktop Assistant/app_exe_locations.txt',mode) as f:
            if mode=='w':
                write_text=file_name
            if mode=='r+':
                lines=f.readlines()
                lines=[line.strip() for line in lines]
                if file_name in lines:
                    write_text=''
                else:
                    write_text='\n'+write_text
            f.write(write_text)

    lbl_info=tk.Label(master=window,text='Please select file locations of app executables.')
    btn_open=tk.Button(master=window,text='Open',command=open_file)
    lbl_file_names=tk.Label(master=window,text='Selected files will be displayed here.')

    lbl_info.grid(row=0,column=0,padx=5,pady=5)
    btn_open.grid(row=1,column=0,padx=5,pady=5)
    lbl_file_names.grid(row=2,column=0,padx=5,pady=5)

    height=300
    width=400
    window.geometry(f'{width}x{height}')
    window.mainloop()

window=tk.Tk()
window.title('Desktop Assistant')

# configuring main window cells properties
window.rowconfigure(0,minsize=100,weight=1)
window.columnconfigure(0,minsize=200,weight=1)

# configuring buttons frame cells properties
btns_frame=tk.Frame(master=window,relief=tk.RAISED, bd=3)
btns_frame.rowconfigure(0,weight=1)
btns_frame.columnconfigure(list(range(3)),weight=1)

# Adding buttons
btn_voice_ass = tk.Button(master=btns_frame,text='Voice Assistant 🎤',command= voice_assistant.clickVoiceAssistantButton)
btn_open_apps=tk.Button(master=btns_frame,text='Open Applications',command= voice_assistant.clickOpenApplicationsButton)
btn_music_player=tk.Button(master=btns_frame,text='Play music',command= voice_assistant.clickMusicPlayerButton)

# Placing buttons
btn_voice_ass.grid(row=0,column=0)
btn_open_apps.grid(row=0,column=1)
btn_music_player.grid(row=0,column=2)
# Placing frame
btns_frame.grid(row=0, column=0,sticky='nsew')

# starting mainloop
height=300
width=400
window.geometry(f'{width}x{height}')
window.mainloop()
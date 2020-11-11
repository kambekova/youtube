from tkinter import*
from pytube import YouTube # YouTube - тан видео жүктеу программасы

root = Tk()
root.geometry('500x300') # ширина х высота окна
root. resizable(0, 0)    # нельзя изменить размер окна
root.title("качать с youtube")

Label(root, text='Скачать с youtube', font='arial 20 bold'). pack() # терезеге мәтін енгізу ұяшығын жасау
Label(root, text='Вставьте ссылку:', font='arial 15 bold'). place(x=160, y=80) # Вставьте ссылку батырмасын қосу

Label(root, text='Автор Камбекова А.А.', font='arial 15 bold'). place(x=80, y=40) # Вставьте ссылку батырмасын қосу

link = StringVar()
link_enter = Entry(root, width=60, textvariable=link).place(x=32, y=120)

def Downloader():
	print(link.get())
	url = YouTube(str(link.get()))
	video = url.streams.first() 
	video.download()
	Label(root, text='Скачивание завершено!', font='arial 15').place(x=180, y=210)

Button(root, text='Скачать', font='arial 15 bold', bg='red', fg='white', command=Downloader).place(x=200, y=170)	
root.mainloop()


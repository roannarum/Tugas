from tkinter import*
from tkinter import messagebox
# Frame pertama lobby
class StartPage(Frame):
	def __init__(self,parent,lobby):
		Frame.__init__(self,parent)
		self.lobby=lobby
		
		self.lobby.title('Elearning UNIVERSITAS INDOHARVARD')
		self.lobby.state('zoomed')

		self.frame_awal=Label(self, bg='coral',width=200,height=5)                                                             
		self.frame_awal.pack()
		self.judul = Label(self,text='\n\t\tUNIVERSITAS INDOHARVARD\n \t\tJaya Menggelora\n',font=('times new roman',14,'bold'),bg='coral')
		self.judul.place(x=100,y=0)
		self.label_awal3=Label(self, bg='orangered',width=200,height=2)
		self.label_awal3.pack()
		
		
		self.home=Button(self, text='Home',relief=GROOVE,font=('times new roman',12,'bold'),bg='coral', bd=1,)
		self.home.place(x=1080,y=40)

		self.home=Button(self, text='Login',command = lambda : lobby.show_frame(PageLogin),font=('times new roman',12,'bold'),bg='coral', bd=1,)
		self.home.place(x=1180,y=40)
		
		self.filname=PhotoImage(file='9.gif') 
		self.bc=Label(self,image=self.filname).pack(side=LEFT)
		

		self.labelinf1=LabelFrame(self,bg='white',width=260,height=225,).place(x=1010,y=125)
		self.labelinf1=Label(self,font=('segoe ui semibold',12), bg = "white",
			text='Selamat Datang di E-learning\n UNIVERSITAS INDOHARVAD\n Jaya Menggelora\n\n Silahkan Login untuk\nperkuliahan')
		self.labelinf1.pack(pady=50,padx=0)
		self.canvaslog2=Frame(self,width=260,height=288).place(x=1010,y=400)

		self.lanjudlog=LabelFrame(self,text='  Login  ',font =("times new roman", 16),width=260,height=280).place(x=1010,y=380)
		self.laser=Label(self,text='Username', font = ("times new roman", 14))
		self.laser.place(x=1030,y=430)
		self.lapas=Label(self,  text='Password', font = ("times new roman", 14))
		self.lapas.place(x=1030,y=500)

		self.enser=Entry(self, width = 30, bg = "gainsboro")
		self.enser.place(x=1030,y=460)

		self.enpas=Entry(self, width = 30, bg = "gainsboro")
		self.enpas.place(x=1030,y=530)

		self.checkbutton=Checkbutton(self, text='remember me')
		self.checkbutton.place(x=1030,y=570)

		self.home2=Button(self,text='Login',bg='tomato',width = 10,command = lambda : lobby.show_frame(PageLogin1)).place(x=1170,y=600)

class HalamanCourses(Frame):
	def __init__(self,parent,lobby):
		Frame.__init__(self,parent)
		self.lobby=lobby
		self.frame_awal=Label(self, bg='coral',width=200,height=5)                                                             
		self.frame_awal.pack()
		self.judul=Label(self,text='\n\t\tUNIVERSITAS INDOHARVARD\n \t\tJaya Menggelora\n',font=('times new roman',14,'bold'),bg='coral')
		self.judul.place(x=100,y=0)
		self.label_awal3=Label(self, bg='orangered',width=200,height=2)
		self.label_awal3.pack()

		self.home=Button(self, text='Home',command = lambda : lobby.show_frame(StartPage),font=('times new roman',12,'bold'),bg='coral', bd=1,)
		self.home.place(x=1080,y=40)

		self.home=Button(self, text='Login',command = lambda : lobby.show_frame(PageLogin),font=('times new roman',12,'bold'),bg='coral', bd=1,)
		self.home.place(x=1180,y=40)

		self.filname=PhotoImage(file='12345.gif')
		self.bc=Label(self,image=self.filname).pack(side=TOP)
		self.lf = Frame(self, bg = "white", relief=GROOVE, bd =5,width=1000,height=515).place(x = 150, y = 135)
		self.var1 = IntVar()
		self.var2 = IntVar()
		self.var3 = IntVar()
		self.var4 = IntVar()
		self.var5 = IntVar()
		self.var6 = IntVar()
		

		self.labeldafcos=Label(self, text='DAFTAR MATA KULIAH',font =("arial", 14, "bold"), bg = "white")
		self.labeldafcos.place(x=550,y=160)
		self.mk1 = Checkbutton(self, text = "Manajemen dan Organisasi Bisnis ", fg = "forestgreen", bg = "white", font =("segoe ui", 14, "bold"),
			variable = self.var1).place(x=200,y=220)
		self.mk2 = Checkbutton(self, text = "Pemprograman Orientasi Objek",fg = "forestgreen", bg = "white",font =("segoe ui", 14, "bold"), 
			variable = self.var2).place(x=200 ,y=295)
		self.mk3 = Checkbutton(self, text = "Ilmu Dasar Keperawatan", fg = "forestgreen", bg = "white", font =("segoe ui", 14, "bold"), 
			variable = self.var3).place(x=200,y=370)
		self.mk4 = Checkbutton(self, text = "Kalkulus", fg = "forestgreen", bg = "white", font =("segoe ui", 14, "bold"), 
			variable = self.var4).place(x=200,y=445)
		self.mk5 = Checkbutton(self, text = "Teori Probabilitas", fg = "forestgreen", bg = "white", font =("segoe ui", 14, "bold"), 
			variable = self.var5).place(x=200,y=520)


		ket1 = Label(self, text ="Mata kuliah ini diselenggarakan untuk Prodi Manajemen", 
			bg = "white",font =("segoe ui",12)).place(x= 250, y =255)
		ket2 = Label(self, text ="Mata kuliah ini diselenggarakan untuk Prodi Sistem Informasi",
			bg = "white",font =("segoe ui",12)).place(x= 250, y =330)
		ket3 = Label(self, text ="Mata kuliah ini diselenggarakan untuk Prodi Keperawatan", 
			bg = "white",font =("segoe ui",12)).place(x= 250, y =405)
		ket4 = Label(self, text ="Mata kuliah ini diselenggarakan untuk Prodi Teknik Informatika", 
			bg = "white",font =("segoe ui",12)).place(x= 250, y =480)
		ket5 = Label(self, text ="Mata kuliah ini diselenggarakan untuk Prodi Teknik Industri", 
			bg = "white",font =("segoe ui",12)).place(x= 250, y =555)
	
		self.zsdf = Button(self, text = "Selesai", bg ="mediumseagreen", command = self.get, width =10).place(x=900,y=600)

		self.keluar = Button(self, text = "Keluar", bg = "crimson", command =self.quit, width = 10).place(x = 300, y = 600)

	def get(self):
		if self.var1.get() == 1:
			messagebox.showinfo("","Terimakasih Data telah disimpan")
		elif self.var2.get() == 1:
			messagebox.showinfo("","Terimakasih data telah disimpan")
		elif self.var3.get() == 1:
			messagebox.showinfo("","Terimakasih data telah disimpan")
		elif self.var4.get() == 1:
			messagebox.showinfo("","Terimakasih data telah disimpan")
		elif self.var5.get() == 1:
			messagebox.showinfo("","Terimakasih data telah disimpan")
		elif self.var6.get() == 1:
			messagebox.showinfo("","Terimakasih data telah disimpan")
		else :
			messagebox.showwarning("","Silahkan Pilih Mata Kuliah")

		
class PageLogin(Frame):
	def __init__(self,parent,lobby):
		Frame.__init__(self,parent)
		self.lobby=lobby

		self.frame_awal=Label(self, bg='coral',width=200,height=5)                                                             
		self.frame_awal.pack()
		self.judul=Label(self,text='\n\t\tUNIVERSITAS INDOHARVAD\n \t\tJaya Menggelora\n',font=('times new roman',14 ,'bold'),bg='coral')
		self.judul.place(x=100,y=0)
		self.label_awal3=Label(self, bg='orangered',width=200,height=2)
		self.label_awal3.pack()

		self.home=Button(self, text='Home',command = lambda : lobby.show_frame(StartPage),font=('times new roman',12,'bold'),bg='coral', bd=1,)
		self.home.place(x=1080,y=40)

		self.home=Button(self, text='Login',relief=SUNKEN,font=('times new roman',12,'bold'),bg='coral', bd=1,)
		self.home.place(x=1180,y=40)

		self.filname=PhotoImage(file='20.gif')
		self.bc=Label(self,image=self.filname).pack(side=LEFT)
		
		
		self.logfrm=Frame(self, bg='tan',relief=SUNKEN,bd=10,width=520,height=300).place(x=400,y=220)
		self.Label_logfrm=Label(self,text='Login your account', bg = "tan",font=('arial',12,'bold')).place(x=450,y=250)

		self.laser=Label(self,text='Username' , bg = "tan", font = ("arial",12))
		self.laser.place(x=480,y=320)

		self.lapas=Label(self,  text='Password', bg = "tan", font = ("arial",12))
		self.lapas.place(x=720,y=320)

		self.enser=Entry(self, bg = "darkkhaki" )
		self.enser.place(x=480,y=350)

		self.enpas=Entry(self, bg = "darkkhaki" )
		self.enpas.place(x=720,y=350)

		self.checkbutton=Checkbutton(self, text='remember me', bg = "tan")
		self.checkbutton.place(x=480,y=380)

		self.home2=Button(self,text='Login',bg='burlywood', font = ( "arial",11), command = lambda : lobby.show_frame(PageLogin1)).place(x=650,y=450)
		
class PageLogin1(Frame):
	def __init__(self,parent,lobby):
		Frame.__init__(self,parent)
		self.lobby=lobby
		self.frame_awal=Label(self, bg='coral',width=200,height=5)                                                             
		self.frame_awal.pack()
		judul=Label(self,text='\n\t\tUNIVERSITAS INDOHARVARD\n \t\tJaya Menggelora\n',font=('times new roman',14,'bold'),bg='coral')
		judul.place(x=100,y=0)
		self.label_awal3=Label(self, bg='orangered',width=200,height=2)
		self.label_awal3.pack()

		self.home=Button(self, text='Home',command = lambda : lobby.show_frame(StartPage),font=('times new roman',12,'bold'),bg='coral', bd=1,)
		self.home.place(x=1080,y=40)

		self.home=Button(self, text='Login',relief=SUNKEN,font=('times new roman',12,'bold'),bg='coral', bd=1,)
		self.home.place(x=1180,y=40)

		self.filname=PhotoImage(file='14.gif') 
		self.bc=Label(self,image=self.filname).pack(side=RIGHT)

		self.labdatdir=Label(self,text='Data Diri Mahasiswa', font = 14).place(x=580,y=160)
		self.labnam=Label(self,text='Nama Depan	:', font = 13).place(x=420,y=230)
		self.labnam2=Label(self,text='Nama Belakang	:', font = 13).place(x=420,y=270)
		self.labpro=Label(self,text='Program Studi	:', font = 13).place(x=420,y=310)
		self.labsem=Label(self,text='Semester		:', font = 13).place(x=420,y=350)
		self.labemai=Label(self,text='Email		:', font = 13).place(x =420,y=390)
		self.labemaipri=Label(self,text='indharvard@gmail.com',fg='darkred').place(x=670,y=425)

		self.entrnam=Entry(self)
		self.entrnam.place(x=670,y=230)
		self.entrnam2=Entry(self)
		self.entrnam2.place(x=670,y=270)
		self.entrpro=Entry(self)
		self.entrpro.place(x=670,y=310)
		self.entrsem=Entry(self)
		self.entrsem.place(x=670,y=350)
		self.entremai=Entry(self)
		self.entremai.place(x=670,y=390)

		self.Button=Button(self,text='Simpan', bg = "tomato",command = lambda : lobby.show_frame(HalamanCourses)).place(x=660,y=550)


class tkinterApp(Tk):
    def __init__(self, *args, **kwargs):  
        Tk.__init__(self, *args, **kwargs)
        
        container_awal =Frame(self) 
        container_awal.pack(side = TOP, fill = BOTH, expand = YES)
  
        container_awal.grid_rowconfigure(0, weight = 1)
        container_awal.grid_columnconfigure(0, weight = 1)
 
        self.frames = {}
        for F in (StartPage,HalamanCourses,PageLogin,PageLogin1):
            frame = F(container_awal,self)
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage) 
 
    def show_frame(self, contoh):
        frame = self.frames[contoh]
        frame.tkraise()

if __name__ == '__main__':
	app = tkinterApp()
	app.mainloop()

import tkinter as tk
from tkinter import *
import random
import time as tm

Signin=tk.Tk()
Signin.geometry("300x100")
Signin.title("M O F A 3 L N A W W Y")

name_default=""
pw_default = ""

name_var=tk.StringVar()
passw_var=tk.StringVar()

######################################-----Gauge Window Start-----##################################################

def OpenGaugeWindow():
	window_3=tk.Tk()
	def update_gauge():
		newvalue = random.randint(low_r,hi_r)
		cnvs.itemconfig(id_text,text = str(newvalue))
		# Rescale value to angle range (0%=120deg, 100%=30 deg)
		angle = 120 * (hi_r - newvalue)/(hi_r - low_r) + 30
		cnvs.itemconfig(id_needle,start = angle)
		window_3.after(1000, update_gauge)  
######################################-----Window start-----#######################################################
	
	
	canvas_width = 400
	canvas_height =300
	cnvs = Canvas(window_3, width=canvas_width, height=canvas_height)
	cnvs.grid(row=2, column=1)
 
	coord = 10, 50, 350, 350 #define the size of the gauge
	low_r = 350 # chart low range
	hi_r = 520 # chart hi range
 
	# Create a background arc with a number of range lines
	numpies = 8
	for i in range(numpies):
		cnvs.create_arc(coord, start=(i*(120/numpies) +30), extent=(120/numpies), fill="white",  width=1)    
 
	# add hi/low bands
	cnvs.create_arc(coord, start=30, extent=120, outline="green", style= "arc", width=40)
	cnvs.create_arc(coord, start=30, extent=20, outline="red", style= "arc", width=40)
	cnvs.create_arc(coord, start=50, extent=20, outline="yellow", style= "arc", width=40)
	# add needle/value pointer
	id_needle = cnvs.create_arc(coord, start= 119, extent=1, width=7)
 
	# Add some labels
	cnvs.create_text(180,15,font="Times 20 italic bold", text="Temperature")
	cnvs.create_text(25,140,font="Times 12 bold", text=low_r)
	cnvs.create_text(330,140,font="Times 12 bold", text=hi_r)
	id_text = cnvs.create_text(170,210,font="Times 15 bold")

	######################################-----Window end-----######################################################
	window_3.after(1000, update_gauge)

######################################-----Gauge Window End-----####################################################
######################################-----window_2 start------#####################################################
def OpenNewWindow():
	def update_humdity():
		HL=0
		HH=100
		Humidity = random.randint(HL,HH)
		Label2=Label(window_2,text=Humidity,bg='white')
		Label2.place(x=150,y=300)
		window_2.after(1000,update_humdity)

	window_2=tk.Tk()
	window_2.title("I N T E R F A C E")
	window_2.geometry("500x500")
	window_2.configure(bg='white')
	current_time=tm.strftime('%p')
	clock_label=tk.Label(window_2,text='Day: ',bd='10',bg='white')
	clock_label.place(x=50,y=200)
	if current_time == 'PM':
		DayLabel=tk.Label(window_2,text='Night',bg='white')
		DayLabel.place(x=100,y=210)
	else:
		DayLabel=tk.Label(window_2,text='Morning',bg='white')
		DayLabel.place(x=100,y=210)
	Temp_btn=tk.Button(window_2,text = 'View Temperature', command = OpenGaugeWindow)
	Temp_btn.place(x=50,y=100)
	mofal=PhotoImage(file='mofal.png')
	mofal=mofal.subsample(1,1)
	Label1=Label(window_2,image=mofal,bg='white').pack(side=RIGHT)
	Label3=Label(window_2,text='Humidity',bg='white')
	Label3.place(x=50,y=300)
	window_2.after(1000,update_humdity)
	window_2.mainloop()
############################################-Window_2 end##########################################################
thief_counter=0
def submit():
	global thief_counter
	name=name_var.get()
	password=passw_var.get()
	if thief_counter<2:
		if name==name_default and password==pw_default:
			Signin.destroy()
			OpenNewWindow()
		else:
			wrong_password()
			thief_counter+=1
	else:
		print("HARAAAAMYYYYY")



def wrong_password():
	wrong.grid(row=3,column=1)

######################################-----Functions end-----###################################################


######################################-----Signin start-----####################################################
name_label = tk.Label(Signin, text = 'Username', font=('calibre',10, 'bold'))

# creating a entry for input
# name using widget Entry
name_entry = tk.Entry(Signin,textvariable = name_var, font=('calibre',10,'normal'))
wrong = tk.Label(Signin, text = 'Wrong Username or Password', font=('calibre',10, 'bold'))
# creating a label for password
passw_label = tk.Label(Signin, text = 'Password', font = ('calibre',10,'bold'))
# creating a entry for password
passw_entry=tk.Entry(Signin, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
# creating a button using the widget
# Button that will call the submit function
sub_btn=tk.Button(Signin,text = 'Submit', command = submit)
# placing the label and entry in
# the required position using grid
# method
name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
passw_label.grid(row=1,column=0)
passw_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)

######################################-----Signin end-----###################################################

Signin.mainloop()
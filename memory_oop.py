from fltk import *
import random
from PIL import Image
import os,io
# use deactivate() on completed pairs
# 6x4 grid



class window(Fl_Window):
	def __init__(self,w,h,l):
		Fl_Window.__init__(self,w,h,l)
		self.begin()
		self.butlist = []
		x = 0
		I=[]
		fnames=os.listdir('marvel_pics')
		fnames=fnames+fnames
		random.shuffle(fnames)
		imgs=[]
		for fname in fnames:
			imgs.append(self.img_resize(f'./marvel_pics/{fname}',150))
			#imgs.append(Fl_PNG_Image(f'./marvel_pics/{fname}').copy(150,150))
		for row in range(6):
			for col in range(4):
				but=Fl_Button(col*150,row*150,150,150)
				but.color(FL_BACKGROUND2_COLOR)
				marvel=self.img_resize('marvel.png',150)
				but.image(marvel)
				but.clear_visible_focus()
				but.callback(show)
				x+=1
				buttons.append(but)
	
	# mr ark's code start
	def img_resize(self,fname,width):
		
		#resizes any image type using high quality PIL library

		img = Image.open(fname) #opens all image formats supported by PIL
		w,h = img.size
		height = int(width*h/w)  #correct aspect ratio
		img = img.resize((width, height), Image.BICUBIC) #high quality resizing
		mem = io.BytesIO()  #byte stream memory object
		img.save(mem, format="PNG") #converts image type to PNG byte stream
		siz = mem.tell() #gets size of image in bytes without reading again
		return Fl_PNG_Image(None, mem.getbuffer(), siz)
	# mr ark code end

	def show(self,w):
		i=buttons.index(w)
		if i in I: 
			#do nothing if same button. 
			return

		I.append(i)
		w.image(imgs[i]) #show image
		w.redraw()
		  
		#check if same image
		if len(I)==2:
			if fnames[I[0]]==fnames[I[1]]:
				buttons[I[0]].deactivate()
				buttons[I[0]].image().inactive()
				buttons[I[1]].deactivate()
				buttons[I[1]].image().inactive()
				I.clear()
		elif len(I)==3:
			buttons[I[1]].image(marvel)
			buttons[I[1]].redraw()
			buttons[I[0]].image(marvel)
			buttons[I[0]].redraw()
			I.pop(1)
			I.pop(0)#order matters. Must remove in reverse order

		#check if win
		win=True
		for but in buttons:
			  if but.active():
					win=False
					break
		if win:
			fl_message('You Win!')

				


app = window(600,400,'test')
app.show()
Fl.run()

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
		self.I=[]
		self.fnames=os.listdir('marvel_pics')
		self.fnames=self.fnames+self.fnames
		random.shuffle(self.fnames)
		self.imgs=[]
		for fname in self.fnames:
			self.imgs.append(self.img_resize(f'./marvel_pics/{fname}',120))
			#imgs.append(Fl_PNG_Image(f'./marvel_pics/{fname}').copy(150,150))
		for row in range(4):
			for col in range(6):
				but=Fl_Button(col*120,row*120,120,120)
				but.color(FL_BACKGROUND2_COLOR)
				self.marvel=self.img_resize('marvel.png',120)
				but.image(self.marvel)
				but.clear_visible_focus()
				but.callback(self.reveal)
				self.butlist.append(but)
		self.show()
	
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

	def reveal(self,w):
		i=self.butlist.index(w)
		if i in self.I: 
			#do nothing if same button. 
			return

		self.I.append(i)
		w.image(self.imgs[i]) #show image
		w.redraw()
		  
		#check if same image
		if len(self.I)==2:
			if self.fnames[self.I[0]]==self.fnames[self.I[1]]:
				self.butlist[self.I[0]].deactivate()
				self.butlist[self.I[0]].image().inactive()
				self.butlist[self.I[1]].deactivate()
				self.butlist[self.I[1]].image().inactive()
				self.I.clear()
		elif len(self.I)==3:
			self.butlist[self.I[1]].image(self.marvel)
			self.butlist[self.I[1]].redraw()
			self.butlist[self.I[0]].image(self.marvel)
			self.butlist[self.I[0]].redraw()
			self.I.pop(1)
			self.I.pop(0)#order matters. Must remove in reverse order

		#check if win
		win=True
		for but in self.butlist:
			if but.active():
				win=False
				break
		if win:
			fl_message('You Win!')

				


app = window(720,480,'test')
Fl.run()

 # testColorPicker

'''A simple RGB color mixer with three sliders. The selected color can be copied to the clipboard as an HTML hex string.'''

import ui
import clipboard
import random
import copy
from console import hud_alert

#locked = False
v = ui.load_view('testColorPicker')

maxHighlightHueMain = 0.166
maxShadeHueMain = 0.666
maxHueAdj = 0.10
storage = list()

class adjustments:
	def __init__(self):
		""

	def get(self):
		lumHLadj = v['lumHLadj'].value
		lumShadj = v['lumShadj'].value
		hueHLadj = v['hueHLadj'].value
		hueShadj = v['hueShadj'].value
		satHLadj = v['satHLadj'].value
		satShadj = v['satShadj'].value
		adjMaxHighlightHue = v['maxHighlightHue'].value
		adjMaxShadeHue = v['maxShadeHue'].value
		allAdjustments = [lumHLadj, lumShadj, hueHLadj, hueShadj, satHLadj, satShadj, adjMaxHighlightHue, adjMaxShadeHue]
		return(allAdjustments)
	
	def saved(self):
		storage = copy.deepcopy(currentAdjustments.get())
		print(storage)
		return(storage)

	def push(sender):
		ss = sender.superview

		global storage

		v['lumHLadj'].value = storage[0]
		v['lumShadj'].value = storage[1]
		v['hueHLadj'].value = storage[2]
		v['hueShadj'].value = storage[3]
		v['satHLadj'].value = storage[4]
		v['satShadj'].value = storage[5]
		v['adjMaxHighlightHue'].value = storage[6]
		v['adjMaxShadeHue'].value = storage[7]

	def store(sender):
		ss = sender.superview
		storage = currentAdjustments.get
		
		return(storage)
		#print(currentAdjustments)

currentAdjustments = adjustments()

def upload(sender):
	ss = sender.superview
	ss['temp1'].background_color = ss['display1'].background_color
	ss['temp2'].background_color = ss['display2'].background_color
	ss['temp3'].background_color = ss['display3'].background_color
	ss['temp4'].background_color = ss['display4'].background_color
	ss['temp5'].background_color = ss['display5'].background_color
	ss['temp6'].background_color = ss['display6'].background_color
	ss['temp7'].background_color = ss['display7'].background_color
	ss['temp8'].background_color = ss['display8'].background_color
	ss['temp9'].background_color = ss['display9'].background_color
	ss['temp10'].background_color = ss['display10'].background_color

def upload1(sender):
	ss = sender.superview
	ss['temp1'].background_color = ss['display11'].background_color
	ss['temp2'].background_color = ss['display12'].background_color
	ss['temp3'].background_color = ss['display13'].background_color
	ss['temp4'].background_color = ss['display14'].background_color
	ss['temp5'].background_color = ss['display15'].background_color
	ss['temp6'].background_color = ss['display16'].background_color
	ss['temp7'].background_color = ss['display17'].background_color
	ss['temp8'].background_color = ss['display18'].background_color
	ss['temp9'].background_color = ss['display19'].background_color
	ss['temp10'].background_color = ss['display20'].background_color

def upload2(sender):
	ss = sender.superview
	ss['temp1'].background_color = ss['display21'].background_color
	ss['temp2'].background_color = ss['display22'].background_color
	ss['temp3'].background_color = ss['display23'].background_color
	ss['temp4'].background_color = ss['display24'].background_color
	ss['temp5'].background_color = ss['display25'].background_color
	ss['temp6'].background_color = ss['display26'].background_color
	ss['temp7'].background_color = ss['display27'].background_color
	ss['temp8'].background_color = ss['display28'].background_color
	ss['temp9'].background_color = ss['display29'].background_color
	ss['temp10'].background_color = ss['display30'].background_color

def upload3(sender):
	ss = sender.superview
	ss['temp1'].background_color = ss['display31'].background_color
	ss['temp2'].background_color = ss['display32'].background_color
	ss['temp3'].background_color = ss['display33'].background_color
	ss['temp4'].background_color = ss['display34'].background_color
	ss['temp5'].background_color = ss['display35'].background_color
	ss['temp6'].background_color = ss['display36'].background_color
	ss['temp7'].background_color = ss['display37'].background_color
	ss['temp8'].background_color = ss['display38'].background_color
	ss['temp9'].background_color = ss['display39'].background_color
	ss['temp10'].background_color = ss['display40'].background_color

def upload4(sender):
	ss = sender.superview
	ss['temp1'].background_color = ss['display41'].background_color
	ss['temp2'].background_color = ss['display42'].background_color
	ss['temp3'].background_color = ss['display43'].background_color
	ss['temp4'].background_color = ss['display44'].background_color
	ss['temp5'].background_color = ss['display45'].background_color
	ss['temp6'].background_color = ss['display46'].background_color
	ss['temp7'].background_color = ss['display47'].background_color
	ss['temp8'].background_color = ss['display48'].background_color
	ss['temp9'].background_color = ss['display49'].background_color
	ss['temp10'].background_color = ss['display50'].background_color

def upload5(sender):
	ss = sender.superview
	ss['temp1'].background_color = ss['display51'].background_color
	ss['temp2'].background_color = ss['display52'].background_color
	ss['temp3'].background_color = ss['display53'].background_color
	ss['temp4'].background_color = ss['display54'].background_color
	ss['temp5'].background_color = ss['display55'].background_color
	ss['temp6'].background_color = ss['display56'].background_color
	ss['temp7'].background_color = ss['display57'].background_color
	ss['temp8'].background_color = ss['display58'].background_color
	ss['temp9'].background_color = ss['display59'].background_color
	ss['temp10'].background_color = ss['display60'].background_color

def upload6(sender):
	ss = sender.superview
	ss['temp1'].background_color = ss['display61'].background_color
	ss['temp2'].background_color = ss['display62'].background_color
	ss['temp3'].background_color = ss['display63'].background_color
	ss['temp4'].background_color = ss['display64'].background_color
	ss['temp5'].background_color = ss['display65'].background_color
	ss['temp6'].background_color = ss['display66'].background_color
	ss['temp7'].background_color = ss['display67'].background_color
	ss['temp8'].background_color = ss['display68'].background_color
	ss['temp9'].background_color = ss['display69'].background_color
	ss['temp10'].background_color = ss['display70'].background_color

def upload7(sender):
	ss = sender.superview
	ss['temp1'].background_color = ss['save1'].background_color
	ss['temp2'].background_color = ss['save2'].background_color
	ss['temp3'].background_color = ss['save3'].background_color
	ss['temp4'].background_color = ss['save4'].background_color
	ss['temp5'].background_color = ss['save5'].background_color
	ss['temp6'].background_color = ss['save6'].background_color
	ss['temp7'].background_color = ss['save7'].background_color
	ss['temp8'].background_color = ss['save8'].background_color
	ss['temp9'].background_color = ss['save9'].background_color
	ss['temp10'].background_color = ss['save10'].background_color

def upload8(sender):
	ss = sender.superview
	ss['temp1'].background_color = ss['save11'].background_color
	ss['temp2'].background_color = ss['save12'].background_color
	ss['temp3'].background_color = ss['save13'].background_color
	ss['temp4'].background_color = ss['save14'].background_color
	ss['temp5'].background_color = ss['save15'].background_color
	ss['temp6'].background_color = ss['save16'].background_color
	ss['temp7'].background_color = ss['save17'].background_color
	ss['temp8'].background_color = ss['save18'].background_color
	ss['temp9'].background_color = ss['save19'].background_color
	ss['temp10'].background_color = ss['save20'].background_color

def upload9(sender):
	ss = sender.superview
	ss['temp1'].background_color = ss['save21'].background_color
	ss['temp2'].background_color = ss['save22'].background_color
	ss['temp3'].background_color = ss['save23'].background_color
	ss['temp4'].background_color = ss['save24'].background_color
	ss['temp5'].background_color = ss['save25'].background_color
	ss['temp6'].background_color = ss['save26'].background_color
	ss['temp7'].background_color = ss['save27'].background_color
	ss['temp8'].background_color = ss['save28'].background_color
	ss['temp9'].background_color = ss['save29'].background_color
	ss['temp10'].background_color = ss['save30'].background_color

def upload10(sender):
	ss = sender.superview
	ss['temp1'].background_color = ss['save31'].background_color
	ss['temp2'].background_color = ss['save32'].background_color
	ss['temp3'].background_color = ss['save33'].background_color
	ss['temp4'].background_color = ss['save34'].background_color
	ss['temp5'].background_color = ss['save35'].background_color
	ss['temp6'].background_color = ss['save36'].background_color
	ss['temp7'].background_color = ss['save37'].background_color
	ss['temp8'].background_color = ss['save38'].background_color
	ss['temp9'].background_color = ss['save39'].background_color
	ss['temp10'].background_color = ss['save40'].background_color

def upload11(sender):
	ss = sender.superview
	ss['temp1'].background_color = ss['save41'].background_color
	ss['temp2'].background_color = ss['save42'].background_color
	ss['temp3'].background_color = ss['save43'].background_color
	ss['temp4'].background_color = ss['save44'].background_color
	ss['temp5'].background_color = ss['save45'].background_color
	ss['temp6'].background_color = ss['save46'].background_color
	ss['temp7'].background_color = ss['save47'].background_color
	ss['temp8'].background_color = ss['save48'].background_color
	ss['temp9'].background_color = ss['save49'].background_color
	ss['temp10'].background_color = ss['save50'].background_color

def upload12(sender):
	ss = sender.superview
	ss['temp1'].background_color = ss['save51'].background_color
	ss['temp2'].background_color = ss['save52'].background_color
	ss['temp3'].background_color = ss['save53'].background_color
	ss['temp4'].background_color = ss['save54'].background_color
	ss['temp5'].background_color = ss['save55'].background_color
	ss['temp6'].background_color = ss['save56'].background_color
	ss['temp7'].background_color = ss['save57'].background_color
	ss['temp8'].background_color = ss['save58'].background_color
	ss['temp9'].background_color = ss['save59'].background_color
	ss['temp10'].background_color = ss['save60'].background_color

def upload13(sender):
	ss = sender.superview
	ss['temp1'].background_color = ss['save61'].background_color
	ss['temp2'].background_color = ss['save62'].background_color
	ss['temp3'].background_color = ss['save63'].background_color
	ss['temp4'].background_color = ss['save64'].background_color
	ss['temp5'].background_color = ss['save65'].background_color
	ss['temp6'].background_color = ss['save66'].background_color
	ss['temp7'].background_color = ss['save67'].background_color
	ss['temp8'].background_color = ss['save68'].background_color
	ss['temp9'].background_color = ss['save69'].background_color
	ss['temp10'].background_color = ss['save70'].background_color

def download(sender):
	ss = sender.superview
	ss['display1'].background_color = ss['temp1'].background_color
	ss['display2'].background_color = ss['temp2'].background_color
	ss['display3'].background_color = ss['temp3'].background_color
	ss['display4'].background_color = ss['temp4'].background_color
	ss['display5'].background_color = ss['temp5'].background_color
	ss['display6'].background_color = ss['temp6'].background_color
	ss['display7'].background_color = ss['temp7'].background_color
	ss['display8'].background_color = ss['temp8'].background_color
	ss['display9'].background_color = ss['temp9'].background_color
	ss['display10'].background_color = ss['temp10'].background_color

def tempSwitchFromMain(sender):	
	u['temp1'].background_color = v['temp1'].background_color
	u['temp2'].background_color = v['temp2'].background_color
	u['temp3'].background_color = v['temp3'].background_color
	u['temp4'].background_color = v['temp4'].background_color
	u['temp5'].background_color = v['temp5'].background_color
	u['temp6'].background_color = v['temp6'].background_color
	u['temp7'].background_color = v['temp7'].background_color
	u['temp8'].background_color = v['temp8'].background_color
	u['temp9'].background_color = v['temp9'].background_color
	u['temp10'].background_color = v['temp10'].background_color

def tempSwitchToMain(sender):	
	v['temp1'].background_color = u['temp1'].background_color
	v['temp2'].background_color = u['temp2'].background_color
	v['temp3'].background_color = u['temp3'].background_color
	v['temp4'].background_color = u['temp4'].background_color
	v['temp5'].background_color = u['temp5'].background_color
	v['temp6'].background_color = u['temp6'].background_color
	v['temp7'].background_color = u['temp7'].background_color
	v['temp8'].background_color = u['temp8'].background_color
	v['temp9'].background_color = u['temp9'].background_color
	v['temp10'].background_color = u['temp10'].background_color

def switchUI(sender):
	tempSwitchFromMain(sender)
	if ui.get_screen_size()[1] >= 768:
		# iPad
		u.present('sheet')
	else:
		# iPhone
		u.present()

def lockAction(sender):
	ss = sender.superview
	if sender._pyui['attributes'].get('custom_attributes') == '0':
		ss['lockbutton'].image = ui.Image.named('iob:locked_256')
		ss['lockbutton']._pyui['attributes']['custom_attributes'] = '1'
	elif sender._pyui['attributes'].get('custom_attributes') == '1':
		ss['lockbutton'].image = ui.Image.named('iob:unlocked_256')
		ss['lockbutton']._pyui['attributes']['custom_attributes'] = '0'
	
def locked(sender):
	ss = sender.superview
	if sender._pyui['attributes'].get('custom_attributes') == '0':
		return(false)
	elif sender._pyui['attributes'].get('custom_attributes') == '1':
		return(true)

def saveSlot1(sender):
	u['display1'].background_color = u['temp1'].background_color
	u['display2'].background_color = u['temp2'].background_color
	u['display3'].background_color = u['temp3'].background_color
	u['display4'].background_color = u['temp4'].background_color
	u['display5'].background_color = u['temp5'].background_color
	u['display6'].background_color = u['temp6'].background_color
	u['display7'].background_color = u['temp7'].background_color
	u['display8'].background_color = u['temp8'].background_color
	u['display9'].background_color = u['temp9'].background_color
	u['display10'].background_color = u['temp10'].background_color
	return()

def saveSlot2(sender):
	u['display11'].background_color = u['temp1'].background_color
	u['display12'].background_color = u['temp2'].background_color
	u['display13'].background_color = u['temp3'].background_color
	u['display14'].background_color = u['temp4'].background_color
	u['display15'].background_color = u['temp5'].background_color
	u['display16'].background_color = u['temp6'].background_color
	u['display17'].background_color = u['temp7'].background_color
	u['display18'].background_color = u['temp8'].background_color
	u['display19'].background_color = u['temp9'].background_color
	u['display20'].background_color = u['temp10'].background_color
	return()

def saveSlot3(sender):
	u['display21'].background_color = u['temp1'].background_color
	u['display22'].background_color = u['temp2'].background_color
	u['display23'].background_color = u['temp3'].background_color
	u['display24'].background_color = u['temp4'].background_color
	u['display25'].background_color = u['temp5'].background_color
	u['display26'].background_color = u['temp6'].background_color
	u['display27'].background_color = u['temp7'].background_color
	u['display28'].background_color = u['temp8'].background_color
	u['display29'].background_color = u['temp9'].background_color
	u['display30'].background_color = u['temp10'].background_color
	return()

def saveSlot4(sender):
	u['display31'].background_color = u['temp1'].background_color
	u['display32'].background_color = u['temp2'].background_color
	u['display33'].background_color = u['temp3'].background_color
	u['display34'].background_color = u['temp4'].background_color
	u['display35'].background_color = u['temp5'].background_color
	u['display36'].background_color = u['temp6'].background_color
	u['display37'].background_color = u['temp7'].background_color
	u['display38'].background_color = u['temp8'].background_color
	u['display39'].background_color = u['temp9'].background_color
	u['display40'].background_color = u['temp10'].background_color
	return()

def saveSlot5(sender):
	u['display41'].background_color = u['temp1'].background_color
	u['display42'].background_color = u['temp2'].background_color
	u['display43'].background_color = u['temp3'].background_color
	u['display44'].background_color = u['temp4'].background_color
	u['display45'].background_color = u['temp5'].background_color
	u['display46'].background_color = u['temp6'].background_color
	u['display47'].background_color = u['temp7'].background_color
	u['display48'].background_color = u['temp8'].background_color
	u['display49'].background_color = u['temp9'].background_color
	u['display50'].background_color = u['temp10'].background_color
	return()

def saveSlot6(sender):
	u['display51'].background_color = u['temp1'].background_color
	u['display52'].background_color = u['temp2'].background_color
	u['display53'].background_color = u['temp3'].background_color
	u['display54'].background_color = u['temp4'].background_color
	u['display55'].background_color = u['temp5'].background_color
	u['display56'].background_color = u['temp6'].background_color
	u['display57'].background_color = u['temp7'].background_color
	u['display58'].background_color = u['temp8'].background_color
	u['display59'].background_color = u['temp9'].background_color
	u['display60'].background_color = u['temp10'].background_color
	return()

def saveSlot7(sender):
	u['display61'].background_color = u['temp1'].background_color
	u['display62'].background_color = u['temp2'].background_color
	u['display63'].background_color = u['temp3'].background_color
	u['display64'].background_color = u['temp4'].background_color
	u['display65'].background_color = u['temp5'].background_color
	u['display66'].background_color = u['temp6'].background_color
	u['display67'].background_color = u['temp7'].background_color
	u['display68'].background_color = u['temp8'].background_color
	u['display69'].background_color = u['temp9'].background_color
	u['display70'].background_color = u['temp10'].background_color
	return()

def saveSlot11(sender):
	u['save1'].background_color = u['temp1'].background_color
	u['save2'].background_color = u['temp2'].background_color
	u['save3'].background_color = u['temp3'].background_color
	u['save4'].background_color = u['temp4'].background_color
	u['save5'].background_color = u['temp5'].background_color
	u['save6'].background_color = u['temp6'].background_color
	u['save7'].background_color = u['temp7'].background_color
	u['save8'].background_color = u['temp8'].background_color
	u['save9'].background_color = u['temp9'].background_color
	u['save10'].background_color = u['temp10'].background_color
	return()

def saveSlot21(sender):
	u['save11'].background_color = u['temp1'].background_color
	u['save12'].background_color = u['temp2'].background_color
	u['save13'].background_color = u['temp3'].background_color
	u['save14'].background_color = u['temp4'].background_color
	u['save15'].background_color = u['temp5'].background_color
	u['save16'].background_color = u['temp6'].background_color
	u['save17'].background_color = u['temp7'].background_color
	u['save18'].background_color = u['temp8'].background_color
	u['save19'].background_color = u['temp9'].background_color
	u['save20'].background_color = u['temp10'].background_color
	return()

def saveSlot31(sender):
	u['save21'].background_color = u['temp1'].background_color
	u['save22'].background_color = u['temp2'].background_color
	u['save23'].background_color = u['temp3'].background_color
	u['save24'].background_color = u['temp4'].background_color
	u['save25'].background_color = u['temp5'].background_color
	u['save26'].background_color = u['temp6'].background_color
	u['save27'].background_color = u['temp7'].background_color
	u['save28'].background_color = u['temp8'].background_color
	u['save29'].background_color = u['temp9'].background_color
	u['save30'].background_color = u['temp10'].background_color
	return()

def saveSlot41(sender):
	u['save31'].background_color = u['temp1'].background_color
	u['save32'].background_color = u['temp2'].background_color
	u['save33'].background_color = u['temp3'].background_color
	u['save34'].background_color = u['temp4'].background_color
	u['save35'].background_color = u['temp5'].background_color
	u['save36'].background_color = u['temp6'].background_color
	u['save37'].background_color = u['temp7'].background_color
	u['save38'].background_color = u['temp8'].background_color
	u['save39'].background_color = u['temp9'].background_color
	u['save40'].background_color = u['temp10'].background_color
	return()

def saveSlot51(sender):
	u['save41'].background_color = u['temp1'].background_color
	u['save42'].background_color = u['temp2'].background_color
	u['save43'].background_color = u['temp3'].background_color
	u['save44'].background_color = u['temp4'].background_color
	u['save45'].background_color = u['temp5'].background_color
	u['save46'].background_color = u['temp6'].background_color
	u['save47'].background_color = u['temp7'].background_color
	u['save48'].background_color = u['temp8'].background_color
	u['save49'].background_color = u['temp9'].background_color
	u['save50'].background_color = u['temp10'].background_color
	return()

def saveSlot61(sender):
	u['save51'].background_color = u['temp1'].background_color
	u['save52'].background_color = u['temp2'].background_color
	u['save53'].background_color = u['temp3'].background_color
	u['save54'].background_color = u['temp4'].background_color
	u['save55'].background_color = u['temp5'].background_color
	u['save56'].background_color = u['temp6'].background_color
	u['save57'].background_color = u['temp7'].background_color
	u['save58'].background_color = u['temp8'].background_color
	u['save59'].background_color = u['temp9'].background_color
	u['save60'].background_color = u['temp10'].background_color
	return()

def saveSlot71(sender):
	u['save61'].background_color = u['temp1'].background_color
	u['save62'].background_color = u['temp2'].background_color
	u['save63'].background_color = u['temp3'].background_color
	u['save64'].background_color = u['temp4'].background_color
	u['save65'].background_color = u['temp5'].background_color
	u['save66'].background_color = u['temp6'].background_color
	u['save67'].background_color = u['temp7'].background_color
	u['save68'].background_color = u['temp8'].background_color
	u['save69'].background_color = u['temp9'].background_color
	u['save70'].background_color = u['temp10'].background_color
	return()	

def colorMatrix(h,s,l, adjustments):

	xyzMatrix = []
	maxShades = 6
	maxHighlights = 5
	hNew = h
	sNew = s
	lNew = l
	HSL = [copy.deepcopy(h), copy.deepcopy(s), copy.deepcopy(l)]

	adjustments = currentAdjustments.get()
	
	maxShadeHue, maxHighlightHue = float(adjustments[7]), float(adjustments[6])

	lightHightlightAdj, lightShadeAdj, hueHighlightAdj = float(adjustments[0])*maxHueAdj, float(adjustments[1])*maxHueAdj, float(adjustments[2])*maxHueAdj
	hueShadeAdj, satHighlightAdj, satShadeAdj = float(adjustments[3]*maxHueAdj), float(adjustments[4]*maxHueAdj), float(adjustments[5])*maxHueAdj
	

	for rowCount in range(0,maxShades):
		xyzList = []
		xyzRow = []
		hNew = h
		sNew = s
		lNew = l
		if rowCount < 1:
			firstCell = [hNew,sNew,lNew]
			xyzRow.append(firstCell)	
			#l = max(0.0, min(1.0, l - lightShadeAdj))
			for zCount in range(0,maxHighlights-1):
				if maxHighlightHue <= hNew <= maxShadeHue:
					if hNew - hueHighlightAdj <= maxHighlightHue:
						hNew = maxHighlightHue
					else:
						hNew = hNew - hueHighlightAdj
				elif hNew <= maxHighlightHue:
					if hNew + hueHighlightAdj >= maxHighlightHue:
						hNew = maxHighlightHue
					else:
						hNew = hNew + hueHighlightAdj
				elif hNew >= maxShadeHue:
					if hNew + hueHighlightAdj >= 1:
						hNew = 1 - hNew + hueHighlightAdj
					else:
						hNew = hNew + hueHighlightAdj
				else:
					hNew = maxHighlightHue
				sNew = min(1.0, max(0.0, sNew - satHighlightAdj))
				lNew = max(0.0, min(1.0, lNew + lightHightlightAdj))
				cell = [hNew,sNew,lNew]
				xyzRow.append(cell)
			#xyzList.append(xyzRow)
		
		else:
			if maxHighlightHue <= h <= maxShadeHue:
				if h + hueShadeAdj >= maxShadeHue:
					h = maxShadeHue
				elif h + hueShadeAdj <= maxShadeHue:
					h = h + hueShadeAdj
				else:
					h = hueShadeAdj
			elif h <= maxHighlightHue:
				if h - hueShadeAdj <= 0:
					h = 1 + h - hueShadeAdj
				else:
					h = h - hueShadeAdj
			elif h >= maxShadeHue:
				if h - hueShadeAdj >= maxShadeHue:
					h = h - hueShadeAdj
				else:
					h = maxShadeHue
			else:
				if h - hueShadeAdj <= maxShadeHue:
					h = maxShadeHue
				else:
					h = h - hueShadeAdj
			s = min(1.0, max(0.0, s - satShadeAdj))
			l = max(0.0, min(1.0, l - lightShadeAdj))
			cell = [h,s,l]
			xyzRow.append(cell)
			for zCount in range(0,maxHighlights-1):
				cell = 0,0,0
				xyzRow.append(cell)
			#xyzList.append(xyzRow)
		xyzMatrix.append(xyzRow)

	return(HSL, xyzMatrix)

def returnRGB(temp1, temp2, tempValue):
	if 6 * tempValue < 1:
		value = temp2 + (temp1 - temp2) * 6 * tempValue
	elif 2 * tempValue < 1:
		value = temp1
	elif 3 * tempValue < 2:
		value = temp2 + (temp1 - temp2) * (2/3 - tempValue) * 6
	else:
		value = temp2
	
	return(value)
	
def convertHSLtoRGB(HSL):
	# Convert to rgb:
	h = float(HSL[0])
	s = float(HSL[1])
	l = float(HSL[2])
	
	if l < 0.5:
		temp1 = l*(1.0+s)
	else:
		temp1 = l + s - (l*s)
	
	temp2 = 2*l - temp1
	
	tempR = h + (1/3)
	tempG = h
	tempB = h - (1/3)
	
	if tempR < 0:
		tempR = tempR + 1
	elif tempR > 1:
		tempR = tempR - 1

	if tempG < 0:
		tempG = tempG + 1
	elif tempG > 1:
		tempG = tempG - 1

	if tempB >= 1:
		tempB = tempB - 1
	elif tempB < 0:
		tempB = tempB + 1
	
	r = returnRGB(temp1, temp2, tempR)
	g = returnRGB(temp1, temp2, tempG)
	b = returnRGB(temp1, temp2, tempB)
	
	r,g,b = round(r,3), round(g,3), round(b,3)

	return(r,g,b)
	
def convertRGBtoHSL(RGB):
	# Convert to rgb:
	r = round(float(RGB[0]),3)
	g = round(float(RGB[1]),3)
	b = round(float(RGB[2]),3)
	
	minValue = min(r,g,b)
	maxValue = max(r,g,b)

	lum = (minValue + maxValue)/2

	if minValue == maxValue:
		sat = 0
	else:
		if lum < 0.5:
			sat = (maxValue - minValue)/(maxValue+minValue)
		else:
			sat = (maxValue - minValue)/(2.0 - maxValue-minValue)

	if maxValue == r:
		hue = (g-b)/(maxValue-minValue)
		#print('maxValue = r')
	elif maxValue == g:
		hue = 2.0 + (b-r)/(maxValue-minValue)
		#print('maxValue = g')
	elif maxValue == b:
		hue = 4.0 + (r-g)/(maxValue-minValue)
		#print('maxValue = b')
	else:
		hue = (g-b)/(maxValue-minValue)
		#print('maxValue none')
	

	hue = round((hue*60/360),3)

	while hue < 0:
		hue = hue + 1
	while hue > 1:
		hue = hue - 1

	return(round(hue,3),round(sat,3),round(lum,3))

def adjustmentSliderBgs(h,s,l,adjustments):

	hueAdj = maxHueAdj

	lightHightlightAdj, lightShadeAdj, hueHighlightAdj = float(adjustments[0])*maxHueAdj, float(adjustments[1])*maxHueAdj, float(adjustments[2])*maxHueAdj
	hueShadeAdj, satHighlightAdj, satShadeAdj = float(adjustments[3])*maxHueAdj, float(adjustments[4])*maxHueAdj, float(adjustments[5])*maxHueAdj
	maxShadeHue, maxHighlightHue = float(adjustments[7]), float(adjustments[6])

	if maxHighlightHue <= h <= maxShadeHue:
		if h + hueAdj >= maxShadeHue:
			adjustedHLHue = h - hueAdj
			adjustedShHue = maxShadeHue
		elif h + hueAdj < maxShadeHue:
			adjustedShHue = h + hueAdj
			if h - hueAdj <= maxHighlightHue:
				adjustedHLHue = maxHighlightHue
			else:
				adjustedHLHue = h - hueAdj
		else:
			adjustedShHue = h
			adjustedHLHue = h
	elif 0 <= h <= maxHighlightHue:
		if h - hueAdj <= 0:
			adjustedHLHue = 1 + h + hueAdj
			adjustedShHue = 1 + h - hueAdj
		elif h - hueAdj > 0:
			adjustedShHue = h - hueAdj
			if h - hueAdj <= maxHighlightHue:
				adjustedHLHue = maxHighlightHue
			else:
				adjustedHLHue = h - hueAdj
		else:
			adjustedHLHue = h + hueAdj
			adjustedShHue = h - hueAdj
	elif maxShadeHue <= h <= 1:
		if h - hueAdj >= maxShadeHue:
			adjustedHLHue = h + hueAdj
			adjustedShHue = h - hueAdj
		else:
			adjustedShHue = h
			adjustedHLHue = h
	else:
		print("error")
		adjustedShHue = h
		adjustedHLHue = h

	v['hueHLmax'].background_color = (convertHSLtoRGB([adjustedHLHue,s,l]))
	v['hueHLmin'].background_color = (convertHSLtoRGB([h,s,l]))
	v['satHLmax'].background_color = (convertHSLtoRGB([h,max(s-0.20,0),l]))
	v['satHLmin'].background_color = (convertHSLtoRGB([h,s,l]))
	v['lumHLmax'].background_color = (convertHSLtoRGB([h,s,min(l+0.20,100)]))
	v['lumHLmin'].background_color = (convertHSLtoRGB([h,s,l]))

	v['hueShmax'].background_color = (convertHSLtoRGB([adjustedShHue,s,l]))
	v['hueShmin'].background_color = (convertHSLtoRGB([h,s,l]))
	v['satShmax'].background_color = (convertHSLtoRGB([h,s-0.20,l]))
	v['satShmin'].background_color = (convertHSLtoRGB([h,s,l]))
	v['lumShmax'].background_color = (convertHSLtoRGB([h,s,l-0.20]))
	v['lumShmin'].background_color = (convertHSLtoRGB([h,s,l]))

def rotateHue(h,s,l,degree):
	# h1 = hkk
	s1 = round(s, 3)
	l1 = round(l, 3)
	h2 = h + degree
	if h2 > 1.00:
		h2 = round((h2 - 1.00), 3)
	#print("h2,s1,l1" + str([h2,s1,l1]))
	return(h2,s1,l1)

def get_adjustments(sender):
	
	lumHLadj = v['lumHLadj'].value
	lumShadj = v['lumShadj'].value
	hueHLadj = v['hueHLadj'].value
	hueShadj = v['hueShadj'].value
	satHLadj = v['satHLadj'].value
	satShadj = v['satShadj'].value
	adjMaxHighlightHue = v['maxHighlightHue'].value
	adjMaxShadeHue = v['maxShadeHue'].value

	return([lumHLadj, lumShadj, hueHLadj, hueShadj, satHLadj, satShadj, adjMaxHighlightHue, adjMaxShadeHue])

def shadowsHighlights(h,s,l, adjustments):

	HSL, xyzMatrix = colorMatrix(h,s,l, adjustments)

	# Create the new color from the slider values:
	v['display1'].background_color = (convertHSLtoRGB(xyzMatrix[0][0]))
	v['display2'].background_color = (convertHSLtoRGB(xyzMatrix[0][1]))
	v['display3'].background_color = (convertHSLtoRGB(xyzMatrix[0][2]))
	v['display4'].background_color = (convertHSLtoRGB(xyzMatrix[0][3]))
	v['display5'].background_color = (convertHSLtoRGB(xyzMatrix[0][4]))
	v['display6'].background_color = (convertHSLtoRGB(xyzMatrix[1][0]))
	v['display7'].background_color = (convertHSLtoRGB(xyzMatrix[2][0]))
	v['display8'].background_color = (convertHSLtoRGB(xyzMatrix[3][0]))
	v['display9'].background_color = (convertHSLtoRGB(xyzMatrix[4][0]))
	v['display10'].background_color = (convertHSLtoRGB(xyzMatrix[5][0]))

	return([h,s,l])
	
def hueChanges(h,s,l,adjustments):

	hueMatrix = []
	hueMatrix.append(convertHSLtoRGB(rotateHue(h,s,l,0.0)))
	hueMatrix.append(convertHSLtoRGB(rotateHue(h,s,l,0.1)))
	hueMatrix.append(convertHSLtoRGB(rotateHue(h,s,l,0.2)))
	hueMatrix.append(convertHSLtoRGB(rotateHue(h,s,l,0.3)))
	hueMatrix.append(convertHSLtoRGB(rotateHue(h,s,l,0.4)))
	hueMatrix.append(convertHSLtoRGB(rotateHue(h,s,l,0.5)))
	hueMatrix.append(convertHSLtoRGB(rotateHue(h,s,l,0.6)))
	hueMatrix.append(convertHSLtoRGB(rotateHue(h,s,l,0.7)))
	hueMatrix.append(convertHSLtoRGB(rotateHue(h,s,l,0.8)))
	hueMatrix.append(convertHSLtoRGB(rotateHue(h,s,l,0.9)))

	# Create the new hue from the slider values
	v['hue1'].background_color = hueMatrix[1]
	v['hue2'].background_color = hueMatrix[2]
	v['hue3'].background_color = hueMatrix[3]
	v['hue4'].background_color = hueMatrix[4]
	v['hue5'].background_color = hueMatrix[5]
	v['hue6'].background_color = hueMatrix[6]
	v['hue7'].background_color = hueMatrix[7]
	v['hue8'].background_color = hueMatrix[8]
	v['hue9'].background_color = hueMatrix[9]
	v['hue0'].background_color = hueMatrix[0]

def createSliderBarColors(h,s,l,adjustments):
	
	r,g,b = convertHSLtoRGB([h,s,l])

	# Create background for hue bar:
	v['hbar0'].background_color = (convertHSLtoRGB([0.05,s,l]))
	v['hbar1'].background_color = (convertHSLtoRGB([0.15,s,l]))
	v['hbar2'].background_color = (convertHSLtoRGB([0.25,s,l]))
	v['hbar3'].background_color = (convertHSLtoRGB([0.35,s,l]))
	v['hbar4'].background_color = (convertHSLtoRGB([0.45,s,l]))
	v['hbar5'].background_color = (convertHSLtoRGB([0.55,s,l]))
	v['hbar6'].background_color = (convertHSLtoRGB([0.65,s,l]))
	v['hbar7'].background_color = (convertHSLtoRGB([0.75,s,l]))
	v['hbar8'].background_color = (convertHSLtoRGB([0.85,s,l]))
	v['hbar9'].background_color = (convertHSLtoRGB([0.95,s,l]))
	v['hbar10'].background_color = (convertHSLtoRGB([1.00,s,l]))

	# Create background for saturation bar:
	v['sbar0'].background_color = (convertHSLtoRGB([h,0,l]))
	v['sbar1'].background_color = (convertHSLtoRGB([h,0.1,l]))
	v['sbar2'].background_color = (convertHSLtoRGB([h,0.2,l]))
	v['sbar3'].background_color = (convertHSLtoRGB([h,0.3,l]))
	v['sbar4'].background_color = (convertHSLtoRGB([h,0.4,l]))
	v['sbar5'].background_color = (convertHSLtoRGB([h,0.5,l]))
	v['sbar6'].background_color = (convertHSLtoRGB([h,0.6,l]))
	v['sbar7'].background_color = (convertHSLtoRGB([h,0.7,l]))
	v['sbar8'].background_color = (convertHSLtoRGB([h,0.8,l]))
	v['sbar9'].background_color = (convertHSLtoRGB([h,0.9,l]))
	v['sbar10'].background_color = (convertHSLtoRGB([h,1.0,l]))

	# Create background for luminescence bar:
	v['lbar0'].background_color = (convertHSLtoRGB([h,s,0]))
	v['lbar1'].background_color = (convertHSLtoRGB([h,s,0.1]))
	v['lbar2'].background_color = (convertHSLtoRGB([h,s,0.2]))
	v['lbar3'].background_color = (convertHSLtoRGB([h,s,0.3]))
	v['lbar4'].background_color = (convertHSLtoRGB([h,s,0.4]))
	v['lbar5'].background_color = (convertHSLtoRGB([h,s,0.5]))
	v['lbar6'].background_color = (convertHSLtoRGB([h,s,0.6]))
	v['lbar7'].background_color = (convertHSLtoRGB([h,s,0.7]))
	v['lbar8'].background_color = (convertHSLtoRGB([h,s,0.8]))
	v['lbar9'].background_color = (convertHSLtoRGB([h,s,0.9]))
	v['lbar10'].background_color = (convertHSLtoRGB([h,s,1.0]))
	
	v['slider1'].tint_color = (convertHSLtoRGB([h,s,l]))
	v['slider2'].tint_color = (convertHSLtoRGB([h,s,l]))
	v['slider3'].tint_color = (convertHSLtoRGB([h,s,l]))

	v['label1'].text = str("h = " + str(h) + ", s = " + str(s) + ", l = " + str(l))
	v['label1'].background_color = (convertHSLtoRGB([h,s,l]))

def slider_action(sender):
	# Get the root view:
	v = sender.superview
	
	# Get the sliders:
	h = round(v['slider1'].value, 3)
	s = round(v['slider2'].value, 3)
	l = round(v['slider3'].value, 3)
	
	lumHLadj = round(v['lumHLadj'].value, 3)
	lumShadj = round(v['lumShadj'].value, 3)
	hueHLadj = round(v['hueHLadj'].value, 3)
	hueShadj = round(v['hueShadj'].value, 3)
	satHLadj = round(v['satHLadj'].value, 3)
	satShadj = round(v['satShadj'].value, 3)

	adjMaxHighlightHue = round(v['maxHighlightHue'].value, 3)
	adjMaxShadeHue = round(v['maxShadeHue'].value,3)

	adjustments = [lumHLadj, lumShadj, hueHLadj, hueShadj, satHLadj, satShadj, adjMaxHighlightHue, adjMaxShadeHue]

	hueChanges(h,s,l,adjustments)
	HSL = shadowsHighlights(h,s,l,adjustments)
	# h = HSL[0]
	# s = HSL[1]
	# l = HSL[2]
	createSliderBarColors(h,s,l,adjustments)
	adjustmentSliderBgs(h,s,l,adjustments)

def copy_action(sender):
	clipboard.set(sender.superview['label1'].text)
	hud_alert('Copied')

def shuffle_action(sender):
	v = sender.superview
	s1 = v['slider1']
	s2 = v['slider2']
	s3 = v['slider3']
	s1.value = random.random()
	s2.value = random.random()
	s3.value = random.random()
	slider_action(s1)
	
def push_hue1(sender):

	RGB = v['hue1'].background_color
	
	RGB = [round(x, 3) for x in RGB]
	
	#print(str('RGB') + str(RGB))
	HSL = convertRGBtoHSL(RGB)
	#print(str('HSL') + str(HSL))
	h,s,l = HSL[0:3]
	#h2,s,l = rotateHue(h,s,l,0.16)

	adjustments = get_adjustments(sender)
	
	v['slider1'].value = float(h)
	v['slider2'].value = float(s)
	v['slider3'].value = float(l)

	HSL = shadowsHighlights(h,s,l,adjustments)
	h = HSL[0]
	s = HSL[1]
	l = HSL[2]
	shadowsHighlights(h,s,l,adjustments)
	
	return(h,s,l)

def push_hue2(sender):

	HSL = convertRGBtoHSL(v['hue2'].background_color)
	h,s,l = HSL[0:3]
	#h2,s,l = rotateHue(h,s,l,0.16)

	adjustments = get_adjustments(sender)
	
	v['slider1'].value = float(h)
	v['slider2'].value = float(s)
	v['slider3'].value = float(l)
	
	HSL = shadowsHighlights(h,s,l,adjustments)
	h = HSL[0]
	s = HSL[1]
	l = HSL[2]
	shadowsHighlights(h,s,l,adjustments)
	
	return(h,s,l)
	
def push_hue3(sender):

	HSL = convertRGBtoHSL(v['hue3'].background_color)
	h,s,l = HSL[0:3]
	adjustments = get_adjustments(sender)
	v['slider1'].value = float(h)
	v['slider2'].value = float(s)
	v['slider3'].value = float(l)
	
	HSL = shadowsHighlights(h,s,l,adjustments)
	h = HSL[0]
	s = HSL[1]
	l = HSL[2]
	shadowsHighlights(h,s,l,adjustments)
	
	return(h,s,l)
	
def push_hue4(sender):

	HSL = convertRGBtoHSL(v['hue4'].background_color)
	h,s,l = HSL[0:3]
	#h2,s,l = rotateHue(h,s,l,0.16)

	adjustments = get_adjustments(sender)
	
	v['slider1'].value = float(h)
	v['slider2'].value = float(s)
	v['slider3'].value = float(l)
	
	HSL = shadowsHighlights(h,s,l,adjustments)
	h = HSL[0]
	s = HSL[1]
	l = HSL[2]
	shadowsHighlights(h,s,l,adjustments)
	
	return(h,s,l)

def push_hue5(sender):

	HSL = convertRGBtoHSL(v['hue5'].background_color)
	h,s,l = HSL[0:3]
	#h2,s,l = rotateHue(h,s,l,0.16)

	adjustments = get_adjustments(sender)
	
	v['slider1'].value = float(h)
	v['slider2'].value = float(s)
	v['slider3'].value = float(l)
	
	HSL = shadowsHighlights(h,s,l,adjustments)
	h = HSL[0]
	s = HSL[1]
	l = HSL[2]
	shadowsHighlights(h,s,l,adjustments)
	
	return(h,s,l)

def push_hue6(sender):

	HSL = convertRGBtoHSL(v['hue6'].background_color)
	h,s,l = HSL[0:3]
	#h2,s,l = rotateHue(h,s,l,0.16)

	adjustments = get_adjustments(sender)
	
	v['slider1'].value = float(h)
	v['slider2'].value = float(s)
	v['slider3'].value = float(l)
	
	HSL = shadowsHighlights(h,s,l,adjustments)
	h = HSL[0]
	s = HSL[1]
	l = HSL[2]
	shadowsHighlights(h,s,l,adjustments)
	
	return(h,s,l)

def push_hue7(sender):

	HSL = convertRGBtoHSL(v['hue7'].background_color)
	h,s,l = HSL[0:3]
	#h2,s,l = rotateHue(h,s,l,0.16)

	adjustments = get_adjustments(sender)
	
	v['slider1'].value = float(h)
	v['slider2'].value = float(s)
	v['slider3'].value = float(l)
	
	HSL = shadowsHighlights(h,s,l,adjustments)
	h = HSL[0]
	s = HSL[1]
	l = HSL[2]
	shadowsHighlights(h,s,l,adjustments)
	
	return(h,s,l)

def push_hue8(sender):

	HSL = convertRGBtoHSL(v['hue8'].background_color)
	h,s,l = HSL[0:3]
	#h2,s,l = rotateHue(h,s,l,0.16)

	adjustments = get_adjustments(sender)
	
	v['slider1'].value = float(h)
	v['slider2'].value = float(s)
	v['slider3'].value = float(l)
	
	HSL = shadowsHighlights(h,s,l,adjustments)
	h = HSL[0]
	s = HSL[1]
	l = HSL[2]
	shadowsHighlights(h,s,l,adjustments)
	
	return(h,s,l)

def push_hue9(sender):

	HSL = convertRGBtoHSL(v['hue9'].background_color)
	h,s,l = HSL[0:3]
	#h2,s,l = rotateHue(h,s,l,0.16)

	adjustments = get_adjustments(sender)
	
	v['slider1'].value = float(h)
	v['slider2'].value = float(s)
	v['slider3'].value = float(l)
	
	HSL = shadowsHighlights(h,s,l,adjustments)
	h = HSL[0]
	s = HSL[1]
	l = HSL[2]
	shadowsHighlights(h,s,l,adjustments)
	
	return(h,s,l)

def push_hue0(sender):

	HSL = convertRGBtoHSL(v['hue0'].background_color)
	h,s,l = HSL[0:3]
	#h2,s,l = rotateHue(h,s,l,0.16)

	adjustments = get_adjustments(sender)
	
	v['slider1'].value = float(h)
	v['slider2'].value = float(s)
	v['slider3'].value = float(l)
	
	HSL = shadowsHighlights(h,s,l,adjustments)
	h = HSL[0]
	s = HSL[1]
	l = HSL[2]
	createSliderBarColors(h,s,l,adjustments)
	
	return(h,s,l)

v = ui.load_view('testColorPicker')
u = ui.load_view('testColorPicker2')

v['lockbutton'].image = ui.Image.named('iob:unlocked_256')

#v = sender.superview

h = v['slider1'].value
s = v['slider2'].value
l = v['slider3'].value

slider_action(v['slider1'])
slider_action(v['slider2'])
slider_action(v['slider3'])

if ui.get_screen_size()[1] >= 768:
	# iPad
	v.present('sheet')
else:
	# iPhone
	v.present('fullscreen')

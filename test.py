import ui
import copy

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

def rotateHue(h,s,l,degree):
	# h1 = hkk
	s1 = round(s, 3)
	l1 = round(l, 3)
	h2 = h + degree
	if h2 > 1.00:
		h2 = round((h2 - 1.00), 3)
	#print("h2,s1,l1" + str([h2,s1,l1]))
	return(h2,s1,l1)

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

def colorMatrix(h,s,l):

	xyzMatrix = []
	maxShades = 6
	maxHighlights = 5
	hNew = h
	sNew = s
	lNew = l
	HSL = [copy.deepcopy(h), copy.deepcopy(s), copy.deepcopy(l)]

	adjustments = [0.5,0.5,0.5,0.5,0.5,0.5,0.166,0.666]

	maxHueAdj = 0.25

	# adjustments = currentAdjustments.get()
	
	lightHightlightAdj, lightShadeAdj, hueHighlightAdj = float(adjustments[0])*maxHueAdj, float(adjustments[1])*maxHueAdj, float(adjustments[2])*maxHueAdj
	hueShadeAdj, satHighlightAdj, satShadeAdj = float(adjustments[3])*maxHueAdj, float(adjustments[4])*maxHueAdj, float(adjustments[5])*maxHueAdj
	maxShadeHue, maxHighlightHue = float(adjustments[7])*maxHueAdj, float(adjustments[6])*maxHueAdj

	for rowCount in range(0,5):
		highlights = []
		shadows = []
		hNew = h
		sNew = s
		lNew = l
		
	for rowCount in range(0,5):
		#highlights = []
		hNew = h
		sNew = s
		lNew = l
		firstCell = [hNew,sNew,lNew]
		highlights.append(firstCell)
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
			highlights.append(cell)

	for rowCount in range(0,5):
		shadows = []
		hNew = h
		sNew = s
		lNew = l
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
		shadows.append(cell)

	#shadows.append(highlights)

	return(HSL, shadows, highlights)

class storageUnit:
	def __init__(self,storage,h,s,l):
		count = 0
		for i in storage:
			count = count + 1
			i.background_color = (convertHSLtoRGB([h+count*0.05,s,l]))

	def hueChanges(storage,h,s,l):
		hueMatrix = storageUnit.hueMatrix(storage,h,s,l)
		count = 0
		for i in storage:
			i.background_color = hueMatrix[count]
			count = count + 1

	def hueMatrix(storage,h,s,l):
		hueMatrix = []
		count = 0
		for i in storage:
			hueMatrix.append(convertHSLtoRGB(rotateHue(h,s,l,count*0.1)))
			count = count + 1
		return(hueMatrix)

	def shadowsAndHighlights(storage,h,s,l):
		HSL, shadows, highlights = colorMatrix(h,s,l)
		count = 0
		for i in shadows:
			highlights.insert(0,i)

		(convertHSLtoRGB(i) for i in highlights)

		for i in storage:
		 	i.background_color = (highlights[count][0],highlights[count][1],highlights[count][2])
		 	count = count + 1
		 	print(count)
		 	print(len(highlights))
		 	print(len(storage))
		print(shadows)
	
def makeHueBar(h,s,l):
	hueBar['0'].background_color = (convertHSLtoRGB([0.05,s,l]))
	hueBar['1'].background_color = (convertHSLtoRGB([0.15,s,l]))
	hueBar['2'].background_color = (convertHSLtoRGB([0.25,s,l]))
	hueBar['3'].background_color = (convertHSLtoRGB([0.35,s,l]))
	hueBar['4'].background_color = (convertHSLtoRGB([0.45,s,l]))
	hueBar['5'].background_color = (convertHSLtoRGB([0.55,s,l]))
	hueBar['6'].background_color = (convertHSLtoRGB([0.65,s,l]))
	hueBar['7'].background_color = (convertHSLtoRGB([0.75,s,l]))
	hueBar['8'].background_color = (convertHSLtoRGB([0.85,s,l]))
	hueBar['9'].background_color = (convertHSLtoRGB([0.95,s,l]))
	hueBar['10'].background_color = (convertHSLtoRGB([1.00,s,l]))
	hueBar['slider'].tint_color = (convertHSLtoRGB([h,s,l]))

def makeSatBar(h,s,l):
	satBar['0'].background_color = (convertHSLtoRGB([h,0.05,l]))
	satBar['1'].background_color = (convertHSLtoRGB([h,0.15,l]))
	satBar['2'].background_color = (convertHSLtoRGB([h,0.25,l]))
	satBar['3'].background_color = (convertHSLtoRGB([h,0.35,l]))
	satBar['4'].background_color = (convertHSLtoRGB([h,0.45,l]))
	satBar['5'].background_color = (convertHSLtoRGB([h,0.55,l]))
	satBar['6'].background_color = (convertHSLtoRGB([h,0.65,l]))
	satBar['7'].background_color = (convertHSLtoRGB([h,0.75,l]))
	satBar['8'].background_color = (convertHSLtoRGB([h,0.85,l]))
	satBar['9'].background_color = (convertHSLtoRGB([h,0.95,l]))
	satBar['10'].background_color = (convertHSLtoRGB([h,1.00,l]))
	satBar['slider'].tint_color = (convertHSLtoRGB([h,s,l]))

def makeLumBar(h,s,l):
	lumBar['0'].background_color = (convertHSLtoRGB([h,s,0.05]))
	lumBar['1'].background_color = (convertHSLtoRGB([h,s,0.15]))
	lumBar['2'].background_color = (convertHSLtoRGB([h,s,0.25]))
	lumBar['3'].background_color = (convertHSLtoRGB([h,s,0.35]))
	lumBar['4'].background_color = (convertHSLtoRGB([h,s,0.45]))
	lumBar['5'].background_color = (convertHSLtoRGB([h,s,0.55]))
	lumBar['6'].background_color = (convertHSLtoRGB([h,s,0.65]))
	lumBar['7'].background_color = (convertHSLtoRGB([h,s,0.75]))
	lumBar['8'].background_color = (convertHSLtoRGB([h,s,0.85]))
	lumBar['9'].background_color = (convertHSLtoRGB([h,s,0.95]))
	lumBar['10'].background_color = (convertHSLtoRGB([h,s,1.00]))
	lumBar['slider'].tint_color = (convertHSLtoRGB([h,s,l]))

def slider_action(sender):
	ss = sender.superview
	
	# Get the sliders:
	h = round(hueBar['slider'].value,3)
	s = round(satBar['slider'].value,3)
	l = round(lumBar['slider'].value,3)

	makeHueBar(h,s,l)
	makeSatBar(h,s,l)
	makeLumBar(h,s,l)

	storage = ui.load_view('storage')
	v['storage1'].add_subview(storage)
	storageList = [storage['0'],storage['1'],storage['2'],storage['3'],storage['4'],storage['5'],storage['6'],storage['7'],storage['8']]
	madeStorage = storageUnit.shadowsAndHighlights(storageList,h,s,l)

### For each instance of a .pyui file, load it and assign it a variable name
v = ui.load_view('paletteMaker')

hueBar = ui.load_view('spectrumBar')
satBar = ui.load_view('spectrumBar')
lumBar = ui.load_view('spectrumBar')

### Connect the subviews to main views
v['hBar'].add_subview(hueBar)
v['sBar'].add_subview(satBar)
v['lBar'].add_subview(lumBar)

### Initialize h,s,l
h = round(hueBar['slider'].value,3)
s = round(satBar['slider'].value,3)
l = round(lumBar['slider'].value,3)

storage2 = ui.load_view('storage')
v['storage2'].add_subview(storage2)
storage2List = [storage2['0'],storage2['1'],storage2['2'],storage2['3'],storage2['4'],storage2['5'],storage2['6'],storage2['7'],storage2['8']]
madeStorage2 = storageUnit.hueChanges(storage2List,h,s,l)

storage3 = ui.load_view('storage')
v['storage3'].add_subview(storage3)
storage3List = [storage3['0'],storage3['1'],storage3['2'],storage3['3'],storage3['4'],storage3['5'],storage3['6'],storage3['7'],storage3['8']]
madestorage3 = storageUnit(storage3List,h,s,l)

storage4 = ui.load_view('storage')
v['storage4'].add_subview(storage4)
storage4List = [storage4['0'],storage4['1'],storage4['2'],storage4['3'],storage4['4'],storage4['5'],storage4['6'],storage4['7'],storage4['8']]
madestorage4 = storageUnit.hueChanges(storage4List,h,s,l)

slider_action(hueBar['slider'])
slider_action(satBar['slider'])
slider_action(lumBar['slider'])

v.present('sheet')


#print(v.subviews)


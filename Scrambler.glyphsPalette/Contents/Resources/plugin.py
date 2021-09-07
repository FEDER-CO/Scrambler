# encoding: utf-8

###########################################################################################################
#
#
#	Palette Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Palette
#
#
###########################################################################################################

import random, objc
random.seed()
from GlyphsApp import *
from GlyphsApp.plugins import *
from vanilla import *

class Scrambler(PalettePlugin):
	@objc.python_method
	def settings(self):
		self.name = "Scrambler"
		self.value = 500

		# Create Vanilla window and group with controls
		width = 150
		height = 40
		self.paletteView = Window((width, height))
		self.paletteView.group = Group((0, 0, width, height))
		self.paletteView.group.scramblerButton = Button((7, 10, 100, -10), "Scramble!", callback=self.scramblerCallback_, sizeStyle='small')
		self.paletteView.group.scramblerButton.getNSButton().setToolTip_(u"Get random text")
		self.paletteView.group.text = EditText((114, 10, -10, -10), text=self.value, placeholder='500', sizeStyle='small', callback=self.scramblerCallback_)
		self.paletteView.group.text.getNSTextField().setToolTip_(u"Number of characters")

		# Set dialog to NSView
		self.dialog = self.paletteView.group.getNSView()

	@objc.python_method
	def newValue(self):
		try:
			n = self.paletteView.group.text.get()
			return int(n)
		except ValueError:
			return 500

	def scramblerCallback_(self, sender):
		thisFont = self.windowController().documentFont()
		currentLayers = thisFont.selectedLayers
		printableLayers = []
		tab = []
		scrambledEggs = ('\"The Key to Scrambled Eggs: Slow Cooking Scrambled eggs made in the usual quick, offhand way are usually hard and forgettable. The key to moist scrambled eggs is low heat and patience; they will take several minutes to cook. The eggs should be added to the pan just as butter begins to bubble, or oil makes a water drop dance gently. Texture is determined by how and when the eggs are disturbed. Large, irregular curds result if the cook lets the bottom layer set for some time before scraping to distribute the heat. Constant scraping and stirring prevents the egg proteins at the bottom from setting into a separate, firm layer, and produces a creamy, even mass of yolk and thin white punctuated with very fine curds of thick white. Scrambled eggs should be removed from the pan while still slightly underdone, since they will continue to thicken for some time with their residual heat.\"\nOn Food and Cooking, Harold McGee')
		if sender == self.paletteView.group.scramblerButton:
				if not currentLayers:
						if self.paletteView.group.text.get() == ('egg'):
							thisFont.newTab(scrambledEggs)
						else:
							inputValue = int(self.newValue())
							for glyph in thisFont.glyphs:
								printableLayers.append('/'+ glyph.name)
							for i in range(inputValue):
								tab.append(random.choice(printableLayers))
							thisFont.newTab(''.join(tab))
				else:
						if self.paletteView.group.text.get() == ('egg'):
							thisFont.newTab(scrambledEggs)
						else:
							inputValue = int(self.newValue())
							for eachLayer in currentLayers:
								printableLayers.append('/'+ eachLayer.parent.name)
							for i in range(inputValue):
								tab.append(random.choice(printableLayers))
							thisFont.newTab(''.join(tab))

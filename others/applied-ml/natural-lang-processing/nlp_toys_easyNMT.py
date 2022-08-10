"""
	Set up the PyPI library for deep learning -based machine translation, so that it can be imported subsequently.

	The sacremoses package from PyPI helps to display languages from different parts of the world.
	
	pip install -U easynmt
	pip install sacremoses
"""

# Import the PyPI library module for deep learning -based machine translation.
from easynmt import EasyNMT
# Load one of the (pre-)trained machine translation models from the EasyNMT module.
model = EasyNMT('opus-mt')
# Translate birthday wishes, as several sentences, into different languages.
sentences = ['Happy Birthday!',
             'Have a great day!',
             'May your life be filled with joy!']

# Translate birthday wishes into Italian.
print(model.translate(sentences, target_lang='it'))
# Translate birthday wishes into Spanish.
print(model.translate(sentences, target_lang='es'))
# Translate birthday wishes into French.
print(model.translate(sentences, target_lang='fr'))
# Translate birthday wishes into Romanian.
print(model.translate(sentences, target_lang='ro'))
# Translate birthday wishes into Portuguese.
# Portuguese model fails to work, due to an Error being thrown.
#print(model.translate(sentences, target_lang='pt'))
# Translate birthday wishes into Mandarin/Chinese.
print(model.translate(sentences, target_lang='zh'))
# Translate birthday wishes into Hungarian.
print(model.translate(sentences, target_lang='hu'))
# Translate birthday wishes into Malayalam.
print(model.translate(sentences, target_lang='ml'))
# Translate birthday wishes into Hindi.
print(model.translate(sentences, target_lang='hi'))
# Translate birthday wishes into Malay.
# Malay model fails to work, due to an Error being thrown.
#print(model.translate(sentences, target_lang='ms'))
# Translate birthday wishes into Indonesian Malay.
print(model.translate(sentences, target_lang='id'))
# Translate birthday wishes into Vietnamese.
print(model.translate(sentences, target_lang='vi'))
# Translate birthday wishes into Tagalog/Filipino.
print(model.translate(sentences, target_lang='tl'))
# Translate birthday wishes into Dutch.
print(model.translate(sentences, target_lang='nl'))
# Translate birthday wishes into German.
print(model.translate(sentences, target_lang='de'))
# Translate birthday wishes into Swedish.
print(model.translate(sentences, target_lang='sv'))
# Translate birthday wishes into Korean.
#print(model.translate(sentences, target_lang='ko'))
# Translate birthday wishes into Hebrew.
print(model.translate(sentences, target_lang='he'))
# Translate birthday wishes into Arabic.
print(model.translate(sentences, target_lang='ar'))
# Translate birthday wishes into Kiswahili/Swahili.
print(model.translate(sentences, target_lang='sw'))

# Load another (pre-)trained machine translation model from the EasyNMT module.
model = EasyNMT('m2m_100_1.2B') 
# Translate birthday wishes into Portuguese.
print(model.translate(sentences, target_lang='pt'))
# Translate birthday wishes into Malay.
print(model.translate(sentences, target_lang='ms'))
# Translate birthday wishes into Turkish.
print(model.translate(sentences, target_lang='tr'))
# Translate birthday wishes into Japanese.
print(model.translate(sentences, target_lang='ja'))
# Translate birthday wishes into Korean.
print(model.translate(sentences, target_lang='ko'))
# Translate birthday wishes into Persian/Farsi.
print(model.translate(sentences, target_lang='fa'))
# Translate birthday wishes into Bulgarian.
print(model.translate(sentences, target_lang='bg'))
# Translate birthday wishes into Tamil.
print(model.translate(sentences, target_lang='ta'))
# Translate birthday wishes into Sinhala, or Singhalese.
print(model.translate(sentences, target_lang='si'))

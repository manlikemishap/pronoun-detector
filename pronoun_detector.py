import re

class PronounDetector:

	def __init__(self, language='en'):
		self.language = language

	def enumerate_pronouns(self, text):

		#self.femalePronouns = pronouns.female(self.language)
		#self.malePronouns = pronouns.male(self.language)
		#self.neutralPronouns = pronouns.neutral(self.language)

		femalePronouns = ['she', 'her', 'herself', 'hers']
		malePronouns = ['he', 'him', 'himself', 'his']
		neutralPronouns = ['Ne','nem','nir','nirs','nemself','Ve','ver','vis','vis','verself','ey','em','eir','eirs','eirself','ze','hir','hir','hirs','hirself','ze','zir','zir','zirs','zirself','Xe','xem','xyr','xyrs','xemself','they','it','their','theirs','them','themselves','itself','its']

		femaleCount = len(re.findall(' (' + '|'.join(femalePronouns)+'){1}[^A-Za-z0-9]+',text,re.I))
		maleCount = len(re.findall(' (' + '|'.join(malePronouns)+'){1}[^A-Za-z0-9]{1}',text,re.I))
		neutralCount = len(re.findall(' (' + '|'.join(neutralPronouns)+'){1}[^A-Za-z0-9]+',text,re.I))

		return {'female_pronouns':femaleCount, 'male_pronouns':maleCount, 'neutral_pronouns':neutralCount}
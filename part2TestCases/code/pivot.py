from dictionary import Dictionary, UnboundedProblemException
from copy import deepcopy

class Pivotter:
	def nextDictionary(self, dictionary):
		self.dictionary = dictionary
		try:
			self.entering = self.dictionary.enteringVariable()
			self.leaving = self.dictionary.leavingVariable(self.entering)
			return self.__pivot()
		except UnboundedProblemException:
			return self.dictionary

	def __pivot(self):
		new = Dictionary()
		(new.basic, new.noBasic) = self.__updateSets()
		enteringCoefs, enteringConst = self.__enteringCoefs()
		(new.coefs, new.consts) = self.__updateCoefs(enteringCoefs, enteringConst)
		(new.objective, new.objective[0]) = self.__updateObjective(enteringCoefs, enteringConst)
		return new

	def __updateSets(self):
		newBasic = self.dictionary.basic - {self.leaving}
		newBasic.add(self.entering)
		newNoBasic = self.dictionary.noBasic - {self.entering}
		newNoBasic.add(self.leaving)
		return (newBasic, newNoBasic)

	def __enteringCoefs(self):
		t,s 	= self.leaving, self.entering
		xt  	= deepcopy(self.dictionary.coefs[t])
		ats	 	= xt[s]
		xt.pop(s, None)
		xs  	= {k : - (xt[k] / ats) for k in xt.keys()}
		xs[t] = (1/ats)
		bs		= - (self.dictionary.consts[t] / ats)
		return (xs, bs)

	def __updateCoefs(self, enteringCoefs, enteringConst):
		t,s		= self.leaving, self.entering
		base	= self.dictionary.basic - {t}
		xs		= enteringCoefs
		bs		= enteringConst
		b			= dict()
		newCoefs = dict()
		for j in base:
			xj 		= deepcopy(self.dictionary.coefs[j])
			ajs 	= xj[s]
			xj.pop(s)
			xj[t]	= 0
			xj 		= {k : (xj[k] + xs[k]*ajs) for k in xs.keys()}
			b[j]	= self.dictionary.consts[j] + ajs*bs
			newCoefs[j] = xj
		newCoefs[s] = xs
		newConsts 	= b
		newConsts[s]= bs
		return (newCoefs, newConsts)

	def __updateObjective(self, enteringCoefs, enteringConst):
		t,s		= self.leaving, self.entering
		z		= deepcopy(self.dictionary.objective)
		cs		= self.dictionary.objective[s]
		c0		= self.dictionary.objective[0]
		xs		= enteringCoefs
		bs		= enteringConst
		z.pop(s)
		z[t]	= 0
		obje	= {k : z[k] + cs*xs[k] for k in xs.keys()}
		objV	= c0 + cs*bs
		return (obje, objV)

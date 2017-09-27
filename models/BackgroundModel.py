from pyDiamonds import Model
import numpy as np

class BackgroundModel(Model):
    def __init__(self, covariates, dimension, name):
        covariates = covariates.astype(float)
        Model.__init__(self,covariates)
        self._dimension = parameterDimensions
        self._name = name
        pass

    def getResponseFunction(self):
        return self._responseFunction

    def getNyquistFrequency(self):
        return self._nyquistFrequency

    def readNyquistFrequencyFromFile(self,fileName):
        self._nyquistFrequency = np.loadtxt(fileName).T

    def predict(self,predictions,modelParameters):
        raise NotImplementedError("You need to implement predict if you derive from BackgroundModel")

    @property
    def dimension(self):
        return self._dimension

    @property
    def name(self):
        return self._name
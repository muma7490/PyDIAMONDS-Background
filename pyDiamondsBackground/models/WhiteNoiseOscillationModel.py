import numpy as np

from pyDiamondsBackground.models.BackgroundModel import BackgroundModel


class WhiteNoiseOscillationModel(BackgroundModel):
    def __init__(self, covariates):
        self._covariates = covariates
        BackgroundModel.__init__(self, covariates, 10, "White noise oscillation model")

    def predict(self, predictions, modelParameters):
        flatNoiseLevel = modelParameters[0]
        amplitudeHarvey1 = modelParameters[1]
        frequencyHarvey1 = modelParameters[2]
        amplitudeHarvey2 = modelParameters[3]
        frequencyHarvey2 = modelParameters[4]
        amplitudeHarvey3 = modelParameters[5]
        frequencyHarvey3 = modelParameters[6]
        heightOscillation = modelParameters[7]
        nuMax = modelParameters[8]
        sigma = modelParameters[9]

        zeta = 2 * np.sqrt(2) / np.pi
        predictions = zeta * amplitudeHarvey1 ** 2 / (
            frequencyHarvey1 * (1 + np.power(self._covariates / frequencyHarvey1, 4)))

        predictions += zeta * amplitudeHarvey2 ** 2 / (
            frequencyHarvey2 * (1 + np.power(self._covariates / frequencyHarvey2, 4)))

        predictions += zeta * amplitudeHarvey3 ** 2 / (
            frequencyHarvey3 * (1 + np.power(self._covariates / frequencyHarvey3, 4)))

        predictions += heightOscillation * np.exp(-1*np.power(nuMax-self._covariates,2)/(2*sigma**2))

        predictions *= self._responseFunction

        predictions += flatNoiseLevel

        return predictions
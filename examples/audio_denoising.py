import math

import numpy as np
import soundfile

from wavelet.fast_transform import FastWaveletTransform
from wavelet.util import getExponent, threshold, mad

inputFile = "../example/input.wav"
outputFile = "../example/input_denoised.wav"

# reading the input file
data, rate = soundfile.read(inputFile)

# the implementation limit data to the power of 2
expo = getExponent(len(data))
s = math.pow(2, expo)

t = FastWaveletTransform(waveletName='haar')
coefficients = t.waveDec(data[: int(s)])

# calculating noise threshold value
sigma = mad(coefficients)
thresh = sigma * np.sqrt(2 * np.log(len(coefficients)))
coefficients = threshold(coefficients, thresh)

coefficients = t.waveRec(coefficients)

# writing the reconstructed file
soundfile.write(outputFile, coefficients, rate)

import os
from time import time

import numpy as np
import soundfile

from wavelet.fast_transform import FastWaveletTransform
from wavelet.util.utility import threshold, mad
from wavelet.wavelets import getAllWavelets

INPUT_FILE = "/example/inputs"
OUTPUT_DIR = "/example/output"

info = soundfile.info(INPUT_FILE)  # getting info of the audio
rate = info.samplerate

for wavelet in getAllWavelets():
    try:

        WAVELET_NAME = wavelet
        t = FastWaveletTransform(WAVELET_NAME)
        outputFileName = os.path.join(OUTPUT_DIR, "test_" + WAVELET_NAME + ".wav")

        with soundfile.SoundFile(outputFileName, "w", samplerate=rate, channels=1) as of:
            start = time()
            for block in soundfile.blocks(INPUT_FILE, int(rate * info.duration * 0.10)):  # reading 10 % of duration

                # processing only single channel
                if block.ndim > 1:
                    block = block.T
                    block = block[0]
                else:
                    block = block.flatten()

                coefficients = t.waveDec(block)

                # VISU Shrink
                sigma = mad(coefficients)
                thresh = sigma * np.sqrt(2 * np.log(len(block)))

                # thresholding using the noise threshold generated
                coefficients = threshold(coefficients, thresh)

                # getting the clean signal as in original form and writing to the file
                clean = t.waveRec(coefficients)
                clean = np.asarray(clean)
                of.write(clean)

            end = time()

            print(f"Finished processing with {WAVELET_NAME}")
            print(f"Time taken :: {end - start} s")
            print()

    except:
        print(f"Wavelet {wavelet} died")
        print()

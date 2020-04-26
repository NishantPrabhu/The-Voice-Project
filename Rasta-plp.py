import numpy as np
import numpy.matlib
import scipy
import scipy.io.wavfile as wav
from scipy.fftpack.realtransforms import dct
from sidekit.frontend.vad import pre_emphasis
from sidekit.frontend.io import *
from sidekit.frontend.normfeat import *
from sidekit.frontend.features import *


def PLP(file_path):
    rate, signal = wav.read(file_path)
    plp_features = plp(signal,rasta=True)
    print(plp_features)
    return plp_features

## You may get an error saying one of the functions is not found. Go to the source code file and add that function.
## The function exists in one of the other files in the same library

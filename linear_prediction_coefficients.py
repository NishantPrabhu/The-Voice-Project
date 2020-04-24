import matplotlib.pyplot as plt
import numpy as np
import time
import wave
import scipy.io.wavfile as wav
from scipy import signal
from audiolazy import lpc

## The function takes the path of the audio file and order of lpc as input and returns Linear Prediction coefficients
def LPC(file_path='audio_files/1.wav',order=13):
    rate, signal = wav.read(file_path)
    p = order
    ##preemphasize the signal
    emp_signal = np.append(signal[0],signal[1:]-0.97*signal[:-1]) #y[n] = x[n] - a*x[n-1]
    filt = lpc(emp_signal,order=p)
    lpc_coeff = filt.numerator[1:]
    return lpc_coeff

## Function to visualize the signal
def visualize(file_path='audio_files/1.wav'):
	#taking the signal's time
    rate, signal = wav.read(file_path)
	Time=np.linspace(0, len(signal)/rate, num=len(signal))
	#plots using matplotlib
	plt.figure(figsize=(10, 6))
	plt.subplot(facecolor='darkslategray')
	plt.title('Signal wave')
	plt.ylim(-40000, 40000)
	plt.ylabel('Amplitude', fontsize=16)
	plt.xlabel('Time(s)', fontsize=8)
	plt.plot(Time,signal,'C1')
	plt.draw()
	#plt.show()

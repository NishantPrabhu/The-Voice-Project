from pydub import AudioSegment

sound = AudioSegment.from_mp3("audio_files/1.mp3")
sound.export("audio_files/1.wav", format="wav")

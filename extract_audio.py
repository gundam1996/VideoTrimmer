import librosa, soundfile

audio, sr = librosa.load("./ToParse/test_candidate.MOV")
soundfile.write("./Output/shortened_test_candidate.FLAC", audio, sr, format="FLAC")

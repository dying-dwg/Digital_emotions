import speech_recognition as speech_r
# import pyaudio
# import wave
# import amfm_decompy.basic_tools as basic
# import amfm_decompy.pYAAPT as pYAAPT
# import matplotlib.pyplot as plt
# import numpy as np
# import sys
# import os
# import librosa.display
# import seaborn as sns
import telebot
import soundfile as sfl
# IPython.display as ipd
from CreateMsg import *
from emotion_recognition import EmotionRecognizer

from aubio import source, pitch
import os
import wave
from sys import byteorder
from array import array
from struct import pack
from sklearn.ensemble import GradientBoostingClassifier, BaggingClassifier
import  random
from utils import get_best_estimators

# кейсы применимости   те для кого и где
token = {'dan':"5667111210:AAFbvGosUzq11ey12f_a_ppxB_ltfz1JpEQ",'and':"5658170929:AAF-fKk5enZ7-cVaBpRVzFLJYwqnoc_Iobg"}
bot = telebot.TeleBot(token['and'])
THRESHOLD = 500
RATE = 16000
__detector: EmotionRecognizer

mood = {
	'happy':'OutEmojiMp4/happy.mp4',
	'neutral':'OutEmojiMp4/Neutral_1.mp4',
	'sad':f'OutEmojiMp4/Sad_{random.randint(1,3)}.mp4',
	'calm':'OutEmojiMp4/Calm.mp4',
	'angry':f'OutEmojiMp4/angry_{random.randint(1,2)}.mp4',
	'fear':'OutEmojiMp4/Fear.mp4',
	'disgust':'OutEmojiMp4/Disgust.mp4',
	'ps':f'OutEmojiMp4/Surprise_{random.randint(1,2)}.mp4',
	'boredom':'OutEmojiMp4/Скука.mp4'
}

def init():
	estimators = get_best_estimators(True)
	estimators_str, estimator_dict = get_estimators_name(estimators)
	import argparse

	parser = argparse.ArgumentParser(description = """
										Testing emotion recognition system using your voice, 
										please consider changing the model and/or parameters as you wish.
										""")
	parser.add_argument("-e", "--emotions", help =
	"""Emotions to recognize separated by a comma ',', available emotions are
	"neutral", "calm", "happy" "sad", "angry", "fear", "disgust", "ps" (pleasant surprise)
	and "boredom", default is "sad,neutral,happy"
	""", default = "neutral,happy,angry")#,calm,sad,fear,disgust,ps,boredom
	parser.add_argument("-m", "--model", help =
	"""	
	The model to use, 8 models available are: {},
	default is "BaggingClassifier"
	""".format(estimators_str), default = "BaggingClassifier")
	# Parse the arguments passed
	args = parser.parse_args()

	features = ["mfcc", "chroma", "mel"]
	global __detector
	__detector = EmotionRecognizer(estimator_dict[args.model], emotions = args.emotions.split(","), features = features,
								 verbose = 0, custom_db=False)
	__detector.train()
	print("Test accuracy score: {:.3f}%".format(__detector.test_score() * 100))
	print("Please talk")


def normalize(snd_data):
	"Average the volume out"
	MAXIMUM = 16384
	times = float(MAXIMUM)/max(abs(i) for i in snd_data)

	r = array('h')
	for i in snd_data:
		r.append(int(i*times))
	return r


def convert_audio(audio_path, target_path):
	try:
		strg = f"{audio_path[:audio_path.rfind('/')+1]}raw{audio_path[audio_path.rfind('/')+1:]}"
		print(strg)
		data, samplerate = sfl.read(audio_path)
		sfl.write(strg, data, samplerate)

	except Exception as e:
		pass
	"""This function sets the audio `audio_path` to:
		- 16000Hz Sampling rate
		- one audio channel ( mono )
			Params:
				audio_path (str): the path of audio wav file you want to convert
				target_path (str): target path to save your new converted wav file
				remove (bool): whether to remove the old file after converting
		Note that this function requires ffmpeg installed in your system."""
	if os.path.exists(target_path):
		os.remove(target_path)
	v = os.system(f"D:/ProjectsPyCharm/HackaTons/DigEm_2_0/venv/Lib/site-packages/imageio_ffmpeg/binaries/ffmpeg-win64-v4.2.2.exe -i {strg} -ac 1 -ar 16000 {target_path}")
	# os.system(f"ffmpeg -i {audio_path} -ac 1 {target_path}")
	if os.path.exists(strg):
		os.remove(strg)
	return v


def trim(snd_data):
	"Trim the blank spots at the start and end"
	def _trim(snd_data):
		snd_started = False
		r = array('h')

		for i in snd_data:
			if not snd_started and abs(i)>THRESHOLD:
				snd_started = True
				r.append(i)

			elif snd_started:
				r.append(i)
		return r

	# Trim to the left
	snd_data = _trim(snd_data)

	# Trim to the right
	snd_data.reverse()
	snd_data = _trim(snd_data)
	snd_data.reverse()
	return snd_data


def add_silence(snd_data, seconds):
	"Add silence to the start and end of 'snd_data' of length 'seconds' (float)"
	r = array('h', [0 for i in range(int(seconds*RATE))])
	r.extend(snd_data)
	r.extend([0 for i in range(int(seconds*RATE))])
	return r


def get_estimators_name(estimators):
	result = [ '"{}"'.format(estimator.__class__.__name__) for estimator, _, _ in estimators ]
	return ','.join(result), {estimator_name.strip('"'): estimator for estimator_name, (estimator, _, _) in zip(result, estimators)}


def run_check(filename, detector):
	#filename = "test.wav"

	#record_to_file(filename)

	result = detector.predict(filename)
	return result


def recognize(_filename):
	r = speech_r.Recognizer()
	r.energy_threshold = 300
	sample = speech_r.AudioFile(_filename)
	with sample as audio:
		content = r.record(audio)
	#with sample as audio:
	#	content = r.record(audio)
	#	r.adjust_for_ambient_noise(audio)
	try:
		result = r.recognize_google(content, language="ru-RU")
		print("in the try block")
		print(result)
	except speech_r.UnknownValueError as e:
		print("Текст не распознан")
		print(e)
		result = "Текст не распознан"
	return result


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	if message.text == "Привет":
		bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
	elif message.text == "/help":
		bot.send_message(message.from_user.id, "Напиши привет")
	elif message.text == "/letsgo":
		bot.send_message(message.from_user.id, "Полетели девачки")
	else:
		bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


@bot.message_handler(content_types=['voice'])
def voice_processing(message):
	file_name_ogg = f'__genaudio__/output{message.from_user.id}.ogg'
	file_name_wav = f'__genaudio__/output{message.from_user.id}.wav'
	pathVideoOut = f'__genvideo__/out{message.from_user.id}.mp4'
	file_info = bot.get_file(message.voice.file_id)
	downloaded_file = bot.download_file(file_info.file_path)
	with open(file_name_ogg, 'wb') as new_file:
		new_file.write(downloaded_file)
	new_file.close()

	convert_audio(file_name_ogg, file_name_wav)
	text_content = recognize(file_name_wav)
	print(text_content)
	bot.send_message(message.from_user.id, text_content)

	global __detector
	mood_content = run_check(file_name_wav, __detector)#настроение
	print(mood_content)
	bot.send_message(message.from_user.id, mood_content)

	createNewVideoNote(mood[mood_content], pathVideoOut, file_name_wav)
	bot.send_video_note(
		message.from_user.id,
		data=open(pathVideoOut, 'rb'),
		duration=None,
		length=None,
		disable_notification=False,
		reply_to_message_id=None,
		reply_markup=None,
		timeout=60,
		thumb=None
	)
	if os.path.exists(file_name_wav):
		os.remove(file_name_wav)
	if os.path.exists(file_name_ogg):
		os.remove(file_name_ogg)
	if os.path.exists(pathVideoOut):
		os.remove(pathVideoOut)


init()
bot.polling(none_stop=True, interval=0)

from telebot.types import ReplyKeyboardMarkup, KeyboardButton 

class Day(object):
	def __init__(self, *args):
		self.lessons = []
		for lesson in args:
			self.lessons.append(lesson)
	def get_lessons(self):
		lessons_text = ""
		number = 1
		for lesson in self.lessons:
			lessons_text += "{0}) {1}\n".format(number, lesson)
			number += 1
		return lessons_text
time_table_markup = ReplyKeyboardMarkup(row_width = 3)

days = ['Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba', 'Juma', 'Shanba']


weekday_buttons = [
	KeyboardButton(text = "Dushanba"),
	KeyboardButton(text = "Seshanba"),
	KeyboardButton(text = "Chorshanba"),
	KeyboardButton(text = "Payshanba"),
	KeyboardButton(text = "Juma"),
	KeyboardButton(text = "Shanba")
]

time_table_markup.add(*weekday_buttons)

EMPTY = "-----------------------------"

weekdays = [
	Day(EMPTY, EMPTY, EMPTY),
	Day("Elektron hukumat - 117A \xF0\x9F\x9A\xAA\nQuvnakov A \xF0\x9F\x92\xB0", "DTADTKK - 117A \xF0\x9F\x9A\xAA\nBoboyev L"),
	Day(EMPTY, EMPTY, EMPTY, "Chet tili - Kafedra \xF0\x9F\x9A\xAA\nMiss Diyora"),
	Day(EMPTY, "OT va L - 03B \xF0\x9F\x9A\xAA\n Ro'ziboyev O", "Tizimli Dasturlash - 117A \xF0\x9F\x9A\xAA\nKarimov D \xF0\x9F\x92\xB0", EMPTY),
	Day(EMPTY, EMPTY, "Dasturlash tamoyili - 109A \xF0\x9F\x9A\xAA\nMamaraufov O", EMPTY),
	Day("DTML - 522B \xF0\x9F\x9A\xAA\nKamalov Sh ", EMPTY, "Kompyuter Tarmoqlari - 117A \xF0\x9F\x9A\xAA\nXabirova D")
]

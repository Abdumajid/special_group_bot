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
	Day(
		"Ma'lumotlar kommunikatsiyasi - Mashq\n\xF0\x9F\x95\x90 10:00\n\xF0\x9F\x9A\xAA 310(D)",
		"Ma'lumotlar kommunikatsiyasi - Ma'ruza\n\xF0\x9F\x95\x90 11:30\n\xF0\x9F\x9A\xAA 115"
	),
	Day(
		"Axborot xavfsizligi - Mashq\n\xF0\x9F\x95\x90 13:30\n\xF0\x9F\x9A\xAA 205(D)",
		"DTADTKK - Ma'ruza\n\xF0\x9F\x95\x90 15:00\n\xF0\x9F\x9A\xAA 21(B)",
		"DTADTKK - Mashq\n\xF0\x9F\x95\x90 16:30\n\xF0\x9F\x9A\xAA 21(B)"
	),
	Day(
		"/Ilmiy tadqiqot metodologiyasi - Ma'ruza\n\xF0\x9F\x95\x90 11:30\n\xF0\x9F\x9A\xAA 310(D)",
		EMPTY,
		"WEB ilovalarni ishlab chiqish - Laboratoriya/Mashq\n\xF0\x9F\x95\x90 15:00\n\xF0\x9F\x9A\xAA 513(B)/515(B)",
		"Chet tili \n\xF0\x9F\x95\x90 16:30\n\xF0\x9F\x9A\xAA Kafedra"
	),
	Day(
		"OYDT - Ma'ruza\n\xF0\x9F\x95\x90 10:00\n\xF0\x9F\x9A\xAA 21(B)",
		"OYDT - Mashq\n\xF0\x9F\x95\x90 11:30\n\xF0\x9F\x9A\xAA 520(B)",
	),
	Day(
		"MKUDV - \n\xF0\x9F\x95\x90 11:30\n\xF0\x9F\x9A\xAA 21(B)",
		"Chet tili/O'zbekiston Tarixi - /Ma'ruza\n\xF0\x9F\x95\x90 10:00\n\xF0\x9F\x9A\xAA 445",
		"WEB ilovalarni ishlab chiqish - Ma'ruza\n\xF0\x9F\x95\x90 15:00\n\xF0\x9F\x9A\xAA 522(B)"
	),
	Day(
		"Axborot xavfsizligi - Ma'ruza\n\xF0\x9F\x95\x90 13:30\n\xF0\x9F\x9A\xAA 117",
		"TT va T - (Laboratoriya/Ma'ruza)\n\xF0\x9F\x95\x90 15:00\n\xF0\x9F\x9A\xAA 01(B)/518(B)",
		"TT va T - (Mashq)\n\xF0\x9F\x95\x90 16:30\n\xF0\x9F\x9A\xAA 01(B)/518(B)",
		
	
	)
]

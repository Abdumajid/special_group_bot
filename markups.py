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
		"Ma'lumotlar kommunikatsiyasi - Practice\n\xF0\x9F\x95\x90 Time: 10:00\n\xF0\x9F\x9A\xAA Room: 310(D)",
		"Ma'lumotlar kommunikatsiyasi - Lecture\n\xF0\x9F\x95\x90 Time: 11:30\n\xF0\x9F\x9A\xAA Room: 115"
	),
	Day(
		"Axborot xavfsizligi - Practice\n\xF0\x9F\x95\x90 Time: 13:30\n\xF0\x9F\x9A\xAA Room: 205(D)",
		"DTADTKK - Lecture\n\xF0\x9F\x95\x90 Time: 15:00\n\xF0\x9F\x9A\xAA Room: 21(B)",
		"DTADTKK - Practice\n\xF0\x9F\x95\x90 Time: 16:30\n\xF0\x9F\x9A\xAA Room: 21(B)"
	),
	Day(
		"/Ilmiy tadqiqot metodologiyasi - Lecture\n\xF0\x9F\x95\x90 Time: 11:30\n\xF0\x9F\x9A\xAA Room: 310(D)",
		EMPTY,
		"WEB ilovalarni ishlab chiqish - Laboratory/Practice\n\xF0\x9F\x95\x90 Time: 15:00\n\xF0\x9F\x9A\xAA Room: 513(B)/515(B)",
		"Chet tili \n\xF0\x9F\x95\x90 Time: 16:30\n\xF0\x9F\x9A\xAA Room: Har doimgi(kafedra)"
	),
	Day(
		"OYDT - Lecture\n\xF0\x9F\x95\x90 Time: 10:00\n\xF0\x9F\x9A\xAA Room: 21(B)",
		"OYDT - Practice\n\xF0\x9F\x95\x90 Time: 11:30\n\xF0\x9F\x9A\xAA Room: 520(B)",
	),
	Day(
		"MKUDV - \n\xF0\x9F\x95\x90 Time: 11:30\n\xF0\x9F\x9A\xAA Room: 21(B)",
		"Chet tili/O'zbekiston Tarixi - Lecture\n\xF0\x9F\x95\x90 Time: 10:00\n\xF0\x9F\x9A\xAA Room: 445",
		"WEB ilovalarni ishlab chiqish - Lecture\n\xF0\x9F\x95\x90 Time: 15:00\n\xF0\x9F\x9A\xAA Room: 522(B)"
	),
	Day(
		"Axborot xavfsizligi - Lecture\n\xF0\x9F\x95\x90 Time: 13:30\n\xF0\x9F\x9A\xAA Room: 117",
		"TT va T - (Laboratory/Lecture)\n\xF0\x9F\x95\x90 Time: 15:00\n\xF0\x9F\x9A\xAA Room: 01(B)/518(B)",
		"TT va T - (Practive)\n\xF0\x9F\x95\x90 Time: 16:30\n\xF0\x9F\x9A\xAA Room: 01(B)/518(B)",
		
	
	)
]

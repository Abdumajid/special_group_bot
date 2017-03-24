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
		"Ma'lumotlar kommunikatsiyasi - Mashq (Shukurov K)\n\xF0\x9F\x95\x90 10:00\n\xF0\x9F\x9A\xAA 310(D)",
		"Ma'lumotlar kommunikatsiyasi - Ma'ruza (Toshev S)\n\xF0\x9F\x95\x90 11:30\n\xF0\x9F\x9A\xAA 115"
	),
	Day(
		"Axborot xavfsizligi - Mashq (Mardiyev U)\n\xF0\x9F\x95\x90 13:30\n\xF0\x9F\x9A\xAA 205(D)",
		"DTADTKK - Ma'ruza (Boboyev L)\n\xF0\x9F\x95\x90 15:00\n\xF0\x9F\x9A\xAA 21(B)",
		"DTADTKK - Mashq (Boboyev L)\n\xF0\x9F\x95\x90 16:30\n\xF0\x9F\x9A\xAA 21(B)"
	),
	Day(
		"/Ilmiy tadqiqot metodologiyasi - Ma'ruza\n\xF0\x9F\x95\x90 11:30\n\xF0\x9F\x9A\xAA 310(D)",
		"Axborot xavfsizligi - Ma'ruza (Mardiyev U)\n\xF0\x9F\x95\x90 13:30\n\xF0\x9F\x9A\xAA 205(D)",
		"WEB ilovalarni ishlab chiqish - Laboratoriya/Mashq (Kerimov K)\n\xF0\x9F\x95\x90 15:00\n\xF0\x9F\x9A\xAA 513(B)/515(B)",
		"Chet tili \n\xF0\x9F\x95\x90 16:30\n\xF0\x9F\x9A\xAA Kafedra"
	),
	Day(
		"OYDT - Ma'ruza (Abdurahimov Qudrat)\n\xF0\x9F\x95\x90 10:00\n\xF0\x9F\x9A\xAA 21(B)",
		"OYDT - Mashq (Abdurahimov Qudrat)\n\xF0\x9F\x95\x90 11:30\n\xF0\x9F\x9A\xAA 520(B)",
	),
	Day(
		"DTADTK (Boboyev Lochin)\n\xF0\x9F\x95\x90 11:30\n\xF0\x9F\x9A\xAA 21(B)",
		"Chet tili/O'zbekiston Tarixi - /Ma'ruza\n\xF0\x9F\x95\x90 13:30\n\xF0\x9F\x9A\xAA 445",
		"WEB ilovalarni ishlab chiqish - Ma'ruza (Kerimov K)\n\xF0\x9F\x95\x90 15:00\n\xF0\x9F\x9A\xAA 522(B)"
	),
	Day(
		"TT va T - (Laboratoriya/Ma'ruza) (Kamalov Sh)\n\xF0\x9F\x95\x90 15:00\n\xF0\x9F\x9A\xAA 01(B)/518(B)",
		"TT va T - (Mashq) (Kamalov Sh)\n\xF0\x9F\x95\x90 16:30\n\xF0\x9F\x9A\xAA 01(B)/518(B)",
		
	
	)
]

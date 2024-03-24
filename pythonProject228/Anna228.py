import telebot
from Class import TheoryDB


API_TOKEN = '6950174779:AAEqq7utcgLHLWxmKCnczgLgN6OKiuiM4DA'
bot = telebot.TeleBot(API_TOKEN)



#объявление уровней
A1 = TheoryDB("A1")




#команда help
@bot.message_handler(commands=['help'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton("Грамматика")
    btn2 = telebot.types.KeyboardButton("Чтение")
    btn3 = telebot.types.KeyboardButton("Аудирование")
    btn4 = telebot.types.KeyboardButton("Говорение")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, text="Выберите нужный вам раздел",
                     reply_markup=markup)  # грамматика чтение аудирование говорение


#команда start
@bot.message_handler(commands=["start"])
def repeat_all_messages(message):
    # приветсвие
    bot.send_photo(message.chat.id, 'https://i.pinimg.com/originals/7a/9c/c3/7a9cc36f478969da92e2e9fee391a5b2.jpg',
                   caption=''' Приветствую тебя, мой милый котик, с этого момента я твой пушистый репетитор 😊.

Тебе не нужно меня бояться, ведь ругать за ошибки или отсутствие никто не будет! 
Могу только покусать хи-хи

Моя задача- сделать твое обучение максиально комфортным, несмотря на каком уровне ты находишься. Неважно, только начал ты свое обучение или уже готов лететь в Лондон, чтобы хвастаться своими навыками с носителями.
Всем нам здесь нужно как можно больше знаний и мотивации! 

И раз ты уже здесь я буду рад скрасить твое обучение

✨✨✨✨✨✨
''')


    #рекомендации
    bot.send_message(message.chat.id, '''
❗Хочу порекомендовать тебе❗

🌸 Завести тетрадочки для самостоятельных работ - первая для записи новых слов, а вторая для конспектирования теории, практики письменных задач

🌸 Попробовать найти репетитора или друга, который сможет отслеживать твой прогресс и тоже будет помогать в обучении

🌸 В изучении языка важна практика, постарайся внедрить английский в свою жизнь- слушай песни на английском, читай их тексты, выписывай новые слова и пробуй подпевать. 
Смотри фильмы и сериалы с субтитрами, слушай интервью носителей, подкасты

🌸 Самое главное- будь позитивно настроен и уверен в себе, ведь у тебя обязательно все получится, а я с радостью погому тебе с этим! ''')

    keyboard = telebot.types.InlineKeyboardMarkup()

    # добавляем на нее три кнопки
    button1 = telebot.types.InlineKeyboardButton(text="Начальный", callback_data="button1")
    button2 = telebot.types.InlineKeyboardButton(text="Средний", callback_data="button2")
    button3 = telebot.types.InlineKeyboardButton(text="Продвинутый", callback_data="button3")
    keyboard.add(button1, button2, button3)
    # отправляем сообщение пользователю
    bot.send_message(message.chat.id, f'''Пожалуйста, не стесняйся и выбери свой уровень знаний 😸''',
                     parse_mode='MarkdownV2', reply_markup=keyboard)



@bot.callback_query_handler(func=lambda call: call.data == "button1")
def callback_inline_button1(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    urovenA1 = telebot.types.InlineKeyboardButton(text="1️⃣ (A1)", callback_data="urovenA1")
    button5 = telebot.types.InlineKeyboardButton(text="2️⃣ (A2)", callback_data="button5")
    keyboard.add(urovenA1)
    keyboard.add(button5)
    bot.send_message(call.message.chat.id, '''Вы большой молодец, что начали изучать английский язык!
    *здесь должна быть мотивационная фраза но мой мозг уже отключается пхпхпх*
    Я с радостью помогу вам с этим!💓

    Какой раздел Вы бы хотели выбрать?

    1️⃣ Вы только приступили к обучению(A1)

    2️⃣ Вы уже умеете читать диалоги, владеете базовой грамматикой, понимаете несложное аудирование(A2)''',
                     reply_markup=keyboard)




@bot.callback_query_handler(func=lambda call: call.data == "urovenA1")
def callback_inline_urovenA1(call):
    text = "Первым делом попрошу тебя ознакомиться со списком тем уровня\n"
    for i in range(0, len(A1.full_opisanie())):
        text += (f"\U00002B50 {i+1}. {A1.full_opisanie()[i]} \n")

    bot.send_animation(call.message.chat.id,'https://media1.tenor.com/m/qnE69DpVcCoAAAAd/mrfresh-sad-cat.gif', caption=f'''
💓Поздравляю с началом обучения,
💓котёнок!
{text}
Введите:    
''', parse_mode='HTML')
    bot.send_sticker(call.message.chat.id,
                     'CAACAgIAAxkBAAELkvZl36ApehuUGQyMiLsAAUk8h9bH70wAAlonAAI-3iFI-YQyCDUbwek0BA')
    bot.send_message(call.message.chat.id, "Введите число, пожалуйста ")
    bot.register_next_step_handler(call.message, func1)

user_input = None
def func1(message):
    global user_input
    try:
        user_input = int(message.text)  # Конвертируем введённый пользователем текст в число
        response = A1.text(user_input)  # Получаем соответствующий текст из класса A1
        if response:  # Проверяем, что response не пустая
            bot.send_message(message.chat.id, response)
        bot.register_next_step_handler(message, func1)  # Регистрируем func1 для обработки следующего сообщения
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите правильное число.")
        bot.register_next_step_handler(message, func1)  # Регистрируем func1 для обработки следующего сообщения



@bot.callback_query_handler(func=lambda call: call.data == "button2")
def callback_inline_button2(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button6 = telebot.types.InlineKeyboardButton(text="1️⃣ (B1)", callback_data="button6")
    button7 = telebot.types.InlineKeyboardButton(text="2️⃣ (B2)", callback_data="button7")
    keyboard.add(button6)
    keyboard.add(button7)
    bot.send_message(call.message.chat.id, '''Вы уже можете похвастаться хорошим знанием языка!
Ваши силы и старания принесли вам такой замечательный результат!
Продолжайте в том же духе и еще большим энтузиазмом!💓

Какой раздел Вы бы хотели выбрать?

1️⃣ Вы неплохо разговариваете на английском и у вас есть понимание речи носителя (B1)

2️⃣ Вы спокойно дискутируете на различные темы, уверенно излагая собственные мысли, соблюдая правильное произношение (B2)''',
                     reply_markup=keyboard)



@bot.callback_query_handler(func=lambda call: call.data == "button3")
def callback_inline_button3(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button6 = telebot.types.InlineKeyboardButton(text="1️⃣ (C1)", callback_data="button6")
    button7 = telebot.types.InlineKeyboardButton(text="2️⃣ (C2)", callback_data="button7")
    keyboard.add(button6)
    keyboard.add(button7)
    bot.send_message(call.message.chat.id, '''Вы уже настоящий профи и точно знаете, какой раздел, вы бы хотели выбрать!

Выражаю Вам уважение за этот долгий путь изучения языка, Вашей мотивации можно только позавидовать!
Так держать!💓

Какой раздел Вы бы хотели выбрать?

1️⃣ У Вас свободное владение языком, практически отсутствуют грамматические ошибки (C1)

2️⃣ У Вас английский на уровне носителя, доскональное знание грамматики, можете даже преподавать (C2)''', reply_markup=keyboard)

bot.polling(none_stop=True)
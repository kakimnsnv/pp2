import pyrogram, psycopg2, os, re
from psycopg2.extras import DictCursor
from dotenv import load_dotenv
load_dotenv()

# Connecting to postgreSQL database--------------------------------------------------------
connection = psycopg2.connect(
    host='localhost',
    database='telegramBot',
    user='kakimbekn',
    password='Sadasa@2015'
)
connection.autocommit = True

# database cursor configuration------------------------------------------------------------
cursor = connection.cursor()

# creating table if not exists
createTable = '''
    CREATE TABLE IF NOT EXISTS users(
        id VARCHAR(20),
        username VARCHAR(100),
        name VARCHAR(100),
        surname VARCHAR(100),
        phoneNumber VARCHAR(20),
        chatId VARCHAR(20));
'''
cursor.execute(createTable)
connection.commit()

# Environmental variables-----------------------------------------------------------------
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_API_ID = os.getenv("TELEGRAM_API_ID")
TELEGRAM_API_HASH = os.getenv("TELEGRAM_API_HASH")

# Variables--------------------------------------------------------------------------------
id = ""
name = ""
surname = ""
username = ""
chatId = ""
phoneNumber = ""
messageId = 0

newUsername = ""
newPhoneNumber = ""
newChatId = ''
newName = ''
newSurname = ''

phonePattern = "\d{11}|\d{10}|\d{1}[(]\d{3}[)]\d{7}|\d{1}[(]\d{3}[)]-\d{3}-\d{2}-\d{2}|\d{1}[(]\d{3}[)] \d{3} \d{2} \d{2}|[(]\d{3}[)]-\d{3}-\d{2}-\d{2}|[(]\d{3}[)] \d{3} \d{2} \d{2}|[(]\d{3}[)] \d{3}-\d{2}-\d{2}|[(]\d{3}[)]\d{7}"

inline_keyboard = pyrogram.types.InlineKeyboardMarkup([
    [
        pyrogram.types.InlineKeyboardButton(
            text='Registration',
            callback_data='registerCallback'
        )
    ],
    [
        pyrogram.types.InlineKeyboardButton(
            text='by:Kakimbek Nyssanov',
            url='t.me/kakimnsnv'
        ),
        pyrogram.types.InlineKeyboardButton(
            text='github',
            url="https://github.com/kakimnsnv"
        )
    ]
])

register_keyboard = pyrogram.types.ReplyKeyboardMarkup([
    [pyrogram.types.KeyboardButton(text="Отправить номер", request_contact=True)]
    ], one_time_keyboard=True, resize_keyboard=True, placeholder="Нажмите на кнопку")
changeSurname = pyrogram.types.InlineKeyboardMarkup([
    [pyrogram.types.InlineKeyboardButton(text="Yes, I'm sure",callback_data="changeSurname")],
    [pyrogram.types.InlineKeyboardButton(text="Cancel", callback_data="cancel changeSurname")]
    ])

changeName = pyrogram.types.InlineKeyboardMarkup([
    [pyrogram.types.InlineKeyboardButton(text="Yes, I'm sure",callback_data="changeName")],
    [pyrogram.types.InlineKeyboardButton(text="Cancel", callback_data="cancel changeName")]
    ])

bot_commands = [
    pyrogram.types.BotCommand(
        command='start',description='Start, log in.'
    ),
    pyrogram.types.BotCommand(
        command='help',description='Help'
    ),
    pyrogram.types.BotCommand(
        command='setsurname',description='Set / change surname'
    ),
    pyrogram.types.BotCommand(
        command='setname',description='Set / change name.'
    ),
    pyrogram.types.BotCommand(
        command='setphone',description='Set / change phone number.'
    ),
    pyrogram.types.BotCommand(
        command='getme',description='Shows your data'
    )
]

# --------------------------------------------------------------------------------Variables

# Creating bot instance------------------------------------------------------------
bot = pyrogram.Client("ps5_28bot", api_id=TELEGRAM_API_ID, api_hash=TELEGRAM_API_HASH, parse_mode=pyrogram.enums.ParseMode.HTML)

# bot handlers----------------------------------------------------------------------
@bot.on_message(pyrogram.filters.command('start') & pyrogram.filters.private)
def command_start(_, message):
    global id
    global name
    global surname
    global username
    global chatId

    id = str(message.from_user.id)
    name = message.from_user.first_name
    surname = message.from_user.last_name
    username = message.from_user.username
    chatId = message.chat.id

    cursor.execute('SELECT phonenumber FROM users WHERE id = %s', (str(message.from_user.id),))
    if cursor.fetchone() == None:
        message.reply(
            '''Здравствуйте, это бот для управления плейстейшн клубом PS5_28, кажется вы у нас не зарегистрированы.''',
            reply_markup=inline_keyboard)
    else:
        cursor.execute('SELECT name, surname FROM users WHERE id = %s', (str(message.from_user.id),))
        res = cursor.fetchall()
        message.reply(f"Добро пожаловать, {res[0][0]} {res[0][1]}.")

@bot.on_message(pyrogram.filters.command('help') & pyrogram.filters.private)
def help(bot, message):
    cursor.execute('SELECT surname, name FROM users WHERE id = %s', (str(message.from_user.id),))
    res = cursor.fetchall()
    message.reply(
        f'''Hey {res[0][0]} {res[0][1]}, how you doing ?
        
This bot is created by @kakimnsnv.
If you have any question about me, just ask him.

So these are my commands:
/start - to start bot or login,
/help - obviously to show this message,
/getme - shows all your data from database.

Also if you have any missing information or mistake you can set it by:
/setsurname - to set/change surname,
/setname - to set/change name,
/setphone - to set/change phone number''')

@bot.on_message(pyrogram.filters.command('getme') & pyrogram.filters.private)
def getme(bot, message):
    cursor.execute("SELECT * FROM users WHERE id = %s", (str(message.from_user.id),))
    res = cursor.fetchone()
    if res == []:
        message.reply("Kажется вы у нас не зарегистрированы.")
    else:
        message.reply(f'''id : {res[0]},
username : {res[1]},
name : {res[2]},
surname : {res[3]},
phone number : {res[4]},
chat id : {res[5]}.
    ''')
    
@bot.on_message(pyrogram.filters.command('setsurname') & pyrogram.filters.private)
def setsurname(bot, message):
    global newSurname
    global messageId
    messageId = message.id + 1
    if len(message.command) == 1 or len(message.command) > 2:
        message.reply('Usage of this command is /setsurname "surname that you want to set".')
    else:
        cursor.execute('SELECT surname FROM users WHERE id = %s', (str(message.from_user.id),))
        res = cursor.fetchall()
        newSurname = message.command[1]
        message.reply(f'''You are going to change your surname on database
    from : {res[0][0]} 
    to : {message.command[1]}''', reply_markup=changeSurname)

@bot.on_message(pyrogram.filters.command('setname') & pyrogram.filters.private)
def setname(bot, message):
    global newName
    global messageId
    messageId = message.id + 1
    if len(message.command) == 1 or len(message.command) > 2:
        message.reply('Usage of this command is /setname "name that you want to set".')
    else:
        cursor.execute('SELECT name FROM users WHERE id = %s', (str(message.from_user.id),))
        res = cursor.fetchall()
        newName = message.command[1]
        message.reply(f'''You are going to change your name on database
    from : {res[0][0]} 
    to : {message.command[1]}''', reply_markup=changeName)


@bot.on_callback_query()
def Callback(Client, CallbackQuery):
    global newSurname
    global id
    global messageId
    global newName
    if CallbackQuery.data == 'registerCallback':
        CallbackQuery.message.reply("Вы начали процесс регистрации. Для начала отправьте нам ваш номер", reply_markup=register_keyboard)
    elif CallbackQuery.data == 'changeSurname':
        cursor.execute('UPDATE users SET surname = %s WHERE id = %s', (newSurname, str(CallbackQuery.from_user.id)))
        cursor.execute('SELECT chatid FROM users WHERE id = %s', (str(CallbackQuery.from_user.id),))
        res = cursor.fetchall()[0][0]
        bot.edit_message_text(res, messageId,'''<i>You are going to change your surname on database...</i>

Succesfully changed
Try /getme again''')
    elif CallbackQuery.data == "cancel changeSurname":
        cursor.execute('SELECT chatid FROM users WHERE id = %s', (str(CallbackQuery.from_user.id),))
        res = cursor.fetchall()[0][0]
        bot.edit_message_text(res, messageId, '''<i>You are going to cahange your surname on database...</i>

<b>Canceled</b>''')
    elif CallbackQuery.data == 'changeName':
        cursor.execute('UPDATE users SET name = %s WHERE id = %s', (newName, str(CallbackQuery.from_user.id)))
        cursor.execute('SELECT chatid FROM users WHERE id = %s', (str(CallbackQuery.from_user.id),))
        res = cursor.fetchall()[0][0]
        bot.edit_message_text(res, messageId,'''<i>You are going to change your name on database...</i>

Succesfully changed
Try /getme again''')
    elif CallbackQuery.data == "cancel changeSurname":
        cursor.execute('SELECT chatid FROM users WHERE id = %s', (str(CallbackQuery.from_user.id),))
        res = cursor.fetchall()[0][0]
        bot.edit_message_text(res, messageId, '''<i>You are going to cahange your name on database...</i>

<b>Canceled</b>''')
    
@bot.on_message(pyrogram.filters.contact)
def contact(bot, message):
    global name
    global surname
    global username
    global chatId
    global id

    cursor.execute('SELECT phonenumber FROM users WHERE username = %s', (username,))
    if cursor.fetchall() == []:
        phoneNumber = message.contact.phone_number
        SQLcontactRegister = f'INSERT INTO users VALUES(%s, %s, %s, %s, %s, %s);'
        cursor.execute(SQLcontactRegister, (id, username, name, surname, phoneNumber, chatId))
        message.reply('Вы зарегистрированы, введите команду "/start" заново')
    else:
        message.reply(f"You sent a contact !")


@bot.on_message(pyrogram.filters.private)
def onMessage(bot, message):
    global id
    global phoneNumber
    res = re.findall(phonePattern, message.text)
    if id != '' and phoneNumber != '':
        message.reply(message.text)
    elif id == "":
        message.reply("You haven't registered yet. Please register first.")
    elif res == [] and phoneNumber == "":
        message.reply('''Напишите номер в одном из форматов:
77777777777
7777777777
7(777)7777777
7(777)-777-77-77
7(777) 777 77 77
(777)-777-77-77
(777) 777 77 77
(777) 777-77-77
(777)7777777
''')
    elif res[0] != message.text:
        message.reply('''Напишите номер в одном из форматов:
77777777777
7777777777
7(777)7777777
7(777)-777-77-77
7(777) 777 77 77
(777)-777-77-77
(777) 777 77 77
(777) 777-77-77
(777)7777777
''')
    else:
        phoneNumber = res[0]
        SQLcontactRegister = f'INSERT INTO users VALUES(%s, %s, %s, %s, %s, %s);'
        cursor.execute(SQLcontactRegister, (id, username, name, surname, phoneNumber, chatId))
        message.reply('Вы зарегистрированы, введите команду "/start" заново')

# ----------------------------------------------------------------------bot handlers

# run the bot
bot.start()
bot.set_bot_commands(bot_commands)
pyrogram.idle()
bot.stop()

# closing the cursor, commiting to db and closing db connection
cursor.close()
connection.commit()
connection.close()

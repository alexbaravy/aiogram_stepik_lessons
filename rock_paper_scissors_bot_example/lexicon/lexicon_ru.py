LEXICON_RU: dict[str, str] = {
    'start': 'Привет! Я бот игры "Камень-ножницы-бумага"! Ты готов сыграть со мной в игру\n',
    'help': 'Правила игры очень просты:\n'
            ' \n'
            '🗿 побеждает ✂️ (камень затупляет ножницы).\n'
            '✂️ побеждают 📄 (ножницы режут бумагу).\n'
            '📄 побеждает 🗿 (бумага заворачивает камень).\n',
    'play': 'Сделайте свой выбор!\n',
    'stop': 'Жаль, что вам надоело, но вы можете начать заново /start\n',
    'no_echo': 'Данный тип апдейтов не поддерживается '
               'методом send_copy',
    'something': 'Кнопочки видишь? Нажимай! Не видишь? Жми /start',
    'user_won': 'Вы победили',
    'bot_won': 'Компьютер победил',
    'nobody_won': 'Ничья',
    'bet_info': "Вы: {user_choice} | Комьютер: {bot_choice}",
    'stat': 'Всего игр сыграно: {total_games}\n'
            '************************\n'
            'Игр выиграно: {wins}\n'
            'Игр вничью: {draws}\n'
            'Игр проиграно: {loses}\n'
            '*************************\n'
            'Процент побед: {per_wins}%\n'
            'Процент ничьих: {per_draws}%\n'
            'Процент проигрышей: {per_loses}%\n',
    'rock': '🗿',
    'paper': '📜',
    'scissors': '✂️',
    'yes_button': 'Давай!',
    'no_button': 'Не хочу!',
    'help_button': 'Помощь',
    'stat_button': 'Статистика',
    'exit_button': 'Выйти',

}

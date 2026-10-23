import random
list_of_question = [
"У вас є слово, яке ви вигадали самі?",
"Ви коли-небудь брехали про свій вік?",
"Який найбільший жарт, який ви коли-небудь робили?",
"У вас є який-небудь дивний або особливий талант?",
"Чи співаєте ви в ванні?",
"Як ви намагаєтесь обманути, щоб уникнути допомоги з домашніми справами?",
"Ви боїтесь привидів?",
"Чи коли-небудь ви поливали рослину молоком?",
"Чи коли-небудь ви щось зламали, не розповідаючи про це нікому?",
"Якщо вам дали 1 хвилину, щоб швидко вийти з будинку, що б ви взяли з собою?"
]
list_of_action = [
"Не моргай протягом хвилини.",
"Пробігти навколо будинку три рази.",
"Обійміть ваш поштовий ящик (або дерево/прикрасу на газоні) протягом 20 секунд.",
"Розмовляйте з виставленим язиком.",
"Виконайте дію, якщо ви наступний гравець для вибору категорії Дія.",
"Напишіть комусь повідомлення, використовуючи лише ніс.",
"Уявіть, що ви граєте на повітряній гітарі.",
"Заспівайте дитячу пісеньку.",
"Розмовляйте та поводьтесь, як робот.",
"Після кожної вашої фрази додайте слова 'Ого... я молодець!' протягом наступних 15 хвилин."
]
gamer_list = []
def gamers(list):
    while True:
        name = input("Введіть ім'я гравця - ")
        if 0 < len(name) <= 2:
            continue
        list.append(str.capitalize(name))
        if len(list)>=2:
            need_next_player = input("Додати ще гравців? - Так(т) / Ні(н)")
            if need_next_player == str.lower("т") or need_next_player == str.lower("так"):
                continue
            else:
                break
gamers(gamer_list)

def game(list_of_question, list_of_action, *args):
    while True:
        next_step = None
        for gamer in args:
            print(gamer)
            user_choise = input("Питання(п) або Дія(д)? ")
            if user_choise == str.lower("п") or user_choise == str.lower("питання"):
                question_index = random.randint(0, len(list_of_question) - 1)
                print(list_of_question[question_index])
                list_of_question.pop(question_index)
            elif user_choise == str.lower("д") or user_choise == str.lower("дія"):
                action_index = random.randint(0, len(list_of_action) - 1)
                print(list_of_action[action_index])
                list_of_action.pop(action_index)
            else:
                print("Виберіть питання(п) або дію(д)")
                question_index = random.randint(0, len(list_of_question) - 1)
                print(list_of_question[question_index])
                list_of_question.pop(question_index)
                action_index = random.randint(0, len(list_of_action) - 1)
                print(list_of_action[action_index])
                list_of_action.pop(action_index)
            if args[-1] == gamer:
                break
        next_step = input("Наступний гравець? - Так(т)/Ні(н)")
        if next_step == str.lower("т") or next_step == str.lower("так"):
            continue
        else:
            print("Гра закінчена")
            break
        if next_step == str.lower('т') or next_step == str.lower('так'):
            pass
        else:
            break
        select = input("Новий раунд? - Так(т)/Ні(н)")
        if select == str.lower("т") or select == str.lower("так"):
            continue
        else:
            break

game(list_of_question, list_of_action, *gamer_list)
import re

def create_hashtag_link(tag_word):  # функция форматирования
    return f'<a href="/tag/{tag_word[1:]}">{tag_word}</a>'

""" За главный тег поста принимает первый тег, который был напечатан в посте"""
def return_first_tag(con):  # Функция возврата первого тега в посте
    for word in con.split():
        if word[0] == "#" and len(word) > 1:
            return "#" + re.sub(r'[^\w\s]', '', word)  # Удаление запрещённых знаков
    return ""  # возвращает пустую строку, если хэштэг не был найден


def content_edit_hashtag_links(con):  # Функция замены хэштэгов на ссылки
    hashtag_list = []
    con = re.split(r'(\s+)', con)  # Из строки в список с сохранением пробелов
    for word_index in range(len(con)):
        if con[word_index][0] == "#" and con[word_index] not in hashtag_list and len(con[word_index]) > 1:
            hashtag_list.append(con[word_index])
            con[word_index] = create_hashtag_link(con[word_index])
    con = ''.join(str(word) for word in con)
    return con


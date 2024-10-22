from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from random import choice
browser = webdriver.Chrome()

request = input("Что ищем? ")
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
assert "Википедия" in browser.title

search_box = browser.find_element(By.ID, "searchInput")
search_box.send_keys(request)
search_box.send_keys(Keys.RETURN)
a = browser.find_element(By.LINK_TEXT, "Солнечная система")
a.click()

option = input("Выбери одно из дествий: [1] - листать параграфы текущей статьи, "
               "[2] - перейти на одну из связанных страниц, [3] - выйти из программы")
if option == '1':
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    #Для перебора пишем цикл
    for paragraph in paragraphs:
        print(paragraph.text)
        q = input('Нажми Enter для продолжения или пробел для выхода: ')
        if q == ' ' :
            break
elif option == '2':
    hatnotes = []
    for elem in browser.find_elements(By.TAG_NAME, "div"):
        cl = elem.get_attribute("class")
        if cl == 'hatnote navigation-not-searchable':
            hatnotes.append(elem)

    print(hatnotes)
    hatnote = choice(hatnotes)
    link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
    browser.get(link)
    option2 = input("Выбери одно из дествий: [1] - листать параграфы текущей статьи, "
                   "[2] - перейти на одну из внутренних статей, [3] - выйти из программы")
    if option2 == '1':
        paragraphs = browser.find_elements(By.TAG_NAME, "p")
        for paragraph in paragraphs:
            print(paragraph.text)
            q = input('Нажми Enter для продолжения или пробел для выхода: ')
            if q == ' ' :
                break
    elif option2 == '2':
        links = browser.find_elements(By.TAG_NAME, "a")
        #Для перебора пишем цикл
        for link in links:
            print(link.text)
            q = input('Нажми Enter для продолжения или пробел для выхода: ')
            if q == ' ' :
                break

elif option == '3':
    browser.quit()
print('Всего хорошего!')
browser.quit()
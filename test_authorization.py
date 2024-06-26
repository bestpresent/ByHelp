#валидные данные
from selene import browser, be, have

browser.open('https://dev.byhelp.ru/authorization')
browser.element('[id=rc-tabs-0-tab-password]').click()
(browser.element('[id=authorization-by-password_email]').should(be.blank).type('karmatestirovschicy@yandex.ru'))
(browser.element('[id=authorization-by-password_password]').should(be.blank).type('12345678').press_enter())


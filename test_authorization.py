#валидные данные
from selene import browser, be, have

browser.open('https://dev.byhelp.ru/authorization')
browser.element('[id=rc-tabs-0-tab-password]').click()
(browser.element('[id=authorization-by-password_email]').should(be.blank).type('karmatestirovschicy@yandex.ru'))
(browser.element('[id=authorization-by-password_password]').should(be.blank).type('12345678').press_enter())

#авторизация с невалидным логином
from selene import browser, be, have

browser.open('https://dev.byhelp.ru/authorization')
browser.element('[id=rc-tabs-0-tab-password]').click()
(browser.element('[id=authorization-by-password_email]').should(be.blank).type('karmates123tirovschicy@yandex.ru'))
(browser.element('[id=authorization-by-password_password]').should(be.blank).type('12345678').press_enter())

#авторизация с невалидным паролем
from selene import browser, be, have

browser.open('https://dev.byhelp.ru/authorization')
browser.element('[id=rc-tabs-0-tab-password]').click()
(browser.element('[id=authorization-by-password_email]').should(be.blank).type('karmatestirovschicy@yandex.ru'))
(browser.element('[id=authorization-by-password_password]').should(be.blank).type('00045678').press_enter())

#авторизация с пустой формой
from selene import browser, be, have

browser.open('https://dev.byhelp.ru/authorization')
browser.element('[id=rc-tabs-0-tab-password]').click()
(browser.element('[id=authorization-by-password_email]').should(be.blank).type(' '))
(browser.element('[id=authorization-by-password_password]').should(be.blank).type(' ').press_enter())

#авторизация с пустым логином, но валидным паролем
from selene import browser, be, have

browser.open('https://dev.byhelp.ru/authorization')
browser.element('[id=rc-tabs-0-tab-password]').click()
(browser.element('[id=authorization-by-password_email]').should(be.blank).type(' '))
(browser.element('[id=authorization-by-password_password]').should(be.blank).type('12345678').press_enter())

#авторизация с пустым паролем, но валидным логином
from selene import browser, be, have

browser.open('https://dev.byhelp.ru/authorization')
browser.element('[id=rc-tabs-0-tab-password]').click()
(browser.element('[id=authorization-by-password_email]').should(be.blank).type('karmatestirovschicy@yandex.ru'))
(browser.element('[id=authorization-by-password_password]').should(be.blank).type(' ').press_enter())

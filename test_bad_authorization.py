#авторизация с невалидным логином
from selene import browser, be

browser.open('https://dev.byhelp.ru/authorization')
browser.element('#rc-tabs-0-tab-password').click()
browser.element('#authorization-by-password_email').should(be.blank).type('karmates123tirovschicy@yandex.ru')
browser.element('#authorization-by-password_password').should(be.blank).type('12345678').press_enter()

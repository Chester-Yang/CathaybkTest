# -*- coding: UTF-8 -*-
import WebTools

"""
2-1. Enter the credit card menu and take the screenshot.
"""
web = WebTools.WebBrowser()
web.setup()
web.homepage()
web.card_menu()
web.browser.get_screenshot_as_file("2. cathaybk_credit_card_menu_items.png")

"""
2-2. Calculate the credit card items in the menu.
"""
element = {'class': 'cubre-o-menuLinkList__content'}
credit_card_contents = web.beautifulsoup_and_find(web.browser.page_source, "html.parser", "div", flag=True, **element)
credit_card_items = credit_card_contents.find_all('a', {'id': 'lnk_Link'})
for credit_card_item in credit_card_items:
    print(credit_card_item.get_text())
print("信用卡列表項目數量為: {}".format(len(credit_card_items)))

web.teardown()

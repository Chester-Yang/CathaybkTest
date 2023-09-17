# -*- coding: UTF-8 -*-
import WebTools

"""
3-1. Enter the credit card menu, calculate the credit card amount, and take the screenshot.
"""
web = WebTools.WebBrowser()
web.setup()
web.homepage()
web.card_menu()
web.card_introduction()
element = {"class": "cubre-m-compareCard__title"}
card_production_contents = web.beautifulsoup_and_find(web.browser.page_source, "html.parser", "div", **element)
card_productions = [card_production_content.get_text() for card_production_content in card_production_contents]
print("所有信用卡的總數量為: {}".format(len(card_productions)))
web.browser.get_screenshot_as_file("3-1. card_productions.png")

"""
3-2. Compare out-of-production credit cards with screenshot credit card quantity.
"""
out_of_production_card = []
for i in range(1, 14):
    out_of_production_card.append(card_productions[-i])
if(len(out_of_production_card) != 13):
    print("Check failed, 與網頁上的數量不一致。")
print("停發卡總數量為: {}".format(len(out_of_production_card)))
web.browser_find_element("//a[@class='cubre-m-anchor__btn swiper-slide'][@data-anchor-btn='blockname06']")
web.browser.get_screenshot_as_file("3-2. out_of_production_card.png")

web.teardown()

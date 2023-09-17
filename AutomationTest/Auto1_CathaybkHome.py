# -*- coding: UTF-8 -*-
import WebTools

"""
1. Open the browser and take the screenshot.
"""
web = WebTools.WebBrowser()
web.setup()
web.homepage()
web.browser.get_screenshot_as_file("1. cathaybk_HomePage.png")
web.teardown()

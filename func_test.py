from splinter import Browser

browser=Browser("chrome")
url = "http://127.0.0.1:8000"
browser.visit(url)
assert 'Django' in browser.title


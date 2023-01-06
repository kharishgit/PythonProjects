from selenium import webdriver
search = input("Enter topic")
search=search.replace(' ','+')
browser = webdriver.Chrome('chromedriver')
for i in range(1):
    res = browser.get("https://www.google.com/search?q="+search+"&start"+str(i))
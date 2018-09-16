# Get the User object for twitter...
def crawl(url):
    chromedriverPath = "你的本地driver地址"
    # twitter每次更新13条
    eachCount = 13
    # 滚动几次。滚动次数越多，采集的数据越多
    scrollTimes = 100
    # driver = webdriver.Firefox()
    driver = webdriver.Chrome(chromedriverPath)
    driver.get(url)
    try:
        for i in range(scrollTimes):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            lastTweetCss = "#stream-items-id >li:nth-of-type(" + str(eachCount * (i + 2) + 1) + ") .tweet-text"
            print lastTweetCss
            elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, lastTweetCss)))
            printTweet(driver)
    finally:
        driver.close()

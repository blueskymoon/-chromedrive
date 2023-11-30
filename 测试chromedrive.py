
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service=Service(executable_path='D:/Chrome低版本103内部版本/Chrome_1170582/chrome-win/chromedriver.exe')  # 将路径替换为您解压缩的ChromeDriver的实际路径

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location= 'D:/Chrome低版本103内部版本/Chrome_1170582/chrome-win/chrome.exe' # 将路径替换为您免安装版Chrome可执行文件的实际路径

browser = webdriver.Chrome(service=service,options=chrome_options)
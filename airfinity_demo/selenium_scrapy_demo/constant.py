from shutil import which

SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH = which("D:\downloads\chromedriver.exe")
SELENIUM_DRIVER_ARGUMENTS=['-headless']  # '--headless' if using chrome instead of chrome

from Page.page_login import Login_Page


class Page:
    def __init__(self, driver):
        self.driver = driver

    @property
    def initloginpage(self):
        return Login_Page(self.driver)


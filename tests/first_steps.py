import logging
import time
from datetime import timedelta

import allure


class FirstSteps():
    @allure.step("Create stuff")
    def create_stuff(self):
        for index in range(60):
            logging.getLogger().info("Start sleep for 10 seconds")
            delay = timedelta(seconds=10)
            time.sleep(delay.total_seconds())
        pass

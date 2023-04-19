import pytest
from pages.trails_page import Trails


@pytest.mark.usefixtures('setup')
class BaseTests:

    @pytest.fixture
    def init(self):
        driver = self.driver
        self.trials_page = Trails(driver)

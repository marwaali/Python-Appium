from tests.base_tests import BaseTests
from settings import TEST_DATA


class TestCases(BaseTests):

    def test_search(self, init):
        # Fetch Data from YAML file and use it in test cases instead of hard coding
        self.trials_page.search_for_trail(trial_name=TEST_DATA['trail']['name'])




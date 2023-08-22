import os
import time
import pytest
from pages.explore_neuron_density import ExploreNeuronDensityPage
from util.util_links_checker import LinkChecker


class TestExploreNeuronDensity:
    @pytest.mark.build_page
    @pytest.mark.run(order=7)
    def test_explore_neuron_density_page(self, setup, login, logger):
        browser, wait = setup
        explore_ndensity_page = ExploreNeuronDensityPage(browser, wait)
        explore_ndensity = explore_ndensity_page.go_to_explore_neuron_density_page()
        assert explore_ndensity == "https://bbp.epfl.ch/mmb-beta/explore/neuron-density"

        validate_table_fields = explore_ndensity_page.perform_full_validation()

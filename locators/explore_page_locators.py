# Copyright (c) 2024 Blue Brain Project/EPFL
#
# SPDX-License-Identifier: Apache-2.0

from selenium.webdriver.common.by import By


class ExplorePageLocators:
    EXPLORE_LINK1 = (By.XPATH, "//a[@href='/mmb-beta/explore/simulation-campaigns']//h1[text("
                               ")='Brain & cells annotations']")
    EXPLORE_TITLE = (By.XPATH, "//a[text()='Explore']")
    INTERACTIVE_EXPLORATION = (By.XPATH, "//h2[text()='Interactive exploration']")
    EXPERIMENTAL_DATA_BTN = (By.XPATH, "//button[text()='Experimental data']")
    MODEL_DATA_BTN = (By.XPATH, "//button[text()='Model data']")
    LITERATURE = (By.XPATH, "//button[text()='Literature']")
    NEURON_ELECTROPHYSIOLOGY = (By.XPATH, "//h3[contains(text(),'Neuron "
                                          "electrophysiology')]//ancestor::a[1]["
                                          "@href='/app/explore/electrophysiology']")
    NEURON_MORPHOLOGY = (By.XPATH, "//h3[contains(text(),'Neuron morphology')]//ancestor::a[1]["
                                   "@href='/app/explore/morphology']")
    BOUTON_DENSITY = (By.XPATH, "//h3[contains(text(),'Bouton density')]//ancestor::a[1]["
                                "@href='/app/explore/bouton-density']")
    NEURON_DENSITY = (By.XPATH, "//h3[contains(text(),'Neuron density')]//ancestor::a[1]["
                                "@href='/app/explore/neuron-density']")
    SYNAPSE_PER_CONNECTION = (By.XPATH, "//h3[contains(text(),'Synapse per "
                                        "connection')]//ancestor::a[1]["
                                        "@href='/app/explore/synapse-per-connection']")
    EXPLORE_URL = (By.XPATH, "//a[@href='/app/explore']")
    LITERATURE_LINK = (By.ID, "#explore-navigation-/explore/literature")
    MORPHOLOGY_NRECORDS = (By.XPATH, "//a[@data-testid='experiment-dataset"
                                     "-ExperimentalNeuronMorphology']//span[@class='mr-2 "
                                     "font-light']")
    NEURON_EPHYS_NRECORDS = (By.XPATH, "//a[@data-testid='experiment-dataset"
                                       "-ExperimentalElectroPhysiology']//span[@class='mr-2 "
                                       "font-light']")
    NEURON_DENSITY_NRECORDS = (By.XPATH, "//a[@data-testid='experiment-dataset"
                                         "-ExperimentalNeuronDensity']//span[@class='mr-2 "
                                         "font-light']")
    BOUTON_DENSITY_NRECORDS = (By.XPATH, "//a[@data-testid='experiment-dataset"
                                         "-ExperimentsBoutonDensity']//span[@class='mr-2 "
                                         "font-light']")
    SYNAPSE_PER_CONNECTION_NRECORDS = (By.XPATH, "//a[@data-testid='experiment-dataset"
                                                 "-ExperimentalSynapsePerConnection']//span["
                                                 "@class='mr-2 font-light']")

    BRAIN_REGION_PANEL = (By.XPATH, "//span[text()='Brain region']")
    BRP_CEREBRUM = (By.XPATH, "//span[@title='Cerebrum' and text()='Cerebrum']")
    CEREBRUM_BTN = (By.XPATH, "(//button[@type='button' and @aria-expanded='false'])[3]")
    CEREBRAL_CORTEX_TITLE = (By.XPATH, "//span[@title='Cerebral Cortex']")
    ATLAS = (By.CSS_SELECTOR, "div[id='3d-area']")
    ATLAS_FULLSCREEN = (By.CSS_SELECTOR, "span[class='anticon anticon-fullscreen h-5 w-5 text-xl']")
    FULLSCREEN_EXIT = (By.CSS_SELECTOR, "span[aria-label='fullscreen-exit']")
    NEURONS_PANEL = (By.CSS_SELECTOR, "div[id='neurons-panel']")
    COUNT_SWITCH = (By.CSS_SELECTOR, "button[type='button'][role='switch'][aria-checked='false']")

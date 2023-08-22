from selenium.webdriver.common.by import By


class ExplorePageLocators:
    EXPLORE_URL = (By.XPATH, "//a[@href='/mmb-beta/explore']")
    EXPLORE_LINK1 = (By.XPATH, "//a[@href='/mmb-beta/explore/simulation-campaigns']//h1[text()='Brain & cells annotations']")
    EXPLORE_TITLE = (By.XPATH, "//h1[text()='Explore']")
    BRAIN_CELL_ANNOTATIONS = (By.XPATH, "//h1[text()='Brain & cells annotations']")
    BRAIN_CELL_ANNOTATIONS_URL = (By.XPATH,  "//a[@href='/mmb-beta/simulation-campaigns']")
    EXPERIMENTAL_DATA = (By.XPATH, "//h2[contains(text(), 'Experimental Data')]")
    EXPERIMENTAL_DATA_BUTTON = (By.XPATH, "//h2[contains(text(),'Experimental Data')]//ancestor::div[2]")
    BRAIN_MODELS = (By.XPATH, "//h2[text()='Brain Models']")
    BRAIN_MODELS_LINK = (By.XPATH, "//h2[contains(text(),'Brain Models')]//ancestor::a[1][@href='/mmb-beta/explore/brain-models']")
    SIMULATIONS_LINK = (By.XPATH, "//h2[contains(text(),'Simulations')]//ancestor::a[1][@href='/mmb-beta/explore/simulation-campaigns']")
    PORTALS_LINK = ()
    GALLERY_LINK = ()
    LITERATURE_LINK = ()
    SIMULATIONS = (By.XPATH, "//h2[text()='Simulations']")
    PORTALS = (By.XPATH, "//h2[text()='Portals']")
    GALLERY = (By.XPATH, "//h2[text()='Gallery']")
    LITERATURE = (By.XPATH, "//h2[text()='Literature']")
    NEURON_ELECTROPHYSIOLOGY = (By.XPATH, "//h3[contains(text(),'Neuron electrophysiology')]//ancestor::a[1][@href='/mmb-beta/explore/electrophysiology']")
    NEURON_MORPHOLOGY = (By.XPATH, "//h3[contains(text(),'Neuron morphology')]//ancestor::a[1][@href='/mmb-beta/explore/morphology']")
    BOUTON_DENSITY = (By.XPATH, "//h3[contains(text(),'Bouton density')]//ancestor::a[1][@href='/mmb-beta/explore/bouton-density']")
    NEURON_DENSITY = (By.XPATH, "//h3[contains(text(),'Neuron density')]//ancestor::a[1][@href='/mmb-beta/explore/neuron-density']")
    LAYER_THICKNESS = (By.XPATH, "//h3[contains(text(),'Layer thickness')]//ancestor::a[1][@href='/mmb-beta/explore/layer-thickness']")
    SYNAPSE_PER_CONNECTION = (By.XPATH, "//h3[contains(text(),'Synapse per connection')]//ancestor::a[1][@href='/mmb-beta/explore/synapse-per-connection']")


"""
This module contains shared fixtures.
"""
import json
import pytest
import selenium.webdriver

@pytest.fixture
def config(scope='session'):

    # Read the file
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    assert config['browser'] in ['Firefox' , 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # return config so it can be used
    return config    
    
@pytest.fixture
def browser(config):
        
    # Initialize  the WebDrive instance
    if config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Make its calls wait for elements to apper
    b.implicitly_wait(config['implicit_wait'])

    # Return the webdrive  instance for the setup
    yield b

    # Quit the webdrive instance for the cleanup
    b.quit()       
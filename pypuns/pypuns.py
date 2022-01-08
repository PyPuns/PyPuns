import random

from .puns.languages import all_languages


class LanguageNotFoundError(Exception):
    pass

class CategoryNotFoundError(Exception):
    pass



# Gets all puns of a category.
def get_all_puns(language='en', category='all', puns_file='default'):
    """
    PARAMETERS
    __________
    language: str
        possibilities: 'en', 'it'
    category: str
        possibilities: 'all', 'blackhumor', 'thonguetwist', 'puns'
    puns_file: str
        possibilities: 'default'
    ----------------------------
    OUTPUT
    ______
    puns: list
    """

    if language not in all_languages:
        raise LanguageNotFoundError(f'Currently the {language} language is not supported. Submit your puns for this new language on github!')

    puns = all_languages[language]

    if category not in puns:
        raise CategoryNotFoundError(f'Currently the {category} category is not supported. Submit new categories for the {language} language on github!')

    return puns[category]
    


# Random selection of a pun from all puns of a category.
def get_pun(language='en', category='all', puns_file='default'):
    """
    PARAMETERS
    __________
    language: str
        possibilities: 'en', 'it'
    category: str
        possibilities: 'all', 'blackhumor', 'thonguetwist', 'puns'
    puns_file: str
        possibilities: 'default'
    ----------------------------
    OUTPUT
    ______
    pun: str
    """

    pun = get_all_puns(language, category, puns_file)
    
    return random.choice(pun)

import random
import string

from yacut.models import URLMap
from yacut.variables import MAX_ATTEMPTS, LEN_OF_DEFAULT_LINK


def get_unique_short_id():
    """
    Creates a unique id.
    """
    source_symbols = string.ascii_letters + string.digits
    max_attempts = MAX_ATTEMPTS
    for _ in range(max_attempts):
        short_link = ''.join(random.choice(source_symbols)
                             for _ in range(LEN_OF_DEFAULT_LINK))
        if not URLMap.query.filter_by(short=short_link).first():
            return short_link
    raise Exception(f'Невозможно сгенерировать id после {max_attempts}.')

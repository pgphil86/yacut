import random
import string

from yacut.models import URLMap


def get_unique_short_id():
    """
    Creates a unique id.
    """
    source_symbols = string.ascii_letters + string.digits
    short_link = ''.join(random.choice(source_symbols)
                         for __ in range(6))
    if URLMap.query.filter_by(short=short_link).first():
        return get_unique_short_id()
    return short_link

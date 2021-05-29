try:
    # Trying to find module in the parent package
    from webscrapwrite2 import article2
except ImportError:
    from .webscrapwrite2 import article2
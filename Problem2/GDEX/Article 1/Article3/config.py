try:
    # Trying to find module in the parent package
    from webscrapwrite3 import article3
except ImportError:
    from .webscrapwrite3 import article3
import logging

# if cp_test_nn is imported, make sure the importer doesn't see
#  any logs by default, but can choose to enable them by calling
#  cp_test_nn.logging_setup()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
log.addHandler(logging.NullHandler())

def logging_setup(level=logging.INFO):
    handler = logging.StreamHandler()
    handler.setLevel(level)
    log.addHandler(handler)

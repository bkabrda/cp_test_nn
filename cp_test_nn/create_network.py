from cp_test_nn.process import process
from cp_test_nn.tokenizer import create_token_dict
from cp_test_nn.dataset import create_dataset
from cp_test_nn.train import train
from cp_test_nn.util import FAILS_FILE, TOKEN_DICT_FILE, DATASET_FILE

def create_network(input):
    process(input, FAILS_FILE)
    create_token_dict(FAILS_FILE, TOKEN_DICT_FILE)
    create_dataset(FAILS_FILE, TOKEN_DICT_FILE, DATASET_FILE)
    return train(DATASET_FILE)

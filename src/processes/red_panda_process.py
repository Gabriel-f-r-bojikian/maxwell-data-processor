import multiprocessing as mp


PARSED_DATA_QUEUE = mp.Queue()


def red_panda_process():
    while parsed_data := PARSED_DATA_QUEUE.get(block=True):
        # Send parsed data to Red Panda
        print(parsed_data)

import multiprocessing as mp

from services import (
    fft_data_analysis_service,
    send_parsed_data_service,
)


FFT_PROCESS_QUEUE = mp.Queue()


def fft_process():
    while fft_data := FFT_PROCESS_QUEUE.get(block=True):
        parsed_data = fft_data_analysis_service(fft_data)
        send_parsed_data_service(parsed_data)

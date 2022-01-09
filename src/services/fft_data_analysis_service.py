from typing import List

from numpy import abs, array, float64
from numpy.fft import fft, fftfreq
from numpy.typing import NDArray

from py_types import Buffer


def _fft(signal: NDArray[float64]):
    transform = fft(signal)
    transform_normalized = 2.0 * abs(transform / signal.size)

    return transform_normalized


def fft_data_analysis_service(fft_data: Buffer) -> List[dict]:
    sampling_rate = 1920  # Hz
    # Frequencies in fraction of sample rate
    freq = fftfreq(len(fft_data.dt))  # type: ignore
    # Mask with positive frequency values
    mask = freq > 0

    VA_transform = _fft(array(fft_data.VA))[mask]
    VB_transform = _fft(array(fft_data.VB))[mask]
    VC_transform = _fft(array(fft_data.VC))[mask]
    IA_transform = _fft(array(fft_data.IA))[mask]
    IB_transform = _fft(array(fft_data.IB))[mask]
    IC_transform = _fft(array(fft_data.IC))[mask]

    return [
        sampling_rate * 2 * freq[mask],
        VA_transform,
        VB_transform,
        VC_transform,
        IA_transform,
        IB_transform,
        IC_transform,
    ]

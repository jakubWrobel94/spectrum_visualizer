import numpy as np
from scipy import signal as sp_signal


class FftChunkToLargeException(Exception):
    pass


class FftHandler:
    def __init__(self, nfft=2048, chunk_size=2048, sample_rate=44100, window='hanning'):
        self.amplitude_spectrum = np.zeros(nfft)
        self.phase_spectrum = np.zeros(nfft)
        self.f_vector = np.linspace(0, nfft, sample_rate)

        self._nfft = nfft
        self._chunk_size = chunk_size
        self._sample_rate = sample_rate

        self._window = window
        self._window_values = self._create_window_function()
        self._fft_in = np.zeros(nfft)

    def calculate_freq_and_phase_spectrum(self, chunk):
        if self._window_values is not None:
            chunk = chunk * self._window_values
        if chunk.shape[0] <= self.nfft:
            self._fft_in[:chunk.shape[0]] = chunk
        else:
            raise FftChunkToLargeException(f'Chunk size = {chunk.shape[0]} is larger than fft size {self.nfft}')
        raw_fft = np.fft.fft(chunk, n=self.nfft)
        freq_spec = np.abs(raw_fft)
        phase_spec = np.angle(raw_fft)
        return self.f_vector, freq_spec, phase_spec

    def _create_window_function(self):
        if self._window == 'hanning':
            window = sp_signal.hanning(self._chunk_size)
        else:
            window = None
        return window

    @property
    def nfft(self):
        return self._nfft

    @nfft.setter
    def nfft(self, value):
        self._nfft = value
        self.f_vector = np.linspace(0, self._nfft, self._sample_rate)

    @property
    def sample_rate(self):
        return self._nfft

    @sample_rate.setter
    def sample_rate(self, value):
        self._sample_rate = value
        self.f_vector = np.linspace(0, self._nfft, self._sample_rate)

    @property
    def chunk_size(self):
        return self._chunk_size

    @chunk_size.setter
    def chunk_size(self, value):
        self._chunk_size = value
        self._window_values = self._create_window_function()
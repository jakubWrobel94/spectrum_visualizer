from input_audio_stream_provider import InputAudioStreamProvider
from fft_handler import FftHandler


class RealTimeSpectrumController:
    def __init__(self):
        self.input_devices_info = InputAudioStreamProvider.get_input_available_devices()

        default_host_api_info = InputAudioStreamProvider.get_default_host_api_info()
        default_input_device_info = InputAudioStreamProvider.get_default_input_device()
        default_output_device_info = InputAudioStreamProvider.get_default_output_device()

        self.host_api_index = default_host_api_info['index']
        self.host_api_name = default_host_api_info['name']

        self.input_device_index = default_input_device_info['index']
        self.output_device_index = default_output_device_info['index']

        self.input_device_name = default_input_device_info['name']
        self.output_device_name = default_output_device_info['name']

        self.max_input_channels = default_input_device_info['maxInputChannels']
        self._sample_rate = int(default_input_device_info['defaultSampleRate'])

        self._chunk_size = 2048
        self._nfft = self.chunk_size
        self._input_channel_index = 0

        self.current_chunk = None
        self.stream_provider = InputAudioStreamProvider(self.input_device_index, self.output_device_index,
                                                        self._input_channel_index, self._sample_rate, self._chunk_size,
                                                        self.max_input_channels)
        self.stream_provider.add_observer(self)
        self.fft_handler = FftHandler(self._nfft, self._chunk_size, self._sample_rate)

        self.amplitude_spectrum = self.fft_handler.amplitude_spectrum
        self.phase_spectrum = self.fft_handler.phase_spectrum
        self.frequency_vector = self.fft_handler.f_vector

    def update(self, chunk):
        self.fft_handler.calculate_freq_and_phase_spectrum(chunk)

    def start_stream(self):
        self.stream_provider.open_stream()

    def stop_stream(self):
        self.stream_provider.stop_stream()

    def close_stream(self):
        self.stream_provider.close_stream()

    @property
    def sample_rate(self):
        return self._sample_rate

    @sample_rate.setter
    def sample_rate(self, value):
        self.close_stream()
        self.stream_provider.sample_rate = value
        self.fft_handler.sample_rate = value

    @property
    def chunk_size(self):
        return self._chunk_size

    @chunk_size.setter
    def chunk_size(self, value):
        self.chunk_size = value
        self.close_stream()
        self.stream_provider.chunk_size = value
        self.fft_handler.chunk_size = value

    @property
    def nfft(self):
        return self._nfft

    @nfft.setter
    def nfft(self, value):
        self.nfft = value
        self.fft_handler.nfft = value

    @property
    def input_channel_index(self):
        return self._input_channel_index

    @input_channel_index.setter
    def input_channel_index(self, value):
        self.input_channel_index = value
        self.close_stream()
        self.stream_provider.input_channel_index = value


if __name__ == '__main__':
    controller = RealTimeSpectrumController()
    controller.start_stream()
    print('a')
    for n in range(0, 100000000):
        pass
    print('b')
    controller.stop_stream()
    print('c')
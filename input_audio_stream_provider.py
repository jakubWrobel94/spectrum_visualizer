import numpy as np
import pyaudio as pa
from typing import Optional


class InputAudioStreamProvider:
    """
    Class which provides audio stream handling.
    """
    _py_audio_obj = pa.PyAudio()

    def __init__(self, input_device_index: int, output_device_index: int, input_channel_index: int,
                 sample_rate: int = 44100, chunk_size: int = 256, channels_number: int = 2):

        self.input_device_index = input_device_index
        self.output_device_index = output_device_index
        self.input_channel_index = input_channel_index
        self.sample_rate = sample_rate
        self.chunk_size = chunk_size
        self.channels_number = channels_number

        self.current_chunk = np.zeros(self.chunk_size)

        self._stream: Optional[pa.Stream] = None
        self._observers = []

    def open_stream(self):
        if self._stream is None:
            self._stream = self._py_audio_obj.open(rate=self.sample_rate,
                                                   frames_per_buffer=self.chunk_size,
                                                   format=pa.paFloat32,
                                                   input_device_index=self.input_device_index,
                                                   input=True,
                                                   output_device_index=self.output_device_index,
                                                   output=True,
                                                   channels=self.channels_number,
                                                   stream_callback=self._callback_function)
        else:
            if self._stream.is_stopped():
                self._stream.start_stream()

    def stop_stream(self):
        if self._stream is not None:
            self._stream.stop_stream()

    def close_stream(self):
        if self._stream.is_active():
            self._stream.stop_stream()
            self._stream.close()
            self._stream = None

    def _callback_function(self, in_data, frame_count, time_info, status):
        frames = np.frombuffer(in_data, dtype=np.float32).reshape(-1, self.channels_number)
        self.current_chunk = frames[:, self.input_channel_index]
        return in_data, pa.paComplete

    def add_observer(self, observer):
        self._observers.append(observer)

    def _notify_observes(self):
        for observer in self._observers:
            observer.update(self.current_chunk)

    @staticmethod
    def get_all_devices_info():
        devices = {}
        for device_index in range(InputAudioStreamProvider._py_audio_obj.get_device_count()):
            devices[device_index] = InputAudioStreamProvider._py_audio_obj.get_device_info_by_index(device_index)
        return devices

    @staticmethod
    def get_input_available_devices():
        input_devices = {}
        for device_index in range(InputAudioStreamProvider._py_audio_obj.get_device_count()):
            device_info = InputAudioStreamProvider._py_audio_obj.get_device_info_by_index(device_index)
            if device_info['maxInputChannels'] > 0:
                input_devices[device_index] = device_info
        return input_devices

    @staticmethod
    def get_default_host_api_info():
        return InputAudioStreamProvider._py_audio_obj.get_default_host_api_info()

    @staticmethod
    def get_default_input_device():
        return InputAudioStreamProvider._py_audio_obj.get_default_input_device_info()

    @staticmethod
    def get_default_output_device():
        return InputAudioStreamProvider._py_audio_obj.get_default_output_device_info()

    @staticmethod
    def get_all_host_api_info():
        host_api_info = {}
        for host_api_index in range(InputAudioStreamProvider._py_audio_obj.get_host_api_count()):
            host_api_info[host_api_index] = InputAudioStreamProvider._py_audio_obj.get_host_api_info_by_index(host_api_index)
        return host_api_info

    @staticmethod
    def get_input_devices_by_host_api_index(host_api_index):
        input_devices = {}
        for device_index in range(InputAudioStreamProvider._py_audio_obj.get_device_count()):
            device_info = InputAudioStreamProvider._py_audio_obj.get_device_info_by_index(device_index)
            if device_info['maxInputChannels'] > 0 and device_info['hostApi'] == host_api_index:
                input_devices[device_index] = device_info
        return input_devices

    @staticmethod
    def get_output_devices_by_host_api_index(host_api_index):
        output_devices = {}
        for device_index in range(InputAudioStreamProvider._py_audio_obj.get_device_count()):
            device_info = InputAudioStreamProvider._py_audio_obj.get_device_info_by_index(device_index)
            if device_info['maxOutputChannels'] > 0 and device_info['hostApi'] == host_api_index:
                output_devices[device_index] = device_info
        return output_devices

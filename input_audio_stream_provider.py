import numpy as np
import pyaudio as pa
from typing import Optional


class InputAudioStreamProvider:
    """
    Class which provides audio stream handling.
    """
    _py_audio_obj = pa.PyAudio()

    def __init__(self, audio_device_index: int, input_channel_index: int,
                 sample_rate: int = 44100, chunk_size: int = 256, channels_number: int = 2):

        self.audio_device_index = audio_device_index
        self.input_channel_index = input_channel_index
        self.sample_rate = sample_rate
        self.chunk_size = chunk_size
        self.channels_number = channels_number

        self.current_chunk = np.zeros(self.chunk_size)
        self.f_new_chunk = False

        self._stream: Optional[pa.Stream] = None

    def open_stream(self):
        if self._stream is None:
            self._stream = self._py_audio_obj.open(rate=self.sample_rate,
                                                   frames_per_buffer=self.chunk_size,
                                                   format=pa.paFloat32,
                                                   input_device_index=self.audio_device_index,
                                                   channels=self.channels_number)
        else:
            if self._stream.is_stopped():
                self._stream.start_stream()

    def close_stream(self):
        if self._stream.is_active():
            self.stream.stop_stream()
            self.stream.close()

    def _callback_function(self, in_data, frame_count, time_info, status):
        frames = np.frombuffer(in_data, dtype=np.float32).reshape(-1, self._channels)
        self.current_chunk = frames[:, self._input_channel_idx]
        self.f_new_chunk = True
        return in_data, pa.paComplete

    @staticmethod
    def get_available_devices():
        devices = {}
        for device_index in range(InputAudioStreamProvider._py_audio_obj.get_device_count()):
            devices[device_index] = InputAudioStreamProvider._py_audio_obj.get_device_info_by_index(device_index)
        return devices

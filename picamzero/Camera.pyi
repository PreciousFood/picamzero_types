from typing import Any, Literal, Callable, TypeVar
from functools import wraps

import numpy as np

T = TypeVar("T")

class Camera:
    pc2: Any # PiCamera2
    hflip: bool
    vflip: bool

    def __init__(self) -> None:
        """
            Creates a Camera object based on a Picamera2 object

            :param Picamera2 pc2:
                An internal Picamera2 object. This can be accessed by
                advanced users who want to use methods we have not
                wrapped from the Picamera2 library.
        """

    def __del__(self):
        """
        Cleanup the Camera instance when it is deleted
        """

    @property
    def preview_size(self) -> tuple[int, int]: ...

    @preview_size.setter
    def preview_size(self, size: tuple[int, int]):
        """
        Width and height must be integers greater than 15
        """

    @property
    def still_size(self) -> tuple[int, int]: ...

    @still_size.setter
    def still_size(self, size: tuple[int, int]) -> None:
        """
        Width and height must be integers greater than 15
        """

    @property
    def video_size(self) -> tuple[int, int]: ...

    @video_size.setter
    def video_size(self, size: tuple[int, int]) -> None:
        """
        Width and height must be integers greater than 15
        """

    @property
    def brightness(self) -> float:
        """
        Get the brightness

        :return float:
            Brightness value between -1.0 and 1.0
        """

    @brightness.setter
    def brightness(self, bvalue: float):
        """
        Set the brightness

        :param float bvalue:
            Floating point number between -1.0 and 1.0
        """

    @property
    def contrast(self) -> float:
        """
        Get the contrast

        :return float:
            Contrast value between 0.0 and 32.0
        """

    @contrast.setter
    def contrast(self, cvalue: float):
        """
        Set the contrast

        :param float cvalue:
            Floating point number between 0.0 and 32.0
            Normal value is 1.0
        """

    @property
    def exposure(self) -> int:
        """
        Get the exposure

        :returns int:
            Exposure value (max and min depend on mode)
        """

    @exposure.setter
    def exposure(self, etime: int):
        """
        Set the exposure

        :param int etime:
            The exposure time (max and min depend on mode)
        """
    @property
    def gain(self) -> float:
        """
        Get the gain

        :returns float:
            Gain value (max and min depend on mode)
        """

    @gain.setter
    def gain(self, gvalue: float):
        """
        Set the analogue gain

        :param float gvalue:
            The analogue gain (max and min depend on mode)
        """

    @property
    def white_balance(self) -> Literal["auto", "tungsten", "fluorescent", "indoor", "daylight", "cloudy"] | None:
        """
        Get the white balance mode

        :return str:
            The selected white balance mode as a string
        """

    @white_balance.setter
    def white_balance(self, wbmode: Literal["auto", "tungsten", "fluorescent", "indoor", "daylight", "cloudy"]):
        """
        Set the white balance mode

        :param str wbmode:
            A white balance mode from the allowed list
            (at present, Custom is not allowed)
        """

    @property
    def greyscale(self) -> bool: ...

    @greyscale.setter
    def greyscale(self, on: bool) -> None:
        """
        Apply greyscale to the preview and image
        You have to call this _after_ the preview has started or it wont apply
        Does NOT apply to video

        :param bool on:
            Whether greyscale should be on
        """

    @staticmethod
    def retain_controls(method: Callable[..., T | None]) -> Callable[..., T | None]:
        """
        Decorator to note the controls status before a method
        and return to that state after the method ends.

        Apply by adding @retain_controls before method definition.
        """
        @wraps(method)
        def wrapper(self, *args, **kwargs) -> T | None: ...

    def flip_camera(self, vflip: bool = False, hflip: bool = False) -> None:
        """
        Flip the image horizontally or vertically
        """

    @retain_controls
    def start_preview(self) -> None:
        """
        Show a preview of the camera
        """

    @retain_controls
    def stop_preview(self) -> None:
        """
        Stop the preview
        """

    def annotate(self, 
                 text: str = "Default Text", 
                 font = "plain1", 
                 color: tuple[int, int, int, int] = (255, 255, 255, 255), 
                 scale: int = 3, 
                 thickness: int  = 3, 
                 position: tuple[int, int] = (0, 0), 
                 bgcolor: tuple[int, int, int, int]| None = None) -> None:
        """
        Set a text overlay on the preview and on images
        """

    def add_image_overlay(self, image_path: str, position: tuple[int, int]=(0, 0), transparency: float=0.5) -> None: ...

    @retain_controls
    def take_video_and_still(self, filename: str|None=None, duration: float=20, still_interval: float=4):
        """
        Take video for <duration> and take a still every <interval> seconds?
        """

    @retain_controls
    def capture_array(self) -> np.ndarray:
        """
        Takes a photo at full resolution and saves it as an
        (RGB) numpy array.

        This can be used in further processing using libraries
        like opencv.

        :return np.ndarray:
            A full resolution image as a raw RGB numpy array
        """
    
    @retain_controls
    def take_photo(self, filename: str|None=None, 
                   gps_coordinates: tuple[
                       tuple[float, float, float, float], 
                       tuple[float, float, float, float]
                       ]|None=None) -> str:
        """
        Takes a jpeg image using the camera
        :param str filename: The name of the file to save the photo.
        If it doesn't end with '.jpg', the ending '.jpg' is added.
        :param tuple[tuple[float, float, float, float],
                     tuple[float, float, float, float]] gps_coordinate:
        The gps coordinates to be associated
        with the image, specified as a (latitude, longitude) tuple where
        both latitude and longitude are themselves tuples of the
        form (sign, degrees, minutes, seconds). This format
        can be generated from the skyfield library's signed_dms
        function.


        Returns the filename
        """

    # Synonym method for take a picture
    capture_image = take_photo

    @retain_controls
    def capture_sequence(self, 
                         filename: str|None=None, 
                         num_images: int=10, 
                         interval: float=1, 
                         make_video: bool=False
                         ):
        """
        Take a series of <num_images> and save them as
        <filename> with auto-number, also set the interval between
        """
    
    # Synonym method for capture_sequence
    take_sequence = capture_sequence

    @retain_controls
    def record_video(self, filename: str|None=None, duration: float=5):
        """
        Record a video
        """
    take_video = record_video

    @retain_controls
    def start_recording(self, filename: str|None=None, preview: bool=False):
        """
        Record a video of undefined length
        """

    @retain_controls
    def stop_recording(self):
        """
        Stop recording video
        """

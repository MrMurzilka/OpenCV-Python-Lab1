from abc import ABC, abstractmethod

class ImageFilter(ABC):
    """Abstract base class for image filters."""
    @abstractmethod
    def apply(self, image_data):
        pass

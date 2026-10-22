from abc import ABC, abstractmethod

class ImageFilter(ABC):
    """Abstract base class for image filters."""
    @abstractmethod
    def apply(self, media_data):
        pass

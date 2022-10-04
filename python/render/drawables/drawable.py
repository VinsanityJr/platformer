# Every drawable object on a screen object should be an instance of the
# drawable class, so that the render loop of the screen can easily handle
# it. Drawables should not be used in the platformer.

class Drawable:
    def __init__(self):
        pass

    # The child class must implement render.
    def render(self):
        raise NotImplementedError

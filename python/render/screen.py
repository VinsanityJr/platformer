from python.render.drawables import button


# The screen class provides a framework for adding different screens
# to the game. Anything displayed to the user while viewing menus should
# be an instance of the screen class.

class Screen:
    def __init__(self):
        self.drawables = []

    def add_drawable(self, drawable):
        self.drawables.append(drawable)

    def on_click(self, mousepos):
        for drawable in self.drawables:
            if isinstance(drawable, button.Button):
                drawable.click(mousepos)

    # Render all the drawable items in this screen
    def render(self):
        for drawable in self.drawables:
            drawable.render()

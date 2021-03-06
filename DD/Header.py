from DD.utils import Vector22NumpyArray, NumpyArray2Vector2
from DD.Entity import Entity

class Header(Entity):
    def __init__(self, json, scale=256):
        super(Header, self).__init__(json)
        self.scale = scale
        self.camera_position = Vector22NumpyArray(self._json['editor_state']['camera_position'])

    def get_json(self):
        json = self._json
        json['editor_state']['camera_position'] = NumpyArray2Vector2(self.camera_position)
        return json

    def pad(self, top, bottom, left, right):
        self.camera_position += [left*self.scale, top*self.scale]

    def crop(self, top, bottom, left, right):
        pass

    def fliplr(self, width):
        self.camera_position[0] = width*self.scale - self.camera_position[0]

    def flipud(self, height):
        self.camera_position[1] = height*self.scale - self.camera_position[1]

    def rot90(self, width, height):
        pass
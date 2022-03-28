# accessing the objects

class Mobile:
    def __init__(self, model, camera ):
        self.model = model
        self.camera = camera
        # print(model)
        # print(camera)

    def get_model(self):
        print(self.model)
        print(self.camera)
        
mobile_obj = Mobile("Galaxy M51","64 MP")
mobile_obj.get_model()
print(mobile_obj.model)
print(mobile_obj.camera)
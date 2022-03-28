#multiple instance

class Mobile:
    def __init__(self, model, camera):
        self.model = model
        self.camera = camera
        print(model)
        print(camera)
    def make_call(self, number):
        print("calling...{}".format(number))
        
mobile_obj = Mobile("Galaxy M51","64 MP")
mobile_obj.make_call(7799880661)
print(id(mobile_obj))
print(type(mobile_obj))
mobile_obj = Mobile("Galaxy J7","16 MP")
mobile_obj.make_call(9000714409)
print(id(mobile_obj))
print(type(mobile_obj))
#updating the attributes or properties

class Mobile:
    def __init__(self, model, camera):
        self.model = model
        self.camera = camera
        # print(camera)
    	# print(model)
        
    def update_model(self, model, camera):
    	self.model = model
    	self.camera = camera
    	# print(camera)
    	# print(model)

mobile_obj = Mobile("Galaxy M51","64 MP")
mobile_obj.update_model("Realme 7", "32 MP")
print(mobile_obj.model)
print(mobile_obj.camera)
    
        

class DTH:
    package = {"EnglishPack" : {"price" : 12, "channel" : ["HBO_Movies","NDTV_NewS"]}, "NewsPack" : { "price" : 5, "channel" : ["NDTV","Zee_News"]}}
    channels = {"HBO_Movies" : 10 , "KTV" : 12 , "Zee_News" : 2 , "NDTV_News" : 5 , "FOX" : 10}
    cost = 0 
    l = []
    def __init__(self,package_names,channels_names):
        self.package_names = package_names
        self.channels_names = channels_names
    
    def total_cost(self):
        for i in self.package_names:
            self.cost += self.package[i]["price"]
            self.l.append(self.package[i]["channel"])
        
        for j in self.channels_names:
            self.cost += self.channels[j]
            self.l.append(j)
        return self.cost

a = input("")
b = a.split(",")
c = input("")
d = c.split(",")
cost = DTH(b,d)
print("Channels Selected : {},{}".format(a,c))
print("TotalCost : {}".format(cost.total_cost()))
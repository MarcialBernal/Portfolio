class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
            
        #else:
        self.cart = cart
    ###
    def add(self, item):
        if str(item.id) not in self.cart.keys():
            self.cart[item.id] = {
                "item_id":item.id, 
                "name":item.name, 
                "price":float(item.price),
                "quantity": 1,
                "image":item.image.url
                }
            
        else:
            for key, value in self.cart.items():
                if key == str(item.id):
                    value["quantity"] = value["quantity"]+ 1
                    value["price"] = float(value["price"]) + item.price
                    break
                
        self.save()
    ###    
    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True
    ###    
    def delete(self, item):
        item.id = str(item.id)
        if item.id in self.cart:
            del self.cart[item.id]
            self.save()
    ###        
    def substract(self, item):
        for key, value in self.cart.items():
                if key == str(item.id):
                    value["quantity"] = value["quantity"]- 1
                    value["price"] = float(value["price"]) - item.price
                    if value["quantity"]<1:
                        self.delete(item)
                    break
        self.save()
    ###    
    def clean(self):
        self.session["cart"] = {}
        self.session.modified = True
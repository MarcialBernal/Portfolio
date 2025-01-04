def cart_total(request):
    total=0
    #if request.user.is_authenticated:
    for key, value in request.session["cart"].items():
        total = total + float(value["price"])
    return {"cart_total":total}
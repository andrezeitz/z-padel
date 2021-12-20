from django.shortcuts import render, redirect


def view_bag(request):
    """ View to return bag page"""

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a product to bag"""

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return render(request, 'bag/bag.html')
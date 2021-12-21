from django.shortcuts import render, redirect, reverse


def view_bag(request):
    """ View to return bag page"""

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a product to bag"""

    quantity = int(request.POST.get('quantity'))
    size = None
    if 'cloth_size' in request.POST:
        size = request.POST['cloth_size']
    if 'shoe_size_man' in request.POST:
        size = request.POST['shoe_size_man']
    if 'shoe_size_woman' in request.POST:
        size = request.POST['shoe_size_woman']             
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return render(request, 'bag/bag.html')


def adjust_bag(request, item_id):
    """ Adjust a product in the bag"""

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    bag = request.session.get('bag', {})

    bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
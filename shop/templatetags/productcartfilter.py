from django import template
register = template.Library()
@register.filter(name='is_in_cart')
def is_in_cart(values,cart):
    keys=cart.keys()
    for id in keys:
        if int(id)==values.id:
            return True
    print(values,cart)
    return False


@register.filter(name='cart_qty')
def cart_qty(values,cart):
    keys=cart.keys()
    print("keys",keys)
    for val in keys:
        print(val)
        #print("id is:",id)
        if int(val)==values.id:
            #print(id,values.id)
           # print(cart[id])
            return cart[val]
    #print(values,cart[id])
    return 0
@register.filter(name='currency')
def currency(number):
    return "₹"+str(number)

@register.filter(name='cart_total')
def cart_total(value,cart):
    
    return value.p_price*cart_qty(value,cart)
    #return value.p_price*cart_qty(value,cart)

@register.filter(name='billing_amount')
def billing_amount(product,cart):
    sum=0;
    for p in product:
        sum +=cart_total(p,cart)

    return sum
   
   
     

       


from pyscript import display, document


def order(e):
    document.getElementById('subtotal').innerHTML = ""
    item1 = document.getElementById('item1')
    item2 = document.getElementById('item2')
    item3 = document.getElementById('item3')
    item4 = document.getElementById('item4')

    subtotal = float(item1.value) * item1.checked + float(item2.value) * item2.checked + float(item3.value) * item3.checked + float(item4.value) * item4.checked
    

    vat= subtotal*0.12

    total = subtotal + vat

    display(f'Subtotal: {subtotal} ₱', target='subtotal')

    display(f'VAT:{vat} ₱', target='subtotal')

    display(f'Total:{total} ₱', target='subtotal')






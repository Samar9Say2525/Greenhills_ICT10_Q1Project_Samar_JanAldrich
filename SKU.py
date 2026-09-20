from pyscript import display, document


def generate(e):
    document.getElementById('result').innerHTML = ""
    category = (document.getElementById('ctgy').value)
    name = (document.getElementById('name').value)
    quantity = (document.getElementById('qnty').value)


    display(f'{category}-{name}-{quantity}', target='result')


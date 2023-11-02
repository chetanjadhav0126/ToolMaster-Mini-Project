from tkinter import *
from tkinter import ttk
import requests
import tkinter.font as font

country = {'USD': "United Statesdollar", 'AED': "United ArabEmeriates dirham", 'ARS': 'Argentine peso',
           'AUD': 'Australian dollar',
           'BGN': 'Bulgarian lev', 'BRL': 'Brazilian real', 'BSD': 'Bahamian Dollar', 'CAD': 'Bahamian doller',
           'CHF': 'Canadian doller', 'CLP': 'Chilean peso', 'CNY': 'Chinese yuan', 'COP': 'Colombian peso',
           'CZK': 'Czech koruna', 'DKK': 'Denmark', 'DOP': 'Dominican peso', 'EGP': 'Egyptian pound',
           'EUR': 'EURO', 'FJD': 'Fijian doller', 'GBP': 'British pound', 'GTQ': 'Guatemalan quetzal',
           'HKD': 'Hong Kong dollar', 'HRK': 'Croatian kuna', 'HUF': 'Hungarian forint', 'IDR': 'Indonesian rupiah',
           'ILS': 'Israeli new shekel', 'INR': 'Indian rupees', 'ISK': 'Icelandic krona', 'JPY': 'Japanese yen',
           'KRW': 'South Korean won', 'KZT': 'Kazakhstani tenge', 'MXN': 'Mexican peso', 'MYR': 'Malaysian ringgit',
           'NOK': 'Norwegian krone', 'NZD': 'New Zealand Dollar', 'PAB': 'Panamanian balboa', 'PEN': 'Peruvian sol',
           'PHP': 'Philippine peso', 'PKR': 'Pakistani rupees', 'PLN': 'Polish zloty', 'PYG': 'Paraguayan guarani',
           'RON': 'Romanian leu', 'RUB': 'Russian ruble', 'SAR': 'Saudi riyal', 'SEK': 'Swedish Krona',
           'SGD': 'Singapore dollar', 'THB': 'Thai baht', 'TRY': 'Turkish lira', 'TWD': 'Taiwan New Dollar',
           'UAH': 'Ukraine hryvnia', 'UYU': 'Uruguayan peso', 'ZAR': 'South African rand'}


def func():
    getIndex = coun.index(cb.get())
    setIndex = coun1[getIndex]
    url = 'https://api.exchangerate-api.com/v4/latest/{}'.format(setIndex)
    response = requests.get(url)
    data = response.json()

    From = cb1.get()
    to = cb.get()

    toCountry = content1.get()
    print(toCountry)
    getIndex = coun.index(cb1.get())
    setIndex = coun1[getIndex]

    fromCountry = data['rates'][setIndex]
    print(fromCountry)
    print(float(toCountry) * fromCountry)

    content2.set(float(toCountry) * fromCountry)


def callfunc(event):
    getIndex = coun.index(cb.get())
    setIndex = coun1[getIndex]
    getIndex = coun.index(cb1.get())
    setIndex = coun1[getIndex]


win = Tk()
win.geometry('580x300')
win.title('Currency Converter')
myfont = font.Font(weight="bold", size="20")
l1 = Label(win, text="Currency Converter", bd='20', fg='grey')
l1['font'] = myfont
l1.place(height=30, x=140, y=20)

# Combobox for fromCountry
from1 = Label(win, text="From")
myfont = font.Font(size="15")
from1['font'] = myfont
from1.place(height=20, x=140, y=60)

coun = []
for i in country.values():
    coun.append(i)

coun1 = []
for i in country.keys():
    coun1.append(i)

print(coun1)

cb = ttk.Combobox(win, values=coun, width=30)
cb.place(height=35, x=75, y=100)
cb.current(0)
cb.bind("<<ComboboxSelected>>", callfunc)

# Combobox for toCountry
to1 = Label(win, text="To")
myfont = font.Font(size="15")
to1['font'] = myfont
to1.place(height=20, x=450, y=60)

cb1 = ttk.Combobox(win, values=coun, width=30)
cb1.place(height=35, x=365, y=100)
cb1.current(0)
cb1.bind("<<ComboboxSelected>>", callfunc)

# amount of currency
amount = ttk.Label(win, text="Amount")
myfont = font.Font(size="15")
amount['font'] = myfont
amount.place(height=25, x=135, y=150)
content1 = StringVar()
content2 = StringVar()

e1 = ttk.Entry(win, textvariable=content1)
e1.place(height=25, x=110, y=180)

content1.set('1')
content2.set('1')
result = ttk.Label(win, text="Result")
myfont = font.Font(size="15")
result['font'] = myfont
result.place(height=25, x=440, y=150)

e2 = ttk.Entry(win, state='readonly', textvariable=content2)
e2.place(height=25, x=400, y=180)

b = Button(win, text="Convert", width=20, bg='#afd6ad', command=func)
b.place(height=30, x=220, y=230)

win.mainloop()
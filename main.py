import requests
import tkinter as tk
import tkinter.messagebox

from countryinfo import CountryInfo


WEATHER_API_URL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline'
WEATHER_API_ID = '6L8FBNSMZB9DMUL9FFBPJZHDQ'


def show_entry_fields():
    country_name = e1.get()
    country = CountryInfo(country_name)

    try:
        tk.Label(window, text=f"Country name: {country.name()}").place(x=7, y=200)
        tk.Label(window, text=f"Country region: {country.region()}").place(x=7, y=220)
        tk.Label(window, text=f"Country area: {country.area()}").place(x=7, y=240)
        tk.Label(window, text=f"Country capital: {country.capital()}").place(x=7, y=260)
        tk.Label(window, text=f"Country currency: {country.currencies()[0]}").place(x=7, y=280)
        tk.Label(window, text=f"Country calling code: {country.calling_codes()[0]}").place(x=7, y=300)
        tk.Label(window, text=f"Country domain: {country.tld()[0]}").place(x=7, y=320)
        tk.Label(window, text=f"Country population: {country.population()}").place(x=7, y=340)
        tk.Label(window, text=f"Country language: {country.languages()[0]}").place(x=7, y=360)
        tk.Label(window, text=f"Country provinces count: {len(country.provinces())}").place(x=7, y=380)
        tk.Label(window, text=f"Country timezone: {country.timezones()[0]}").place(x=7, y=400)
        tk.Label(window, text=f"Country wikipedia link: {country.wiki()}").place(x=7, y=420)

        try:
            response = requests.get(f'{WEATHER_API_URL}/{country_name}?key={WEATHER_API_ID}').json().get('days')
            tk.Label(window, text=f"Weather temp: {(response[0].get('temp') - 32) / 1.8}").place(x=7, y=100)
            tk.Label(window, text=f"Weather sunrise: {response[0].get('sunrise')}").place(x=7, y=120)
            tk.Label(window, text=f"Weather sunset: {response[0].get('sunset')}").place(x=7, y=140)
            tk.Label(window, text=f"Weather conditions: {response[0].get('conditions')}").place(x=7, y=160)
        except:
            pass

    except KeyError:
        tkinter.messagebox.showerror("Wrong Country", "There is\'not any country with this name!")

    e1.delete(0, tk.END)


window = tk.Tk()
window.title('Country Info')
window.geometry("400x500")

tk.Label(window, text="Country name").place(x=80, y=20)
e1 = tk.Entry(window)
e1.place(x=170, y=20)
tk.Button(window, text='search', command=show_entry_fields).place(x=160, y=50)

window.mainloop()

import tkinter
from tkinter import *
import requests
from PIL import Image, ImageTk
from io import BytesIO

def mix():
    namingcocktail = enter.get()
    responses = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={namingcocktail}")
    data = responses.json()
    
    if data["drinks"]:
        cocktail = data["drinks"][0]
        cocktailname.config(text=cocktail["strDrink"],bg='cornflowerblue',fg='white',font=('Arial',20,'bold'))
        ingredients = [f"{cocktail[f'strIngredient{i}']} - {cocktail[f'strMeasure{i}']}" for i in range(1, 16) if cocktail[f'strIngredient{i}']]
        ingredientslist.config(text="\n".join(ingredients),bg='cornflowerblue',fg='white',font=('Arial',10,'bold'))
        instructions.config(text=cocktail["strInstructions"],bg='cornflowerblue',fg='white',font=('Arial',10,'bold'))
        imageurl = cocktail["strDrinkThumb"]
        response = requests.get(imageurl)
        thumbnail = Image.open(BytesIO(response.content))
        resized = thumbnail.resize((350,350))
        photo = ImageTk.PhotoImage(resized)
        thumbnailabel = Label(main,image=photo)
        thumbnailabel.thumbnail = photo
        thumbnailabel.pack()
        
    else:
        cocktailname.config(text="Cocktail doesn't exist",bg='cornflowerblue',fg='red',font=('Arial',10,'bold'))
        ingredientslist.config(text="",bg='cornflowerblue',font=('Arial',10,'bold'))
        instructions.config(text="",bg='cornflowerblue',font=('Arial',10,'bold'))
        
main = Tk()
main.title("Python Assessment 2")
main.configure(bg='cornflowerblue')



drink = Label(main,text="State your cocktail:",fg='white',bg='cornflowerblue',font=('Arial',20,'bold')).pack()

enter = Entry(main,font=('Arial',12))
enter.pack()

search = Button(main,text="Search",command=mix,fg='black',font=('Arial',12)).pack()

cocktailname = Label(main,text="",bg='cornflowerblue',font=('Arial',16,'bold'))
cocktailname.pack()
ingredientslist = Label(main,text="",bg='cornflowerblue',font=('Arial',12,'bold'))
ingredientslist.pack()
instructions = Label(main,text="",bg='cornflowerblue',font=('Arial',12,'bold'))
instructions.pack()

main.mainloop()
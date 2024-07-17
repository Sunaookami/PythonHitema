import customtkinter

class Recettes:
    def __init__(self, nom, ingredients, prix):
        self.nom = nom
        self.ingredients = ingredients
        self.prix = prix

    def __str__(self):
        return f"Recettes(nom={self.nom}, ingredients={self.ingredients}, prix={self.prix})"

    def afficher_informations(self):
        return (self.nom, self.ingredients, self.prix)

class Glace(Recettes):
    def __init__(self, nom, ingredients, prix):
        super().__init__(nom, ingredients, prix)

    def afficher_informations(self):
        info = super().afficher_informations()
        return info + ("Glace",)

class Dessert(Recettes):
    def __init__(self, nom, ingredients, prix):
        super().__init__(nom, ingredients, prix)

    def afficher_informations(self):
        info = super().afficher_informations()
        return info + ("Dessert",)

def main():
    app = App()
    app.mainloop()

# Interface principale

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # Configure Windows 
        self.title("CookHub")
        self.geometry(f"{1100}x{580}")

        # Configure main frame
        self.main_frame = customtkinter.CTkFrame(self)
        self.main_frame.grid(row=0, column=1, rowspan=3)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="CookHub", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # Configure recipe frame
        self.recipe_frame = customtkinter.CTkFrame(self.main_frame)
        self.recipe_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.recipe_frame.grid_columnconfigure(0, weight=1)
        self.recipe_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

        self.title_label = customtkinter.CTkLabel(self.recipe_frame, text="Titre de la recette:")
        self.title_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")
        self.title_entry = customtkinter.CTkEntry(self.recipe_frame)
        self.title_entry.grid(row=0, column=1, padx=20, pady=10, sticky="ew")

        self.ingredients_label = customtkinter.CTkLabel(self.recipe_frame, text="Ingrédients:")
        self.ingredients_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        self.ingredients_entry = customtkinter.CTkEntry(self.recipe_frame)
        self.ingredients_entry.grid(row=1, column=1, padx=20, pady=10, sticky="ew")

        self.price_label = customtkinter.CTkLabel(self.recipe_frame, text="Prix:")
        self.price_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")
        self.price_entry = customtkinter.CTkEntry(self.recipe_frame)
        self.price_entry.grid(row=2, column=1, padx=20, pady=10, sticky="ew")

        self.type_label = customtkinter.CTkLabel(self.recipe_frame, text="Type:")
        self.type_label.grid(row=3, column=0, padx=20, pady=10, sticky="w")
        self.type_optionemenu = customtkinter.CTkOptionMenu(self.recipe_frame, values=["Recette", "Glace", "Dessert"])
        self.type_optionemenu.grid(row=3, column=1, padx=20, pady=10, sticky="ew")

        self.save_button = customtkinter.CTkButton(self.recipe_frame, text="Enregistrer", command=self.save_recipe)
        self.save_button.grid(row=4, column=1, padx=20, pady=20, sticky="ew")

        self.info_label = customtkinter.CTkLabel(self.recipe_frame, text="")
        self.info_label.grid(row=5, column=0, columnspan=2, padx=20, pady=10, sticky="ew")
    
    def save_recipe(self):
        title = self.title_entry.get()
        ingredients = self.ingredients_entry.get().split(",")
        price = self.price_entry.get()
        type_recette = self.type_optionemenu.get()

        if type_recette == "Glace":
            recette = Glace(title, ingredients, price)
        elif type_recette == "Dessert":
            recette = Dessert(title, ingredients, price)
        else:
            recette = Recettes(title, ingredients, price)

        info = recette.afficher_informations()
        self.info_label.configure(text=f"Recette enregistrée : {info}")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

if __name__ == "__main__":
    main()

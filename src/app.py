import customtkinter

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
        self.main_frame.grid(row=0, column=1, rowspan=3, sticky="nsew")
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)

        # Create search bar
        self.search_bar = customtkinter.CTkEntry(self.main_frame, placeholder_text="Rechercher une entrée...")
        self.search_bar.grid(row=0, column=0, padx=20, pady=10)
        self.search_button = customtkinter.CTkButton(self.main_frame, text="Rechercher", command=self.search_recipes)
        self.search_button.grid(row=0, column=1, padx=20, pady=10)

        # Create result text box
        self.result_text = customtkinter.CTkTextbox(self.main_frame)
        self.result_text.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")

        # Configure sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="CookHub", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        # self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text= "",command=self.split_pdf)
        # self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        # self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Envoyer", command=self.send_emails)
        # self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

    def search_recipes(self):
        query = self.search_bar.get().lower()
        results = self.get_recipe_info(query)
        self.result_text.delete(1.0, customtkinter.END)
        self.result_text.insert(customtkinter.END, results)

    def get_recipe_info(self, query):
        recipes = {
            "tartare de tomate": {
                "ingredients": [
                    "2 gros filets de daurade (2,2 kg)",
                    "fleur de sel",
                    "poivre noir sarawak",
                    "huile d'olive de première pression provence fruitée verte",
                    "3/4 d'un petit piment vert long (auquel on a retiré les pépins)",
                    "le zeste de 1 citron vert",
                    "le zeste de 1/4 d'orange",
                    "1 càc de sel fin",
                    "30 g de gingembre frais",
                    "46 goutte(s) de tabasco",
                    "180 g de jus de citron vert frais pressé",
                    "100 g de jus d'orange",
                    "1/2 oignon rouge coupé",
                    "4 radis roses",
                    "1/2 botte de coriandre"
                ],
                "price": 10
            },
            "caviar d’aubergine facile": {
                "ingredients": [
                    "4 belles aubergines",
                    "4 ou 5 oignons nouveaux",
                    "4 brins de basilic",
                    "1 ou 2 gousses d'ail (facultatif)",
                    "25 cl d'huile d'olive crétoise",
                    "le jus de 2 ou 3 citrons",
                    "vinaigre de vin",
                    "sel, poivre"
                ],
                "price": 6
            },
            "salade catalane": {
                "ingredients": [
                    "1 laitue",
                    "2 tomates",
                    "2 oignons rouges",
                    "1 poivron rouge cuit ou grillé",
                    "quelques anchois",
                    "quelques olives"
                ],
                "price": 8
            },
            "bruschetta à la tomate": {
                "ingredients": [
                    "1 pain italien",
                    "500 g de tomates mûres",
                    "1 oignon rouge",
                    "huile d'olive",
                    "sel, poivre",
                    "1 gousse d'ail",
                    "basilic"
                ],
                "price": 9
            },
            "salade japonaise": {
                "ingredients": [
                    "1 petit chou blanc",
                    "graines de sésame blanc grillé",
                    "30 cl de vinaigre de riz (à défaut utiliser du vinaigre de cidre)",
                    "3 cuillère(s) à soupe de cassonade",
                    "sel fin",
                    "2 cuillère(s) à soupe de nuocmâm",
                    "3 cuillère(s) à soupe d'huile neutre",
                    "1 cuillère(s) à café de sauce soja"
                ],
                "price": 5
            },
            "ceviche de daurade": {
                "ingredients": [
                    "2 gros filets de daurade (2,2 kg)",
                    "fleur de sel",
                    "poivre noir sarawak",
                    "huile d'olive de première pression provence fruitée verte",
                    "3/4 d'un petit piment vert long (auquel on a retiré les pépins)",
                    "le zeste de 1 citron vert",
                    "le zeste de 1/4 d'orange",
                    "1 càc de sel fin",
                    "30 g de gingembre frais",
                    "46 goutte(s) de tabasco",
                    "180 g de jus de citron vert frais pressé",
                    "100 g de jus d'orange",
                    "1/2 oignon rouge coupé",
                    "4 radis roses",
                    "1/2 botte de coriandre"
                ],
                "price": 8.50
            }
        }

        if query in recipes:
            ingredients = "\n".join(recipes[query]["ingredients"])
            price = recipes[query]["price"]
            result = f"{query.title()}:\n\nIngrédients:\n{ingredients}\n\nPrix: {price} €"
        else:
            result = "Recette non trouvée. Veuillez réessayer avec un autre nom de recette."

        return result

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

if __name__ == "__main__":
    main()

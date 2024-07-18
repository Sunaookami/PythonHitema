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

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        # create frame main_frame
        self.main_frame = customtkinter.CTkFrame(self)
        self.main_frame.grid(row=0, column=1, rowspan=3, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
        
        # Create search bar
        self.search_bar = customtkinter.CTkEntry(self.main_frame, placeholder_text="Rechercher une recette")
        self.search_bar.grid(row=4, column=1, columnspan=2, padx=(10, 0), pady=(20, 20), sticky="nsew")
        self.search_button = customtkinter.CTkButton(self.main_frame, border_width=2, text="Rechercher", text_color=("gray10", "#DCE4EE"), command=self.search_recipes)
        self.search_button.grid(row=4, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # Create result text box
        self.result_text = customtkinter.CTkTextbox(self.main_frame, width=250)
        self.result_text.grid(row=0, column=1, columnspan=3, padx=(10, 10), pady=(10, 10), sticky="nsew")

        # Configure sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=3)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="CookHub", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
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
            },
            "glace vanille": {
                "ingredients": [
                    "500 ml de lait",
                    "200 ml de crème fraîche",
                    "150 g de sucre",
                    "4 jaunes d'œufs",
                    "1 gousse de vanille"
                ],
                "price": 4.50
            },
            "glace chocolat": {
                "ingredients": [
                    "500 ml de lait",
                    "200 ml de crème fraîche",
                    "150 g de sucre",
                    "4 jaunes d'œufs",
                    "200 g de chocolat noir"
                ],
                "price": 5.00
            },
            "tarte à la pomme": {
                "ingredients": [
                    "1 pâte brisée",
                    "4 pommes",
                    "50 g de sucre",
                    "30 g de beurre",
                    "1 sachet de sucre vanillé"
                ],
                "price": 7.00
            },
            "cake chocolat": {
                "ingredients": [
                    "200 g de chocolat noir",
                    "150 g de beurre",
                    "150 g de sucre",
                    "4 œufs",
                    "100 g de farine",
                    "1 sachet de levure"
                ],
                "price": 8.00
            },
            "spaghetti carbonara": {
                "ingredients": [
                    "200 g de guanciale (ou pancetta)",
                    "4 jaunes d'œufs",
                    "100 g de pecorino romano",
                    "400 g de spaghetti",
                    "Sel, poivre noir"
                ],
                "price": 12.00
            },
            "tajine de poulet aux olives et citrons confits": {
                "ingredients": [
                    "1 poulet entier coupé en morceaux",
                    "2 citrons confits",
                    "150 g d'olives vertes",
                    "2 oignons",
                    "3 gousses d'ail",
                    "1 bouquet de coriandre",
                    "1 bouquet de persil",
                    "1 cuillère à café de curcuma",
                    "1 cuillère à café de gingembre moulu",
                    "1 cuillère à café de poivre noir",
                    "Sel",
                    "Huile d'olive"
                ],
                "price": 18.00
            },
            "paella": {
                "ingredients": [
                    "300 g de riz à paella",
                    "200 g de moules",
                    "200 g de calamars",
                    "200 g de crevettes",
                    "150 g de petits pois",
                    "2 poivrons rouges",
                    "1 oignon",
                    "2 gousses d'ail",
                    "1 litre de bouillon de volaille",
                    "1 cuillère à café de paprika",
                    "1 dose de safran",
                    "Sel, poivre",
                    "Huile d'olive"
                ],
                "price": 20.00
            },
            "bœuf bourguignon": {
                "ingredients": [
                    "1 kg de bœuf à braiser",
                    "150 g de lardons",
                    "1 bouteille de vin rouge de Bourgogne",
                    "3 carottes",
                    "1 oignon",
                    "2 gousses d'ail",
                    "1 bouquet garni",
                    "200 g de champignons de Paris",
                    "50 g de beurre",
                    "3 cuillères à soupe de farine",
                    "Sel, poivre"
                ],
                "price": 25.00
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

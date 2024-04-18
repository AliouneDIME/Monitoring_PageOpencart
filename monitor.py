import tkinter as tk
from tkinter import ttk
import mysql.connector
import matplotlib.pyplot as plt

# Fonction pour récupérer le nombre total de clients depuis la base de données OpenCart
def fetch_customer_count():
    try:
        # Connexion à la base de données
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="opencart"
        )
        cursor = conn.cursor()

        # Requête pour récupérer le nombre total de clients
        cursor.execute("SELECT COUNT(*) FROM customer")
        total_customers = cursor.fetchone()[0]

        # Fermer la connexion à la base de données
        cursor.close()
        conn.close()

        return total_customers
    except mysql.connector.Error as e:
        print("Erreur lors de la récupération des données:", e)
        return None

# Fonction pour récupérer le nombre total de commandes depuis la base de données OpenCart
def fetch_order_count():
    try:
        # Connexion à la base de données
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="opencart"
        )
        cursor = conn.cursor()

        # Requête pour récupérer le nombre total de commandes
        cursor.execute("SELECT COUNT(*) FROM `order`")  # Utilisation de backticks car 'order' est un mot clé SQL
        total_orders = cursor.fetchone()[0]

        # Fermer la connexion à la base de données
        cursor.close()
        conn.close()

        return total_orders
    except mysql.connector.Error as e:
        print("Erreur lors de la récupération des données:", e)
        return None

# Fonction pour récupérer le nombre total d'utilisateurs connectés depuis la base de données OpenCart
def fetch_user_login_count():
    try:
        # Connexion à la base de données
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="opencart"
        )
        cursor = conn.cursor()

        # Requête pour récupérer le nombre total d'utilisateurs connectés
        cursor.execute("SELECT COUNT(*) FROM user_login")
        total_user_login = cursor.fetchone()[0]

        # Fermer la connexion à la base de données
        cursor.close()
        conn.close()

        return total_user_login
    except mysql.connector.Error as e:
        print("Erreur lors de la récupération des données:", e)
        return None

# Fonction pour récupérer le total des ventes depuis la base de données OpenCart
def fetch_total_sales():
    try:
        # Connexion à la base de données
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="opencart"
        )
        cursor = conn.cursor()

        # Requête pour récupérer le total des ventes
        cursor.execute("SELECT COUNT(*) FROM `order`")
        total_sales = cursor.fetchone()[0]

        # Fermer la connexion à la base de données
        cursor.close()
        conn.close()

        return total_sales
    except mysql.connector.Error as e:
        print("Erreur lors de la récupération des données:", e)
        return None

# Fonction pour afficher les résultats dans un diagramme en barres
def show_bar_chart():
    total_customers = fetch_customer_count()
    total_orders = fetch_order_count()
    total_user_login = fetch_user_login_count()
    total_sales = fetch_total_sales()
    if all([total_customers, total_orders, total_user_login, total_sales]):
        # Création du diagramme en barres
        labels = ['T.clients', 'T.commandes', 'U.connectés', 'T.ventes']
        values = [total_customers, total_orders, total_user_login, total_sales]
        plt.bar(labels, values, color=['blue', 'green', 'orange', 'red'])
        plt.ylabel('Valeurs')
        plt.title('Données OpenCart')
        plt.show()
    else:
        print("Impossible de récupérer les données pour afficher le diagramme en barres.")

# Création de la fenêtre principale Tkinter
root = tk.Tk()
root.title("Tableau de bord OpenCart")

# Cadre pour afficher les résultats dans un tableau de données
table_frame = ttk.Frame(root)
table_frame.grid(row=0, column=0, padx=10, pady=10)

# Création d'un widget Treeview pour afficher les résultats dans un tableau
tree = ttk.Treeview(table_frame, columns=("Données", "Valeurs"))
tree.heading("#0", text="Données")
tree.heading("#1", text="Valeurs")
tree.grid(row=0, column=0, padx=10, pady=5)

# Fonction pour mettre à jour le tableau avec les données des clients, des commandes, des utilisateurs connectés et des ventes
def update_data_table():
    total_customers = fetch_customer_count()
    total_orders = fetch_order_count()
    total_user_login = fetch_user_login_count()
    total_sales = fetch_total_sales()
    if all([total_customers, total_orders, total_user_login, total_sales]):
        tree.insert("", "end", text="Total des clients", values=("Total clients", total_customers))
        tree.insert("", "end", text="Total des commandes", values=("Total commandes", total_orders))
        tree.insert("", "end", text="Utilisateurs connectés", values=("Utilisateurs connectés", total_user_login))
        tree.insert("", "end", text="Total des ventes", values=("Total ventes", total_sales))
    else:
        tree.insert("", "end", text="Erreur", values=("Erreur lors de la récupération des données",))

# Bouton pour mettre à jour le tableau
update_button = ttk.Button(root, text="Mettre à jour le tableau", command=update_data_table)
update_button.grid(row=1, column=0, padx=10, pady=10)

# Bouton pour afficher le diagramme en barres
show_chart_button = ttk.Button(root, text="Afficher le Diagramme en Barres", command=show_bar_chart)
show_chart_button.grid(row=2, column=0, padx=10, pady=10)

# Mettre à jour le tableau initialement lors du lancement de l'application
update_data_table()

# Exécuter la boucle principale Tkinter
root.mainloop()

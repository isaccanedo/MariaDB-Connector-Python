# Importação de Módulo
import mariadb
import sys

# Print List of Contacts
def print_contacts(cur):
     """Recupera a lista de contatos do banco de dados e imprime em stdout"""

     # Initialize Variables
     contacts = []

     # Retrieve Contacts
     cur.execute("SELECT * from usuario")

     # Prepare Contacts
     for (id,nome,telefone) in cur:
        contacts.append(f"{id} {nome} <{telefone}>")

     # List Contacts
     print("\n".join(contacts))

# Instantiate Connection
try:
     conn = mariadb.connect(
        user="root",
        password="root",
        host="localhost",
        database="agenda",
        port=3306)

     # Instantiate Cursor
     cur = conn.cursor()

     print_contacts(cur)

     # Close Connection
     conn.close()

except mariadb.Error as e:
      print(f"Error connecting to MariaDB Platform: {e}")
      sys.exit(1)

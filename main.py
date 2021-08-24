# Importação de Módulo
import mariadb
import sys

# Imprimir lista de contatos
def print_contacts(cur):
     """Recupera a lista de contatos do banco de dados e imprime em stdout"""

     # Inicializar variáveis
     contacts = []

     # Recuperar contatos
     cur.execute("SELECT * from usuario")

     # Prepare Contatos
     for (id,nome,telefone) in cur:
        contacts.append(f"{id} {nome} <{telefone}>")

     # Listar contatos
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

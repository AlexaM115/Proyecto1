from libro import Libro
from isbn import ISBN

# Crear y guardar el libro
libro = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967)
libro.save()

# Crear y guardar el ISBN con referencia al libro
isbn = ISBN("978-0307474728", "Penguin Books", "Colombia")
isbn.libro_id = libro._id
isbn.save()

# Actualizar el libro con el ID del ISBN
libro.update_isbn_id(isbn._id)
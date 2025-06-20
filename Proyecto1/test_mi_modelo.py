import unittest
from libro import Libro
from isbn import ISBN

class TestModeloLibroISBN(unittest.TestCase):
    def test_creacion_y_relacion(self):
        # Crear y guardar un libro
        libro = Libro("1984", "George Orwell", 1949)
        libro.save()

        # Crear y guardar un ISBN vinculado al libro
        isbn = ISBN("978-0451524935", "Signet Classics", "EEUU")
        isbn.libro_id = libro._id
        isbn.save()

        # Actualizar el libro con el ID del ISBN
        libro.update_isbn_id(isbn._id)

        # Validar que ambos tengan ID y estén vinculados correctamente
        self.assertIsNotNone(libro._id)
        self.assertIsNotNone(isbn._id)
        self.assertEqual(str(isbn.libro_id), str(libro._id))

if __name__ == '_main_':
    unittest.main()
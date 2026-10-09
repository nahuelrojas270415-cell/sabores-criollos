## Links de entrega
- **WEB ONLINE:** https://nahuelrojas270415.pythonanywhere.com
- **REPO:** https://github.com/nahuelrojas270415-cell/sabores-criollos

# Sabores Criollos - Blog de Comida Argentina

Blog hecho en Django con 4 recetas argentinas: Milanesas, Fideos con tuco, etc.

### Demo Online (URL desplegada)
**https://nahuelrojas270415.pythonanywhere.com/**

### Funcionalidades
- Modelos: Receta (titulo, descripcion, imagen, autor, fecha)
- Vistas: ListView, DetailView, CreateView, UpdateView, DeleteView
- Formularios: RecetaForm con validación
- Auth: Registro / Login / Logout / Solo usuarios logueados pueden crear
- Admin: /admin con gestión de recetas

### Cómo correrlo local
1. git clone https://github.com/nahuelrojas270415-cell/sabores-criollos.git
2. cd sabores-criollos
3. python -m venv venv
4. venv\Scripts\activate
5. pip install -r requirements.txt
6. python manage.py migrate
7. python manage.py createsuperuser
8. python manage.py runserver
9. Entrar a http://127.0.0.1:8000/

### Evidencia de funcionamiento
- [ ] Listado de recetas en /
- [ ] Detalle de receta /receta/1/
- [ ] Crear receta solo logueado
- [ ] Login/Registro funcionando

### Tecnologías
Python 3.11, Django 5, SQLite, Pillow

# AR Sabores Criollos - Blog de Comida Argentina

Proyecto final para **CoderHouse - Curso Python / Django**

Blog de recetas bien argentinas, hecho con Django. Permite registrar usuarios, publicar, editar y borrar recetas con fotos, categorías criollas y buscador.

**Live Demo:** `http://127.0.0.1:8000/` (local)
**Autor:** Nahuel Rojas - Comisión CoderHouse 2026

### ✨ Captura Actual
Grilla con 4 recetas: Pastel de Papas de la Abuela, Locro Criollo del 25 de Mayo, Milanesa a la Napolitana bien de Bodegón y Guiso de Fideos Moñitos.

### 🚀 Funcionalidades

- **CRUD completo de Recetas:** Crear, listar, ver detalle, editar y borrar.
- **Autenticación:** Registro, Login y Logout con `django.contrib.auth`. Solo usuarios logueados pueden crear/editar/borrar.
- **Categorías Argentinas:** Clásicos de Bodegón, Guisos y Ollas, Carnes y Parrilla, Pastas y Más.
- **Gestión de Imágenes:** Upload de fotos con `MEDIA_URL` y `MEDIA_ROOT`.
- **Panel de Admin:** ABM completo desde `/admin`.
- **Diseño Responsive:** Bootstrap 5, mantel a cuadros, estilo bodegón.

### 🛠️ Tecnologías

- Python 3.12
- Django 6.1.1
- SQLite3
- Bootstrap 5
- Pillow (para imágenes)

### 📁 Estructura del Proyecto

```
config/
  settings.py  -> DIRS = [BASE_DIR / 'templates'] configurado
  urls.py      -> path('', include('blog.urls')) + media
blog/
  models.py    -> Modelo Receta (titulo, categoria, descripcion, ingredientes, pasos, tiempo, dificultad, imagen, autor, fecha)
  views.py     -> Class Based Views: ListView, DetailView, CreateView, UpdateView, DeleteView
  urls.py      -> Rutas de recetas
  forms.py     -> RecetaForm
templates/
  base.html
  blog/
    receta_list.html
    receta_detail.html
    receta_form.html
    receta_confirm_delete.html
  registration/
    login.html
    register.html
media/ -> Fotos de recetas
```

### 🔧 Instalación Local (paso a paso)

1. **Clonar el repo**
```bash
git clone https://github.com/TU_USUARIO/sabores-criollos.git
cd sabores-criollos
```

2. **Crear entorno virtual**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **Instalar dependencias**
```bash
pip install django pillow
```

4. **Migraciones**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Crear superusuario para el admin**
```bash
python manage.py createsuperuser
# Usuario: Nahuel06 (o el que quieras)
# Email: podes dejar vacio
# Password: la que uses para entrar a /admin
```

6. **Correr el servidor**
```bash
python manage.py runserver
```

Abrí en el navegador:
- Blog: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/
- Login: http://127.0.0.1:8000/accounts/login/
- Registro: http://127.0.0.1:8000/registro/

### 👤 Usuario de prueba

- **Usuario:** Nahuel06
- **Recetas cargadas:** 4 (Pastel de Papas, Locro, Milanesa Napo, Guiso Moñitos)

### 📝 Modelo Principal

**Receta**
- titulo (CharField)
- categoria (choices: guisos, carnes, bodegon, pastas)
- descripcion (TextField corta)
- ingredientes (TextField)
- pasos (TextField)
- tiempo_preparacion (Integer - minutos)
- dificultad (choices: facil, media, dificil)
- imagen (ImageField upload_to='recetas/')
- autor (ForeignKey User)
- fecha_creacion (DateTimeField auto_now_add)

### 📌 Para entregar en CoderHouse

1. Subir este proyecto a GitHub (público).
2. Entregar link del repo en la plataforma CoderHouse.
3. Opcional: Deploy en PythonAnywhere.

¡Aguante el guiso de lentejas y Django!

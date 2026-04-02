# Blog Project - Proyecto Final Django

## Descripción

Aplicación web tipo blog desarrollada con Django. Permite a los usuarios crear y gestionar posts, interactuar con otros usuarios mediante likes, comentarios y mensajes privados.

## 🌐 Deploy

**URL de producción:** https://blog-imoberdoff.onrender.com

## Tecnologías utilizadas

- Python 3.14
- Django 6.0.3
- Bootstrap 5.3
- PostgreSQL (producción) / SQLite (desarrollo)
- django-ckeditor
- Pillow
- Gunicorn
- WhiteNoise

## Funcionalidades

- Registro, login y logout de usuarios
- Perfil de usuario con avatar y bio
- CRUD completo de posts (solo el autor puede editar/borrar)
- Texto enriquecido con CKEditor
- Sistema de likes en tiempo real
- Comentarios en posts
- Buscador de posts
- Mensajería privada entre usuarios con bandeja de entrada y enviados
- Notificaciones de likes, comentarios y mensajes

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/SantiImober/ProyectoFinalImober.git
cd ProyectoFinalImober
```

### 2. Crear y activar el entorno virtual

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones

```bash
python manage.py migrate
```

### 5. Crear superusuario

```bash
python manage.py createsuperuser
```

### 6. Correr el servidor

```bash
python manage.py runserver
```

## Rutas principales

| Ruta                        | Descripción                   |
| --------------------------- | ----------------------------- |
| `/`                         | Home                          |
| `/about/`                   | Acerca de mí                  |
| `/pages/`                   | Listado de posts con buscador |
| `/pages/<id>/`              | Detalle del post              |
| `/pages/create/`            | Crear post (requiere login)   |
| `/pages/update/<id>/`       | Editar post (solo el autor)   |
| `/pages/delete/<id>/`       | Borrar post (solo el autor)   |
| `/accounts/register/`       | Registro                      |
| `/accounts/login/`          | Login                         |
| `/accounts/profile/`        | Perfil                        |
| `/messaging/`               | Bandeja de mensajes           |
| `/messaging/send/`          | Enviar mensaje                |
| `/messaging/notifications/` | Notificaciones                |
| `/admin/`                   | Panel de administración       |

## Autor

Santiago Imoberdoff

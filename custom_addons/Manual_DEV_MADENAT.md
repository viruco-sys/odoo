# Manual del Desarrollador (Proyecto MADENAT)

**Objetivo:** Este manual define la arquitectura, configuración y flujo de trabajo para el desarrollo de personalizaciones en Odoo para MADENAT.

## 1. Arquitectura de Entornos

*   **DEV (Desarrollo):** Tu PC con WSL. Aquí se escribe y prueba el código.
*   **TEST (Pruebas):** Servidor en Oracle Cloud. Un clon de producción para que el cliente valide los cambios (UAT).
*   **PROD (Producción):** El sistema en vivo que usará MADENAT. Solo se actualiza con cambios aprobados en TEST.

## 2. Configuración del Entorno de Desarrollo

La estructura del proyecto se encuentra en `/opt/odoo18`.

*   `/opt/odoo18/`: Raíz del proyecto.
*   `/opt/odoo18/odoo-bin`: Ejecutable de Odoo.
*   `/opt/odoo18/addons/`: Módulos nativos de Odoo.
*   `/opt/odoo18/custom_addons/`: **Tu carpeta de trabajo para módulos personalizados.**
*   `/opt/odoo18/odoo.conf`: Archivo de configuración principal.

### Archivo de Configuración (`odoo.conf`)

Asegúrate de que tu archivo `/opt/odoo18/odoo.conf` tenga el siguiente contenido. Está configurado para usar el usuario `viruco-sys` y apuntar a la carpeta de addons correcta.

```ini
[options]
; Contraseña maestra para la gestión de bases de datos
admin_passwd = Manatar#2020$

; Conexión a la base de datos PostgreSQL
db_host = localhost
db_port = 5432
db_user = viruco
db_password = False

; Puerto del servidor Odoo
xmlrpc_port = 8069

; --- RUTA A LOS ADDONS (¡MUY IMPORTANTE!) ---
; Odoo busca módulos primero en 'custom_addons'.
addons_path = /opt/odoo18/custom_addons,/opt/odoo18/addons

; Archivo de log
logfile = /opt/odoo18/odoo.log
log_level = info
```

## 3. Flujo de Trabajo y Comandos Clave

Todos los comandos se ejecutan desde la raíz del proyecto: `/opt/odoo18`.

```bash
cd /opt/odoo18
```

### Crear un nuevo módulo

Usa `scaffold` para generar la estructura base de un nuevo módulo dentro de `custom_addons`.

```bash
# Ejemplo: crear el módulo 'madenat_contacts'
./odoo-bin scaffold madenat_contacts ./custom_addons
```

### Instalar o Actualizar un módulo

Este es el comando más usado. Ejecútalo cada vez que hagas cambios en Python (`.py`) o vistas (`.xml`).

*   `-d [db_name]`: Especifica la base de datos (ej: `madenat_dev`).
*   `-u [module_name]`: **Actualiza** un módulo ya instalado.
*   `-i [module_name]`: **Instala** un módulo por primera vez.

```bash
# Para actualizar el módulo 'madenat_inventory' en la BD 'madenat_dev'
./odoo-bin -c odoo.conf -d madenat_dev -u madenat_inventory
```

## 4. Control de Versiones con Git

Todo el código debe estar versionado con Git.

### Configuración de Identidad (Solo una vez)

Asegura que tus commits se registren con tu identidad correcta.

```bash
# Desde /opt/odoo18
git config user.name "viruco-sys"
git config user.email "mauricio.seo@gmail.com"
```

### Flujo Básico de Git

1.  **Revisar cambios:** `git status`
2.  **Añadir cambios al commit:** `git add .`
3.  **Crear el commit:** `git commit -m "feat: Añadir nueva funcionalidad X"`
4.  **Subir a GitHub:** `git push origin main`
<<<<<<< Updated upstream
=======
# Prueba de herramientas Prueba de herramientas Manual
>>>>>>> Stashed changes

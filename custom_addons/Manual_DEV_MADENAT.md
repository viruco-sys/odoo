Manual del Desarrollador (Proyecto MADENAT)
Objetivo: Este manual está dirigido al desarrollador principal del proyecto.
 Define la arquitectura de entornos, el flujo de trabajo y las buenas prácticas para realizar las personalizaciones menores que MADENAT requiere, manteniendo siempre la estabilidad y la facilidad de migración a futuras versiones de Odoo.

1. Arquitectura de Entornos: DEV, TEST, PROD
Para trabajar de forma profesional, usaremos tres entornos separados y claramente definidos:

Entorno de Desarrollo (DEV):

Ubicación: PC con WSL y Ubuntu.
Propósito: Aquí escribes y pruebas el código. La base de datos se puede borrar y restaurar constantemente. Es tu "taller".


Entorno de Pruebas (TEST / Staging): Ubicación: El servidor en Oracle Cloud.
Propósito: Es un clon del entorno de producción. Aquí, el personal de MADENAT (Gerente, Bodeguero) realizará las "Pruebas de Aceptación de Usuario" (UAT)  para validar que los cambios funcionan como esperan antes de pasarlos al sistema real.

Entorno de Producción (PROD): Ubicación: Servidor final que se definirá (ej. Oracle, Digital Ocean, etc.).
Propósito: Es el sistema en vivo que MADENAT usará todos los días. Es sagrado. Solo se actualiza con cambios que han sido validados y probados en el entorno TEST.

2. Configuración del Entorno de Desarrollo (WSL)
Estructura del Proyecto y Archivo de Configuración
Estructura de Directorios Actual

el proyecto está en ~/odoo-madenat y su estructura es la siguiente:

~/odoo-madenat/: Carpeta raíz del proyecto. Aquí se ha clonado el código fuente de Odoo.

~/odoo-madenat/odoo-bin: El ejecutable principal de Odoo.

~/odoo-madenat/addons/: La carpeta que contiene todos los módulos nativos de Odoo (Ventas, Inventario, Contabilidad, etc.).

~/odoo-madenat/custom_addons/: Tu carpeta de trabajo. Aquí es donde vivirá nuestro módulo madenat_inventory y cualquier otra personalización que creemos.

~/odoo-madenat/odoo.conf: Tu archivo de configuración.

Esta estructura es perfecta. Ahora, ajustemos el archivo de configuración para que Odoo sepa dónde encontrar tus módulos personalizados.

Archivo de Configuración (odoo.conf) - CORREGIDO

Este es el paso más importante. Necesitamos que el parámetro addons_path en tu archivo de configuración apunte a las carpetas correctas.

Abre tu archivo de configuración:

Bash

nano ~/odoo-madenat/odoo.conf
Borra el contenido que pueda tener y reemplázalo con este. He adaptado las rutas para que coincidan con tu usuario (viruco) y tu estructura de carpetas (custom_addons):

Ini, TOML

[options]
; Esta es la contraseña maestra para gestionar bases de datos
admin_passwd = admin_password_super_segura

; Conexión a la base de datos PostgreSQL
db_host = localhost
db_port = 5432
db_user = viruco
db_password = TU_CONTRASEÑA_POSTGRES

; -------------------------------------------------------------------
; RUTA A LOS ADDONS (ESTA ES LA LÍNEA MÁS IMPORTANTE Y CORREGIDA)
; -------------------------------------------------------------------
; Odoo buscará módulos en estas carpetas, en el orden en que aparecen.
; Primero buscará en 'custom_addons', y si no lo encuentra, buscará en los 'addons' nativos.
addons_path = /home/viruco/odoo-madenat/custom_addons,/home/viruco/odoo-madenat/addons

; Archivo de log
logfile = /home/viruco/odoo-madenat/odoo.log
log_level = info
Guarda el archivo (Ctrl+O) y sal (Ctrl+X).

3. Flujo de Trabajo y Comandos Clave (Corregidos)
Con la configuración ya corregida, los comandos para trabajar en el proyecto también cambian ligeramente. Asegúrate de ejecutar siempre los comandos desde la raíz de tu proyecto ~/odoo-madenat.

Crear el Módulo Personalizado para MADENAT (Comando Corregido)

Si ya habías creado un módulo en otra carpeta, te recomiendo borrarlo y crearlo de nuevo en la ubicación correcta para mantener todo limpio.

Bash

# Asegúrate de estar en la carpeta raíz del proyecto
cd ~/odoo-madenat

# Usa el ejecutable 'odoo-bin' para crear la estructura de tu módulo
# dentro de la carpeta 'custom_addons'.
./odoo-bin scaffold madenat_inventory ./custom_addons
Ahora, si revisas la carpeta custom_addons, verás que contiene una nueva carpeta madenat_inventory con todos los archivos base.

Instalar/Actualizar tu Módulo (Comando Corregido)

Este será el comando que más utilices. Cada vez que modifiques el código Python (.py) o las vistas (.xml) de tu módulo, deberás ejecutarlo para que Odoo aplique los cambios.

Asegúrate de que la base de datos donde quieres instalar el módulo ya esté creada en PostgreSQL.

Ejecuta el siguiente comando para iniciar Odoo y actualizar tu módulo:

Bash

# Estando en ~/odoo-madenat/
# -c le dice a Odoo que use tu archivo de configuración.
# -d especifica la base de datos sobre la que quieres trabajar (ej: madenat_dev).
# -u le dice a Odoo que actualice el módulo 'madenat_inventory'.
./odoo-bin -c odoo.conf -d madenat_dev -u madenat_inventory
Si es la primera vez que lo instalas, puedes usar el flag -i en lugar de -u:

Bash

./odoo-bin -c odoo.conf -d madenat_dev -i madenat_inventory
Resumen de las correcciones:

Hemos confirmado que tu estructura de directorios es la definitiva.

Hemos ajustado el archivo odoo.conf, específicamente el addons_path, para que apunte a custom_addons y addons.

Hemos corregido los comandos (scaffold y la ejecución de odoo-bin) para que se ejecuten desde la raíz del proyecto ~/odoo-madenat/.

Próximo Paso Sugerido:

Verifica tu archivo odoo.conf y asegúrate de que tenga el contenido corregido.

Ejecuta el comando scaffold para crear (o re-crear) tu módulo madenat_inventory en la ubicación correcta.

Intenta iniciar Odoo con el comando ./odoo-bin -c odoo.conf -d madenat_dev.
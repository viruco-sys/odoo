Plan Maestro de Implementación v2.0.
________________________________________
Plan Maestro de Implementación: Sistema de Gestión de Inventario y Logística para Madenat
Versión: 2.0 (Corregida y Reforzada)
Fecha: 02-09-2025
Autor: Tu Experto en Implementación Odoo
________________________________________
1. Resumen Ejecutivo
Este documento constituye el plan de acción definitivo para la implementación del sistema de gestión para Madenat sobre Odoo 18 Community. Es el resultado de un riguroso proceso de análisis y una validación colaborativa que ha permitido refinar la arquitectura inicial hacia una solución robusta, escalable y alineada con las mejores prácticas de la plataforma Odoo.
El objetivo es automatizar el ciclo de vida del inventario, desde la recepción de materia prima hasta la documentación de la exportación, eliminando la dependencia de procesos manuales. La arquitectura ha sido corregida y reforzada para utilizar el modelo de Lotes (stock.lot) como pilar central de la trazabilidad, garantizando la integridad de los datos, la correcta valorización del inventario y una integración nativa con todas las funcionalidades del ERP.
La implementación se ejecutará bajo una metodología Ágil en cinco fases bien definidas, comenzando con una Fase 0 de Cimientos para asegurar que toda la configuración y estructura estén en su lugar antes de iniciar el desarrollo de funcionalidades, garantizando así un proceso de entrega de valor predecible y de alta calidad.
________________________________________
2. Metodología y Principios Guía
La excelencia del producto final es un reflejo directo de la calidad de la metodología utilizada para construirlo. Por ello, este proyecto se adhiere a los siguientes principios:
2.1. Metodología Ágil (Scrum/Kanban)
Adoptamos un enfoque iterativo y adaptativo para maximizar la flexibilidad y asegurar que el producto final se alinee perfectamente con las necesidades del negocio.
•	Ciclos de Trabajo (Sprints): El proyecto se divide en fases cortas (1-2 semanas), cada una con un objetivo claro y entregables funcionales que podrás ver y validar.
•	Roles:
o	Product Owner: Mauricio Navarrete. Eres la voz del negocio, responsable de definir qué se construye y en qué orden de prioridad.
o	Equipo de Desarrollo: Mauricio Navarrete. Responsable de la ejecución técnica y la entrega de software de calidad.
•	Transparencia y Comunicación: Mantendremos una comunicación fluida y constante. El tablero Kanban y las revisiones de Sprint asegurarán que siempre tengas una visibilidad completa del progreso del proyecto.
2.2. Principios de Desarrollo y Mejores Prácticas
Construimos software profesional que debe ser tan fácil de mantener y extender como lo es de usar.
•	Control de Versiones con Git: El código fuente es un activo crítico. Se gestionará en un repositorio Git, utilizando una estrategia de ramas (main, develop, feature/) para asegurar que nunca se pierda trabajo y que el código en producción sea siempre estable.
•	Gestión de Entornos (DEV/STAGING/PROD):
o	DEV (Tu WSL): El taller de desarrollo. Aquí se forjan las nuevas funcionalidades.
o	STAGING (Servidor de Pruebas): El control de calidad. Un clon de producción donde validas que todo funciona como se espera antes del lanzamiento.
o	PROD (Servidor en Vivo): El entorno operativo. Intocable y sagrado, solo recibe código que ha sido rigurosamente probado y validado.
•	Calidad de Código y Pruebas: El código no solo debe funcionar, debe ser limpio, legible y robusto. Utilizaremos herramientas de análisis estático (linting) y crearemos pruebas automáticas para las lógicas de negocio críticas (cálculos de volumen, etc.).
•	Kaizen (Mejora Continua): Entendemos que el sistema evolucionará con tu negocio. La arquitectura modular que estamos construyendo está diseñada para facilitar futuras mejoras y la adición de nuevas funcionalidades sin tener que reconstruir los cimientos.
________________________________________
3. Arquitectura de la Solución (Corregida)
Esta es la base técnica sobre la cual se construirá todo el sistema. La corrección arquitectónica es el cambio más significativo y beneficioso de esta versión 2.0 del plan.
3.1. El Pilar Central: stock.lot como Nuestra "Tarja"
Abandonamos el uso de stock.quant.package y adoptamos stock.lot como el modelo para representar la "Tarja".
•	¿Por Qué? Porque una "Tarja" en el negocio de Madenat no es un empaque temporal, es un activo de inventario con identidad propia y persistente. El modelo stock.lot está diseñado precisamente para esto.
•	Beneficios Inmediatos:
1.	Persistencia de Datos: Un lote se crea en la recepción y existe durante toda la vida del producto en el inventario. Su historial de movimientos es inmutable.
2.	Trazabilidad Completa: Podemos seguir un lote específico desde su compra hasta su venta, pasando por todas sus ubicaciones intermedias.
3.	Integración Nativa GARANTIZADA: Se integra de forma nativa y robusta con todas las áreas críticas de Odoo: Compras, Inventario, Ventas y, crucialmente, con la Valorización de Inventario y los Costos en Destino (stock_landed_costs).
3.2. Arquitectura de Módulos Odoo Personalizados
La estructura de 4 módulos se mantiene, pero sus responsabilidades internas se ajustan a la nueva arquitectura.
1.	madenat_lumber_core:
o	Responsabilidad: Definir la "Tarja" y sus propiedades.
o	Componentes: Extensión del modelo stock.lot (no package) para añadir todos los campos de dimensiones, piezas, proveedor y los campos compute para los cálculos de volumen.
2.	madenat_lumber_importer:
o	Responsabilidad: Automatizar la creación de "Tarjas" (Lotes).
o	Componentes: Asistente de importación que leerá el packing list y creará una recepción (stock.picking) y, por cada línea del archivo, creará un nuevo Lote (stock.lot) con todos sus datos.
3.	madenat_lumber_logistics:
o	Responsabilidad: Gestionar y documentar la exportación.
o	Componentes:
	Nuevo modelo lumber.shipment ("Embarque").
	Integración Clave: Este modelo se vinculará directamente a una o varias transferencias de inventario de salida (stock.picking). Esto nos permite usar toda la potencia del motor de inventario de Odoo para gestionar las reservas y salidas de stock.
	El embarque agrupará múltiples Lotes (stock.lot).
4.	madenat_lumber_reports:
o	Responsabilidad: Generar los documentos de salida.
o	Componentes: Plantilla QWeb que leerá los Lotes asociados a un embarque para generar el "Listado de Embarque".

Aquí tienes la continuación del Plan Maestro de Implementación v2.0.
________________________________________
4. Plan de Implementación por Fases (Corregido)
Este roadmap revisado incorpora la Fase 0 y ajusta los objetivos de las fases subsiguientes para alinearse con nuestra nueva arquitectura, asegurando una progresión lógica y sin bloqueos.
Fase 0: Cimientos y Configuración (Sprint 0 - Duración: 3-4 días)
•	Objetivo: Preparar toda la infraestructura técnica, de gestión y de datos maestros para habilitar el desarrollo.
•	Tareas Principales:
1.	Infraestructura: Creación del repositorio Git, definición de la estrategia de ramas y validación del entorno de desarrollo local.
2.	Configuración de Odoo: Activar la trazabilidad por Lotes/Números de serie y crear los atributos de producto (Espesor, Ancho, Largo).
3.	Datos Maestros: Crear las plantillas de producto base para la madera y algunas de sus variantes para las pruebas iniciales.
4.	Scaffolding: Crear la estructura de directorios de los cuatro módulos personalizados.
•	Entregable: Un entorno de desarrollo listo, con el código base inicializado y Odoo configurado para soportar el modelo de negocio.
________________________________________
Fase 1: MVP - El Núcleo del Inventario (Sprint 1 - Duración: 1 Semana)
•	Objetivo: Lograr que el sistema pueda registrar "Tarjas" (como Lotes) con sus dimensiones y que sus volúmenes se calculen de forma automática y precisa.
•	Historias de Usuario a Implementar:
o	US-002 (Corregida): Modelo de Datos de "Tarja" Extendido en stock.lot.
o	US-003 (Corregida): Cálculos de Volumen en "Tarjas" (stock.lot).
•	Proceso de Validación (Sprint Review):
1.	Crearemos manualmente una recepción de un producto maderero.
2.	En el proceso, crearemos un nuevo Lote (nuestra Tarja), y se nos presentarán los nuevos campos para rellenar (piezas, dimensiones, proveedor).
3.	Validaremos que al guardar, los campos de Volumen (m³) y Volumen (MBF) se calculen y muestren el valor correcto.
•	Entregable: Un sistema capaz de gestionar un inventario de Tarjas/Lotes con todos los datos y cálculos del negocio.
________________________________________
Fase 2: Automatización del Ingreso (Sprint 2 - Duración: 1.5 Semanas)
•	Objetivo: Eliminar la tarea de mayor consumo de tiempo: el ingreso manual de packing lists.
•	Historia de Usuario a Implementar:
o	US-004 (Corregida): Asistente de Importación de Packing Lists para crear Lotes.
•	Proceso de Validación (Sprint Review):
1.	Utilizaremos una plantilla de Excel/CSV y un packing list real.
2.	Ejecutaremos el asistente de importación, subiremos el archivo.
3.	Verificaremos que se haya creado una recepción en Odoo y que por cada línea del archivo, se haya generado un nuevo Lote (stock.lot) con todos sus datos y volúmenes ya calculados.
•	Entregable: El importador automático, la funcionalidad de mayor impacto operativo.
________________________________________
Fase 3: Logística y Trazabilidad de Exportación (Sprint 3 - Duración: 1.5 Semanas)
•	Objetivo: Gestionar el proceso de exportación, integrando la logística con el inventario y generando la documentación de salida.
•	Historias de Usuario a Implementar:
o	US-005 (Corregida): Modelo de Datos de "Embarque" integrado con stock.picking.
o	US-006 (Corregida): Generación del "Listado de Embarque" basado en Lotes.
•	Proceso de Validación (Sprint Review):
1.	Crearemos una Transferencia de Salida en Odoo para un cliente. En las operaciones, especificaremos los Lotes (Tarjas) a enviar.
2.	Crearemos un registro de "Embarque", lo asociaremos a esta transferencia de salida y completaremos los datos logísticos.
3.	Presionaremos el botón "Imprimir Listado" y validaremos que el PDF generado sea correcto.
•	Entregable: Capacidad completa para gestionar y documentar los envíos de exportación de forma integrada.
________________________________________
Fase 4: Finanzas y Puesta en Marcha (Sprint 4 - Duración: 1 Semana)
•	Objetivo: Asegurar la correcta valorización del inventario y preparar el sistema para el lanzamiento.
•	Historia de Usuario a Implementar:
o	US-007: Aplicación de Costos en Destino (Landed Costs).
•	Proceso de Validación (Sprint Review):
1.	Tomaremos una recepción creada por el importador.
2.	Aplicaremos un "Costo en Destino" simulado (flete, seguro).
3.	Revisaremos la capa de valoración (stock.valuation.layer) de los Lotes involucrados para confirmar que su costo ha sido actualizado correctamente.
•	Entregable: Un sistema listo para producción con un flujo financiero validado.
________________________________________
5. Desglose Detallado de Historias de Usuario (Corregido)
Este es el backlog de trabajo detallado con las especificaciones técnicas ajustadas a la nueva arquitectura.
US-002 (Corregida): Modelo de Datos de "Tarja" Extendido en stock.lot
•	Como: Jefe de Operaciones
•	Quiero: Que el modelo de "Lotes" de Odoo (stock.lot) incluya los campos específicos de una Tarja.
•	Para: Almacenar de forma persistente toda la información relevante de cada Tarja en el sistema.
•	Módulo: madenat_lumber_core
•	Notas Técnicas: Heredar de stock.lot. Añadir los campos x_espesor_mm, x_ancho_mm, x_largo_m, x_piezas, x_proveedor_id, x_paquete_proveedor_nro, y los campos compute de volumen. Modificar las vistas de formulario y árbol de stock.lot para que estos campos sean visibles y editables.
________________________________________
US-003 (Corregida): Cálculos de Volumen en "Tarjas" (stock.lot)
•	Como: Sistema
•	Quiero: Calcular automáticamente los volúmenes en m³ y MBF para cada Lote/Tarja.
•	Para: Asegurar la precisión de los datos y eliminar cálculos manuales.
•	Módulo: madenat_lumber_core
•	Notas Técnicas: Implementar la función _compute_volume con el decorador @api.depends en el modelo stock.lot. Asegurar que los campos de volumen tengan store=True para permitir reportes y agrupaciones eficientes.
________________________________________
US-004 (Corregida): Asistente de Importación de Packing Lists para crear Lotes
•	Como: Encargado de Bodega
•	Quiero: Un asistente para subir un archivo CSV/Excel con los datos de un packing list de proveedor.
•	Para: Crear automáticamente una recepción y los Lotes/Tarjas asociados.
•	Módulo: madenat_lumber_importer
•	Notas Técnicas: El wizard creará un stock.picking de tipo incoming. Por cada fila del archivo, creará un stock.lot con todas las dimensiones y datos, y luego creará un stock.move.line en el picking, asignándole el lote recién creado y la cantidad de piezas.
________________________________________
US-005 (Corregida): Modelo de Datos de "Embarque" integrado con stock.picking
•	Como: Encargado de Logística
•	Quiero: Crear un registro de "Embarque" que se vincule a las operaciones de salida de inventario.
•	Para: Tener una visión logística unificada y aprovechar la funcionalidad nativa de Odoo.
•	Módulo: madenat_lumber_logistics
•	Notas Técnicas: El modelo lumber.shipment tendrá una relación Many2one a stock.picking. Se puede usar un related field para traer información del picking al embarque (como el cliente o la dirección de destino). La lista de lotes se obtendrá a través de los move_line_ids del picking asociado.
________________________________________
US-006 (Corregida): Generación del "Listado de Embarque" basado en Lotes
•	Como: Encargado de Logística
•	Quiero: Imprimir un "Listado de Embarque" en PDF desde un registro de Embarque.
•	Para: Generar la documentación de exportación.
•	Módulo: madenat_lumber_reports
•	Notas Técnicas: El reporte QWeb obtendrá los lotes a listar desde el stock.picking asociado al lumber.shipment. Iterará sobre los move_line_ids.lot_id para acceder a toda la información de cada Tarja/Lote.
________________________________________
US-007: Aplicación de Costos en Destino (Landed Costs)
•	Como: Contador
•	Quiero: Aplicar costos adicionales a las recepciones de madera.
•	Para: Asegurar que la valoración del inventario sea precisa.
•	Módulo: Configuración nativa (stock_landed_costs).
•	Notas Técnicas: No requiere desarrollo, pero sí configuración y capacitación. Asegurar que los productos estén configurados con método de costeo AVCO y valoración de inventario Automatizada.
________________________________________
6. Plan de Puesta en Marcha y Mejora Continua
•	Migración de Datos: Se realizará una carga inicial de datos maestros (Productos, Proveedores) antes del Go-Live. El inventario inicial se cargará utilizando nuestro nuevo importador.
•	Capacitación: Se realizarán sesiones prácticas enfocadas en los flujos de trabajo clave para asegurar la correcta adopción por parte de los usuarios.
•	Soporte Post-Lanzamiento: Se establecerá un periodo de soporte intensivo ("hypercare") de 2-4 semanas para resolver cualquier incidencia y asistir a los usuarios.
•	Evolución del Sistema: El lanzamiento es el comienzo. Todas las futuras necesidades se gestionarán como nuevas historias de usuario en nuestro backlog, permitiendo que el sistema crezca y evolucione junto con el negocio de Madenat.


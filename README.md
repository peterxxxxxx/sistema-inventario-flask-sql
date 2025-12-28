# Sistema de Inventario con Integración a Banxico mx

Este proyecto es un catálogo de artículos desarrollado en Python (Flask) que se integra con la API de Banxico para calcular precios en dólares en tiempo real.

##  Características
- **CRUD Completo:** Listado y registro de artículos.
- **Integración con API Externa:** Consumo de la API de Banxico (SIE) mediante el backend.
- **Seguridad:** Uso de consultas parametrizadas para evitar Inyección SQL.
- **Base de Datos:** Conexión robusta a SQL Server mediante PyODBC.

##  Tecnologías Usadas
- **Backend:** Python 3.10 en adelante / Flask
- **Base de Datos:** Microsoft SQL Server
- **Frontend:** HTML5, Bootstrap 5, Jinja2
- **Librerías:** Requests (API), PyODBC (SQL)

##  Requisitos
Para ejecutar este proyecto, necesitas:
1. SQL Server instalado.
2. Un Token de consulta de la API de Banxico.
3. Instalar dependencias: `pip install flask pyodbc requests`
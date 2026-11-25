# A1 · Ficha de interpretación del análisis y plataforma tecnológica

Insumo: SRS v2.0 de CoffeeCol / Tantico Café (IEEE 830, hecho por el equipo) y el modelo de análisis de G1. **Diseño individual:** diseño el subconjunto de 17 requisitos funcionales que sostienen los tres casos críticos del análisis (CU-03 iniciar sesión, CU-06 checkout y CU-11 gestionar productos) más el ciclo de estados del pedido.

## Requisitos funcionales que diseño (17)

| ID | Requisito | Prioridad | Actor |
|---|---|---|---|
| RF-011 | Agregar productos al carrito | Alta | Visitante / Cliente |
| RF-012 | Aumentar, disminuir o quitar ítems del carrito | Alta | Visitante / Cliente |
| RF-014 | Calcular subtotal, despacho ($12.000; gratis sobre $150.000) y total | Alta | Visitante / Cliente |
| RF-017 | Formulario de checkout con datos de entrega | Alta | Cliente |
| RF-018 | Validar correo, teléfono de 10 dígitos y campos vacíos | Alta | Cliente |
| RF-019 | Resumen desglosado del pedido antes de confirmar | Alta | Cliente |
| RF-020 | Registrar el pedido con código único | Alta | Cliente |
| RF-021 | Confirmación con número de pedido y vaciado del carrito | Media | Cliente |
| RF-022 | Ciclo de estados del pedido | Alta | Administrador |
| RF-023 | Acceso de clientes con cuenta de Google | Alta | Visitante |
| RF-024 | Acceso de clientes con enlace mágico | Alta | Visitante |
| RF-025 | Acceso del administrador con usuario y clave cifrada (sesión de 60 min) | Alta | Administrador |
| RF-027 | Sincronizar al usuario en la base tras acceder con Firebase | Alta | Cliente |
| RF-028 | Verificar el rol y llevar al usuario a su módulo | Alta | Cliente / Administrador |
| RF-038 | Acreditar 1 punto por cada $1.000 y asignar nivel | Alta | Cliente |
| RF-045 | Alta de productos con nombre, descripción, precio, categoría, stock e imagen | Alta | Administrador |
| RF-046 | Eliminar productos del catálogo activo | Alta | Administrador |

## Requisitos no funcionales que condicionan el diseño (8)

| ID | Categoría | Requisito |
|---|---|---|
| RNF-004 | Concurrencia | 50 peticiones simultáneas por segundo sin perder transacciones |
| RNF-005 | Seguridad | Todo endpoint administrativo valida firma y vigencia del token |
| RNF-006 | Seguridad | El total de cada orden se recalcula en el servidor desde la base de datos |
| RNF-008 | Seguridad | Credenciales y llaves fuera del alcance público (.env) |
| RNF-009 | Fiabilidad | Crear órdenes y canjear puntos son operaciones atómicas |
| RNF-010 | Fiabilidad | Si Firebase no responde, avisar sin romper el catálogo |
| RNF-013 | Mantenibilidad | Acceso a datos centralizado en un único archivo |
| RNF-016 | Legal | Casilla obligatoria de aceptación de la política de datos (Ley 1581) |

## Actores
Visitante, Cliente registrado, Administrador, Firebase Authentication (secundario) y el Temporizador del sistema (bono de cumpleaños, fuera de este subconjunto).

## Restricciones del caso (SRS)
- Backend en PHP 8.5 sobre Apache gestionado con XAMPP; base de datos MariaDB 10.4 / MySQL en 3FN con PDO.
- Identidad de clientes con Firebase Authentication (Google y enlace mágico); administrador con usuario, clave con Bcrypt y token JWT de 60 minutos.
- Frontend sin librerías invasivas: JavaScript ES6+ y Bootstrap 5.3.
- Equipo de 3 aprendices, un cliente disponible semanalmente y plazo de la ficha.

## Plataforma tecnológica y justificación
| Decisión | Elección | Condiciones concretas del caso que la justifican |
|---|---|---|
| Lenguaje orientado a objetos | **PHP 8.5** (clases, interfaces, tipado) | (1) Es una restricción del SRS y el equipo ya lo usó en el año; (2) corre en Apache/XAMPP, que es el servidor disponible; (3) PDO da acceso a datos con sentencias preparadas (RNF-013, RNF-006) y Composer trae las librerías de Firebase y JWT que el SRS exige (RNF-005, RNF-010) |
| Tipo de base de datos | **Relacional** (MariaDB 10.4) | (1) Registrar un pedido y acreditar puntos debe ser atómico (RNF-009), algo que dan las transacciones; (2) las relaciones cliente–pedido–producto son fijas y bien conocidas; (3) el SRS exige 3FN y MariaDB; (4) los reportes del administrador agregan por fecha, estado y cliente con SQL |

## Entregables de diseño que produce esta carpeta
A2 diagrama de clases · A3 patrones · A4 arquitectura · A5 vista de componentes · A6 vista de despliegue · A7 matriz de trazabilidad (más el modelo de datos en G2-P2).

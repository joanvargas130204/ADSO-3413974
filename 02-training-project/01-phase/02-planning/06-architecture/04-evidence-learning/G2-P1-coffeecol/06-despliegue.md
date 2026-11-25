# A6 · Vista de despliegue

Fuente editable: [despliegue.mmd](diagramas/despliegue.mmd) · Imagen: [png](diagramas/despliegue.png) · [svg](diagramas/despliegue.svg)

| Nodo | Artefactos que aloja | Conexión (protocolo y puerto) | Decisión que responde a un RNF |
|---|---|---|---|
| 1 · Cliente (PC o celular) | Navegador con la interfaz (HTML5, CSS3, JavaScript) y el carrito | HTTPS 443 hacia la aplicación; HTTPS 443 hacia Firebase para iniciar sesión | RNF-011 y RNF-015: corre en navegadores de 360 a 1920 px; los datos personales viajan cifrados (RNF-016) |
| 2 · Servidor de aplicación (Apache 2.4 + PHP 8.5, XAMPP) | API REST (controladores, servicios, repositorios) y el archivo `.env` | TCP 3306 hacia la base; HTTPS 443 hacia Firebase | RNF-008: el `.env` queda fuera de la carpeta pública; RNF-004: sin estado, se puede replicar |
| 3 · Servidor de datos (MariaDB 10.4) | Esquema `coffeecol` | Solo acepta conexiones por TCP 3306 de la red local del nodo 2 | Seguridad de red: la base no se expone a internet |
| 4 · Nube de Google | Firebase Authentication | HTTPS 443 | RNF-010: servicio externo desacoplado; su caída no rompe el catálogo |

En desarrollo los nodos 2 y 3 comparten el equipo (XAMPP); la separación lógica se conserva: la base escucha solo en la dirección local.

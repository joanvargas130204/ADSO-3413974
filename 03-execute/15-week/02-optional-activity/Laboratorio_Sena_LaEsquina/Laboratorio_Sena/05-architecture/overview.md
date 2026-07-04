# overview

> Estado: 🟡 En progreso | Última actualización: 2026-06-20
> Autor: Por definir | Equipo: Análisis y Desarrollo de Software (SENA)

## Contexto

El SRS no define una arquitectura técnica; define restricciones de negocio y de calidad (RNF, RN) que la arquitectura debe satisfacer. Este documento traduce esas restricciones en lineamientos de arquitectura. Las decisiones técnicas concretas (framework, base de datos, etc.) deben registrarse como ADR en [`05-architecture/decisions/`](./decisions/).

## Contenido

### Componentes lógicos (derivados de los módulos del SRS)

| Componente | Módulo SRS | Notas de arquitectura |
|------------|------------|------------------------|
| Catálogo | M1 | Debe permitir hasta 90 productos sin degradar el rendimiento (RNF03); diseñar para escalar a 300 (RNF07) |
| POS / Ventas | M2 | Debe responder en ≤3 seg con hasta 15 productos por venta (RNF03) |
| Usuarios y Roles | M3 | Control de acceso por rol (Administrador / Empleado) (RNF04) |
| Corte de Caja | M4 | Requiere consistencia entre lo vendido y lo registrado para el cálculo de diferencias |
| Tiquetes | M5 | Debe soportar al menos dos canales de salida: impresión y PDF/WhatsApp |
| Fiado | M6 | Requiere seguimiento temporal (alertas a 30 días) |

### Restricciones que condicionan la arquitectura

| Restricción | Origen | Implicación arquitectónica |
|-------------|--------|------------------------------|
| Modo offline con sincronización <5 min | RNF02 | Arquitectura local-first con sincronización diferida, no dependiente de conexión permanente |
| Hardware de bajo costo (Android 8.0 / Windows 10, 2 GB RAM) | RNF05 | Evitar componentes de alto consumo de memoria/CPU; sin hardware especializado |
| Sin licencia mensual recurrente | RN01 | Evitar dependencias de pago por suscripción en la pila tecnológica elegida |
| Autonomía operativa sin soporte técnico | RN02 | Instalación, backup y actualización deben poder ejecutarse por el propio Administrador |
| Escalabilidad a 300 productos o segunda sede | RNF07 | Diseño que no requiera rediseño estructural ante ese crecimiento |
| Backup diario + sincronización en nube (Google Drive) | RNF08 | Mecanismo de respaldo local y de sincronización en la nube |

## Referencias

- [04-requirements/non-functional.md](../04-requirements/non-functional.md)
- [05-architecture/deployment.md](./deployment.md)
- [05-architecture/cross-cutting.md](./cross-cutting.md)
- [05-architecture/decisions/README.md](./decisions/README.md)

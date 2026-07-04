# Preguntas abiertas

> Estado: 🟡 En progreso | Última actualización: 2026-06-16
> Autor: Por definir | Equipo: Arquitectura / Gestión

## Flujo de resolución

1. **Registrar:** cualquier equipo puede agregar una pregunta abierta con estado `ABIERTA`.
2. **Asignar:** el equipo de arquitectura o gestión asigna un responsable y una fecha límite de respuesta.
3. **Resolver:** el responsable responde y cambia el estado a `RESUELTA`.
4. **Escalar si aplica:** si la resolución genera una decisión técnica relevante, crear un ADR en `05-architecture/decisions/records/`. Si afecta requisitos, actualizar `04-requirements/`.
5. **Cerrar:** preguntas resueltas se mantienen en el historial (no eliminar). Mover a sección `## Resueltas` cuando el registro sea largo.

## Formato de registro

| # | Pregunta | Área | Responsable | Fecha límite | Estado | Resolución / ADR |
|---|----------|------|-------------|--------------|--------|------------------|

## Estados válidos

| Estado | Significado |
|--------|-------------|
| `ABIERTA` | Sin respuesta aún |
| `EN REVISIÓN` | Responsable asignado, trabajando en ella |
| `RESUELTA` | Tiene respuesta, puede generar ADR o actualización |
| `CANCELADA` | Ya no aplica (indicar por qué) |

---

## Preguntas abiertas

| # | Pregunta | Área | Responsable | Fecha límite | Estado | Resolución / ADR |
|---|----------|------|-------------|--------------|--------|------------------|
| 1 | ¿Qué stack técnico y arquitectura de despliegue concreta soportará el modo offline (RNF02) y el hardware mínimo (RNF05)? | Arquitectura | Por definir | Por definir | ABIERTA | — |
| 2 | ¿Qué mecanismo de autenticación se usará para diferenciar Administrador y Empleado en hardware sin conexión permanente? | Arquitectura / Seguridad | Por definir | Por definir | ABIERTA | — |
| 3 | ¿Cuál será el proveedor y formato exacto de sincronización en nube además de Google Drive (RNF08)? | DevOps / Operaciones | Por definir | Por definir | ABIERTA | — |
| 4 | ¿En qué iteración se abordarán los requisitos Could Have (RF07–RF10, RNF07)? | Producto | Por definir | Por definir | ABIERTA | — |

---

## Resueltas

| # | Pregunta | Área | Resolución | ADR / Doc relacionado |
|---|----------|------|------------|-----------------------|

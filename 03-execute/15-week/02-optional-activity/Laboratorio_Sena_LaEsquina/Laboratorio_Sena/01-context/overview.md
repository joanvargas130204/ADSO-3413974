# Overview

> Estado: 🟡 En progreso | Última actualización: 2026-06-20
> Autor: Por definir | Equipo: Análisis y Desarrollo de Software (SENA)

## Contexto institucional

Proyecto formativo del programa **Análisis y Desarrollo de Software (SENA)**. El caso de estudio es el **Supermercado La Esquina**, un negocio familiar atendido por su propietario, **Carlos Ruiz** (Administrador), y 3 empleados (Martha Suárez, Julián Torres y Diego Morales). El catálogo del negocio tiene 90 productos y la operación actual es 100 % manual (cuaderno + calculadora), con un promedio de 42,5 ventas/día en horario de 7 a.m. a 7 p.m.

| Actor | Rol en el sistema | Turno | Observación |
|-------|-------------------|-------|-------------|
| Carlos Ruiz | Administrador | 7 a.m.–7 p.m. | Único decisor del negocio. Resistencia moderada a la tecnología. |
| Martha Suárez | Empleado | 7 a.m.–4 p.m. | Apoya caja en hora pico. |
| Julián Torres | Empleado | 8 a.m.–4 p.m. | Más errores en hora pico (12 p.m.–2 p.m.). |
| Diego Morales | Empleado | 2 p.m.–7 p.m. | Consulta frecuente el cuaderno de precios. |

## Problema

La operación manual del supermercado genera seis problemas medibles, documentados con evidencia (D01–D06):

| Problema | Dato concreto | Impacto |
|----------|---------------|---------|
| Cobro lento | Sumar con calculadora toma 120 seg (44 % del tiempo de la transacción) | Tiempos de espera inaceptables para 5 de cada 15 clientes |
| Precios incorrectos | 8 de 90 productos desactualizados (D04) | Cobros erróneos a 3 clientes identificados |
| Sin control de inventario | Pedidos hechos de memoria por el propietario (D05) | Quiebres de stock no detectados hasta que el cliente los reporta |
| Cartera sin trazabilidad | $336.000 COP en fiado sin registro de abonos (D02) | Pérdidas no cuantificadas por olvido |
| Sin pagos digitales | 4 de 15 clientes se retiran sin comprar | Ventas perdidas medibles |
| Sin auditoría | D01–D06 sin trazabilidad por empleado o producto | Imposible detectar hora pico, producto líder o faltante de caja |

## Objetivos

- Desarrollar un sistema **POS + Inventario (MVP)** que permita registrar ventas, controlar el stock de hasta 90 productos y gestionar créditos (fiado).
- Reducir el tiempo promedio por transacción de **382 seg a 145 seg (−62 %)**, eliminando la suma manual con calculadora.
- Garantizar una curva de aprendizaje máxima de **2 horas** para usuarios sin experiencia técnica (RNF01).
- Dar trazabilidad por empleado, producto y método de pago, hoy inexistente (D01–D06).

## Referencias

- [SRS — Supermercado La Esquina v1.0, abril 2026 (SENA — Análisis y Desarrollo de Software)](../04-requirements/README.md)
- [01-context/scope.md](./scope.md)
- [04-requirements/functional.md](../04-requirements/functional.md)

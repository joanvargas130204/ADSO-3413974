# Changelog

## [Unreleased]

### Added
- Integración completa del SRS — Supermercado La Esquina v1.0 (abril 2026) en la estructura documental existente: `01-context`, `02-domain`, `03-product`, `04-requirements`, `05-architecture`, `06-data`, `07-api`, `08-uml`, `09-microservices`, `10-devops`, `11-quality`, `12-ux-ui`, `13-operations`, `14-training`, `15-project-control`.
- `04-requirements/functional.md` y `non-functional.md`: RF01–RF10, RNF01–RNF08 y RN01–RN02 completos, con prioridad MoSCoW.
- `04-requirements/user-stories.md`: HU01–HU03 derivadas de CU01–CU03 (Registrar Venta, Gestionar Catálogo, Corte de Caja Diario).
- `04-requirements/traceability-matrix.md`: trazabilidad entre módulos (M1–M6), requisitos, historias y problemas identificados (D01–D06).
- `08-uml/diagram-index.md`: registro de diagramas pendientes de creación (casos de uso, secuencia, clases) para CU01–CU03.
- `.github/CODEOWNERS`: regla catch-all `*` para archivos sin owner específico
- `00-governance/git-conventions.md`: sección de hotfix en main con flujo y cherry-pick a qa/dev
- `00-governance/security-rules.md`: sección de contacto de seguridad con placeholder de handles
- `.github/pull_request_template.md`: sección de rama destino (dev / qa / main) al inicio del template

### Changed
- `README.md` y `CONTRIBUTING.md`: nombre del proyecto actualizado a **Supermercado La Esquina** (antes referenciaban un proyecto distinto, "Horarios SENA", usado como plantilla base).

### Fixed
- `00-governance/documentation-rules.md`: estado ⚫ Deprecado ahora tiene criterio de decisión por tabla (sustituido / reestructurado / ADR)
- `00-governance/definition-of-ready.md`: criterio "alcance mínimo acordado" reemplazado por criterio verificable (secciones Contexto y Contenido con texto real)
- `00-governance/definition-of-done.md`: criterio "afecta a varios equipos" reemplazado por condición concreta (gobernanza, estructura, contratos compartidos)
- `00-governance/microservices-documentation.md`: agregado requisito de ADR o decisión registrada antes de crear carpeta de servicio nuevo
- `06-data/README.md`: agregada nota de diferenciación con modelos transaccionales en `09-microservices/`

### Added (sesión anterior)
- `.github/CODEOWNERS`: ownership de revisión por sección del repositorio
- `05-architecture/decisions/_template-adr.md`: template standalone para crear ADRs
- `15-project-control/open-questions.md`: flujo de registro y resolución de preguntas abiertas
- `00-governance/git-conventions.md`: reglas de ramas, ambientes, releases y commits
- `00-governance/microservices-documentation.md`: flujo para documentar microservicios reales
- `00-governance/security-rules.md`: reglas contra fugas de información sensible

### Fixed
- `05-architecture/decisions/README.md`: aclarada política de ADRs deprecadas (permanecen en `records/`, no se mueven)
- `CONTRIBUTING.md`: corregida instrucción contradictoria sobre mover ADRs a `99-archive/`
- `.github/pull_request_template.md`: añadidos criterios de Definition of Ready y Done al checklist
- `09-microservices/_template/README.md`: identificado claramente como plantilla (no documento pendiente)

### Improved
- `07-api/README.md`: añadida regla de contrato canónico vs contrato de implementación
- `00-governance/documentation-rules.md`: añadida tabla de dónde van recursos visuales (`assets/` vs `08-uml/`)
- `02-domain/README.md`: añadida nota de diferenciación con `06-data/`
- `06-data/README.md`: añadida nota de diferenciación con `02-domain/`
- `14-training/README.md`: añadida tabla de audiencias y orientación para equipo de soporte
- `README.md`: añadidos CHANGELOG y CODEOWNERS a documentos de gobierno
- `CONTRIBUTING.md`: reducido a hub operativo con enlaces a reglas especializadas
- `00-governance/documentation-rules.md`: enfocado en reglas documentales, índices y diagramas

---

## [Estructura inicial]

### Added
- Estructura inicial del repositorio de documentación

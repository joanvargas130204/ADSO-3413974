# SERVICIO NACIONAL DE APRENDIZAJE - SENA
## PROGRAMA DE FORMACIÓN: ANÁLISIS Y DESARROLLO DE SOFTWARE (ADSO)
### FICHA: 3413974 | COMPETENCIA: APLICACIÓN DE CONOCIMIENTOS DE LAS TIC
**Instructor:** Jesús Ariel González Bonilla  
**Evidencia 1 (Alistar):** Cuadro comparativo de equipos TIC, periféricos, tecnologías de almacenamiento, sistemas operativos y servicios de Internet.

---

## 1. INTRODUCCIÓN
El presente documento consolida el análisis comparativo integral de los componentes fundamentales que integran la infraestructura tecnológica contemporánea. Se evalúan y contrastan equipos TIC, periféricos de entrada/salida/mixtos, arquitecturas de almacenamiento de datos, sistemas operativos y servicios de conectividad a Internet, proporcionando una base técnica sólida para la selección, diseño y optimización de soluciones de software y hardware.

---

## 2. CUADRO COMPARATIVO 1: EQUIPOS TIC (COMPUTADORES Y DISPOSITIVOS)

| Tipo de Equipo TIC | Propósito / Uso Principal | Rendimiento y Capacidad de Cómputo | Portabilidad | Escalabilidad / Expansión | Rango de Costo Relativo |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **Computador de Escritorio (Desktop)** | Trabajo de oficina, desarrollo intensivo, diseño gráfico, gaming de alto rendimiento. | **Alto a Muy Alto.** Procesadores de escritorio sin limitaciones térmicas severas, GPU dedicada. | Baja (estación fija). | **Muy Alta.** Fácil reemplazo de RAM, almacenamiento, GPU y fuente de poder. | Medio - Alto |
| **Computador Portátil (Laptop)** | Productividad móvil, estudiantes, desarrolladores remotos y ejecutivos. | **Medio a Alto.** Optimizado para eficiencia energética y control térmico. | **Muy Alta.** Batería integrada y diseño compacto. | **Baja a Media.** Generalmente limitado a cambio de SSD y/o RAM. | Medio - Alto |
| **Servidor (Rack / Tower)** | Alojamiento de bases de datos, APIs, microservicios, virtualización y computación empresarial. | **Extremo.** Múltiples sockets CPU (Intel Xeon / AMD EPYC), memoria ECC masiva. | Nula (instalación en centro de datos / rack). | **Máxima.** Bahías hot-swap, fuentes redundantes, múltiples interfaces PCIe/Red. | Alto a Muy Alto |
| **Dispositivo Móvil (Smartphone / Tablet)** | Comunicación, consumo de contenido, validación de apps móviles y telemetría ligera. | **Moderado a Alto.** Arquitectura ARM optimizada para bajo consumo energético. | **Máxima.** Portabilidad de bolsillo. | **Nula.** Hardware soldado e integrado en SoC (System on Chip). | Bajo - Alto |
| **Estación de Trabajo (Workstation)** | Renderizado 3D, simulación de modelos de Machine Learning y compilación pesada. | **Muy Alto / Especializado.** GPUs profesionales (NVIDIA RTX A-series), memoria con corrección de errores (ECC). | Baja a Media. | **Alta.** Diseñado para operación continua 24/7 y cargas críticas. | Muy Alto |

---

## 3. CUADRO COMPARATIVO 2: CLASIFICACIÓN DE PERIFÉRICOS

| Categoría | Dispositivo | Función Técnica Principal | Interfaz / Conexión | Impacto en la Experiencia / Desarrollo |
| :--- | :--- | :--- | :--- | :--- |
| **Entrada** | **Teclado Mecánico / Membrana** | Captura de caracteres e instrucciones mediante pulsaciones de teclas. | USB-A, USB-C, Bluetooth, 2.4 GHz RF | Ergonomía y velocidad de codificación para el programador. |
| **Entrada** | **Ratón Óptico / Láser (Mouse)** | Control del cursor e interacción bidimensional con la interfaz gráfica (GUI). | USB, Bluetooth | Precisión en navegación, diagramación y diseño de interfaces. |
| **Entrada** | **Cámara Web / Micrófono** | Captura de flujo de video y audio analógico convertido a digital. | USB, Jack 3.5mm, Integrado | Comunicación en reuniones ágiles (Scrum), soporte y teleconferencia. |
| **Salida** | **Monitor (IPS / OLED / VA)** | Renderizado visual del entorno de trabajo, código, interfaces y salidas gráficas. | HDMI, DisplayPort, Thunderbolt / USB-C | Área de trabajo visual; monitores múltiples aumentan la productividad. |
| **Salida** | **Impresora / Plóter** | Transferencia de información digital a soporte físico mediante tinta/tóner. | USB, Wi-Fi, Ethernet | Generación de reportes físicos, planos de arquitectura o documentación legal. |
| **Salida** | **Altavoces / Auriculares** | Conversión de señales digitales a ondas acústicas para retroalimentación sonora. | Jack 3.5mm, USB, Bluetooth | Monitoreo auditivo en software multimedia y aislamiento acústico. |
| **Mixto (E/S)** | **Pantalla Táctil (Touchscreen)** | Entrada de eventos táctiles directos y salida visual simultánea. | I2C, SPI, USB + HDMI interno | Interacción natural en cajeros, kioscos, POS y aplicaciones móviles. |
| **Mixto (E/S)** | **Tarjeta de Red (NIC / Wi-Fi / Ethernet)** | Transmisión y recepción bidireccional de paquetes de datos a través del medio. | PCIe, USB, M.2 | Conectividad esencial para APIs, bases de datos y despliegues en red. |
| **Mixto (E/S)** | **Casco VR / AR (Realidad Virtual/Aumentada)** | Entrada de seguimiento posicional (6DOF) y salida inmersiva visual/audio. | USB-C, DisplayPort, Wi-Fi 6 | Desarrollo de simuladores inmersivos y software industrial avanzado. |

---

## 4. CUADRO COMPARATIVO 3: TECNOLOGÍAS DE ALMACENAMIENTO

| Tecnología de Almacenamiento | Mecanismo Físico / Lógico | Velocidad Lectura Típica | Velocidad Escritura Típica | Latencia | Resistencia Mecánica | Uso Óptimo Recomendado |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **HDD (Disco Duro Mecánico)** | Platos magnéticos giratorios con cabezal electromagnético. | 120 – 200 MB/s | 100 – 180 MB/s | Alta (~12 - 18 ms) | **Baja** (sensible a golpes y vibración). | Almacenamiento masivo pasivo, copias de seguridad (backups) y servidores de archivos (NAS). |
| **SSD SATA 2.5" / M.2 SATA** | Memoria flash NAND basada en interfaz SATA III (6 Gbps). | ~500 – 550 MB/s | ~450 – 520 MB/s | Baja (~0.1 ms) | **Muy Alta** (sin partes mecánicas móviles). | Actualización de equipos antiguos, almacenamiento secundario de alta velocidad. |
| **SSD M.2 NVMe (PCIe 3.0)** | Memoria NAND Flash bajo protocolo NVMe sobre bus PCIe 3.0 x4. | ~2.500 – 3.500 MB/s | ~2.000 – 3.000 MB/s | Muy Baja (~0.03 ms) | **Muy Alta** | Equipos de desarrollo estándar, arranque del sistema operativo y apps pesadas. |
| **SSD M.2 NVMe (PCIe 4.0)** | Protocolo NVMe sobre bus PCIe 4.0 x4 con mayor ancho de banda. | ~5.000 – 7.400 MB/s | ~4.500 – 6.800 MB/s | Ultra Baja (~0.02 ms) | **Muy Alta** | Compilación masiva de software, edición de video 4K/8K, bases de datos locales rápidas. |
| **SSD M.2 NVMe (PCIe 5.0)** | Protocolo NVMe sobre bus PCIe 5.0 x4 de última generación. | Hasta 14.000 MB/s | Hasta 12.000 MB/s | Extrema (~0.01 ms) | **Muy Alta** (requiere disipador térmico). | Servidores de alto rendimiento, estaciones de trabajo para IA y análisis de Big Data. |
| **Almacenamiento Cloud (AWS S3, Google Drive, Azure Blob)** | Servidores distribuidos con redundancia geográfica y acceso por API/HTTP. | Variable (limitada por ancho de banda de red) | Variable (limitada por ancho de banda de red) | Media (~20 - 80 ms por red) | **Máxima** (alta disponibilidad y tolerancia a fallos). | Persistencia compartida, respaldos off-site, activos estáticos de aplicaciones web. |

---

## 5. CUADRO COMPARATIVO 4: SISTEMAS OPERATIVOS

| Criterio de Comparación | Microsoft Windows (11 / Server) | GNU/Linux (Ubuntu, Debian, RedHat) | Apple macOS | Google Android |
| :--- | :--- | :--- | :--- | :--- |
| **Tipo de Kernel** | Híbrido (*NT Kernel*). | Monolítico modular (*Linux Kernel*). | Híbrido (*XNU / Darwin - BSD/Mach*). | Monolítico modificado (*Linux Kernel*). |
| **Tipo de Licencia** | Propietaria / Comercial. | Código Abierto (*GPL / Open Source*). | Propietaria (hardware Apple). | Código Abierto (*AOSP*) con capas propietarias. |
| **Consumo de Recursos** | Medio a Alto (requiere >= 8 GB RAM recomendado). | **Bajo a Muy Bajo** (altamente configurable y escalable). | Optimizado (alta eficiencia memoria unificada). | Bajo a Medio (gestión agresiva de memoria en segundo plano). |
| **Seguridad y Permisos** | Modelo ACL, Windows Defender, UAC. | **Muy Alto.** Modelo POSIX estricto, separación root/user, SELinux. | Alto. Entorno sandbox, SIP (*System Integrity Protection*), Gatekeeper. | Modelo Sandbox por aplicación, permisos granulares en tiempo de ejecución. |
| **Entorno de Uso Predominante** | Ofimática corporativa, gaming, entornos .NET y Active Directory. | **Servidores web, contenedores (Docker/K8s), pipelines CI/CD y backend.** | Desarrollo web, diseño UI/UX, desarrollo nativo iOS/macOS. | Dispositivos móviles, tabletas, Smart TVs y terminales embebidos. |

---

## 6. CUADRO COMPARATIVO 5: SERVICIOS Y MEDIOS DE CONECTIVIDAD A INTERNET

| Tecnología de Conexión | Medio de Transmisión | Velocidad Típica de Descarga / Subida | Latencia Promedio (Ping) | Estabilidad / Resiliencia | Escenario de Aplicación Recomendado |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Fibra Óptica (FTTH)** | Filamentos de vidrio / pulsos de luz. | 100 Mbps – 1.000+ Mbps (Simétrica) | **1 – 10 ms** (Ultra baja) | **Excelente.** Inmune a interferencias electromagnéticas. | Trabajo de desarrollo profesional, despliegue continuo, streaming y trabajo en nube. |
| **Cable Coaxial / HFC** | Cable de cobre coaxial apantallado. | 50 – 500 Mbps (Asimétrica: subida menor) | 15 – 35 ms | **Buena**, susceptible a saturación por concurrencia en nodo barrial. | Hogares y oficinas con consumo estándar de internet. |
| **Red Móvil 4G LTE** | Ondas de radiofrecuencia (Espectro móvil). | 10 – 50 Mbps | 35 – 70 ms | **Media**, afectada por obstáculos físicos y saturación de antenas. | Movilidad básica, conectividad de respaldo para smartphones. |
| **Red Móvil 5G** | Microondas milimétricas y bandas medias. | 100 – 1.000 Mbps | **5 – 15 ms** | **Alta**, con soporte masivo para dispositivos IoT simultáneos. | Dispositivos IoT avanzados, vehículos conectados, telemedicina y trabajo remoto de alta velocidad. |
| **Satelital LEO (Starlink)** | Microondas a constelación de satélites en órbita baja. | 50 – 220 Mbps | 25 – 50 ms | **Buena**, con sensibilidad a tormentas intensas o follaje denso. | Zonas rurales, campamentos, fincas y sitios sin cobertura terrestre. |
| **Wi-Fi 6 / 6E / 7 (LAN Inalámbrica)** | Frecuencias 2.4 GHz, 5 GHz y 6 GHz en red local. | 500 Mbps – 9.6+ Gbps (en LAN) | < 5 ms (hacia el router local) | **Muy Alta**, con protocolos OFDMA y MU-MIMO contra interferencias. | Conexión inalámbrica de estaciones de trabajo, portátiles y periféricos en la oficina/hogar. |

---

## 7. CONCLUSIONES
1. **Sinergia Hardware-Software:** El rendimiento global de un sistema depende del equilibrio entre las especificaciones físicas (CPU, RAM, bus PCIe) y la eficiencia del software y sistema operativo seleccionado.
2. **Evolución del Almacenamiento:** La transición de interfaces mecánicas SATA hacia protocolos NVMe sobre PCIe 4.0/5.0 ha eliminado el cuello de botella tradicional de I/O en la compilación y lectura de datos.
3. **Conectividad como Pilar del Desarrollo:** En el desarrollo de software actual orientado a microservicios y despliegue en la nube, una conexión simétrica de fibra óptica o 5G de baja latencia es indispensable para la integración continua (CI/CD) y la colaboración en equipo.

---
*Documento preparado conforme a los lineamientos de la Guía de Aprendizaje de la Competencia TIC - SENA ADSO Ficha 3413974.*

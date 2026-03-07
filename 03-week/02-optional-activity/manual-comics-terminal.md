# 🎨 Manual: Diseño de Cómics desde la Terminal

> Guía completa para crear cómics usando herramientas de línea de comandos

---

## Tabla de Contenidos

1. [Introducción](#introducción)
2. [Herramientas necesarias](#herramientas-necesarias)
3. [Estructura de un cómic](#estructura-de-un-cómic)
4. [Creación de viñetas con ASCII Art](#creación-de-viñetas-con-ascii-art)
5. [Generación de imágenes con ImageMagick](#generación-de-imágenes-con-imagemagick)
6. [Diálogos y bocadillos de texto](#diálogos-y-bocadillos-de-texto)
7. [Composición de páginas](#composición-de-páginas)
8. [Exportar a PDF](#exportar-a-pdf)
9. [Flujo de trabajo completo](#flujo-de-trabajo-completo)
10. [Recursos y referencias](#recursos-y-referencias)

---

## Introducción

Crear cómics desde la terminal puede sonar inusual, pero es una forma poderosa, reproducible y automatizable de producir historietas. Este manual cubre desde el arte ASCII hasta el procesamiento de imágenes con herramientas CLI profesionales.

### ¿Por qué desde la terminal?

- **Reproducibilidad**: todo el proceso queda en scripts
- **Automatización**: genera series de páginas con un solo comando
- **Control total**: sin GUIs que limiten tu flujo
- **Integración con Git**: versiona tu cómic como código

---

## Herramientas necesarias

### Instalación en sistemas basados en Debian/Ubuntu

```bash
# Herramientas esenciales
sudo apt update
sudo apt install -y \
  imagemagick \
  figlet \
  toilet \
  jp2a \
  ffmpeg \
  ghostscript \
  pandoc \
  python3-pip

# Herramientas Python
pip3 install Pillow rich click
```

### Instalación en macOS (Homebrew)

```bash
brew install imagemagick figlet toilet jp2a ffmpeg pandoc
pip3 install Pillow rich click
```

### Verificar instalaciones

```bash
convert --version       # ImageMagick
figlet --version        # FIGlet (texto ASCII)
toilet --version        # TOIlet (texto estilizado)
python3 -c "import PIL; print('Pillow OK')"
```

---

## Estructura de un cómic

Un cómic se organiza en la siguiente jerarquía de directorios:

```
mi_comic/
├── assets/
│   ├── personajes/
│   │   ├── heroe.png
│   │   └── villano.png
│   ├── fondos/
│   │   ├── ciudad.png
│   │   └── cueva.png
│   └── efectos/
│       ├── explosion.png
│       └── golpe.png
├── paginas/
│   ├── pagina_01/
│   │   ├── vineta_01.png
│   │   ├── vineta_02.png
│   │   └── vineta_03.png
│   └── pagina_02/
├── salida/
│   ├── pagina_01.png
│   └── comic_completo.pdf
└── scripts/
    ├── crear_vineta.sh
    └── componer_pagina.sh
```

### Crear la estructura automáticamente

```bash
#!/bin/bash
# setup_comic.sh
NOMBRE="$1"

mkdir -p "$NOMBRE"/{assets/{personajes,fondos,efectos},paginas,salida,scripts}
echo "✅ Estructura creada para: $NOMBRE"
```

```bash
bash setup_comic.sh mi_comic
```

---

## Creación de viñetas con ASCII Art

### Arte ASCII básico con figlet

```bash
# Texto grande estilo cómic
figlet -f banner "¡BOOM!"
figlet -f big "¡POW!"
figlet -f block "CRASH"

# Ver todos los estilos disponibles
figlet -l
```

**Ejemplo de salida:**
```
 ____   ___   ___  __  __ 
| __ ) / _ \ / _ \|  \/  |
|  _ \| | | | | | | |\/| |
| |_) | |_| | |_| | |  | |
|____/ \___/ \___/|_|  |_|
```

### Arte ASCII estilizado con toilet

```bash
# Efectos visuales
toilet -f mono12 -F gay "¡SUPER HÉROE!"
toilet -f future -F border "Capítulo 1"
toilet -f bigascii12 "KA-POW"

# Guardar en archivo
toilet -f mono12 "¡BOOM!" > efectos/boom.txt
```

### Convertir imágenes a ASCII

```bash
# Convertir PNG a ASCII art
jp2a --width=80 personaje.png

# Guardar la conversión
jp2a --width=60 --output=ascii_personaje.txt personaje.png

# Con colores (si el terminal lo soporta)
jp2a --width=80 --color personaje.png
```

### Crear una viñeta ASCII completa

```bash
cat << 'EOF'
┌─────────────────────────────────────┐
│                                     │
│    [PERSONAJE]    ( ¡Detente,  )    │
│      o/           ( villano!  )     │
│     /|            (___________) )   │
│     / \                             │
│                                     │
│  ~~~~~~ Ciudad nocturna ~~~~~~      │
└─────────────────────────────────────┘
EOF
```

---

## Generación de imágenes con ImageMagick

ImageMagick es la herramienta más poderosa para crear y manipular las viñetas como imágenes reales.

### Crear una viñeta en blanco

```bash
# Viñeta básica: 800x600 px, fondo blanco con borde negro
convert \
  -size 800x600 \
  xc:white \
  -border 5x5 \
  -bordercolor black \
  vineta_base.png
```

### Agregar texto de diálogo a una viñeta

```bash
# Añadir texto con estilo de cómic
convert vineta_base.png \
  -font "Comic-Sans-MS" \
  -pointsize 28 \
  -fill black \
  -annotate +50+80 "¡No te escaparás!" \
  vineta_con_texto.png
```

### Crear un bocadillo de texto (speech bubble)

```bash
# Bocadillo de diálogo
convert -size 300x120 xc:white \
  -fill white \
  -stroke black \
  -strokewidth 2 \
  -draw "roundrectangle 5,5 295,100 20,20" \
  -draw "polygon 100,100 130,100 115,120" \
  -font "DejaVu-Sans-Bold" \
  -pointsize 20 \
  -fill black \
  -annotate +20+40 "¡Imposible!" \
  bocadillo.png
```

### Superponer personaje y fondo

```bash
# Combinar fondo + personaje + bocadillo
convert fondo_ciudad.png \
  \( personaje_heroe.png -resize 200x300 \) \
  -geometry +50+250 -composite \
  \( bocadillo.png \) \
  -geometry +300+100 -composite \
  vineta_completa.png
```

### Agregar efectos de acción (onomatopeyas)

```bash
# Texto de golpe estilo cómic
convert vineta_completa.png \
  -font Impact \
  -pointsize 72 \
  -fill yellow \
  -stroke red \
  -strokewidth 3 \
  -annotate 0x0+200+200 "¡KA-POW!" \
  vineta_con_efecto.png
```

### Aplicar filtro estilo cómic (halftone)

```bash
# Efecto de puntos de trama (halftone)
convert imagen_original.png \
  -colorspace gray \
  -ordered-dither o8x8,4 \
  estilo_comic.png

# Aumentar contraste para look de cómic
convert imagen_original.png \
  -brightness-contrast 10x30 \
  -edge 1 \
  estilo_ink.png
```

---

## Diálogos y bocadillos de texto

### Script para crear bocadillos automáticamente

```bash
#!/bin/bash
# crear_bocadillo.sh
# Uso: bash crear_bocadillo.sh "Texto del diálogo" salida.png

TEXTO="$1"
SALIDA="$2"
ANCHO=320
ALTO=130

convert -size ${ANCHO}x${ALTO} xc:white \
  -fill white \
  -stroke black \
  -strokewidth 3 \
  -draw "roundrectangle 5,5 $((ANCHO-5)),$((ALTO-30)) 20,20" \
  -draw "polygon 60,$((ALTO-30)) 90,$((ALTO-30)) 75,$((ALTO))" \
  -font "DejaVu-Sans-Bold" \
  -pointsize 18 \
  -fill black \
  -size $((ANCHO-30))x$((ALTO-50)) \
  caption:"$TEXTO" \
  -geometry +15+15 \
  -composite \
  "$SALIDA"

echo "✅ Bocadillo creado: $SALIDA"
```

### Tipos de bocadillos

```bash
# Bocadillo de pensamiento (nubes)
convert -size 300x120 xc:white \
  -fill white -stroke black -strokewidth 2 \
  -draw "ellipse 150,50 140,45 0,360" \
  -draw "circle 60,105 60,115" \
  -draw "circle 80,112 80,120" \
  -draw "circle 100,116 100,124" \
  bocadillo_pensamiento.png

# Bocadillo de grito (puntiagudo)
convert -size 300x120 xc:white \
  -fill yellow -stroke red -strokewidth 3 \
  -draw "polygon 10,10 290,10 290,90 180,90 150,120 120,90 10,90" \
  bocadillo_grito.png
```

---

## Composición de páginas

### Diseño de página estándar (3 viñetas)

```bash
#!/bin/bash
# componer_pagina.sh
# Combina viñetas en un layout de página

V1="$1"
V2="$2"
V3="$3"
SALIDA="$4"

# Tamaño de página: A4 a 150 DPI = 1240x1754 px
PAGINA_W=1240
PAGINA_H=1754
MARGEN=20

# Redimensionar viñetas
convert "$V1" -resize 1200x550 v1_r.png
convert "$V2" -resize 590x580 v2_r.png
convert "$V3" -resize 590x580 v3_r.png

# Crear página base
convert -size ${PAGINA_W}x${PAGINA_H} xc:white pagina_base.png

# Componer
convert pagina_base.png \
  \( v1_r.png \) -geometry +${MARGEN}+${MARGEN} -composite \
  \( v2_r.png \) -geometry +${MARGEN}+590 -composite \
  \( v3_r.png \) -geometry +630+590 -composite \
  "$SALIDA"

# Limpiar temporales
rm v1_r.png v2_r.png v3_r.png
echo "✅ Página creada: $SALIDA"
```

### Layout en cuadrícula con Python

```python
#!/usr/bin/env python3
# componer_grid.py
# Uso: python3 componer_grid.py vineta1.png vineta2.png vineta3.png vineta4.png pagina.png

import sys
from PIL import Image

def componer_pagina(vinetas_paths, salida, cols=2, ancho=1240, alto=1754, margen=20):
    pagina = Image.new('RGB', (ancho, alto), 'white')
    
    filas = (len(vinetas_paths) + cols - 1) // cols
    v_w = (ancho - margen * (cols + 1)) // cols
    v_h = (alto - margen * (filas + 1)) // filas
    
    for i, path in enumerate(vinetas_paths):
        col = i % cols
        fila = i // cols
        
        vineta = Image.open(path).resize((v_w, v_h))
        x = margen + col * (v_w + margen)
        y = margen + fila * (v_h + margen)
        
        pagina.paste(vineta, (x, y))
    
    pagina.save(salida)
    print(f"✅ Página guardada: {salida}")

if __name__ == "__main__":
    paths = sys.argv[1:-1]
    salida = sys.argv[-1]
    componer_pagina(paths, salida)
```

```bash
python3 componer_grid.py v1.png v2.png v3.png v4.png pagina_01.png
```

---

## Exportar a PDF

### Combinar páginas en un PDF

```bash
# Unir todas las páginas en un PDF
convert \
  salida/pagina_01.png \
  salida/pagina_02.png \
  salida/pagina_03.png \
  -compress jpeg \
  -quality 90 \
  comic_completo.pdf

echo "✅ PDF generado: comic_completo.pdf"
```

### Exportar con alta resolución

```bash
# Para impresión (300 DPI)
convert \
  -density 300 \
  -compress jpeg \
  -quality 95 \
  salida/pagina_*.png \
  comic_impresion.pdf
```

### Optimizar PDF con ghostscript

```bash
# Reducir tamaño para web
gs \
  -sDEVICE=pdfwrite \
  -dCompatibilityLevel=1.4 \
  -dPDFSETTINGS=/ebook \
  -dNOPAUSE -dQUIET -dBATCH \
  -sOutputFile=comic_web.pdf \
  comic_completo.pdf

echo "✅ PDF optimizado para web: comic_web.pdf"
```

---

## Flujo de trabajo completo

### Script maestro: crear una página de cómic

```bash
#!/bin/bash
# crear_pagina_comic.sh
# Flujo completo de una página

set -e  # Salir si hay errores

PAGINA="$1"
mkdir -p "paginas/$PAGINA"

echo "🎨 Creando página: $PAGINA"

# 1. Crear fondos base
echo "  → Generando fondos..."
convert -size 1200x550 gradient:skyblue-white \
  -font Impact -pointsize 20 -fill "#888888" \
  -annotate +10+540 "© Mi Cómic 2024" \
  "paginas/$PAGINA/fondo_v1.png"

# 2. Crear viñeta 1 (escena de acción)
echo "  → Creando viñeta 1..."
convert "paginas/$PAGINA/fondo_v1.png" \
  -font Impact -pointsize 60 \
  -fill yellow -stroke red -strokewidth 2 \
  -annotate 15x15+400+300 "¡WHOOSH!" \
  "paginas/$PAGINA/vineta_01.png"

# 3. Crear viñeta 2 (diálogo)
echo "  → Creando viñeta 2..."
convert -size 590x580 xc:lightgray \
  -font "DejaVu-Sans" -pointsize 22 -fill black \
  -annotate +20+40 "¿Pensabas que\npodías escapar?" \
  "paginas/$PAGINA/vineta_02.png"

# 4. Crear viñeta 3 (reacción)
echo "  → Creando viñeta 3..."
convert -size 590x580 xc:white \
  -font Impact -pointsize 48 \
  -fill black \
  -annotate +50+290 "¡NUNCA!" \
  "paginas/$PAGINA/vineta_03.png"

# 5. Componer página
echo "  → Componiendo página..."
convert -size 1240x1754 xc:white \
  \( "paginas/$PAGINA/vineta_01.png" -resize 1200x550 \) \
    -geometry +20+20 -composite \
  \( "paginas/$PAGINA/vineta_02.png" \) \
    -geometry +20+590 -composite \
  \( "paginas/$PAGINA/vineta_03.png" \) \
    -geometry +630+590 -composite \
  "salida/pagina_${PAGINA}.png"

echo "✅ Página $PAGINA completada → salida/pagina_${PAGINA}.png"
```

```bash
# Ejecutar para crear páginas
bash crear_pagina_comic.sh 01
bash crear_pagina_comic.sh 02

# Exportar todo como PDF
convert salida/pagina_*.png comic_final.pdf
echo "📚 ¡Cómic exportado a comic_final.pdf!"
```

---

## Recursos y referencias

### Herramientas CLI mencionadas

| Herramienta | Uso | Documentación |
|-------------|-----|---------------|
| `ImageMagick` | Creación y edición de imágenes | `man convert` / `convert --help` |
| `figlet` | Arte ASCII de texto | `man figlet` |
| `toilet` | Texto ASCII estilizado | `toilet --help` |
| `jp2a` | Imágenes a ASCII | `jp2a --help` |
| `ghostscript` | Optimización de PDFs | `man gs` |
| `Pillow (Python)` | Composición programática | `pip show Pillow` |

### Atajos útiles de ImageMagick

```bash
# Ver información de una imagen
identify imagen.png

# Redimensionar manteniendo proporción
convert original.png -resize 800x800 resultado.png

# Convertir a escala de grises
convert color.png -colorspace Gray bw.png

# Rotar imagen
convert imagen.png -rotate 90 rotada.png

# Añadir borde
convert imagen.png -border 10x10 -bordercolor black con_borde.png
```

### Fuentes recomendadas para cómics

```bash
# Listar fuentes disponibles
convert -list font | grep -i comic

# Fuentes que funcionan bien
# - Impact (onomatopeyas y títulos)
# - Comic-Sans-MS (diálogos)
# - DejaVu-Sans-Bold (texto alternativo)
# - Bangers (si se instala desde Google Fonts)

# Instalar Bangers (fuente de cómic)
wget https://fonts.google.com/download?family=Bangers -O bangers.zip
```

---

*Manual creado para flujos de trabajo CLI — versión 1.0*

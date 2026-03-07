# 🎨 Diseño de Cómics desde la Terminal

> Guía rápida para crear historietas con herramientas CLI

---

## 1. Instalación

```bash
# Ubuntu/Debian
sudo apt install imagemagick figlet toilet jp2a ghostscript python3-pip
pip3 install Pillow

# macOS
brew install imagemagick figlet toilet jp2a
pip3 install Pillow
```

---

## 2. Estructura del proyecto

```
mi_comic/
├── assets/        # personajes, fondos, efectos
├── paginas/       # viñetas por página
├── salida/        # páginas compuestas y PDF final
└── scripts/       # automatización
```

```bash
mkdir -p mi_comic/{assets,paginas,salida,scripts}
```

---

## 3. Arte ASCII (texto y efectos)

```bash
# Onomatopeyas con figlet
figlet -f big "¡BOOM!"
figlet -f banner "POW"

# Texto estilizado con toilet
toilet -f future -F border "Capítulo 1"

# Convertir imagen a ASCII
jp2a --width=80 personaje.png
```

---

## 4. Crear viñetas con ImageMagick

```bash
# Viñeta en blanco con borde
convert -size 800x600 xc:white -border 5x5 -bordercolor black vineta.png

# Agregar texto de diálogo
convert vineta.png -font Impact -pointsize 28 -fill black \
  -annotate +50+80 "¡No te escaparás!" vineta_texto.png

# Onomatopeya estilo cómic
convert vineta.png -font Impact -pointsize 72 \
  -fill yellow -stroke red -strokewidth 3 \
  -annotate 0x0+200+200 "¡KA-POW!" vineta_efecto.png

# Superponer personaje sobre fondo
convert fondo.png \( personaje.png -resize 200x300 \) \
  -geometry +50+250 -composite vineta_final.png
```

### Bocadillo de diálogo

```bash
convert -size 300x120 xc:white \
  -fill white -stroke black -strokewidth 2 \
  -draw "roundrectangle 5,5 295,100 20,20" \
  -draw "polygon 100,100 130,100 115,120" \
  -font DejaVu-Sans-Bold -pointsize 20 -fill black \
  -annotate +20+40 "¡Imposible!" bocadillo.png
```

---

## 5. Componer una página

```bash
# Página A4 con 3 viñetas (1 arriba, 2 abajo)
convert -size 1240x1754 xc:white \
  \( vineta_01.png -resize 1200x550 \) -geometry +20+20   -composite \
  \( vineta_02.png -resize 590x580  \) -geometry +20+590  -composite \
  \( vineta_03.png -resize 590x580  \) -geometry +630+590 -composite \
  pagina_01.png
```

---

## 6. Exportar a PDF

```bash
# Unir páginas en un PDF
convert salida/pagina_*.png -compress jpeg -quality 90 comic_final.pdf

# Optimizar para web con ghostscript
gs -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook \
   -dNOPAUSE -dQUIET -dBATCH \
   -sOutputFile=comic_web.pdf comic_final.pdf
```

---

## Referencia rápida de herramientas

| Herramienta | Uso |
|-------------|-----|
| `ImageMagick` | Crear y editar imágenes |
| `figlet` | Texto ASCII grande |
| `toilet` | Texto ASCII estilizado |
| `jp2a` | Imagen → ASCII |
| `ghostscript` | Optimizar PDF |
| `Pillow` | Composición con Python |

---

*Manual CLI — v1.0*

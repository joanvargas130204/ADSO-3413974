-- CoffeeCol / Tantico Café · esquema coffeecol · G2-P2
-- Motor objetivo: MariaDB 10.4 / MySQL (XAMPP). Archivo generado desde schema.py; mismo modelo que esquema-sqlite.sql.
CREATE DATABASE IF NOT EXISTS coffeecol CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE coffeecol;

CREATE TABLE cliente (
  id_cliente INT NOT NULL AUTO_INCREMENT,
  uid_firebase VARCHAR(128) NOT NULL,
  nombre VARCHAR(100) NOT NULL,
  correo VARCHAR(120) NOT NULL,
  fecha_vinculacion DATE NOT NULL,
  fecha_cumpleanos DATE,
  puntos_acumulados INT NOT NULL DEFAULT 0,
  CONSTRAINT pk_cliente PRIMARY KEY (id_cliente),
  CONSTRAINT uq_cliente_uid UNIQUE (uid_firebase),
  CONSTRAINT uq_cliente_correo UNIQUE (correo),
  CONSTRAINT ck_cliente_puntos CHECK (puntos_acumulados >= 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE administrador (
  id_admin INT NOT NULL AUTO_INCREMENT,
  usuario VARCHAR(40) NOT NULL,
  nombre VARCHAR(100) NOT NULL,
  correo VARCHAR(120) NOT NULL,
  hash_contrasena VARCHAR(255) NOT NULL,
  CONSTRAINT pk_administrador PRIMARY KEY (id_admin),
  CONSTRAINT uq_admin_usuario UNIQUE (usuario),
  CONSTRAINT uq_admin_correo UNIQUE (correo)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE municipio (
  id_municipio INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(60) NOT NULL,
  altitud INT,
  notas_cata VARCHAR(200),
  CONSTRAINT pk_municipio PRIMARY KEY (id_municipio),
  CONSTRAINT uq_municipio_nombre UNIQUE (nombre),
  CONSTRAINT ck_municipio_altitud CHECK (altitud IS NULL OR altitud > 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE categoria (
  id_categoria INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  CONSTRAINT pk_categoria PRIMARY KEY (id_categoria),
  CONSTRAINT uq_categoria_nombre UNIQUE (nombre)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE producto (
  id_producto INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(100) NOT NULL,
  descripcion VARCHAR(500),
  notas_aromaticas VARCHAR(150),
  precio DECIMAL(10,2) NOT NULL,
  precio_anterior DECIMAL(10,2),
  stock INT NOT NULL DEFAULT 0,
  imagen VARCHAR(255),
  valoracion DECIMAL(2,1),
  estado VARCHAR(10) NOT NULL DEFAULT 'activo',
  id_categoria INT NOT NULL,
  CONSTRAINT pk_producto PRIMARY KEY (id_producto),
  CONSTRAINT fk_producto_categoria FOREIGN KEY (id_categoria) REFERENCES categoria (id_categoria) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT ck_producto_precio CHECK (precio > 0),
  CONSTRAINT ck_producto_precio_ant CHECK (precio_anterior IS NULL OR precio_anterior > 0),
  CONSTRAINT ck_producto_stock CHECK (stock >= 0),
  CONSTRAINT ck_producto_valoracion CHECK (valoracion IS NULL OR (valoracion >= 0 AND valoracion <= 5)),
  CONSTRAINT ck_producto_estado CHECK (estado IN ('activo','retirado'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE direccion_entrega (
  id_cliente INT NOT NULL,
  consecutivo INT NOT NULL,
  id_municipio INT NOT NULL,
  destinatario VARCHAR(100) NOT NULL,
  direccion VARCHAR(150) NOT NULL,
  telefono CHAR(10) NOT NULL,
  CONSTRAINT pk_direccion_entrega PRIMARY KEY (id_cliente, consecutivo),
  CONSTRAINT fk_dir_cliente FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_dir_municipio FOREIGN KEY (id_municipio) REFERENCES municipio (id_municipio) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT ck_dir_consecutivo CHECK (consecutivo >= 1),
  CONSTRAINT ck_dir_telefono CHECK (length(telefono) = 10)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE pedido (
  id_pedido INT NOT NULL AUTO_INCREMENT,
  codigo VARCHAR(20) NOT NULL,
  fecha DATETIME NOT NULL,
  estado VARCHAR(12) NOT NULL DEFAULT 'pendiente',
  subtotal DECIMAL(12,2) NOT NULL,
  valor_despacho DECIMAL(10,2) NOT NULL,
  total DECIMAL(12,2) NOT NULL,
  id_cliente INT NOT NULL,
  consecutivo_direccion INT NOT NULL,
  CONSTRAINT pk_pedido PRIMARY KEY (id_pedido),
  CONSTRAINT uq_pedido_codigo UNIQUE (codigo),
  CONSTRAINT fk_pedido_cliente FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT fk_pedido_direccion FOREIGN KEY (id_cliente, consecutivo_direccion) REFERENCES direccion_entrega (id_cliente, consecutivo) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT ck_pedido_estado CHECK (estado IN ('pendiente','procesando','enviado','entregado','cancelado')),
  CONSTRAINT ck_pedido_valores CHECK (subtotal >= 0 AND valor_despacho >= 0),
  CONSTRAINT ck_pedido_total CHECK (total = subtotal + valor_despacho)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE detalle_pedido (
  id_pedido INT NOT NULL,
  id_producto INT NOT NULL,
  cantidad INT NOT NULL,
  precio_unitario DECIMAL(10,2) NOT NULL,
  CONSTRAINT pk_detalle_pedido PRIMARY KEY (id_pedido, id_producto),
  CONSTRAINT fk_det_pedido FOREIGN KEY (id_pedido) REFERENCES pedido (id_pedido) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_det_producto FOREIGN KEY (id_producto) REFERENCES producto (id_producto) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT ck_det_cantidad CHECK (cantidad > 0),
  CONSTRAINT ck_det_precio CHECK (precio_unitario > 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE favorito (
  id_cliente INT NOT NULL,
  id_producto INT NOT NULL,
  fecha_agregado DATE NOT NULL,
  CONSTRAINT pk_favorito PRIMARY KEY (id_cliente, id_producto),
  CONSTRAINT fk_fav_cliente FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_fav_producto FOREIGN KEY (id_producto) REFERENCES producto (id_producto) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE recompensa (
  id_recompensa INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(80) NOT NULL,
  puntos_requeridos INT NOT NULL,
  CONSTRAINT pk_recompensa PRIMARY KEY (id_recompensa),
  CONSTRAINT ck_recompensa_puntos CHECK (puntos_requeridos > 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE nivel_fidelizacion (
  id_nivel INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(30) NOT NULL,
  puntos_minimos INT NOT NULL,
  CONSTRAINT pk_nivel_fidelizacion PRIMARY KEY (id_nivel),
  CONSTRAINT uq_nivel_nombre UNIQUE (nombre),
  CONSTRAINT uq_nivel_puntos UNIQUE (puntos_minimos),
  CONSTRAINT ck_nivel_puntos CHECK (puntos_minimos >= 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE transaccion_puntos (
  id_transaccion INT NOT NULL AUTO_INCREMENT,
  id_cliente INT NOT NULL,
  id_pedido INT,
  id_recompensa INT,
  fecha DATETIME NOT NULL,
  tipo VARCHAR(10) NOT NULL,
  puntos INT NOT NULL,
  motivo VARCHAR(100),
  CONSTRAINT pk_transaccion_puntos PRIMARY KEY (id_transaccion),
  CONSTRAINT fk_tp_cliente FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT fk_tp_pedido FOREIGN KEY (id_pedido) REFERENCES pedido (id_pedido) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT fk_tp_recompensa FOREIGN KEY (id_recompensa) REFERENCES recompensa (id_recompensa) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT ck_tp_tipo CHECK (tipo IN ('abono','canje','bono')),
  CONSTRAINT ck_tp_puntos CHECK (puntos <> 0),
  CONSTRAINT ck_tp_abono_pedido CHECK (tipo <> 'abono' OR id_pedido IS NOT NULL)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE contacto (
  id_contacto INT NOT NULL AUTO_INCREMENT,
  id_municipio INT,
  nombre VARCHAR(100) NOT NULL,
  empresa_finca VARCHAR(100),
  telefono VARCHAR(15),
  correo VARCHAR(120) NOT NULL,
  mensaje VARCHAR(1000) NOT NULL,
  fecha_envio DATETIME NOT NULL,
  CONSTRAINT pk_contacto PRIMARY KEY (id_contacto),
  CONSTRAINT fk_contacto_municipio FOREIGN KEY (id_municipio) REFERENCES municipio (id_municipio) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE intento_login_admin (
  id_intento INT NOT NULL AUTO_INCREMENT,
  id_admin INT NOT NULL,
  direccion_ip VARCHAR(45) NOT NULL,
  fecha_hora DATETIME NOT NULL,
  exitoso TINYINT NOT NULL,
  CONSTRAINT pk_intento_login_admin PRIMARY KEY (id_intento),
  CONSTRAINT fk_intento_admin FOREIGN KEY (id_admin) REFERENCES administrador (id_admin) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT ck_intento_exitoso CHECK (exitoso IN (0,1))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE aliado (
  id_aliado INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(100) NOT NULL,
  descripcion VARCHAR(300),
  logo VARCHAR(255),
  CONSTRAINT pk_aliado PRIMARY KEY (id_aliado)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

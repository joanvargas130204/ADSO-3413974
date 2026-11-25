-- Cuentas de base de datos con mínimo privilegio (MariaDB 10.4). No ejecutado en esta evidencia: se aplica en el servidor de datos.
-- Las contraseñas reales NO se escriben aquí: se generan y se guardan en el archivo .env fuera de la carpeta pública.
CREATE USER 'coffeecol_app'@'localhost' IDENTIFIED BY '<definir-en-servidor>';
GRANT SELECT, INSERT, UPDATE, DELETE ON coffeecol.* TO 'coffeecol_app'@'localhost';
-- (sin CREATE, DROP, ALTER ni GRANT)

CREATE USER 'coffeecol_respaldo'@'localhost' IDENTIFIED BY '<definir-en-servidor>';
GRANT SELECT, LOCK TABLES, SHOW VIEW ON coffeecol.* TO 'coffeecol_respaldo'@'localhost';

-- Respaldo diario (tarea programada 2:00 a. m.):
--   mysqldump --single-transaction -u coffeecol_respaldo coffeecol > respaldo_AAAAMMDD.sql
FLUSH PRIVILEGES;

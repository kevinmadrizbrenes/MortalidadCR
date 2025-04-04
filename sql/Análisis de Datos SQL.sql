-- Contar el total de registros
SELECT COUNT(*) AS total_registros FROM "MortalidadCR";

-- Ver las primeras 10 filas
SELECT * FROM "MortalidadCR" LIMIT 10;

-- Ver las columnas y sus tipos de datos
SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'MortalidadCR';

-- Contar los valores nulos en cada columna
SELECT column_name, COUNT(*) - COUNT(column_name) AS valores_nulos
FROM information_schema.columns 
LEFT JOIN "MortalidadCR" ON true
GROUP BY column_name;

-- Número de accidentes por tipo de accidente
SELECT "tipo de accidente", COUNT(*) AS total_accidentes FROM "MortalidadCR"
GROUP BY "tipo de accidente" 
ORDER BY "tipo de accidente" DESC;

-- Número de accidentes por provincia
SELECT "provincia", COUNT(*) AS total_accidentes 
FROM "MortalidadCR"
GROUP BY "provincia"
ORDER BY total_accidentes DESC

-- Edad promedio al fallecer
SELECT ROUND(AVG(CAST("edad" AS INTEGER)), 2) AS edad_promedio
FROM "MortalidadCR"
WHERE "edad" ~ '^[0-9]+$';  -- Filtra solo números válidos








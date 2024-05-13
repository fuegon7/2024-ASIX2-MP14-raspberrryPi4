#!/bin/bash

while true; do
    sudo mysql -u root -proot -vv <<EOF || { echo ""; exit 1; }

    USE pyproject;

    DROP PROCEDURE IF EXISTS generar_inserts_temperature;

    DELIMITER //
    CREATE PROCEDURE generar_inserts_temperature()
    BEGIN
        DECLARE temperatura INT;
        DECLARE humedad INT;
        DECLARE fecha_inicio TIMESTAMP;

        SET fecha_inicio = NOW();

        SET temperatura = FLOOR(RAND() * (40 - 20 + 1)) + 20;
        SET humedad = FLOOR(RAND() * (80 - 40 + 1)) + 40;

        INSERT INTO temperature (temperature, humidity, date) VALUES (temperatura, humedad, fecha_inicio);
    END //
    DELIMITER ;

    CALL generar_inserts_temperature;

EOF

    sleep 5
done


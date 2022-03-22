PROPERTIES = """
    SELECT 
        p.id, 
        p.address,
        p.city, 
        s.name AS status, 
        p.price,
        p.description
    FROM property p
    INNER JOIN (
        SELECT sh.property_id, sh.status_id, sh.update_date
        FROM status_history sh
        INNER JOIN (
            SELECT property_id, MAX(update_date) AS max_date 
            FROM status_history
            GROUP BY property_id
        ) AS ph
        ON sh.property_id = ph.property_id AND sh.update_date = ph.max_date
    ) sh
    ON sh.property_id = p.id
    INNER JOIN status s ON s.id = sh.status_id
    WHERE p.city IS NOT NULL AND p.address IS NOT NULL AND p.price <> 0
    AND s.name IN ("pre_venta", "en_venta", "vendido")
"""

FILTERED_PROPERTIES = """
    AND (s.name = %s OR p.year = %s OR p.city LIKE %s)
"""

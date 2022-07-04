-- SELECT ac.name as categoryName, COUNT(a.title) as totalProduct, AVG(g.price) as avgPrice FROM ads a
SELECT ac.name as categoryName, a.title as totalProduct, g.price as avgPrice FROM ads a 
JOIN ad_categories ac ON a.ad_category = ac.id 
JOIN goods g ON a.id = g.ad
WHERE  g.price < 50000
AND a.is_banned != 1 
AND ac.name = "Woman Fashion" 
-- GROUP BY ac.name
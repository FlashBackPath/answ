SELECT adverts.category_name from adverts, costs
where costs.advert_id == adverts.advert_id and cost > 500;
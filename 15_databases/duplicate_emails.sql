select p.email from person p
group by p.email
having count(*) > 1
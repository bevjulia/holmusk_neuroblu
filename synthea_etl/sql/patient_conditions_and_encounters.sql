-- explain analyse
select distinct * 
from synthea_native.patients p
inner join synthea_native.conditions c
on c.patient = p.id
inner join synthea_native.encounters e
on e.id = c.encounter
and e.patient = c.patient
where 1=1
and c.start >= '1975-01-01'
and e.encounterclass = 'ambulatory'
select e.nome, c.nome
from empresas as e, empresas_unidades as eu, cidadeS as c
where e.id = eu.empresa_id
and c.id = eu.cidade_id
def generate_prompt(segmentos:list,articulos:list):
    segmentos_txt = "\n".join(
        f"{i}: {nombre}"
        for i, nombre in enumerate(segmentos)
    )

    articulos_txt = "\n".join(
        f"id_articulo: {i}, nombre:{nombre}"
        for i, nombre in enumerate(articulos)
    )

    return f"""
Eres un clasificador del catálogo SUNAT.

Debes clasificar cada artículo en UNO de los segmentos. los articulos pertencen a una empresa la cual es un restaurante

Segmentos:

{segmentos_txt}

Artículos:

{articulos_txt}

Responde únicamente JSON.

Formato:

[
    {{
        "id_articulo": 1,
        "id_grupo": 14,
        "confianza": 0.98
    }}
]
    """    
    
def generar_familias_prompt(familias:list,articulos:list):
    familias_txt = "\n".join(
        f"{i}: {nombre}"
        for i, nombre in enumerate(familias)
    )

    articulos_txt = "\n".join(
        f"id_articulo: {i}, nombre:{nombre}"
        for i, nombre in enumerate(articulos)
    )

    return f"""
Eres un clasificador del catálogo SUNAT.

Debes clasificar cada artículo en UNA de las familias. los articulos pertencen a una empresa la cual es un restaurante

familias:

{familias_txt}

Artículos:

{articulos_txt}

Responde únicamente JSON.

Formato:

[
    {{
        "id_articulo": 1,
        "id_grupo": 14,
        "confianza": 0.98
    }}
]
    """
    
    
def generar_clases_prompt(clases:list,articulos:list):
    clases_txt = "\n".join(
        f"{i}: {nombre}"
        for i, nombre in enumerate(clases)
    )

    articulos_txt = "\n".join(
        f"id_articulo: {i}, nombre:{nombre}"
        for i, nombre in enumerate(articulos)
    )

    return f"""
Eres un clasificador del catálogo SUNAT.

Debes clasificar cada artículo en UNA de las clases. los articulos pertencen a una empresa la cual es un restaurante

clases:

{clases_txt}

Artículos:

{articulos_txt}

Responde únicamente JSON.

Formato:

[
    {{
        "id_articulo": 1,
        "id_grupo": 14,
        "confianza": 0.98
    }}
]
    """
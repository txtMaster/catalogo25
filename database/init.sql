/*
CREATE TABLE catalogo25 (
    id INT AUTO_INCREMENT PRIMARY KEY,

    id_segmento VARCHAR(20),
    segmento VARCHAR(255),

    id_familia VARCHAR(20),
    familia VARCHAR(255),

    id_clase VARCHAR(20),
    clase VARCHAR(255),

    id_producto VARCHAR(20),
    producto VARCHAR(255),

    descripcion_busqueda TEXT,
    keywords TEXT,

    FULLTEXT KEY ft_keywords(keywords),
    FULLTEXT KEY ft_descripcion(descripcion_busqueda)
);
*/

CREATE table segmento(
    id VARCHAR(20) PRIMARY KEY,
    descripcion VARCHAR(500) NOT NULL
);
CREATE table familia(
    id VARCHAR(20) PRIMARY KEY,
    segmento_id VARCHAR(20) NOT NULL,
    descripcion VARCHAR(500) NOT null,
    constraint fk_familia_segmento foreign key (segmento_id)
    	references segmento(id)
    	on delete cascade
);
CREATE table clase(
    id VARCHAR(20) PRIMARY KEY,
    familia_id VARCHAR(20), NOT NULL,
    descripcion VARCHAR(500) NOT null,
    constraint fk_clase_familia foreign key (familia_id)
    	references familia(id)
    	on delete cascade
);

CREATE table producto(
    id VARCHAR(20) PRIMARY KEY,
    clase_id VARCHAR(20) NOT NULL,
    descripcion VARCHAR(500) NOT NULL,
    constraint fk_producto_clase foreign key (clase_id)
        references clase(id)
        on delete cascade
);
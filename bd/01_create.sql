-- Enable use of foregin keys.
PRAGMA foreign_keys = ON;

-- Boja

CREATE TABLE boja (
id INTEGER PRIMARY KEY,
numero INTEGER,
fecha text
);

CREATE UNIQUE INDEX idx_id_boja ON boja(id);

-- Sections.

CREATE TABLE tipo_seccion (
id INTEGER PRIMARY KEY,
nombre TEXT
);

CREATE UNIQUE INDEX idx_id_tipo_seccion ON tipo_seccion(id);

CREATE TABLE seccion (
id INTEGER PRIMARY KEY,
id_tipo_seccion INTEGER REFERENCES tipo_seccion(id)
);

CREATE UNIQUE INDEX idx_id_seccion ON seccion(id);

-- Organism.

CREATE TABLE tipo_organismo (
id INTEGER PRIMARY KEY,
nombre TEXT
);

CREATE UNIQUE INDEX idx_id_tipo_organismo ON tipo_organismo(id);

CREATE TABLE organismo (
id INTEGER PRIMARY KEY,
nombre TEXT,
id_tipo_organismo INTEGER REFERENCES tipo_organismo(id)
);

CREATE UNIQUE INDEX idx_id_organismo ON organismo(id);

-- Content.

CREATE TABLE tipo_contenido (
id INTEGER PRIMARY KEY,
nombre TEXT
);

CREATE UNIQUE INDEX idx_id_tipo_contenido ON tipo_contenido(id);

CREATE TABLE contenido (
id INTEGER PRIMARY KEY,
descripcion TEXT,
fecha text,
url TEXT,
id_tipo_contenido INTEGER REFERENCES tipo_contenido(id),
id_organismo INTEGER REFERENCES organismo(id)
);

CREATE UNIQUE INDEX idx_id_contenido ON contenido(id);

-- Terms.

CREATE TABLE termino (
id INTEGER PRIMARY KEY,
nombre TEXT
);

CREATE UNIQUE INDEX idx_id_termino ON termino(id);

CREATE TABLE tipo_contenido_termino (
id_tipo_contenido INTEGER REFERENCES tipo_contenido(id),
id_termino INTEGER REFERENCES termino(id)
);

CREATE UNIQUE INDEX idx_tipo_contenido_termino ON tipo_contenido_termino(id_tipo_contenido, id_termino);
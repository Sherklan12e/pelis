# Movies web 


# DER

```mermaid

erDiagram
    User {
        INT idusuario PK
        VARCHAR username
        VARCHAR email
        VARCHAR password
    }
    Admin {
        INT idadmin PK
        VARCHAR username
        VARCHAR email
        VARCHAR password
    }
    Peliculas {
        INT id_pelicula PK
        VARCHAR titulo
        VARCHAR subtitulo
        TEXT descripcion
        DATE fecha_estreno
        INT duracion_minutos
        VARCHAR director
        VARCHAR reparto
        VARCHAR trailer_url
        INT id_genero FK
    }
    Muchosgeneros{
        INT id_genero PK
        INT id_peliculas FK
        INT id_genero FK
    }
    Genero {
        INT id_genero PK
        VARCHAR nombre
        VARCHAR descripcion
    }
    Comentarios {
        INT idcomentario PK
        INT id_pelicula FK
        INT id_usuario FK
        TEXT comentario
        DATETIME fecha_comentario
    }

    User ||--o{ Comentarios: "Usuario deja comentario"
    Admin ||--o{ Peliculas: "Admin puede agregar/modificar películas"
    Peliculas ||--o{ Muchosgeneros: "Pertenece a muchos generos"
    Genero ||--o{ Muchosgeneros: "Pertenece a un muchas peliculas"
    User ||--o{ Peliculas: "Usuario marca como vista/favorita"

```


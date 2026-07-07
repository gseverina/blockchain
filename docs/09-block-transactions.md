# Clase 9 — Bloques con Transacciones

## Objetivos

Al finalizar esta clase deberías ser capaz de:

- Comprender que un bloque contiene transacciones y no datos arbitrarios.
- Modelar la relación entre `Block` y `Transaction`.
- Entender por qué un bloque agrupa múltiples transacciones.
- Evolucionar el modelo sin alterar las responsabilidades existentes.

---

# ¿Qué almacena un bloque?

Hasta ahora nuestra clase `Block` almacena un atributo llamado `data`.

Ese atributo fue útil para construir la infraestructura de la blockchain.

Sin embargo, una blockchain existe para registrar transacciones.

Por lo tanto, un bloque debería contener una colección de transacciones.

---

# ¿Por qué varias transacciones?

En una blockchain real, cada bloque agrupa múltiples transacciones.

Esto permite:

- Reducir el costo de incorporar información a la cadena.
- Compartir el proceso de validación entre muchas transacciones.
- Mejorar la eficiencia del sistema.

Nuestro proyecto seguirá esa misma idea.

---

# Evolución del modelo

Conceptualmente, pasaremos de:

```text
Block
├── data
├── index
└── previous_hash
```

a:

```text
Block
├── transactions
├── index
└── previous_hash
```

donde `transactions` será una colección de objetos `Transaction`.

---

# Inmutabilidad

El bloque continúa siendo inmutable.

Esto implica que la colección de transacciones tampoco deberá modificarse una vez creado el bloque.

La inmutabilidad sigue siendo una propiedad fundamental del modelo.

---

# Qué todavía NO estudiaremos

En esta clase no implementaremos:

- Tamaño máximo del bloque.
- Validación de transacciones.
- Merkle Trees.
- Block Header.
- Minería.

El objetivo es únicamente modificar el modelo para que un bloque represente correctamente su contenido.

---

# Trabajo práctico

Modificar la clase `Block` para reemplazar el atributo `data` por una colección de `Transaction`.

Actualizar las validaciones y los tests necesarios para reflejar el nuevo modelo.

---

# Lo que aprenderemos en la próxima clase

Ahora que un bloque puede contener transacciones, necesitaremos definir qué significa agregar una transacción a la blockchain y cómo construir nuevos bloques a partir de ellas.


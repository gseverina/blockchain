# Clase 5 — Validación de la Blockchain

## Objetivos

Al finalizar esta clase deberías ser capaz de:

- Comprender qué significa que una blockchain sea válida.
- Entender cómo verificar la integridad de una cadena de bloques.
- Recorrer una blockchain para comprobar la relación entre sus bloques.
- Implementar un mecanismo básico de validación.

---

# ¿Qué significa validar una blockchain?

Hasta este momento nuestra blockchain puede almacenar bloques, pero nunca verifica si esos bloques forman una cadena consistente.

Validar una blockchain consiste en comprobar que cada bloque mantiene correctamente la relación con el bloque que lo precede.

En otras palabras, queremos responder una única pregunta:

> **¿Los bloques almacenados forman realmente una cadena válida?**

---

# ¿Qué debemos verificar?

Para una blockchain como la que hemos construido hasta ahora, la validación consiste en recorrer la cadena y comprobar que, para cada bloque (excepto el génesis), el valor de `previous_hash` coincida exactamente con el hash del bloque anterior.

Conceptualmente:

```text
Block 0
hash = A

↓

Block 1
previous_hash = A
hash = B

↓

Block 2
previous_hash = B
hash = C
```

Mientras esta condición se mantenga para todos los bloques, la cadena será considerada válida.

---

# ¿Qué ocurre si un bloque cambia?

Supongamos la siguiente cadena:

```text
Block 0 ----> Block 1 ----> Block 2
```

Si alguien modifica el contenido de `Block 1`, su hash cambiará inmediatamente.

Sin embargo, `Block 2` continuará almacenando el hash anterior.

Como consecuencia:

```text
Block 1.hash() != Block 2.previous_hash
```

La blockchain dejará de ser válida.

---

# Responsabilidad de la validación

La validación corresponde a la clase `Blockchain`.

Los bloques conocen únicamente su propio contenido.

Es la blockchain quien conoce el orden de los bloques y, por lo tanto, es la única que puede recorrer la cadena completa para verificar su consistencia.

---

# Qué todavía NO estudiaremos

En esta clase no verificaremos:

- Índices consecutivos.
- Proof of Work.
- Dificultad.
- Nonce.
- Firmas digitales.
- Transacciones.

Nuestro objetivo es únicamente comprobar la consistencia del encadenamiento mediante hashes.

---

# Trabajo práctico

Agregar a la clase `Blockchain` un mecanismo que permita determinar si la cadena almacenada es válida.

La validación deberá recorrer todos los bloques y comprobar la consistencia de los hashes.

---

# Lo que aprenderemos en la próxima clase

Hasta ahora nuestros bloques almacenan datos arbitrarios.

En la próxima clase comenzaremos a estudiar qué tipo de información tiene sentido almacenar dentro de un bloque y construiremos nuestra primera representación de una transacción.


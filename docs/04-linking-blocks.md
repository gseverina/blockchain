# Clase 4 — Encadenando Bloques

## Objetivos

Al finalizar esta clase deberías ser capaz de:

- Comprender por qué una blockchain no almacena referencias directas entre bloques.
- Entender cómo el hash permite vincular bloques de forma segura.
- Comprender cómo una modificación en un bloque afecta a toda la cadena.
- Incorporar el concepto de `previous_hash` a nuestra implementación.

---

# El problema de las referencias directas

En las clases anteriores, cada bloque mantenía una referencia al bloque anterior mediante el atributo `previous_block`.

Conceptualmente esto nos permitió construir una cadena de bloques, pero presenta una limitación importante.

Una referencia en memoria solo tiene sentido mientras el programa está ejecutándose. Si almacenamos la blockchain en un archivo o la transmitimos por una red, esas referencias dejan de ser válidas.

Necesitamos una forma de identificar un bloque que sea independiente de la memoria donde fue creado.

---

# El hash como identidad

En la clase anterior aprendimos que un hash es una representación única del contenido de un bloque.

Eso nos permite utilizar el hash como una forma de identificar un bloque.

En lugar de guardar una referencia al bloque anterior, podemos guardar el hash del bloque anterior.

Conceptualmente:

```text
Antes

Block
 ├── data
 ├── index
 └── previous_block

Después

Block
 ├── data
 ├── index
 └── previous_hash
```

Ahora los bloques ya no dependen de objetos en memoria.

Dependen únicamente de la información que representa al bloque anterior.

---

# ¿Qué ocurre si alguien modifica un bloque?

Supongamos la siguiente cadena.

```text
Block 0 -----> Block 1 -----> Block 2
```

Cada bloque almacena el hash del bloque anterior.

Si alguien modifica el contenido de `Block 1`, su hash cambia inmediatamente.

Sin embargo, `Block 2` continúa almacenando el hash anterior.

Como consecuencia, la cadena deja de ser consistente.

Esta es una de las ideas fundamentales de una blockchain: una modificación en un bloque rompe el encadenamiento de todos los bloques posteriores.

---

# Qué todavía NO estudiaremos

En esta clase todavía no verificaremos automáticamente que la cadena sea válida.

Tampoco implementaremos:

- Validación de la blockchain.
- Proof of Work.
- Minería.
- Dificultad.
- Block Header.

Nuestro objetivo es únicamente modificar el modelo de datos para representar correctamente el encadenamiento mediante hashes.

---

# Trabajo práctico

Modificar la clase `Block` para reemplazar la referencia `previous_block` por el atributo `previous_hash`.

Actualizar las validaciones necesarias para mantener la consistencia entre el bloque génesis y el resto de la cadena.

No será necesario modificar la clase `Blockchain` en esta etapa.

---

# Lo que aprenderemos en la próxima clase

Ahora que cada bloque almacena el hash del bloque anterior, veremos cómo recorrer la cadena para comprobar que ningún bloque haya sido modificado.


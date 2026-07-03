# Clase 3 — Funciones Hash

## Objetivos

Al finalizar esta clase deberías ser capaz de:

- Comprender qué es una función hash.
- Entender por qué las funciones hash son fundamentales en una blockchain.
- Conocer las propiedades que debe cumplir una buena función hash.
- Comprender qué es SHA-256 y por qué Bitcoin la utiliza.
- Implementar el cálculo del hash de un bloque.

---

# ¿Qué es una función hash?

Una función hash es un algoritmo que transforma una entrada de tamaño arbitrario en una salida de tamaño fijo.

Por ejemplo:

```text
"Hola"

↓

185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
```

No importa si la entrada tiene 5 bytes o 5 GB. La salida siempre tendrá el mismo tamaño.

En una blockchain, el hash funciona como una **huella digital** de la información.

---

# Propiedades de una buena función hash

Para que una función hash pueda utilizarse en una blockchain debe cumplir, entre otras, las siguientes propiedades.

## Determinismo

La misma entrada siempre produce exactamente el mismo hash.

```text
hash("Hola") == hash("Hola")
```

---

## Sensibilidad a los cambios

Una modificación mínima en la entrada produce un hash completamente diferente.

Por ejemplo:

```text
"Hola"

↓

185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
```

```text
"hola"

↓

b221d9dbb083a7f3c4a9c65e0f9f3dc4d2f52c6ec7290f1b5e1d3e7f8c1b8d9a
```

Obsérvese que cambiar una única letra modifica completamente el resultado.

Este comportamiento se conoce como **efecto avalancha** (*avalanche effect*).

---

## Longitud fija

La longitud del hash no depende del tamaño de la entrada.

Esto facilita comparar hashes y almacenarlos.

---

## Unidireccionalidad

A partir del hash no debe ser posible reconstruir el dato original.

La función hash no es un algoritmo de cifrado.

---

# SHA-256

Bitcoin utiliza la función hash SHA-256.

SHA significa **Secure Hash Algorithm** y el número 256 indica que el resultado tiene una longitud de 256 bits.

Python incluye una implementación de SHA-256 dentro de la biblioteca estándar, por lo que no será necesario instalar dependencias externas.

---

# ¿Qué información debemos hashear?

Nuestro objetivo no es calcular el hash de un archivo ni de un texto cualquiera.

Queremos calcular el hash de un objeto `Block`.

Por lo tanto, antes de aplicar SHA-256 debemos obtener una representación estable del contenido del bloque.

Es importante comprender que el hash debe depender únicamente de la información contenida en el bloque.

Dos bloques con exactamente el mismo contenido deberán producir el mismo hash.

Si cualquiera de sus datos cambia, el hash también deberá cambiar.

---

# Qué todavía NO estudiaremos

En esta clase todavía no utilizaremos el hash para enlazar bloques.

Tampoco estudiaremos:

- Proof of Work.
- Nonce.
- Dificultad.
- Minería.
- Validación de la blockchain.

El objetivo es únicamente aprender a calcular el hash de un bloque.

---

# Trabajo práctico

Modificar la implementación de `Block` para que pueda calcular su propio hash.

La implementación deberá utilizar SHA-256 y depender exclusivamente del contenido del bloque.

---

# Lo que aprenderemos en la próxima clase

Ahora que cada bloque puede obtener una huella digital única, veremos cómo utilizar esa información para enlazar los bloques y detectar cualquier modificación realizada sobre la cadena.
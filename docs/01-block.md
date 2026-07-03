# Clase 1 — El Bloque

## Objetivos

Al finalizar esta clase deberías ser capaz de:

- Comprender qué es un bloque dentro de una blockchain.
- Entender cuál es la responsabilidad de un bloque.
- Identificar la información mínima que un bloque debe contener.
- Diseñar e implementar una primera versión de la clase `Block` en Python.

---

# ¿Qué es un bloque?

Un bloque es la unidad fundamental de una blockchain.

Puede pensarse como un contenedor que almacena información y que forma parte de una secuencia ordenada de bloques.

Cada bloque conoce cuál fue el bloque que lo precede, formando así una cadena donde cada elemento mantiene una relación con el anterior.

Es importante entender que un bloque **no representa una transacción**, una criptomoneda ni una wallet. Es simplemente un contenedor de datos.

Dependiendo de la aplicación, esos datos pueden ser transacciones financieras, documentos, certificados académicos, registros médicos o cualquier otro tipo de información.

---

# Responsabilidades de un bloque

Desde el punto de vista del diseño de software, un bloque tiene cuatro responsabilidades principales.

## 1. Almacenar información

La responsabilidad principal de un bloque es contener los datos que la aplicación desea registrar.

En esta primera versión del proyecto no nos interesa el contenido específico de esos datos. Solo necesitamos que el bloque pueda almacenarlos.

---

## 2. Conocer su posición dentro de la cadena

Un bloque forma parte de una secuencia ordenada.

Por ese motivo debe existir alguna forma de identificar su posición dentro de la blockchain.

Más adelante discutiremos cuál es la mejor forma de representar esa posición.

---

## 3. Conocer el bloque anterior

La característica que distingue a una blockchain de una colección cualquiera de bloques es que cada bloque mantiene una relación con el bloque inmediatamente anterior.

Esta relación será la base sobre la cual construiremos la cadena completa en las próximas clases.

---

## 4. Ser conceptualmente inmutable

Una vez que un bloque fue agregado a la blockchain, su contenido no debería modificarse.

En esta etapa del curso no estudiaremos todavía los mecanismos criptográficos que permiten detectar modificaciones. Simplemente adoptaremos este comportamiento como una decisión de diseño.

---

# Qué todavía NO estudiaremos

Para mantener el foco en un único concepto, deliberadamente dejaremos fuera de esta primera implementación varios elementos que aparecerán más adelante.

Entre ellos:

- Hashes
- Proof of Work
- Nonce
- Dificultad
- Árboles de Merkle
- Transacciones
- Wallets
- Minería

Todos estos conceptos aparecerán cuando el proyecto los necesite.

---

# Trabajo práctico

Diseñar e implementar una primera versión de la clase `Block`.

Durante esta clase el objetivo no es construir una blockchain completa, sino únicamente el objeto que representará un bloque dentro de nuestro sistema.

Al finalizar la implementación deberías poder explicar el propósito de cada atributo y de cada decisión de diseño adoptada.

---

# Lo que aprenderemos en la próxima clase

Una vez que exista un bloque, el siguiente paso será responder una nueva pregunta:

> ¿Cómo organizamos múltiples bloques para formar una blockchain?
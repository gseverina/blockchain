# Clase 2 — La Blockchain

## Objetivos

Al finalizar esta clase deberías ser capaz de:

- Comprender qué es una blockchain.
- Entender la responsabilidad de una blockchain dentro del sistema.
- Diferenciar un bloque de una blockchain.
- Diseñar e implementar una primera versión de la clase `Blockchain`.

---

# ¿Qué es una blockchain?

Una blockchain es una estructura de datos formada por una secuencia ordenada de bloques.

Sin embargo, desde el punto de vista del diseño de software, una blockchain no debe verse únicamente como una lista de bloques. Una blockchain es el componente responsable de administrar esa colección de bloques y de garantizar que la cadena mantenga una estructura válida.

En esta primera versión todavía no nos preocuparemos por la integridad criptográfica de la cadena. Nuestro objetivo es construir una estructura que permita almacenar y administrar bloques de forma ordenada.

---

# Responsabilidades de una blockchain

## 1. Administrar la colección de bloques

La blockchain es responsable de almacenar todos los bloques que forman parte de la cadena.

La forma en que los almacena es un detalle de implementación que no afecta a los usuarios de la clase.

---

## 2. Incorporar nuevos bloques

Debe existir una forma controlada de agregar nuevos bloques a la cadena.

En esta etapa no analizaremos todavía si un bloque es válido o no. Solamente estudiaremos cómo incorporarlo a la blockchain.

---

## 3. Permitir consultar la cadena

Otros componentes del sistema deberán poder acceder a los bloques almacenados.

La blockchain deberá ofrecer una interfaz sencilla para realizar esas consultas sin exponer innecesariamente su implementación interna.

---

# Qué todavía NO estudiaremos

Para mantener el foco en un único concepto, esta primera versión de `Blockchain` no incluirá:

- Validación de la cadena.
- Cálculo de hashes.
- Proof of Work.
- Minería.
- Persistencia.
- Comunicación entre nodos.
- Resolución de forks.

Todos estos conceptos aparecerán en clases posteriores.

---

# Relación entre Block y Blockchain

Es importante distinguir ambos conceptos.

Un `Block` representa una única unidad de información.

Una `Blockchain` representa la colección organizada de todos los bloques y es responsable de administrarla.

Podemos pensar en la siguiente relación:

```text
Blockchain
    ├── Block
    ├── Block
    ├── Block
    └── Block
```

Cada bloque conoce información sobre sí mismo.

La blockchain conoce la cadena completa.

---

# Trabajo práctico

Diseñar e implementar una primera versión de la clase `Blockchain`.

Al finalizar la implementación deberías ser capaz de:

- Crear una blockchain vacía.
- Agregar bloques.
- Consultar los bloques almacenados.

En esta etapa no será responsabilidad de la blockchain verificar si los bloques son válidos. Esa funcionalidad será incorporada más adelante.

---

# Lo que aprenderemos en la próxima clase

Hasta ahora nuestros bloques existen, pero todavía no tienen una identidad única.

En la próxima clase estudiaremos cómo las funciones hash permiten identificar un bloque de forma confiable y detectar modificaciones en su contenido.
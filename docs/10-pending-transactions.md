# Clase 10 — Transacciones Pendientes

## Objetivos

Al finalizar esta clase deberías ser capaz de:

- Comprender que una transacción no forma parte inmediatamente de la blockchain.
- Entender el concepto de transacción pendiente.
- Incorporar un mecanismo para almacenar transacciones antes de crear un bloque.
- Preparar el modelo para la futura incorporación de minería.

---

# El problema

Hasta ahora nuestras transacciones aparecen directamente dentro de un bloque.

Sin embargo, eso no ocurre en una blockchain real.

Primero alguien crea una transacción.

Esa transacción aún no pertenece a ningún bloque.

Se encuentra esperando.

---

# Mempool

Las blockchains suelen mantener una colección de transacciones pendientes.

Esa colección recibe distintos nombres.

El más habitual es:

> **Mempool (Memory Pool)**

Allí permanecen las transacciones hasta que algún minero decide incorporarlas a un nuevo bloque.

Nuestro proyecto implementará una versión muy simplificada de ese concepto.

---

# Nuevo comportamiento

La blockchain pasará a tener dos responsabilidades diferentes.

1. Almacenar los bloques ya confirmados.
2. Almacenar las transacciones pendientes.

Visualmente:

```text
Blockchain
├── Blocks
└── Pending Transactions
```

---

# Qué todavía NO haremos

En esta clase todavía no construiremos bloques automáticamente.

Tampoco existirá minería.

Únicamente agregaremos un lugar donde las transacciones puedan esperar.

---

# Trabajo práctico

Modificar `Blockchain` para incorporar una colección de transacciones pendientes.

La clase deberá permitir registrar nuevas transacciones sin necesidad de crear inmediatamente un bloque.

---

# Lo que aprenderemos en la próxima clase

Una vez que existan transacciones pendientes, podremos construir el primer mecanismo que las convierta en un nuevo bloque.


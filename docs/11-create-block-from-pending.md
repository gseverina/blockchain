# Clase 11 — Crear un Bloque desde las Transacciones Pendientes

## Objetivos

Al finalizar esta clase deberías ser capaz de:

- Comprender cómo una blockchain incorpora nuevas transacciones a la cadena.
- Entender el ciclo de vida de una transacción.
- Implementar el primer comportamiento que hace crecer automáticamente la blockchain.
- Preparar el modelo para la futura incorporación de minería.

---

# El ciclo de vida de una transacción

Hasta ahora sabemos que una transacción nace como pendiente.

```text
Nueva Transaction
        │
        ▼
Pending Transactions
```

Pero todavía no existe ningún mecanismo para que esa transacción termine formando parte de un bloque.

Ese será el objetivo de esta clase.

---

# Construcción de un bloque

Cuando la blockchain decide crear un nuevo bloque:

1. toma las transacciones pendientes;
2. construye un nuevo bloque con ellas;
3. enlaza ese bloque con el anterior;
4. lo agrega a la cadena;
5. elimina las transacciones pendientes que ya fueron incorporadas.

Visualmente:

```text
Pending Transactions
        │
        ▼
      Block
        │
        ▼
   Blockchain
```

---

# Índice del nuevo bloque

El índice del bloque deberá surgir de la propia blockchain.

No deberá ser indicado por quien utilice la clase.

La blockchain conoce cuántos bloques tiene y, por lo tanto, puede determinar el índice del siguiente.

---

# Hash anterior

Si la blockchain está vacía, el nuevo bloque será el bloque génesis.

En caso contrario, el nuevo bloque deberá enlazarse utilizando el hash del último bloque de la cadena.

---

# Qué todavía NO implementaremos

En esta clase todavía no habrá:

- minería;
- Proof of Work;
- nonce;
- dificultad;
- recompensa al minero.

Simplemente construiremos un bloque válido a partir de las transacciones pendientes.

---

# Trabajo práctico

Incorporar a `Blockchain` un comportamiento que permita crear un nuevo bloque utilizando las transacciones pendientes y agregarlo automáticamente a la cadena.

---

# Lo que aprenderemos en la próxima clase

Una vez que la blockchain pueda crear bloques automáticamente, estudiaremos qué condiciones deben cumplirse para permitir o rechazar esa operación.


# Curso: Construyendo una Blockchain desde Cero con Python

## Objetivo del curso

El objetivo de este curso es comprender cómo funciona una blockchain construyéndola desde cero en Python.

A lo largo del recorrido desarrollaremos una implementación educativa, incorporando cada componente de forma incremental. Cada clase introducirá un único concepto nuevo y finalizará con la implementación de una pieza concreta del sistema.

El propósito no es replicar Bitcoin o Ethereum en todos sus detalles, sino comprender los principios que dieron origen a estas tecnologías y cómo interactúan sus distintos componentes.

---

# Metodología

Cada clase del curso estará compuesta por dos documentos:

- **`docs/`**: explica el concepto desde un punto de vista teórico y didáctico.
- **`specs/`**: define la especificación técnica de la pieza que deberá implementarse.

A partir de estos documentos, el estudiante desarrollará la implementación correspondiente. Una vez finalizada, se realizará una revisión técnica antes de continuar con la siguiente clase.

---

# Programa del curso

## Módulo I — Los fundamentos

### Clase 0 — Visión del proyecto

**Conceptos**

- Objetivos del curso
- Filosofía del proyecto
- Organización del repositorio

**Implementación**

Ninguna.

---

### Clase 1 — El bloque

**Conceptos**

- ¿Qué es un bloque?
- Responsabilidades de un bloque
- Bloque génesis
- Inmutabilidad

**Implementación**

- `Block`

---

### Clase 2 — La blockchain

**Conceptos**

- ¿Qué es una blockchain?
- Responsabilidades de una blockchain
- Administración de bloques
- Cadena de bloques

**Implementación**

- `Blockchain`

---

### Clase 3 — Funciones hash

**Conceptos**

- ¿Qué es una función hash?
- Propiedades de una buena función hash
- SHA-256

**Implementación**

- Cálculo del hash de un bloque

---

### Clase 4 — Encadenando bloques

**Conceptos**

- Integridad de la cadena
- Hash del bloque anterior
- Detección de modificaciones

**Implementación**

- Encadenamiento de bloques mediante hashes

---

### Clase 5 — Validación de la blockchain

**Conceptos**

- Verificación de integridad
- Recorrido de la cadena
- Reglas de validación

**Implementación**

- Validación completa de la blockchain

---

# Módulo II — Transacciones

### Clase 6 — Transacciones

**Conceptos**

- ¿Qué es una transacción?
- Componentes de una transacción
- Modelo de datos

**Implementación**

- `Transaction`

---

### Clase 7 — Wallets

**Conceptos**

- Claves públicas y privadas
- Direcciones
- Identidad en blockchain

**Implementación**

- `Wallet`

---

### Clase 8 — Firmas digitales

**Conceptos**

- Integridad
- Autenticidad
- No repudio

**Implementación**

- Firma y verificación de transacciones

---

### Clase 9 — Bloques con transacciones

**Conceptos**

- Organización de transacciones
- Relación entre bloques y transacciones

**Implementación**

- Integración de `Transaction` dentro de `Block`

---

# Módulo III — Consenso

### Clase 10 — El problema del consenso

**Conceptos**

- Sistemas distribuidos
- Consenso
- Problema del doble gasto

**Implementación**

Ninguna.

---

### Clase 11 — Proof of Work

**Conceptos**

- Nonce
- Dificultad
- Minería

**Implementación**

- Minería de bloques

---

### Clase 12 — Minando una blockchain

**Conceptos**

- Integración del proceso de minería
- Construcción de nuevos bloques

**Implementación**

- Minería integrada en `Blockchain`

---

# Módulo IV — Optimización

### Clase 13 — Árboles de Merkle

**Conceptos**

- Árboles de Merkle
- Verificación eficiente
- Integridad de transacciones

**Implementación**

- `MerkleTree`

---

### Clase 14 — Block Header

**Conceptos**

- Cabecera del bloque
- Separación entre metadatos y contenido

**Implementación**

- `BlockHeader`

---

### Clase 15 — Persistencia

**Conceptos**

- Serialización
- Almacenamiento
- Recuperación de la blockchain

**Implementación**

- Persistencia de la blockchain

---

# Módulo V — Red distribuida

### Clase 16 — Nodos

**Conceptos**

- ¿Qué es un nodo?
- Responsabilidades
- Comunicación

**Implementación**

- `Node`

---

### Clase 17 — Red P2P

**Conceptos**

- Descubrimiento de nodos
- Intercambio de bloques
- Sincronización

**Implementación**

- Comunicación entre nodos

---

### Clase 18 — Resolución de conflictos

**Conceptos**

- Forks
- Cadena más larga
- Resolución de conflictos

**Implementación**

- Algoritmo simplificado de resolución de conflictos

---

# Módulo VI — Cierre

### Clase 19 — Comparación con Bitcoin

**Conceptos**

- Arquitectura de Bitcoin
- Diferencias con nuestra implementación
- Simplificaciones realizadas

**Implementación**

Ninguna.

---

### Clase 20 — Próximos pasos

**Conceptos**

- Ethereum
- Smart Contracts
- Proof of Stake
- Lightning Network
- Otras blockchains

**Implementación**

Ninguna.

---

# Resultado esperado

Al finalizar el curso, el estudiante habrá desarrollado una blockchain educativa completamente funcional en Python y comprenderá el propósito de cada uno de sus componentes, desde la estructura básica de un bloque hasta los mecanismos de consenso utilizados por las principales blockchains modernas.
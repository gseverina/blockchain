# Clase 8 — Integrando Wallet y Transaction

## Objetivos

Al finalizar esta clase deberías ser capaz de:

- Comprender por qué una transacción debe referenciar wallets y no cadenas de texto.
- Modelar relaciones entre entidades del dominio.
- Evolucionar el modelo de `Transaction` sin modificar su propósito.
- Comprender cómo evoluciona un diseño de software de forma incremental.

---

# El problema de utilizar cadenas

Hasta ahora representamos los participantes de una transacción mediante texto.

Por ejemplo:

```python
Transaction(
    sender="alice",
    recipient="bob",
    amount=...
)
```

Esto fue suficiente para introducir el concepto de transacción.

Sin embargo, una cadena no representa una identidad del dominio.

Simplemente representa caracteres.

---

# Las transacciones deben conocer wallets

Ahora contamos con una clase específica para representar identidades:

```text
Wallet
```

Por lo tanto, una transacción ya no debería almacenar cadenas sino referencias a objetos `Wallet`.

Conceptualmente:

```text
Antes

Transaction
 ├── sender: str
 ├── recipient: str
 └── amount

Después

Transaction
 ├── sender: Wallet
 ├── recipient: Wallet
 └── amount
```

---

# Beneficios

Este cambio aporta varias ventajas.

La transacción ahora expresa explícitamente que los participantes son wallets.

Además, en clases futuras podremos incorporar claves, firmas digitales y direcciones sin modificar el concepto de transacción.

La relación entre ambas entidades ya estará correctamente modelada.

---

# Qué todavía NO estudiaremos

En esta clase no implementaremos:

- Firmas digitales.
- Verificación de identidad.
- Autorización de transacciones.
- Criptografía.
- Persistencia.

El objetivo es únicamente reemplazar un tipo primitivo por una entidad del dominio.

---

# Trabajo práctico

Modificar la clase `Transaction` para que `sender` y `recipient` sean instancias de `Wallet`.

Actualizar las validaciones y los tests necesarios para reflejar este cambio.

---

# Lo que aprenderemos en la próxima clase

Hasta ahora las transacciones existen de manera independiente.

En la próxima clase comenzaremos a incorporarlas dentro de los bloques, permitiendo que un bloque contenga múltiples transacciones.


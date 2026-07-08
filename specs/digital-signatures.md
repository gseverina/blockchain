# Especificación — Firmas digitales

## Objetivo

Incorporar un mecanismo de firma digital simplificado que permita a una `Wallet` autorizar una `Transaction` y a cualquier participante verificar posteriormente dicha autorización.

Esta implementación tiene fines exclusivamente educativos y no pretende ser criptográficamente segura.

---

# Alcance

Esta clase incorpora el concepto de firma digital, pero no modifica todavía la estructura de los bloques ni el funcionamiento de la blockchain.

Las firmas existirán únicamente entre `Wallet` y `Transaction`.

---

# Cambios sobre `Wallet`

La clase `Wallet` deberá representar una identidad capaz de firmar transacciones.

Se incorporarán los conceptos de:

- clave privada
- clave pública

La implementación concreta de estas claves queda a criterio del estudiante, siempre que permita firmar y verificar transacciones de manera consistente.

La API pública deberá ofrecer un método para firmar una transacción.

---

# Cambios sobre `Transaction`

Una transacción podrá almacenar una firma digital.

Inicialmente una transacción puede no estar firmada.

Una vez firmada deberá ser posible verificar su autenticidad.

La API pública deberá ofrecer un método para verificar la firma.

---

# Flujo esperado

El flujo de uso será conceptualmente el siguiente:

```
Wallet
    │
    │ firma
    ▼
Transaction
    │
    │ verifica
    ▼
True / False
```

---

# Reglas

## Firma

Una firma deberá depender del contenido completo de la transacción.

Modificar cualquier dato de la transacción deberá invalidar la firma.

---

## Verificación

La verificación deberá devolver:

- `True` cuando la firma sea válida.
- `False` cuando la firma no exista o sea inválida.

La verificación nunca deberá modificar el estado de la transacción.

---

# Restricciones

Durante esta clase:

- no se utilizarán bibliotecas criptográficas externas;
- no se implementará ECDSA, RSA ni algoritmos equivalentes;
- no se incorporarán bloques con transacciones;
- no se implementará minería;
- no se incorporará consenso.

El objetivo es comprender el flujo de firmado y verificación, no construir un sistema criptográfico de producción.

---

# Criterios de aceptación

La implementación deberá permitir verificar, mediante pruebas automatizadas, al menos los siguientes escenarios:

- una wallet puede firmar una transacción;
- una firma válida puede verificarse correctamente;
- una transacción modificada deja de verificar correctamente;
- una transacción sin firma no verifica;
- una firma inválida no verifica;
- verificar una firma no modifica la transacción.


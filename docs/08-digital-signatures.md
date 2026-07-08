# Clase 8 — Firmas digitales

## Objetivo

Hasta ahora hemos construido una blockchain capaz de almacenar bloques y verificar la integridad de la cadena mediante funciones hash.

Sin embargo, todavía existe un problema importante: cualquiera podría crear una transacción diciendo que envía dinero desde cualquier participante.

Por ejemplo:

> Alice envía 100 monedas a Bob.

¿Cómo sabemos que realmente fue Alice quien autorizó esa operación?

En esta clase incorporaremos el concepto de **firma digital**, un mecanismo que permite demostrar que una transacción fue autorizada por su propietario sin necesidad de confiar en un tercero.

---

# El problema de la confianza

Imaginemos la siguiente situación.

Alice crea una transacción:

```
Alice -> Bob : 10
```

Si cualquier persona pudiera escribir ese mensaje, entonces también podría crear:

```
Alice -> Bob : 1.000.000
```

La blockchain no tendría forma de distinguir cuál de las dos transacciones fue realmente creada por Alice.

Necesitamos un mecanismo que permita responder una pregunta fundamental:

> ¿Quién autorizó esta transacción?

Las firmas digitales resuelven exactamente ese problema.

---

# Criptografía asimétrica

Las firmas digitales utilizan un sistema conocido como **criptografía asimétrica**.

Cada participante posee dos claves diferentes:

- una **clave privada**
- una **clave pública**

La clave privada debe permanecer secreta y únicamente su propietario debe conocerla.

La clave pública, en cambio, puede compartirse libremente con cualquier persona.

Estas dos claves están matemáticamente relacionadas, pero conocer la clave pública no permite obtener la clave privada.

---

# Firmar una transacción

Cuando una wallet desea autorizar una transacción, utiliza su **clave privada** para generar una firma digital.

Conceptualmente ocurre algo similar a esto:

```
Transacción
        │
        ▼
Clave privada
        │
        ▼
Firma digital
```

La firma queda asociada a la transacción.

Si posteriormente alguien modifica cualquier dato de la transacción, la firma dejará de ser válida.

---

# Verificar una firma

Cualquier participante puede comprobar la autenticidad de una transacción utilizando la clave pública del emisor.

El proceso es el siguiente:

```
Transacción
        │
        ▼
Firma digital
        │
        ▼
Clave pública
        │
        ▼
¿La firma es válida?
```

Si la verificación tiene éxito, sabemos que la transacción fue firmada por quien posee la clave privada correspondiente.

---

# ¿Qué garantiza una firma digital?

Las firmas digitales aportan tres propiedades fundamentales.

## Autenticidad

Permiten verificar quién autorizó la transacción.

## Integridad

Garantizan que el contenido no fue modificado después de ser firmado.

## No repudio

Quien firmó la transacción no puede negar posteriormente haberlo hecho, ya que únicamente su clave privada podía generar esa firma.

---

# Simplificación utilizada en este curso

Las blockchains reales utilizan algoritmos criptográficos avanzados, como criptografía de curva elíptica (ECDSA o Schnorr).

Implementar correctamente esos algoritmos requiere conocimientos de criptografía y el uso de bibliotecas especializadas.

Como el objetivo de este curso es comprender el funcionamiento de una blockchain, en esta clase construiremos un mecanismo de firma **simplificado**.

No será criptográficamente seguro, pero reproducirá el mismo flujo conceptual:

- una wallet podrá firmar una transacción;
- la transacción almacenará esa firma;
- cualquier participante podrá verificarla.

En clases posteriores compararemos esta implementación educativa con la utilizada por Bitcoin.

---

# Aclaraciones sobre la implementación

## ¿Por qué un hash no reemplaza una firma digital?

Un hash (Clase 3) depende únicamente del contenido: cualquiera puede calcular `sha256(contenido)` sin necesidad de poseer ninguna clave. Sirve para detectar modificaciones, pero no para demostrar quién produjo ese contenido. Una firma, en cambio, solo puede generarse con una clave privada — por eso agrega autenticidad, algo que un hash por sí solo no puede ofrecer.

## Integridad vs. autenticidad

- **Integridad**: el contenido no fue modificado (esto ya lo resuelve un hash).
- **Autenticidad**: el contenido fue efectivamente producido por quien dice haberlo producido (esto requiere una firma, no alcanza con un hash).

Una firma digital bien construida aporta ambas propiedades a la vez: si el contenido cambia, la firma deja de coincidir (integridad); y solo el dueño de la clave privada pudo haberla generado (autenticidad).

## ¿Por qué cualquiera puede verificar una firma?

Porque la verificación usa la clave **pública**, que por definición puede compartirse libremente. Verificar no requiere ningún secreto — solo saber cuál es la clave pública del firmante.

## ¿Por qué solo el dueño de la clave privada puede generarla?

Porque la firma se calcula **a partir de la clave privada**, nunca de la pública. Si el cálculo usara la clave pública, cualquiera que la conociera (es decir, cualquiera) podría fabricar firmas válidas — dejando de tener sentido el concepto de "autorización".

## Nota sobre `public_key = sha256(private_key)`

En este curso derivamos la clave pública aplicando SHA-256 sobre la clave privada, únicamente para tener una relación unidireccional simple (conocer la pública no permite reconstruir la privada) sin depender de bibliotecas externas. **Esto no es cómo funciona una blockchain real**: Bitcoin y Ethereum derivan la clave pública a partir de la privada mediante operaciones sobre curvas elípticas (ECDSA/secp256k1), no aplicando un hash. La relación matemática es distinta y mucho más compleja — la simplificación de este curso solo preserva la propiedad de "unidireccionalidad", no el mecanismo real.


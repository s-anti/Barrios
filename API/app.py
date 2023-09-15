from barrios import Barrios
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
import datetime

barrios = Barrios("./API/barrioswerb.sqlite3", True)

barrios.crearTablas()
barrios.insertarMuestras()

mesAhora = "2023-08"

app = Flask(__name__)

CORS(app)

# TODO: todo esto
# Tengo que hacer
# Vista de propietarios individuales #MAS O MENOS QUEDO
# ISOLAR LAS TABLAS
# ELIMINAR PROPIETARIO NO TE DEJA EL LOTE DISPONIBLE VER ESO
# PODER VENDER LOTES Y CAPAZ VER EL HISTORIAL DEL LOTE
# paginado de las tablas
# Búsqueda # LA VOLAMOS A LA BÚSQUEDA 0 SCOPE CREEP ACÁ
#   Filtros de búsqueda
# Edición básica
# Un picker de mes=?
# Que los lotes de los propietarios sean la misma tabla no un div
# Cuando no hay lote disponible que no te deje agregar uno nuevo
# PAGOOS, fecha, ltoes

diccionario = {
    "propietarios": "prop",
    "manzanas": "manz",
    "proplote": "pl",
    "consumos": "cons",
    "lotes": "lote",
    "costos": "cos",
}


def hacerLista(datos):
    for i in range(len(datos)):
        for j in range(len(datos[i])):
            if len(datos[i][j].values()) == 1:
                datos[i][j] = list(datos[i][j].values())[0]
            else:
                datos[i][j] = list(datos[i][j].values())


def prop_id_dict(datos):
    n_datos = []
    for i, registro in enumerate(datos):
        n_datos.append([])
        for id, dato in enumerate(registro):
            if id == 2:
                dato = {**dato, "p.prop_id": registro[3]["prop_id"]}
            if id == 3:
                continue
            n_datos[i].append(dato)

    return n_datos


@app.route("/mes/<mes>")
def cambiarMes(mes):
    mesAhora = mes


@app.route("/lotes")
def lotes():
    datos = barrios.fetchApi(
        """SELECT l.lote_id, l.lote_manz_id, xd.prop_nombre || ' ' || xd.prop_apellido as "nombre", xd.prop_id, l.lote_m_frente, l.lote_m_prof, l.lote_luz_bool, l.lote_agua_bool, l.lote_asf_bool, l.lote_esq_bool
        FROM Lotes l
        LEFT JOIN  (select * from PropLoteMes pl  JOIN Propietarios p on p.prop_id = pl.pl_prop_id 
        where pl_cons_mes = (
        select p2.pl_cons_mes
        from proplotemes p2
        where p2.pl_prop_id = p.prop_id)) as xd
         on xd.pl_lote_id = l.lote_id
     
        order by 1 asc
        """
    )

    n_datos = prop_id_dict(datos)
    hacerLista(n_datos)

    return jsonify(n_datos)


@app.route("/uno_solo/<tabla>/<id>")
def propietario(tabla, id):
    if tabla == "lotes":
        datos = barrios.fetchApi(
            """SELECT l.*, p.prop_nombre || ' ' || p.prop_apellido
            FROM lotes l
            LEFT JOIN PropLoteMes pl  on pl.pl_lote_id = l.lote_id
            LEFT JOIN Propietarios p on p.prop_id = pl.pl_prop_id
            WHERE l.lote_id = {}""".format(
                id
            )
        )

        return jsonify(datos[0])
    else:
        datos = barrios.fetchApi(
            "SELECT * FROM {} WHERE {}_ID = {}".format(tabla, diccionario[tabla], id)
        )

        return jsonify(datos[0])


@app.route("/propietarios")
def propietarios():
    datos = barrios.fetchApi(
        """SELECT p.*, (SELECT count(pl.pl_id) from PropLoteMes pl where pl_prop_id = p.prop_id)
        FROM Propietarios p
        """
    )

    hacerLista(datos)

    return jsonify(datos)


@app.route("/propietarios/<id>/consumos")
def propietario_id(id):
    datosProp = barrios.fetchApi(
        """SELECT pl_id, pl_lote_id, pl_superficie_cub, pl_habitantes, pl_vehiculos, pl_cons_luz, pl_cons_agua, pl_cons_gas, pl_cons_mes
        FROM PropLoteMes c
        WHERE c.pl_prop_id = {}
            """.format(
            id
        )
    )
    hacerLista(datosProp)
    barrios.actualizar(mesAhora)
    print("Consuymos", datosProp)

    return jsonify(datosProp)


@app.route("/propietarios/<id>")
def propietario_lotes(id):
    datosLotes = barrios.fetchApi(
        """SELECT *
        FROM Propietarios
        WHERE prop_id = {}
       """.format(
            id
        )
    )

    hacerLista(datosLotes)

    return jsonify(datosLotes)


@app.route("/propietarios/<id>/pagos")
def propietario_pagos(id):
    datos = barrios.fetchApi(
        """SELECT cons_id, cons_lot_id, cons_cost_id, cons_seguridad, cons_luz, cons_agua, cons_gas, cons_luz_publica, cons_f_agua, cons_f_asf, cons_vehiculo,
         cons_seguridad + cons_luz + cons_agua + cons_gas + cons_luz_publica + cons_f_agua,
 cons_pagado
        FROM consumos
        WHERE cons_prop_id = {}
      """.format(
            id
        )
    )

    hacerLista(datos)

    return jsonify(datos)


@app.route("/prop_lote_mes/<id>")
def proplotemes(id):
    datos = barrios.fetchApi(
        """SELECT pl_lote_id, pl_superficie_cub, pl_habitantes, pl_vehiculos, pl_cons_luz, pl_cons_agua, pl_cons_gas, pl_cons_mes
        from propLoteMes
        where pl_prop_id = {}""".format(
            id
        )
    )

    return jsonify(datos)


@app.route("/consumos")
def consumos():
    datos = barrios.fetchApi(
        """SELECT c.cons_id, c.cons_lot_id, p.prop_nombre || ' ' || p.prop_apellido as "nombre", p.prop_id as "prop_id",  co.cos_mes, c.cons_seguridad, c.cons_luz, c.cons_agua, c.cons_gas, c.cons_luz_publica, c.cons_f_agua, c.cons_f_asf, c.cons_vehiculo, c.cons_seguridad +
c.cons_luz +
c.cons_agua +
c.cons_gas +
c.cons_luz_publica +
c.cons_f_agua +
c.cons_f_asf +
c.cons_vehiculo as total, c.cons_pagado
        FROM Consumos c
        JOIN propietarios p on p.prop_id = c.cons_prop_id
        join Costos co on co.cos_id = c.cons_cost_id"""
    )

    n_datos = prop_id_dict(datos)
    hacerLista(n_datos)

    # print("tirando", n_datos[0], "\n" * 2, datos[0])

    barrios.actualizar(mesAhora)

    return jsonify(n_datos)


@app.route("/consumos/<id>")
def consumosId(id):
    datos = barrios.fetchApi(
        """SELECT cons_id, cons_lot_id, cos_mes, cons_seguridad, cons_luz, cons_agua, cons_gas, cons_luz_publica, cons_f_agua, cons_f_asf, cons_vehiculo
        FROM Consumos c
        join costos
        on cos_id = cons_cost_id
        where cons_prop_id = {} """.format(
            id
        )
    )

    barrios.actualizar(mesAhora)

    return jsonify(datos)


@app.route("/costos")
def costos():
    datos = barrios.fetchApi("SELECT * FROM Costos")
    hacerLista(datos)
    print("Torando", datos)

    return jsonify(datos)


@app.route("/cargar/<tabla>", methods=["POST"])
def cargar(tabla):
    datos = request.form.to_dict()

    keys = ",".join(datos.keys())
    lista = list(datos.values())

    print("Nos tiraron", lista)

    signos = ""
    for i in range(len(datos.keys()) - 1):
        signos += "?,"
    signos += "?"

    barrios.insertar(f"INSERT INTO {tabla} ({keys}) VALUES ({signos}) ", lista)
    print("Cargamos algo ponele")

    return "ponele que "


@app.route("/editar/<tabla>", methods=["POST"])
def editar(tabla):
    datos = request.form.to_dict()
    print("traemos", datos)

    keys = list(datos.keys())
    lista = list(datos.values())

    sets = ""
    for i, j in zip(keys, lista):
        jxd = j if j is int else f"'{j}'"
        sets += f"{i} = {jxd}, "
    sets = sets[:-2]
    barrios.ejecutar(
        "UPDATE {} SET {} WHERE {} = {}".format(tabla, sets, keys[0], lista[0])
    )

    return "Algo pasó..."


@app.route("/lotes_libres")
def lotes_libre():
    datos = barrios.fetchApi(
        """SELECT l.lote_id
            FROM lotes l
            LEFT JOIN PropLoteVenta pl ON l.lote_id = pl.plv_lote_id
            WHERE pl.plv_lote_id IS NULL
            or pl.plv_fecha_venta is not null"""
    )
    print("Los datos son", datos)

    return jsonify(datos)


@app.route("/proploteMes")
def proplotemesxd():
    datos = barrios.fetchApi(
        """SELECT pl.pl_id, pl.pl_lote_id,  p.prop_nombre || ' ' || p.prop_apellido as "nombre", pl.pl_prop_id as "prop_id",  pl.pl_superficie_cub, pl.pl_habitantes, pl.pl_vehiculos, pl.pl_cons_luz, pl.pl_cons_agua, pl.pl_cons_gas,pl.pl_cons_mes
            FROM PropLoteMes pl
            JOIN propietarios p on p.prop_id = pl.pl_prop_id
            """
    )

    return jsonify(datos)


@app.route("/proplote")
def proplote():
    datos = barrios.fetchApi(
        """SELECT pl.pl_id, pl.pl_lote_id,  p.prop_nombre || ' ' || p.prop_apellido as "nombre", pl.pl_prop_id as "prop_id", pl.pl_superficie_cub, pl.pl_habitantes, pl.pl_vehiculos, pl.pl_cons_luz, pl.pl_cons_agua, pl.pl_cons_gas
            FROM PropLoteMes pl
            JOIN propietarios p on p.prop_id = pl.pl_prop_id
            """
    )

    print("datos son", datos)

    return jsonify(prop_id_dict(datos))


@app.route("/actualizar/<mes>")
def actualizar(mes):
    print("Acá en mes")
    barrios.actualizar(mes)
    datos = barrios.fetchApi(
        """SELECT c.cons_id, c.cons_lot_id, p.prop_nombre || ' ' || p.prop_apellido as "nombre", p.prop_id as "prop_id",  c.cons_cost_id, c.cons_seguridad, c.cons_luz, c.cons_agua, c.cons_gas, c.cons_luz_publica, c.cons_f_agua, c.cons_f_asf, c.cons_vehiculo
        FROM Consumos c
        JOIN propietarios p on p.prop_id = c.cons_prop_id"""
    )

    return jsonify(prop_id_dict(datos))


@app.route("/eliminar/propietarios/<id>")
def eliminar(id):
    barrios.ejecutar("DELETE FROM PROPIETARIOS WHERE prop_id = " + str(id))

    barrios.ejecutar(
        """UPDATE proploteVenta
        set plv_fecha_venta = {}
        WHERE plv_prop_id = {}""".format(
            "'" + str(datetime.date.today()) + "'", id
        )
    )
    print(datetime.date.today())

    return propietarios()


@app.route("/prop_vende_lote/<idProp>/<idLote>")
def prop_vende_lote(idProp, idLote):
    barrios.ejecutar(
        """UPDATE proploteventa
        set plv_fecha_venta = {}
        WHERE plv_prop_id = {} AND plv_lote_id = {}""".format(
            "'" + str(datetime.date.today()) + "'", idProp, idLote
        )
    )

    return propietario_lotes(idProp)


@app.route("/lotes_de/<quien>")
def lotesDe(quien):
    datos = barrios.fetchApi(
        """SELECT l.lote_id as  pl_lote_id
            FROM lotes l
            LEFT JOIN PropLoteVenta pl ON l.lote_id = pl.plv_lote_id
            WHERE pl.plv_lote_id IS NULL
            or pl.plv_fecha_venta is not null
union
       select pl_lote_id
    from propLoteMes
    where pl_prop_id = {}
""".format(
            quien
        )
    )

    return jsonify([list(i[0].values())[0] for i in datos])


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404


app.run(debug=True, use_reloader=False)

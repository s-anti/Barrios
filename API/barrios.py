import sqlite3 as sql
import os

# Consumos variables por més


class Barrios:
    def __init__(self, path: str, eliminar=False):
        if eliminar:
            try:
                os.remove(path)
                print("Eliminando la base de datos en", path)
            except:
                print("No se eliminó la base de datos en", path, "(capaz se creó)")

        self.conn = sql.connect(path, check_same_thread=False)
        self.conn.row_factory = sql.Row
        self.cur = self.conn.cursor()

    def crearTablas(self):
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS Costos (
                cos_id INTEGER PRIMARY KEY AUTOINCREMENT,
                cos_seguridad FLOAT NOT NULL,
                cos_kw FLOAT NOT NULL,
                cos_m3_agua FLOAT NOT NULL,
                cos_m3_gas FLOAT NOT NULL,
                cos_total_luz FLOAT NOT NULL,
                cos_mf_agua FLOAT NOT NULL,
                cos_mf_asf FLOAT NOT NULL,
                cos_vehiculos FLOAT NOT NULL,
                cos_m2_valor FLOAT NOT NULL,
                cos_mes VARCHAR(6) NOT NULL UNIQUE CHECK(cos_mes like '____-__')
            )"""
        )

        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS Propietarios (
                prop_id INTEGER PRIMARY KEY AUTOINCREMENT,
                prop_nombre VARCHAR NOT NULL,
                prop_apellido VARCHAR NOT NULL

            )"""
        )
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS Manzanas (
                manz_id INTEGER PRIMARY KEY AUTOINCREMENT
            )"""
        )
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS Lotes (
                lote_id INTEGER PRIMARY KEY AUTOINCREMENT,
                lote_manz_id INTEGER NOT NULL,
                lote_m_frente FLOAT NOT NULL,
                lote_m_prof FLOAT NOT NULL,
                lote_luz_bool BOOLEAN NOT NULL DEFAULT FALSE,
                lote_agua_bool BOOLEAN NOT NULL DEFAULT FALSE,
                lote_asf_bool BOOLEAN NOT NULL DEFAULT FALSE,
                lote_esq_bool BOOLEAN NOT NULL DEFAULT FALSE,
                FOREIGN KEY (lote_manz_id) REFERENCES Manzanas (manz_id)
            )"""
        )
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS PropLoteMes (
                pl_id INTEGER PRIMARY KEY AUTOINCREMENT,
                pl_lote_id INTEGER NOT NULL,
                pl_prop_id INTEGER NOT NULL,
                pl_superficie_cub FLOAT NOT NULL,
                pl_habitantes INTEGER NOT NULL,
                pl_vehiculos INTEGER NOT NULL,
                pl_cons_luz FLOAT NOT NULL,
                pl_cons_agua FLOAT NOT NULL,
                pl_cons_gas FLOAT NOT NULL,
                pl_cons_mes VARCHAR(6) NOT NULL,
                FOREIGN KEY (pl_lote_id) REFERENCES Lotes (lote_id),
                FOREIGN KEY (pl_prop_id)REFERENCES Propietarios (prop_id),
                CHECK(pl_cons_mes like '____-__')


        )"""
        )

        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS PropLoteVenta (
            plv_id INTEGER PRIMARY KEY AUTOINCREMENT,
            plv_fecha_compra VARCHAR(6) NOT NULL,
            plv_fecha_venta VARCHAR(6),
            plv_lote_id INTEGER NOT NULL,
            plv_prop_id INTEGER NOT NULL,
            foreign key(plv_lote_id) references lotes(lote_id),
            foreign key(plv_prop_id) references propietarios(prop_id),
            CHECK(plv_fecha_compra like '____-__-__' or plv_fecha_compra is Null)

            CHECK(plv_fecha_venta like '____-__-__' or plv_fecha_venta is Null)

          )"""
        )

        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS Consumos (
                cons_id INTEGER PRIMARY KEY AUTOINCREMENT,
                cons_lot_id INTEGER NOT NULL,
                cons_prop_id INTEGER NOT NULL,
                cons_cost_id INTEGER NOT NULL ,
                cons_seguridad FLOAT NOT NULL,
                cons_luz FLOAT NOT NULL,
                cons_agua FLOAT NOT NULL,
                cons_gas FLOAT NOT NULL,
                cons_luz_publica FLOAT NOT NULL,
                cons_f_agua FLOAT NOT NULL,
                cons_f_asf FLOAT NOT NULL,
                cons_vehiculo FLOAT NOT NULL,
                cons_fecha_pago date,
                FOREIGN KEY (cons_lot_id) REFERENCES Lotes (lote_id),
                FOREIGN KEY (cons_prop_id) REFERENCES Propietarios (prop_id),
                FOREIGN KEY (cons_cost_id) REFERENCES Costos (cos_id) --,
               -- CONSTRAINT combinacion UNIQUE (cons_prop_id, cons_lot_id, cons_cost_id)
            )"""
        )
        print("Terminamos de crear las tablas")

    def fetchDatos(self, query: str):
        cur = self.conn.cursor()
        # print("Query es ", query)
        cur.execute(query)
        a = cur.fetchall()
        cur.close()
        return a

    def insertarMuestras(self):
        if self.fetchDatos("SELECT * FROM Costos") == []:
            print("Costos no tiene, agregando")
            self.cur.execute(
                "INSERT INTO Costos VALUES (NULL,?,?,?,?,?,?,?,?,?,?)",
                (
                    30000.00,
                    60.00,
                    30.00,
                    45.00,
                    80000.00,
                    40.00,
                    70.00,
                    10000.00,
                    60000.00,
                    "2023-08",
                ),
            )
        self.conn.commit()

        prop_data = [
            ["María", "Rodriguez"],
            ["Juan", "López"],
            ["Ana", "García"],
            ["Carlos", "Matínez"],
        ]
        if self.fetchDatos("SELECT * FROM Propietarios") == []:
            self.cur.executemany(
                "INSERT INTO Propietarios VALUES (NULL,?,?)", prop_data
            )

        manz_data = [
            [
                1,
            ],
            [
                2,
            ],
            [
                3,
            ],
            [
                4,
            ],
        ]

        if self.fetchDatos("SELECT * FROM Manzanas") == []:
            self.cur.executemany(
                "INSERT INTO Manzanas VALUES ( ?)", manz_data
            )  # manz_data

        lote_data = [
            [1, 100, 120, 0, 1, 1, 1],
            [1, 110, 90, 1, 0, 1, 0],
            [2, 90, 110, 1, 1, 0, 1],
            [2, 110, 100, 0, 1, 0, 0],
            [3, 85, 100, 0, 0, 1, 1],
            [3, 100, 85, 0, 1, 1, 0],
            [4, 100, 120, 1, 1, 1, 1],
        ]

        if self.fetchDatos("SELECT * FROM Lotes") == []:
            self.cur.executemany(
                "INSERT INTO Lotes VALUES (NULL,?,?,?,?,?,?,?)", lote_data
            )

        prop_lote_data = [
            [1, 1, 600, 2, 1, 0, 2400, 1500, "2023-08"],
            [2, 2, 830, 0, 0, 1100, 0, 0, "2023-08"],
            [3, 2, 230, 4, 2, 1200, 200, 2300, "2023-08"],
            [4, 3, 0, 0, 0, 0, 1400, 0, "2023-08"],
            [5, 4, 0, 0, 0, 0, 0, 0, "2023-08"],
            [6, 3, 700, 5, 3, 0, 4230, 3400, "2023-08"],
        ]

        if self.fetchDatos("SELECT * FROM PropLoteMes") == []:
            self.cur.executemany(
                "INSERT INTO PropLoteMes VALUES (NULL,?,?,?,?,?,?,?,?,?)",
                prop_lote_data,
            )

        propLoteVentaData = [
            ["2016-09-22", None, 1, 1],
            ["2016-09-22", None, 2, 2],
            ["2018-12-04", None, 3, 2],
            ["2022-04-31", None, 4, 3],
            ["2021-02-12", None, 5, 4],
            ["2020-05-12", None, 6, 3],
        ]

        if self.fetchDatos("SELECT * FROM PropLoteVenta") == []:
            self.cur.executemany(
                "INSERT INTO PropLoteVenta VALUES (NULL,?,?,?,?)",
                propLoteVentaData,
            )

        self.conn.commit()
        print("Insertamos los datos de muestra")

    def actualizar(self):
        a = self.fetchDatos("select cos_mes from costos")

        print("a es ", a)
        for mesV in a:
            print("\n")
            print(mesV)
            mes = str(list(mesV)[0])
            print("en for con mes", mes)

            datos = self.fetchDatos(
                """SELECT l.*, p.*, pl.*
                FROM PropLoteMes pl
                JOIN Propietarios p on pl.pl_prop_id = p.prop_id
                JOIN Lotes l on pl.pl_lote_id = l.lote_id
                WHERE pl.pl_cons_mes = '{}'
                """.format(
                    mes
                )
            )

            if len(datos) == 0:
                print("len(datos) es 0; algo faltó...")
                return

            mesId = self.fetchDatos(
                f"SELECT cos_id FROM Costos where cos_mes = '{mes}'"
            )[0]["cos_id"]

            costos = self.fetchDatos(f"SELECT * FROM Costos where cos_mes = '{mes}'")

            pago_lot = []
            pago_prop = []
            pago_seguridad = []
            pago_luz = []
            pago_agua = []
            pago_gas = []
            pago_luz_publica = []
            pago_f_agua = []
            pago_f_asf = []
            pago_vehiculo = []
            pago_costos = []

            lotes_construidos = 0
            lotes_luz = 0

            for i in datos:
                # TODO: Optimizar
                # print(i["pl_superficie_cub"])
                if i["pl_superficie_cub"] > 0:
                    lotes_construidos += 1

                if i["lote_luz_bool"]:
                    lotes_luz += 1

            pago_lote_const = costos[0]["cos_seguridad"] / (
                len(datos) + lotes_construidos
            )
            pago_lote_no_const = pago_lote_const * 2

            for i in datos:
                pago_lot.append(i["lote_id"])
                pago_prop.append(i["prop_id"])

                if i["pl_superficie_cub"] > 0:
                    pago_seguridad.append(pago_lote_const)
                else:
                    pago_seguridad.append(pago_lote_no_const)

                # TODO: MES
                pago_luz.append(costos[0]["cos_kw"] * i["pl_cons_luz"])
                pago_agua.append(costos[0]["cos_m3_agua"] * i["pl_cons_agua"])
                pago_gas.append(costos[0]["cos_m3_gas"] * i["pl_cons_gas"])

                if i["lote_luz_bool"]:
                    # TODO: MES
                    pago_luz_publica.append(costos[0]["cos_total_luz"] / lotes_luz)
                else:
                    pago_luz_publica.append(0)

                if i["lote_esq_bool"]:
                    # TODO: MES
                    pago_f_agua.append(
                        costos[0]["cos_mf_agua"]
                        * (i["lote_m_frente"] + i["lote_m_prof"])
                    )
                    pago_f_asf.append(
                        costos[0]["cos_mf_asf"]
                        * (i["lote_m_frente"] + i["lote_m_prof"])
                    )
                else:
                    pago_f_agua.append(costos[0]["cos_mf_agua"] * (i["lote_m_prof"]))
                    pago_f_asf.append(costos[0]["cos_mf_asf"] * (i["lote_m_prof"]))

                pago_vehiculo.append(costos[0]["cos_vehiculos"] * i["pl_vehiculos"])

                pago_costos.append(mesId)

            lista = [
                pago_lot,
                pago_prop,
                pago_costos,
                pago_seguridad,
                pago_luz,
                pago_agua,
                pago_gas,
                pago_luz_publica,
                pago_f_agua,
                pago_f_asf,
                pago_vehiculo,
            ]
            transpuesta = []

            for i in range(len(lista[0])):
                f = []
                for j in range(len(lista)):
                    f.append(lista[j][i])
                transpuesta.append(f)

            trans2 = transpuesta.copy()
            # ESTA ES UNA SOLUCIÓN MEDIO BRUSCA PERO YA FUE QUEDAAa
            for i in trans2:
                print("\n" * 2)

                print(
                    "Arranca el for i es",
                    i,
                    "tra",
                )
                [print(asd) for asd in transpuesta]
                d = self.fetchDatos(
                    f"""SELECT * FROM Consumos where cons_lot_id = {i[0]} and cons_prop_id = {i[1]} and cons_cost_id = {i[2]}"""
                )

                if d:
                    esIgual = True

                    for j in range(3, 11):
                        print("i[j] es", i[j], "d[0][j + 1]", d[0][j + 1])
                        if i[j] != d[0][j + 1]:
                            ban = False

                            break
                    if not esIgual:
                        c = self.conn.cursor()

                        c.execute("delete from consumos where cons_id = ?", (d[0][0],))
                        print("borrando")

                        self.conn.commit()
                        c.close()
                    else:
                        transpuesta.remove(i)

                print("\n" * 2)

                print(
                    "termina el for i es",
                    i,
                    "tra",
                )
                [print(asd) for asd in transpuesta]
                print("\n" * 2)

            cur = self.conn.cursor()

            cur.executemany(
                "INSERT INTO Consumos Values (NULL,?,?,?,?,?,?,?,?,?,?,?, FALSE)",
                transpuesta,
            )
            print("Metiendo datos")
            self.conn.commit()

        print("Actualizamos los datos")

    def fetchApi(self, query):
        datos = self.fetchDatos(query)

        dicc = []
        for i, row in enumerate(datos):
            dicc.append([])
            for key in row.keys():
                # Transformamos 0 y 1 a bool cuando necesitamos
                if key[-4:] == "bool":
                    dicc[i].append({key: bool(row[key])})
                else:
                    dicc[i].append({key: row[key]})
        return dicc

    def insertar(self, query: str, otros: list):
        cur = self.conn.cursor()

        print("Vamos a llamar", query)
        print("con", otros)

        cur.execute(query, otros)
        cur.close()
        self.conn.commit()

    def ejecutar(self, query: str):
        # print("El query es ")
        # print(query)
        cur = self.conn.cursor()
        cur.execute(query)
        cur.close()
        self.conn.commit()


if __name__ == "__main__":
    print("Ejecutando de main")
    path = "./barriosTestMain.sqlite3"
    try:
        os.remove(path)
    except:
        print("Jjas")

    b = Barrios(path)
    b.crearTablas()
    b.insertarMuestras()
    b.actualizar()

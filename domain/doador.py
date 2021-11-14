from flask.json import jsonify
import traceback

import pymysql


class Doador:
    def __init__(self, iddoador=None, bloco_apartamento=None):
        self.iddoador = iddoador
        self.bloco_apartamento = bloco_apartamento

        self.conn = pymysql.connect(host='x8autxobia7sgh74.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
                                    user='uno1istjd900u7yk',
                                    password='igwvpvp6i7xfmrsk',
                                    database='fvr0dnbv5n7s7oip',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)

    def cadastroDoador(self):
        try:
            with self.conn.cursor() as cur:
                sql = "INSERT INTO `doador`(`bloco_apartamento`)VALUES(%s)"
                cur.execute(sql, (self.bloco_apartamento))
                self.conn.commit()
        except:
            print("Erro ao tentar cadastrar os dados")
            traceback.print_exc()
        finally:
            self.conn.close()

    def listarDoador(self):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT * FROM doador")
                result = cur.fetchall()
                return jsonify(result)
        except:
            print("Erro ao tentar listar os dados")
            traceback.print_exc()
        finally:
            self.conn.close()

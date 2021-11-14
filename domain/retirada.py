from flask.json import jsonify
import json
import traceback

import pymysql


class Retirada:
    def __init__(self, idproduto=None, quantidade=None):
        self.idproduto = idproduto
        self.quantidade = quantidade

        self.conn = pymysql.connect(host='x8autxobia7sgh74.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
                                    user='uno1istjd900u7yk',
                                    password='igwvpvp6i7xfmrsk',
                                    database='fvr0dnbv5n7s7oip',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)

    def cadastroRetirada(self):
        try:
            with self.conn.cursor() as cur:
                sql = "INSERT INTO `retirada`(`idproduto`,`quantidade`)VALUES(%s,%s)"
                cur.execute(sql, (self.idproduto, self.quantidade))
                self.conn.commit()
        except:
            print("Erro ao tentar cadastrar os dados")
            traceback.print_exc()
        finally:
            self.conn.close()

    def listarRetirada(self):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT * FROM retirada")
                result = cur.fetchall()
                return jsonify(result)

        except:
            print("Erro ao tentar cadastrar os dados")
        finally:
            self.conn.close()

    def totalRetiradaInicio(self):
        try:
            with self.conn.cursor() as cur:
                cur.execute(
                    "select sum(quantidade) as total from retirada")
                result = cur.fetchall()
                return jsonify(result)
        except:
            print("Erro ao tentar calcular o total de doacoes")
        finally:
            self.conn.close()

    def totalRetirada24(self):
        try:
            with self.conn.cursor() as cur:
                cur.execute(
                    "select sum(quantidade) as total from retirada where dataretirada between curdate() - dayofmonth(curdate()) - 1 and curdate()")
                result = cur.fetchall()
                return jsonify(result)
        except:
            print("Erro ao tentar calcular o total de doacoes")
        finally:
            self.conn.close()

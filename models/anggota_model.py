from config.database import Database

class AnggotaModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "anggota"

    def create_anggota(self, nama, alamat):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                query = f"INSERT INTO {self.table_name} (nama, alamat) VALUES (%s, %s)"
                cursor.execute(query, (nama, alamat))
                self.conn.commit()
                return True
            except Exception as e:
                print(f"Gagal menambah anggota: {e}")
        return False
       
    def get_all_anggota(self):
        if self.conn:
            try:
                cursor = self.conn.cursor(dictionary = True)
                query = f"SELECT * FROM {self.table_name}"
                cursor.execute(query)
                result = cursor.fetchall()
                cursor.close()
                return result
            except Exception as e:
                print(f"Gagal membaca anggota: {e}")
        return []
    

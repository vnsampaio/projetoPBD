from conexao import conectar

def criar_tabela_pessoas():
    
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS projeto.pessoas (
                    id_pessoa SERIAL PRIMARY KEY,
                    nome VARCHAR(50) NOT NULL,
                    sobrenome VARCHAR(50) NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL
                );
            """)
            conn.commit()  
            print("Tabela 'pessoas' criada com sucesso.")
        except Exception as e:
            print("Erro ao criar a tabela 'pessoas':", e)
        finally:
            conn.close()

if __name__ == "__main__":
    criar_tabela_pessoas()

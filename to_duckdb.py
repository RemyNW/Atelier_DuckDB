import duckdb
import os

# Définir les variables
parquet_files_directory = "parquet_directory"  # Chemin de base de votre projet
# parquet_files_directory = os.path.join(base_directory, "parquet_directory")
output_duckdb_file = os.path.join(parquet_files_directory, "data_lake.duckdb")
schema_name = "raw"  # Nom du schéma dans DuckDB


def initialize_duckdb_schema(duckdb_connection, schema_name):
    """
    Initialise le schéma dans la base DuckDB si celui-ci n'existe pas déjà.
    """
    duckdb_connection.execute(f"CREATE SCHEMA IF NOT EXISTS {schema_name};")


def load_parquet_to_duckdb(duckdb_connection, schema_name, parquet_files_directory):
    """
    Charge tous les fichiers Parquet du dossier spécifié dans des tables DuckDB dans le schéma donné.
    """
    for file_name in os.listdir(parquet_files_directory):
        if file_name.endswith(".parquet"):
            table_name = os.path.splitext(file_name)[0]  # Utilise le nom du fichier comme nom de table
            file_path = os.path.join(parquet_files_directory, file_name)

            print(f"Loading {file_name} into DuckDB...")
            try:
                # Supprimer la table si elle existe déjà
                duckdb_connection.execute(f"DROP TABLE IF EXISTS {schema_name}.{table_name};")

                # Charger les données dans une table DuckDB
                duckdb_connection.execute(f"""
                    CREATE TABLE {schema_name}.{table_name} AS
                    SELECT * FROM read_parquet('{file_path}');
                """)
                print(f"Table {schema_name}.{table_name} created successfully.")
            except Exception as e:
                print(f"An error occurred while loading {file_name}: {e}")


def main():
    # Vérifier si le répertoire des fichiers Parquet existe
    if not os.path.exists(parquet_files_directory):
        raise FileNotFoundError(f"The directory {parquet_files_directory} does not exist.")
    # Connexion à la base DuckDB
    conn = duckdb.connect(output_duckdb_file)

    try:
        # Initialiser le schéma
        initialize_duckdb_schema(conn, schema_name)

        # Charger les fichiers Parquet dans le schéma "raw"
        load_parquet_to_duckdb(conn, schema_name, parquet_files_directory)

        print("All Parquet files have been successfully loaded into DuckDB.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Fermer la connexion à la base DuckDB
        conn.close()


if __name__ == "__main__":
    main()

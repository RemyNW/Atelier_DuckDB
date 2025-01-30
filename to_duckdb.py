import duckdb
import os


parquet_files_directory = "parquet_directory"
output_duckdb_file = os.path.join(parquet_files_directory, "data_lake.duckdb")
schema_name = "raw"


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
            table_name = os.path.splitext(file_name)[0]
            file_path = os.path.join(parquet_files_directory, file_name)

            print(f"Loading {file_name} into DuckDB...")
            try:
                duckdb_connection.execute(f"DROP TABLE IF EXISTS {schema_name}.{table_name};")

                duckdb_connection.execute(f"""
                    CREATE TABLE {schema_name}.{table_name} AS
                    SELECT * FROM read_parquet('{file_path}');
                """)
                print(f"Table {schema_name}.{table_name} created successfully.")
            except Exception as e:
                print(f"An error occurred while loading {file_name}: {e}")


def main():
    if not os.path.exists(parquet_files_directory):
        raise FileNotFoundError(f"The directory {parquet_files_directory} does not exist.")
    conn = duckdb.connect(output_duckdb_file)

    try:
        initialize_duckdb_schema(conn, schema_name)

        load_parquet_to_duckdb(conn, schema_name, parquet_files_directory)

        print("All Parquet files have been successfully loaded into DuckDB.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()

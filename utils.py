import pyarrow as pa
import pyarrow.parquet as pq


def save_to_parquet(data, filename):
    """
    Convertit un objet JSON en fichier Parquet à l'aide de PyArrow.
    Args:
        data (list|dict): Les données JSON à convertir.
        filename (str): Le nom du fichier Parquet à générer.
    """
    if isinstance(data, list):
        # Convertir une liste d'objets JSON en Table PyArrow
        table = pa.Table.from_pylist(data)
    elif isinstance(data, dict):
        # Si c'est un seul objet JSON, le convertir en liste d'un seul élément
        table = pa.Table.from_pylist([data])
    else:
        raise ValueError(f"Format inattendu pour les données : {type(data)}")

    # Enregistrer la table PyArrow au format Parquet
    pq.write_table(table, filename)
    print(f"Fichier Parquet généré : {filename}")

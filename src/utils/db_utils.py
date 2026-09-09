from sqlalchemy.dialects.postgresql import insert


def insert_on_conflict_nothing(table, conn, keys, data_iter):
    """
    Insert rows into PostgreSQL.
    If a PRIMARY KEY / UNIQUE conflict occurs,
    ignore that row.
    """

    data = [
        dict(zip(keys, row))
        for row in data_iter
    ]

    stmt = insert(table.table).values(data)

    stmt = stmt.on_conflict_do_nothing()

    conn.execute(stmt)
import sqlalchemy

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String(50)),
    sqlalchemy.Column("email", sqlalchemy.String(100)),
)